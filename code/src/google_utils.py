import ast
import json
import logging
import os
import random
import time
from pathlib import Path
from typing import List

import google.generativeai as genai
from google.api_core import exceptions as google_exceptions
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from utils.json import clean_to_dict

logger = logging.getLogger(__name__)


def init_google_client():
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    if GOOGLE_API_KEY:
        os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    elif os.getenv("GOOGLE_API_KEY") is None:
        raise ValueError("Set either GOOGLE_API_KEY or GoogleAPIKey in env")
    return genai.configure(api_key=GOOGLE_API_KEY)


def is_rate_limit_error(exception):
    """Enhanced rate limit detection for Google API"""
    if isinstance(exception, google_exceptions.ResourceExhausted):
        return True

    # Check for rate limit in error message
    error_msg = str(exception).lower()
    return any(
        phrase in error_msg
        for phrase in [
            "quota exceeded",
            "rate limit",
            "too many requests",
            "429",
            "resource exhausted",
            "quota",
            "limit exceeded",
        ]
    )


def is_retriable_error(exception):
    """Check if error should be retried"""
    if isinstance(
        exception,
        (
            google_exceptions.ResourceExhausted,
            google_exceptions.InternalServerError,
            google_exceptions.ServiceUnavailable,
            google_exceptions.DeadlineExceeded,
        ),
    ):
        return True

    # Check error message for retriable errors
    error_msg = str(exception).lower()
    return any(
        phrase in error_msg
        for phrase in [
            "quota",
            "rate limit",
            "internal error",
            "service unavailable",
            "deadline exceeded",
            "timeout",
            "temporary",
        ]
    )


def custom_wait_strategy(retry_state):
    """Custom wait strategy for Google API with rate limit awareness"""
    attempt = retry_state.attempt_number

    if retry_state.outcome and retry_state.outcome.exception():
        exception = retry_state.outcome.exception()

        if is_rate_limit_error(exception):
            # For rate limits, use longer delays
            base_wait = min(8 * (2 ** (attempt - 1)), 180)  # Cap at 3 minutes

            # Google rate limits can be quite strict, so be more conservative
            if "quota exceeded" in str(exception).lower():
                base_wait = max(base_wait, 60)  # At least 1 minute for quota
        else:
            # For other errors, shorter delays
            base_wait = min(4 * (2 ** (attempt - 1)), 60)
    else:
        base_wait = min(4 * (2 ** (attempt - 1)), 60)

    # Add jitter to avoid thundering herd
    jitter = random.uniform(0.2, 0.5) * base_wait
    total_wait = base_wait + jitter

    logger.info(f"Waiting {total_wait:.2f}s before retry (attempt {attempt})")
    return total_wait


@retry(
    wait=custom_wait_strategy,
    stop=stop_after_attempt(5),
    retry=retry_if_exception(is_retriable_error),
    before_sleep=before_sleep_log(logger, logging.INFO),
    reraise=True,
)
def extract_nomological_network(
    pdf_path: Path,
    model: genai.GenerativeModel,
    prompt: str = "",
    temperature: float = 0,
) -> dict:
    """
    Enhanced extraction with better error handling and retries.
    Default temperature 0 for deterministic extraction; vary only for agreement tests.
    """
    if prompt == "":
        raise ValueError("Prompt is empty")

    # Add small delay to spread out requests
    time.sleep(random.uniform(0.2, 0.8))

    uploaded_file = None
    try:
        # Upload PDF with native document MIME type (LLM API PDF tool use)
        try:
            uploaded_file = genai.upload_file(
                pdf_path, mime_type="application/pdf"
            )
        except TypeError:
            # Some SDK versions only accept path as positional
            uploaded_file = genai.upload_file(
                str(pdf_path), mime_type="application/pdf"
            )

        # Wait for file to be processed (important for large files)
        file_state = genai.get_file(uploaded_file.name)
        while file_state.state.name == "PROCESSING":
            logger.debug("File %s still processing...", pdf_path.name)
            time.sleep(2)
            file_state = genai.get_file(uploaded_file.name)

        if file_state.state.name == "FAILED":
            raise Exception(f"File processing failed for {pdf_path.name}")

        safety_settings = {
            "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
            "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
            "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
            "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
        }

        generation_config = (
            {"temperature": temperature} if temperature is not None else {}
        )
        response = model.generate_content(
            [uploaded_file, prompt],
            safety_settings=safety_settings,
            generation_config=generation_config,
            request_options={"timeout": 300},  # 5 minute timeout
        )

        return parse_gemini_response(response)

    except Exception as e:
        logger.error(
            f"Error in extract_nomological_network for {pdf_path.name}: {str(e)}"
        )
        raise

    finally:
        # Always clean up uploaded file
        if uploaded_file:
            try:
                genai.delete_file(uploaded_file.name)
                logger.debug(
                    f"Successfully deleted uploaded file {uploaded_file.name}"
                )
            except Exception as cleanup_error:
                logger.warning(
                    f"Failed to cleanup uploaded file {uploaded_file.name}: {cleanup_error}"
                )


def extract_nomological_network_batch(
    pdf_paths: List[Path],
    model: genai.GenerativeModel,
    prompt: str = "",
    temperature: float = 0,
) -> List[dict]:
    """
    Enhanced batch processing with better error handling.
    """
    if not pdf_paths:
        logger.warning("The provided list of PDF paths is empty.")
        return []

    if prompt == "":
        raise ValueError("Prompt is empty")

    all_results = []

    # Process each file individually with enhanced error handling
    for pdf_path in pdf_paths:
        try:
            logger.info(f"Processing {pdf_path.name}...")

            result = extract_nomological_network(
                pdf_path, model, prompt, temperature=temperature
            )
            all_results.append(
                {"file": pdf_path.name, "success": True, "response": result}
            )

        except Exception as e:
            error_msg = f"Error processing {pdf_path.name}: {e}"
            logger.error(error_msg)
            all_results.append(
                {
                    "file": pdf_path.name,
                    "success": False,
                    "response": {"error": error_msg},
                }
            )

    return all_results


def _clean_and_parse_text_to_dict(text_string):
    """
    A helper function to robustly parse a string that may be a
    Python dictionary literal or contain a JSON object.
    """
    try:
        # First, try to evaluate it as a Python literal (handles unquoted keys, etc.)
        return ast.literal_eval(text_string)
    except (ValueError, SyntaxError):
        # If that fails, it might be messy JSON. Let's try to clean and parse it.
        try:
            # A common issue is a mix of single/double quotes.
            # This is a simple attempt to fix it.
            cleaned_string = text_string.replace("'", '"')
            return json.loads(cleaned_string)
        except json.JSONDecodeError:
            # If all parsing fails, return the original raw text.
            return text_string


def parse_gemini_response(response):
    """
    Extracts detailed information from a raw Gemini GenerateContentResponse object.
    Enhanced with better error handling.
    """
    parsed_data = {}

    try:
        if not response.candidates:
            parsed_data["error"] = "No candidates in response"
            return parsed_data

        candidate = response.candidates[0]

        # 1. Extract the raw text
        if hasattr(candidate, "content") and candidate.content.parts:
            raw_text = candidate.content.parts[0].text
            parsed_data["raw_text"] = raw_text

            # 2. Attempt to parse the raw text into a dictionary
            parsed_data["parsed_text"] = clean_to_dict(
                _clean_and_parse_text_to_dict(raw_text)
            )
        else:
            parsed_data["raw_text"] = "No text content found"
            parsed_data["parsed_text"] = {"error": "No text content found"}

        # 3. Extract Finish Reason
        if hasattr(candidate, "finish_reason"):
            parsed_data["finish_reason"] = candidate.finish_reason.name
        else:
            parsed_data["finish_reason"] = "UNKNOWN"

        # 4. Extract Safety Ratings for the Output
        if hasattr(candidate, "safety_ratings"):
            parsed_data["response_safety_ratings"] = {
                rating.category.name: rating.probability.name
                for rating in candidate.safety_ratings
            }
        else:
            parsed_data["response_safety_ratings"] = {}

        # 5. Extract Citations (if they exist)
        if (
            hasattr(candidate, "citation_metadata")
            and candidate.citation_metadata
        ):
            citations = candidate.citation_metadata.citation_sources
            parsed_data["citations"] = [
                {
                    "url": getattr(source, "uri", ""),
                    "start_index": getattr(source, "start_index", 0),
                    "end_index": getattr(source, "end_index", 0),
                }
                for source in citations
            ]
        else:
            parsed_data["citations"] = []

    except (IndexError, AttributeError) as e:
        parsed_data["error"] = f"Failed to parse candidate: {e}"
        logger.error(f"Candidate parsing error: {e}")
        return parsed_data

    # --- Extract Prompt Feedback and Usage ---
    try:
        if hasattr(response, "prompt_feedback"):
            feedback = response.prompt_feedback
            parsed_data["prompt_block_reason"] = (
                feedback.block_reason.name
                if hasattr(feedback, "block_reason") and feedback.block_reason
                else "NOT_BLOCKED"
            )
        else:
            parsed_data["prompt_block_reason"] = "UNKNOWN"
    except AttributeError:
        parsed_data["prompt_block_reason"] = "UNKNOWN"

    try:
        if hasattr(response, "usage_metadata"):
            usage = response.usage_metadata
            parsed_data["usage_metadata"] = {
                "prompt_token_count": getattr(usage, "prompt_token_count", 0),
                "candidates_token_count": getattr(
                    usage, "candidates_token_count", 0
                ),
                "total_token_count": getattr(usage, "total_token_count", 0),
            }
        else:
            parsed_data["usage_metadata"] = {}
    except AttributeError:
        parsed_data["usage_metadata"] = {}

    return parsed_data


def upload_file_with_retry(pdf_path: Path, max_retries: int = 3):
    """Upload file with retry logic"""
    for attempt in range(max_retries):
        try:
            return genai.upload_file(pdf_path)
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2**attempt + random.uniform(0.1, 0.5)
                logger.warning(
                    f"Upload attempt {attempt + 1} failed for {pdf_path.name}: {e}. Retrying in {wait_time:.2f}s..."
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"Failed to upload {pdf_path.name} after {max_retries} attempts: {e}"
                )
                raise


def cleanup_uploaded_file(file_name: str, max_retries: int = 3):
    """Safely cleanup uploaded file with retries"""
    for attempt in range(max_retries):
        try:
            genai.delete_file(file_name)
            logger.debug(f"Successfully deleted uploaded file {file_name}")
            return
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2**attempt
                logger.warning(
                    f"Cleanup attempt {attempt + 1} failed for {file_name}: {e}. Retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"Failed to cleanup uploaded file {file_name} after {max_retries} attempts: {e}"
                )


def check_quota_and_limits():
    """Check current quota usage (if available)"""
    try:
        # This is a placeholder - Google doesn't provide easy quota checking
        # But you could implement custom tracking here
        logger.info("Quota checking not implemented for Google API")
    except Exception as e:
        logger.warning(f"Could not check quota: {e}")


def get_optimal_batch_size(model_name: str) -> int:
    """Get optimal batch size based on model and current conditions"""
    if "gemini-2.5-pro" in model_name:
        return 1  # Process one at a time for large models
    else:
        return 2  # Slightly more aggressive for smaller models

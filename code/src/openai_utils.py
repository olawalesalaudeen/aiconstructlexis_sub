import ast
import json
import logging
import os
import random
import re
import time
from pathlib import Path

import openai
from openai import OpenAI
from openai.types.vector_store import VectorStore
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from utils.json import clean_to_dict

logger = logging.getLogger(__name__)


def init_openai_client():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY:
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    elif os.getenv("OPENAI_API_KEY") is None:
        raise ValueError("Set either OPENAI_API_KEY or OpenAIAPIKey in env")
    return OpenAI(api_key=OPENAI_API_KEY)


def is_rate_limit_error(exception):
    """Enhanced rate limit detection"""
    if isinstance(exception, openai.RateLimitError):
        return True

    # Check for rate limit in error message (sometimes wrapped in other exceptions)
    error_msg = str(exception).lower()
    return any(
        phrase in error_msg
        for phrase in [
            "rate limit",
            "quota exceeded",
            "too many requests",
            "429",
        ]
    )


def is_retriable_error(exception):
    """Check if error should be retried"""
    return isinstance(
        exception,
        (
            openai.RateLimitError,
            openai.APITimeoutError,
            openai.InternalServerError,
            openai.APIConnectionError,
        ),
    )


def custom_wait_strategy(retry_state):
    """Custom wait strategy with jitter and rate limit awareness"""
    attempt = retry_state.attempt_number

    if retry_state.outcome and retry_state.outcome.exception():
        exception = retry_state.outcome.exception()

        if is_rate_limit_error(exception):
            # For rate limits, use longer delays
            base_wait = min(4 * (2 ** (attempt - 1)), 120)  # Cap at 2 minutes

            # Extract wait time from rate limit error if available
            error_msg = str(exception)
            import re

            wait_match = re.search(r"try again in (\d+)s", error_msg)
            if wait_match:
                suggested_wait = int(wait_match.group(1))
                base_wait = max(base_wait, suggested_wait)
        else:
            # For other errors, shorter delays
            base_wait = min(2 ** (attempt - 1), 60)
    else:
        base_wait = min(2 ** (attempt - 1), 60)

    # Add jitter to avoid thundering herd
    jitter = random.uniform(0.1, 0.3) * base_wait
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
    model: str = "gpt-4o",
    prompt: str = "",
    client: OpenAI = None,
    vs: VectorStore = None,
    temperature: float = 0,
) -> dict:
    """
    Extract constructs/defs/benchmarks and relationships from a PDF using the
    Responses API native PDF input (input_file). The API sends the PDF as
    input_file so the model gets both text and page images (vision).
    Returns a parsed Python dict.
    """
    if prompt == "":
        raise ValueError("Prompt is empty")

    if client is None:
        raise ValueError("OpenAI client is not initialized")

    time.sleep(random.uniform(0.1, 0.3))

    try:
        # Upload PDF with purpose user_data for Responses API input_file
        with open(pdf_path, "rb") as f:
            file_obj = client.files.create(file=f, purpose="user_data")

        # Responses API: pass PDF via input_file (LLM API PDF tool use)
        resp = client.responses.create(
            model=model,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_file", "file_id": file_obj.id},
                        {"type": "input_text", "text": prompt},
                    ],
                },
            ],
        )

        try:
            client.files.delete(file_obj.id)
        except Exception as cleanup_error:
            logger.warning(
                "Failed to delete file %s: %s", file_obj.id, cleanup_error
            )

        return parse_openai_response(resp)

    except Exception as e:
        logger.error("Error in extract_nomological_network: %s", e)
        raise


def _clean_and_parse_text_to_dict(text_string):
    """
    Helper to robustly parse a string that may be a Python dictionary literal.
    """
    try:
        # ast.literal_eval is safer than eval() and can handle dict-like strings
        return ast.literal_eval(text_string)
    except (ValueError, SyntaxError):
        return {"error": "Failed to parse the text content into a dictionary."}


def parse_openai_response(response):
    """
    Extracts detailed information from a raw OpenAI Response object.
    Enhanced with better error handling.
    """
    parsed_data = {}

    try:
        # Extract Model and Usage from object attributes
        parsed_data["model"] = getattr(response, "model", "unknown")

        usage = getattr(response, "usage", None)
        if usage:
            parsed_data["usage_metadata"] = {
                "input_tokens": getattr(usage, "input_tokens", 0),
                "output_tokens": getattr(usage, "output_tokens", 0),
                "total_tokens": getattr(usage, "total_tokens", 0),
            }
        else:
            parsed_data["usage_metadata"] = {}

        # Initialize default values
        raw_text = "Error: No text content found in response."
        parsed_data["tool_queries"] = []
        parsed_data["citations"] = []

        # Process the main 'output' list of objects
        output = getattr(response, "output", [])
        for item in output:
            # Check the type of the object in the list
            item_type = getattr(item, "type", "")

            if item_type == "message":
                content = getattr(item, "content", None)
                if content and len(content) > 0:
                    text_content = content[0]
                    raw_text = getattr(text_content, "text", raw_text)

                    annotations = getattr(text_content, "annotations", [])
                    parsed_data["citations"] = [
                        {
                            "file_id": getattr(ann, "file_id", ""),
                            "filename": getattr(ann, "filename", ""),
                            "text_index": getattr(ann, "index", 0),
                        }
                        for ann in annotations
                        if getattr(ann, "type", "") == "file_citation"
                    ]

            elif item_type == "file_search_call":
                queries = getattr(item, "queries", [])
                parsed_data["tool_queries"] = queries

        # Fallback: Responses API may expose output_text at top level (e.g. input_file flow)
        if (
            not raw_text
            or raw_text == "Error: No text content found in response."
        ) and getattr(response, "output_text", None):
            raw_text = response.output_text
        parsed_data["raw_text"] = raw_text
        parsed_data["parsed_text"] = clean_to_dict(
            _clean_and_parse_text_to_dict(raw_text)
        )

    except Exception as e:
        parsed_data["error"] = f"Failed to parse response object: {e}"
        logger.error(f"Response parsing error: {e}")

    return parsed_data


def create_unique_vector_store(client: OpenAI, base_name: str) -> VectorStore:
    """Create a vector store with a unique name to avoid conflicts"""
    timestamp = int(time.time())
    random_suffix = random.randint(1000, 9999)
    unique_name = f"{base_name}_{timestamp}_{random_suffix}"

    return client.vector_stores.create(name=unique_name)


def cleanup_vector_store(client: OpenAI, vs_id: str, max_retries: int = 3):
    """Safely cleanup vector store with retries"""
    for attempt in range(max_retries):
        try:
            client.vector_stores.delete(vs_id)
            logger.debug(f"Successfully deleted vector store {vs_id}")
            return
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2**attempt
                logger.warning(
                    f"Cleanup attempt {attempt + 1} failed for {vs_id}: {e}. Retrying in {wait_time}s..."
                )
                time.sleep(wait_time)
            else:
                logger.error(
                    f"Failed to cleanup vector store {vs_id} after {max_retries} attempts: {e}"
                )

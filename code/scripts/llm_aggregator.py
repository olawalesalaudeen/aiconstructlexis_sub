"""
LLM-based aggregation of nomological networks from multiple papers.

This module implements a two-step approach:
1. Collect all nodes (constructs, measurements, behaviors) with their definitions
2. Use LLM to group similar nodes and create canonical names/definitions
   (using the most common definition)
3. Collect all relationships and use LLM to aggregate them using the grouped nodes
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from tqdm import tqdm

    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

    # Dummy tqdm class if not available
    class DummyTqdm:
        def __init__(self, iterable=None, **kwargs):
            self.iterable = iterable if iterable is not None else []

        def update(self, n=1):
            pass

        def set_description(self, desc=None):
            pass

        def close(self):
            pass

        def __iter__(self):
            return iter(self.iterable)

    tqdm = DummyTqdm

# Add project root to path for imports
script_dir = Path(__file__).parent
project_root = script_dir.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from misc import prompts
from utils.json import clean_messy_string, clean_to_dict

def enrich_llm_groups_with_source_snippets(
    groups: list,
    flat_nodes: list,
) -> list:
    """Attach source_snippets_evidence from extraction rows to each LLM group."""
    if not groups or not flat_nodes:
        return groups

    from collections import defaultdict

    originals: set = set()
    for g in groups:
        for n in g.get("original_names") or []:
            if n:
                originals.add(n)

    idx = defaultdict(list)
    for node in flat_nodes:
        name = node.get("name")
        if name not in originals:
            continue
        paper = node.get("paper") or ""
        idx[(name, paper)].append(node)

    for g in groups:
        onames = {n for n in (g.get("original_names") or []) if n}
        papers_llm = g.get("papers") or []
        papers_set = set(papers_llm) if papers_llm else None

        rows = []
        seen = set()
        for (name, paper), node_list in idx.items():
            if name not in onames:
                continue
            if papers_set is not None and paper not in papers_set:
                continue
            for node in node_list:
                defn = (node.get("definition") or "").strip()
                key = (name, paper, defn)
                if key in seen:
                    continue
                seen.add(key)
                snips = node.get("source_snippets") or []
                if not isinstance(snips, list):
                    snips = [str(snips)]
                rows.append(
                    {
                        "original_name": name,
                        "paper": paper,
                        "definition": node.get("definition", ""),
                        "source_snippets": snips,
                    }
                )
        g["source_snippets_evidence"] = rows

    return groups


# Import providers only when needed (they require optional dependencies)
try:
    from src import openai_utils

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    openai_utils = None

try:
    from src import google_utils

    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False
    google_utils = None

from misc.logging_config import (
    setup_logging,
    get_logger,
    log_step,
    log_counts,
)

logger = get_logger(__name__)


def call_llm_for_aggregation(
    prompt: str,
    provider: str = "openai",
    model: str = "gpt-4o",
    temperature: float = 0,
    max_retries: int = 3,
    retry_delay: float = 1.0,
) -> Dict[str, Any]:
    """
    Call LLM to perform aggregation task with retry logic.

    Args:
        prompt: The prompt for the aggregation task
        provider: "openai", "google", or "together"
        model: Model name to use
        temperature: Temperature for generation (lower = more deterministic)
        max_retries: Maximum number of retry attempts
        retry_delay: Initial delay between retries (exponential backoff)

    Returns:
        Parsed JSON response from the LLM

    Raises:
        Exception: If all retry attempts fail
    """
    last_exception = None

    for attempt in range(max_retries):
        try:
            if provider == "openai":
                if not OPENAI_AVAILABLE:
                    raise ImportError(
                        "OpenAI dependencies not installed. "
                        "Install with: pip install openai"
                    )
                client = openai_utils.init_openai_client()

                # Use chat completions for better structured output
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a research assistant specializing "
                                "in academic knowledge synthesis. "
                                "Always respond with valid JSON only."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=temperature,
                    response_format={
                        "type": "json_object"
                    },  # Force JSON output
                )

                result_text = response.choices[0].message.content
                result = json.loads(result_text)
                return result

            elif provider == "google":
                from openai import OpenAI as _OpenAI

                google_api_key = os.getenv("GOOGLE_API_KEY")
                if not google_api_key:
                    raise ValueError(
                        "GOOGLE_API_KEY environment variable not set"
                    )
                client = _OpenAI(
                    api_key=google_api_key,
                    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                    timeout=600.0,
                )

                system_message = (
                    "You are a research assistant specializing "
                    "in academic knowledge synthesis. "
                    "Always respond with valid JSON only."
                )

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=temperature,
                    max_tokens=65536,
                )

                result_text = response.choices[0].message.content or ""

                text = result_text.strip()
                fence = re.search(
                    r"```(?:json)?\s*\n?(.*?)\n?```",
                    text,
                    re.DOTALL,
                )
                if fence:
                    text = fence.group(1).strip()

                text = re.sub(
                    r"<think>.*?</think>",
                    "",
                    text,
                    flags=re.DOTALL,
                ).strip()

                try:
                    result = json.loads(text)
                except json.JSONDecodeError:
                    try:
                        from json_repair import repair_json

                        repaired = repair_json(text, return_objects=True)
                        if isinstance(repaired, (dict, list)):
                            result = repaired
                        else:
                            result = clean_to_dict(
                                clean_messy_string(text)
                            )
                    except Exception:
                        result = clean_to_dict(
                            clean_messy_string(text)
                        )

                return result

            elif provider == "together":
                try:
                    from together import Together
                except ImportError as exc:
                    raise ImportError(
                        "together package not installed. "
                        "Install with: pip install together"
                    ) from exc

                # Initialize Together AI client
                together_api_key = os.getenv("TOGETHER_API_KEY")
                if not together_api_key:
                    raise ValueError(
                        "TOGETHER_API_KEY environment variable not set"
                    )

                client = Together(api_key=together_api_key, timeout=300.0)

                # Together AI uses OpenAI-compatible API
                # Note: Some models may not support response_format, so we'll
                # request JSON in the prompt and parse it
                system_message = (
                    "You are a research assistant specializing "
                    "in academic knowledge synthesis. "
                    "Always respond with valid JSON only."
                )

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=temperature,
                    max_tokens=65536,
                )

                result_text = response.choices[0].message.content or ""

                text = result_text.strip()
                fence = re.search(
                    r"```(?:json)?\s*\n?(.*?)\n?```",
                    text,
                    re.DOTALL,
                )
                if fence:
                    text = fence.group(1).strip()

                text = re.sub(
                    r"<think>.*?</think>",
                    "",
                    text,
                    flags=re.DOTALL,
                ).strip()

                try:
                    result = json.loads(text)
                except json.JSONDecodeError:
                    try:
                        from json_repair import repair_json

                        repaired = repair_json(text, return_objects=True)
                        if isinstance(repaired, (dict, list)):
                            result = repaired
                        else:
                            result = clean_to_dict(clean_messy_string(text))
                    except Exception:
                        result = clean_to_dict(clean_messy_string(text))

                return result

            else:
                raise ValueError(
                    f"Unknown provider: {provider}. "
                    "Supported providers: 'openai', 'google', 'together'"
                )

        except Exception as e:
            last_exception = e
            if attempt < max_retries - 1:
                delay = retry_delay * (2**attempt)  # Exponential backoff
                logger.warning(
                    "LLM call failed (attempt %d/%d): %s. Retrying in %.1fs...",
                    attempt + 1,
                    max_retries,
                    str(e)[:100],
                    delay,
                )
                time.sleep(delay)
            else:
                logger.error(
                    "Error calling LLM for aggregation after %d attempts: %s",
                    max_retries,
                    e,
                )
                logger.error("Prompt: %s...", prompt[:200])
                raise

    # Should not reach here, but just in case
    if last_exception:
        raise last_exception
    raise RuntimeError("Unexpected error in call_llm_for_aggregation")


def _source_snippets_from_entity(entity: Dict[str, Any]) -> Dict[str, Any]:
    raw = entity.get("source_snippets")
    if not raw:
        return {}
    if isinstance(raw, list):
        return {"source_snippets": raw}
    return {"source_snippets": [str(raw)]}


def collect_all_nodes_with_definitions(
    definitions: Dict[str, Any],
) -> Tuple[Dict[str, List[Dict[str, Any]]], int]:
    """
    Collect all nodes (constructs, measurements, behaviors) from all papers
    with their definitions.

    Returns:
        Tuple of (nodes_dict, error_count)
    """
    nodes = {"constructs": [], "measurements": [], "behaviors": []}

    error_count = 0

    logger.info("Collecting nodes from papers...")
    for paper_title, paper_data in definitions.items():
        # Handle both old format (with 'result') and simplified format
        if "result" in paper_data:
            paper_result = paper_data.get("result", {})
            parsed = paper_result.get("parsed_text", {})
        else:
            parsed = paper_data.get("parsed_text", {})

        # Skip papers with parsing errors
        if "error" in parsed or not isinstance(parsed, dict) or not parsed:
            error_count += 1
            continue

        nomnet = parsed.get("Nomological Network", {})

        # Extract constructs with all their definitions
        for construct in nomnet.get("constructs", []):
            name = construct.get("name", "Unknown")
            definitions_list = construct.get("definitions", [])
            description = construct.get("description", "")
            sn = _source_snippets_from_entity(construct)

            if definitions_list:
                for def_text in definitions_list:
                    nodes["constructs"].append(
                        {
                            "name": name,
                            "definition": def_text,
                            "paper": paper_title,
                            **sn,
                        }
                    )
            elif description:
                nodes["constructs"].append(
                    {
                        "name": name,
                        "definition": description,
                        "paper": paper_title,
                        **sn,
                    }
                )
            else:
                nodes["constructs"].append(
                    {
                        "name": name,
                        "definition": name,
                        "paper": paper_title,
                        **sn,
                    }
                )

        # Extract measurements with descriptions
        for measure in nomnet.get("measurements", []):
            name = measure.get("name", "Unknown")
            desc = measure.get("description", "")
            sn = _source_snippets_from_entity(measure)

            nodes["measurements"].append(
                {
                    "name": name,
                    "definition": desc,
                    "paper": paper_title,
                    **sn,
                }
            )

        # Extract behaviors with descriptions
        for behavior in nomnet.get("behaviors", []):
            name = behavior.get("name", "Unknown")
            desc = behavior.get("description", "")
            sn = _source_snippets_from_entity(behavior)

            nodes["behaviors"].append(
                {"name": name, "definition": desc, "paper": paper_title, **sn}
            )

    logger.info(
        "Collected %d constructs, %d measurements, %d behaviors",
        len(nodes["constructs"]),
        len(nodes["measurements"]),
        len(nodes["behaviors"]),
    )

    return nodes, error_count


def _decode_id_groups(
    result: Any,
    batch: List[Dict[str, Any]],
    node_type: str,
    batch_num: int,
) -> Optional[List[Dict[str, Any]]]:
    """Decode compact ID-based LLM response into full group dicts.

    Expected format: {"groups": {"CanonicalName": [0, 3, 7], ...}, "ungrouped": [1, 2]}
    Returns list of group dicts compatible with enrich_groups_with_paper_info,
    or None if the response doesn't match the ID-based format.
    """
    if not isinstance(result, dict):
        return None

    groups_dict = result.get("groups")
    if not isinstance(groups_dict, dict):
        return None

    # Verify it's the ID-based format (values should be lists of ints)
    if not all(isinstance(v, list) for v in groups_dict.values()):
        return None

    decoded = []
    seen_ids = set()

    for canonical_name, ids in groups_dict.items():
        int_ids = []
        for raw_id in ids:
            try:
                int_ids.append(int(raw_id))
            except (ValueError, TypeError):
                continue
        original_names = []
        for idx in int_ids:
            if 0 <= idx < len(batch):
                original_names.append(batch[idx].get("name", ""))
                seen_ids.add(idx)
        if original_names:
            decoded.append({
                "canonical_name": canonical_name,
                "original_names": original_names,
            })

    # Handle ungrouped IDs — each becomes its own singleton group
    ungrouped = result.get("ungrouped", [])
    for raw_id in ungrouped:
        try:
            idx = int(raw_id)
        except (ValueError, TypeError):
            continue
        if 0 <= idx < len(batch) and idx not in seen_ids:
            name = batch[idx].get("name", "")
            decoded.append({
                "canonical_name": name,
                "original_names": [name],
            })
            seen_ids.add(idx)

    # Any IDs not accounted for get their own singleton group
    for idx in range(len(batch)):
        if idx not in seen_ids:
            name = batch[idx].get("name", "")
            decoded.append({
                "canonical_name": name,
                "original_names": [name],
            })

    logger.info(
        "[%s batch %d] Decoded %d groups from ID-based response (%d/%d IDs covered)",
        node_type, batch_num, len(decoded), len(seen_ids), len(batch),
    )
    return decoded


def group_nodes_llm(
    nodes: List[Dict[str, Any]],
    node_type: str,
    provider: str = "openai",
    model: str = "gpt-4o",
    batch_size: int = 100,
    existing_mapping_json: str = "",
) -> Dict[str, Any]:
    """
    Use LLM to group similar nodes and create canonical names/definitions.

    Uses ``misc.prompts.AGGREGATE_*`` templates (``build_aggregate_grouping_prompt``):
    synthesized ``unified_definition`` / ``unified_description`` plus optional ``unclustered``.

    Args:
        nodes: List of node dictionaries with name, definition, paper
        node_type: Type of node ('constructs', 'measurements', 'behaviors')
        provider: LLM provider
        model: Model name
        batch_size: Number of nodes to process at once

    Returns:
        Dictionary with 'groups' list containing canonical groups
    """
    logger.info("Grouping %d %s using LLM...", len(nodes), node_type)

    all_groups = []

    # Build smarter batches via deterministic token-similarity clustering so
    # that surface variants (plurals, hyphens, synonyms) and thematic families
    # (shared content words) end up in the SAME batch. The LLM then sees the
    # full set of merge candidates for a concept together and can decide
    # confidently — rather than getting alphabetical slices that split
    # semantic neighbors across batches.
    try:
        from scripts.cluster_for_batching import make_batches as _make_batches
        names = [n.get("name", "") for n in nodes]
        batch_index_lists = _make_batches(names, batch_size=batch_size)
        # Convert indices back to node lists, in the order produced
        batches_to_run = [[nodes[i] for i in idxs] for idxs in batch_index_lists]
        logger.info(
            "Smart-clustered %d nodes into %d batches (target size %d)",
            len(nodes), len(batches_to_run), batch_size,
        )
    except Exception as e:
        logger.warning(
            "Falling back to alphabetical batching (cluster_for_batching failed: %s)", e,
        )
        batches_to_run = [nodes[i : i + batch_size]
                          for i in range(0, len(nodes), batch_size)]

    total_batches = len(batches_to_run)
    progress_bar = tqdm(
        total=total_batches,
        desc=f"Grouping {node_type}",
        disable=not TQDM_AVAILABLE,
    )

    for batch_idx, batch in enumerate(batches_to_run):
        batch_num = batch_idx + 1
        # `i` is kept for log/debug compatibility downstream
        i = sum(len(b) for b in batches_to_run[:batch_idx])

        progress_bar.set_description(
            f"Grouping {node_type} (batch {batch_num}/{total_batches})"
        )
        logger.debug(
            "Processing %s batch %d/%d (%d nodes)",
            node_type,
            batch_num,
            total_batches,
            len(batch),
        )

        # Add IDs to each row for compact LLM output
        indexed_batch = [
            {**node, "id": idx} for idx, node in enumerate(batch)
        ]
        nodes_json = json.dumps(indexed_batch, indent=2)

        prompt = prompts.build_aggregate_grouping_prompt(
            node_type, nodes_json,
            existing_mapping_json=existing_mapping_json,
        )

        try:
            result = call_llm_for_aggregation(prompt, provider, model)

            # Parse raw string if needed
            if isinstance(result, str):
                text = result.strip()
                fence = re.search(
                    r"```(?:json)?\s*\n?(.*?)\n?```",
                    text, re.DOTALL,
                )
                if fence:
                    text = fence.group(1).strip()
                text = re.sub(
                    r"<think>.*?</think>", "", text,
                    flags=re.DOTALL,
                ).strip()
                try:
                    result = json.loads(text)
                except json.JSONDecodeError:
                    try:
                        from json_repair import repair_json
                        repaired = repair_json(
                            text, return_objects=True,
                        )
                        if isinstance(repaired, (dict, list)):
                            result = repaired
                    except Exception:
                        pass

            # Decode ID-based compact format into full groups
            decoded_groups = _decode_id_groups(result, batch, node_type, batch_num)
            if decoded_groups is not None:
                all_groups.extend(decoded_groups)
            else:
                # Fallback: try legacy format
                if isinstance(result, list):
                    enriched_groups = enrich_groups_with_paper_info(
                        result, batch, node_type
                    )
                    all_groups.extend(enriched_groups)
                elif isinstance(result, dict):
                    merged_list = prompts.merge_aggregate_llm_groups(
                        result, node_type
                    )
                    if merged_list:
                        enriched_groups = enrich_groups_with_paper_info(
                            merged_list, batch, node_type
                        )
                        all_groups.extend(enriched_groups)
                    else:
                        logger.error(
                            "Could not parse groups for %s batch %d. Response: %s",
                            node_type, batch_num, str(result)[:500],
                        )

            progress_bar.update(1)

        except Exception as e:
            logger.error(
                "Error grouping %s batch %d: %s",
                node_type,
                batch_num,
                e,
            )
            progress_bar.update(1)
            # Continue with next batch

    progress_bar.close()

    logger.info(
        "Created %d groups from batches for %s", len(all_groups), node_type
    )

    # Step 2: Enrich all groups with paper information from original nodes
    logger.info("Enriching groups with paper information...")
    enriched_groups = enrich_groups_with_paper_info(
        all_groups, nodes, node_type
    )

    # Step 3: Merge groups across batches that refer to the same concept
    # This handles cases where similar nodes were in different batches
    if len(enriched_groups) > 1:
        logger.info("Merging groups across batches...")
        merged_groups = merge_groups_across_batches(
            enriched_groups, node_type, provider, model
        )
        logger.info(
            "Merged to %d final groups for %s", len(merged_groups), node_type
        )
        return {"groups": merged_groups}

    return {"groups": enriched_groups}


def enrich_groups_with_paper_info(
    groups: List[Dict[str, Any]],
    original_nodes: List[Dict[str, Any]],
    node_type: str,
) -> List[Dict[str, Any]]:
    """
    Enrich groups with papers and paper_count from original nodes.
    Also creates a subdict mapping original names to their definitions and papers.

    Args:
        groups: List of groups from LLM (with canonical_name, canonical_definition, original_names)
        original_nodes: List of original node dictionaries
        node_type: Type of node

    Returns:
        Enriched groups with papers, paper_count, and original_nodes subdict
    """
    enriched = []

    for group in groups:
        original_names = group.get("original_names", [])
        # Deduplicate original_names list
        original_names = list(
            dict.fromkeys(original_names)
        )  # Preserves order while removing duplicates

        papers_set = set()
        original_nodes_dict = (
            {}
        )  # Maps original name -> {"definition": ..., "papers": [...]}

        # Build mapping of original name to definitions and papers
        for node in original_nodes:
            # Ensure node is a dictionary
            if not isinstance(node, dict):
                logger.warning(
                    "Skipping non-dict node: %s (value: %s)",
                    type(node),
                    str(node)[:100],
                )
                continue

            try:
                node_name = node.get("name", "")
                if not isinstance(node_name, str):
                    node_name = str(node_name) if node_name else ""

                if node_name in original_names:
                    paper = node.get("paper", "")
                    definition = node.get("definition", "")

                    # Ensure paper and definition are strings (or convert them)
                    if paper and not isinstance(paper, str):
                        paper = str(paper)
                    if definition and not isinstance(definition, str):
                        definition = str(definition)

                    if paper:
                        papers_set.add(paper)

                    # Initialize entry for this original name if not exists
                    if node_name not in original_nodes_dict:
                        original_nodes_dict[node_name] = {
                            "definition": definition
                            or "",  # Keep first definition encountered
                            "papers": [],
                        }

                    # Add paper if not already in the list for this name
                    if (
                        paper
                        and paper
                        not in original_nodes_dict[node_name]["papers"]
                    ):
                        original_nodes_dict[node_name]["papers"].append(paper)
            except (KeyError, TypeError, AttributeError) as e:
                logger.warning("Error processing node %s: %s", node, e)
                continue

        # Sort papers for each original name
        for name in original_nodes_dict:
            original_nodes_dict[name]["papers"].sort()

        # Create enriched group
        enriched_group = group.copy()
        enriched_group["original_names"] = original_names  # Deduplicated list
        enriched_group["original_nodes"] = (
            original_nodes_dict  # Subdict with name -> {definition, papers}
        )
        enriched_group["papers"] = sorted(list(papers_set))
        enriched_group["paper_count"] = len(papers_set)

        enriched.append(enriched_group)

    return enriched


def _validate_merge_candidates(
    groups: List[Dict[str, Any]],
    min_members_to_check: int = 3,
) -> List[Dict[str, Any]]:
    """Flag or split groups that look over-aggregated.

    Heuristics (no LLM call):
    1. **Name specificity**: if a group's original_names contain both a generic
       term and a clearly more specific variant (e.g. "Reasoning" and
       "Mathematical reasoning"), the specific one should be its own group.
    2. **Definition divergence**: if definitions within a group have very low
       lexical overlap, the group is likely over-merged.

    Returns a (possibly larger) list of groups with suspect merges split apart.
    """
    result: List[Dict[str, Any]] = []

    for g in groups:
        orig_names = g.get("original_names", [])
        if len(orig_names) < min_members_to_check:
            result.append(g)
            continue

        canonical = (g.get("canonical_name") or "").strip().lower()
        # Check if any original_name is a strict superstring of the canonical
        # that adds a meaningful qualifier (not just suffix filler)
        filler = {"ability", "capability", "capacity", "skill", "performance"}
        specifics = []
        generics = []
        for n in orig_names:
            nl = n.strip().lower()
            # Strip filler to get the core
            core_words = [w for w in nl.split() if w not in filler]
            canon_words = [w for w in canonical.split() if w not in filler]
            if set(canon_words).issubset(set(core_words)) and len(core_words) > len(canon_words):
                specifics.append(n)
            else:
                generics.append(n)

        if not specifics:
            result.append(g)
            continue

        # If specifics share a common qualifier (e.g. all start with "Mathematical"),
        # split them into their own group; otherwise keep together
        qualifier_groups: Dict[str, List[str]] = {}
        for n in specifics:
            nl = n.strip().lower()
            extra = set(nl.split()) - set(canonical.split()) - filler
            qualifier = " ".join(sorted(extra)) if extra else ""
            qualifier_groups.setdefault(qualifier, []).append(n)

        if not qualifier_groups:
            result.append(g)
            continue

        # Keep the base group with generics
        if generics:
            base = g.copy()
            base["original_names"] = generics
            _prune_group_metadata(base, set(generics))
            result.append(base)

        # Each qualifier cluster becomes its own group
        for qualifier, names in qualifier_groups.items():
            split_g = g.copy()
            # Pick the longest name as canonical for the split group
            best_name = max(names, key=len)
            split_g["canonical_name"] = best_name
            split_g["original_names"] = names
            _prune_group_metadata(split_g, set(names))
            result.append(split_g)

            logger.info(
                "  Split: '%s' pulled out of '%s' (%d names)",
                best_name, g.get("canonical_name", "?"), len(names),
            )

    return result


def _prune_group_metadata(group: Dict[str, Any], keep_names: set) -> None:
    """Trim original_nodes, papers, source_snippets_evidence to only names in keep_names."""
    on = group.get("original_nodes", {})
    if on:
        group["original_nodes"] = {k: v for k, v in on.items() if k in keep_names}
    sse = group.get("source_snippets_evidence", [])
    if sse:
        group["source_snippets_evidence"] = [
            e for e in sse if e.get("original_name", "") in keep_names
        ]
    papers: set = set()
    for nd in group.get("original_nodes", {}).values():
        for p in nd.get("papers", []):
            papers.add(p)
    group["papers"] = sorted(papers)
    group["paper_count"] = len(papers)


_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"  # ‐ ‑ ‒ – — ― −


def _normalize_name_for_exact_match(name: str) -> str:
    """Aggressive normalization for the deterministic pre-LLM merge pass.

    Catches trivial variants that the LLM should not have to think about:
    - case differences
    - whitespace collapsed/stripped
    - hyphen/space/underscore interchange (incl. unicode hyphens)
    - punctuation stripped
    - slash variants (e.g. 'AI/ML' ≡ 'AI ML')
    """
    if not name:
        return ""
    s = name.strip().lower()
    # Normalize unicode hyphens to ascii
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    # Treat hyphens/underscores/slashes as spaces
    for ch in "-_/":
        s = s.replace(ch, " ")
    # Drop surrounding punctuation characters (keep alphanumerics + space)
    s = "".join(c if (c.isalnum() or c.isspace()) else " " for c in s)
    # Collapse whitespace
    s = " ".join(s.split())
    return s


def _exact_match_merge(groups: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Merge groups that share any original_name or canonical_name after
    aggressive normalization (case + hyphen/space/punctuation).

    Uses union-find to cluster groups connected by shared normalized names,
    then deterministically combines metadata (papers, original_nodes,
    source_snippets_evidence). No LLM call — purely algorithmic.

    Runs before every LLM merge pass so the LLM never has to think about
    trivial surface variants.
    """
    if len(groups) <= 1:
        return groups

    # Union-find
    parent = list(range(len(groups)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    # Index: normalized name → group indices that contain it
    name_to_indices: Dict[str, List[int]] = {}
    for i, g in enumerate(groups):
        canon = _normalize_name_for_exact_match(g.get("canonical_name") or "")
        if canon:
            name_to_indices.setdefault(canon, []).append(i)
        for n in g.get("original_names", []):
            key = _normalize_name_for_exact_match(n or "")
            if key:
                name_to_indices.setdefault(key, []).append(i)

    for indices in name_to_indices.values():
        for j in range(1, len(indices)):
            union(indices[0], indices[j])

    # Collect clusters
    from collections import defaultdict
    clusters: Dict[int, List[int]] = defaultdict(list)
    for i in range(len(groups)):
        clusters[find(i)].append(i)

    merged: List[Dict[str, Any]] = []
    for member_indices in clusters.values():
        if len(member_indices) == 1:
            merged.append(groups[member_indices[0]])
            continue

        # Pick canonical_name from the group with the most papers
        members = [groups[i] for i in member_indices]
        members.sort(key=lambda g: g.get("paper_count", 0), reverse=True)
        base = members[0]

        all_original_names: List[str] = []
        seen_onames: set = set()
        all_papers: set = set()
        merged_original_nodes: Dict[str, Any] = {}
        merged_sse: List[Dict[str, Any]] = []
        seen_sse_keys: set = set()

        for g in members:
            for n in g.get("original_names", []):
                if n and n not in seen_onames:
                    seen_onames.add(n)
                    all_original_names.append(n)
            for p in g.get("papers", []):
                all_papers.add(p)
            for name, node_data in g.get("original_nodes", {}).items():
                if name not in merged_original_nodes:
                    merged_original_nodes[name] = {
                        "definition": node_data.get("definition", ""),
                        "papers": list(node_data.get("papers", [])),
                    }
                else:
                    for p in node_data.get("papers", []):
                        if p not in merged_original_nodes[name]["papers"]:
                            merged_original_nodes[name]["papers"].append(p)
            for sse_entry in g.get("source_snippets_evidence", []):
                key = (
                    sse_entry.get("original_name", ""),
                    sse_entry.get("paper", ""),
                    sse_entry.get("definition", ""),
                )
                if key not in seen_sse_keys:
                    seen_sse_keys.add(key)
                    merged_sse.append(sse_entry)

        out = base.copy()
        out["original_names"] = all_original_names
        out["papers"] = sorted(all_papers)
        out["paper_count"] = len(all_papers)
        out["original_nodes"] = merged_original_nodes
        out["source_snippets_evidence"] = merged_sse
        merged.append(out)

    return merged


def merge_groups_across_batches(
    groups: List[Dict[str, Any]],
    node_type: str,
    provider: str = "openai",
    model: str = "gpt-4o",
    merge_batch_size: int = 5000,
) -> List[Dict[str, Any]]:
    """
    Hierarchically merge groups across batches using tree reduction.

    Each level splits groups into windows of `merge_batch_size`, merges each
    window via LLM, then feeds the merged results into the next level.
    Continues until the count stabilises (no further merges possible).

    At every level the full group metadata (original_names, original_nodes
    with definitions, papers, source_snippets_evidence) is carried through,
    so the LLM always sees all original definitions and counts.

    Args:
        groups: List of groups from all batches
        node_type: Type of node ('constructs', 'measurements', 'behaviors')
        provider: LLM provider
        model: Model name
        merge_batch_size: Number of groups to merge at once (default: 2000)

    Returns:
        Merged list of groups
    """
    if len(groups) <= 1:
        return groups

    current = _exact_match_merge(groups)
    logger.info(
        "Exact-match pre-merge: %d → %d groups", len(groups), len(current),
    )
    level = 0

    while True:
        prev_count = len(current)
        level += 1
        logger.info(
            "Hierarchical merge level %d: %d groups (batch size %d)",
            level, prev_count, merge_batch_size,
        )

        if prev_count <= merge_batch_size:
            current = _merge_groups_batch(current, node_type, provider, model)
        else:
            next_level: List[Dict[str, Any]] = []
            n_windows = (prev_count + merge_batch_size - 1) // merge_batch_size
            for i in range(0, prev_count, merge_batch_size):
                window = current[i : i + merge_batch_size]
                window_num = i // merge_batch_size + 1
                logger.info(
                    "  Level %d window %d/%d (%d groups)",
                    level, window_num, n_windows, len(window),
                )
                merged_window = _merge_groups_batch(
                    window, node_type, provider, model,
                )
                next_level.extend(merged_window)
            current = next_level

        # Exact-match pass after every LLM level to catch overlaps
        # across windows before sending to the next level
        before_exact = len(current)
        current = _exact_match_merge(current)
        if len(current) < before_exact:
            logger.info(
                "  Exact-match post-merge: %d → %d (-%d)",
                before_exact, len(current), before_exact - len(current),
            )

        # Validate: split groups that look over-aggregated
        before_validate = len(current)
        current = _validate_merge_candidates(current)
        if len(current) != before_validate:
            logger.info(
                "  Validation split: %d → %d (%+d)",
                before_validate, len(current), len(current) - before_validate,
            )

        new_count = len(current)
        logger.info(
            "  Level %d result: %d → %d groups (-%d)",
            level, prev_count, new_count, prev_count - new_count,
        )

        if new_count >= prev_count or new_count <= merge_batch_size:
            break

    logger.info(
        "Hierarchical merge complete: %d → %d groups over %d levels",
        len(groups), len(current), level,
    )
    return current


def _merge_groups_batch(
    groups: List[Dict[str, Any]],
    node_type: str,
    provider: str,
    model: str,
) -> List[Dict[str, Any]]:
    """Merge a batch of groups using LLM with ID-based output to save tokens."""
    if len(groups) <= 1:
        return groups

    slim_groups = []
    for i, g in enumerate(groups):
        slim: Dict[str, Any] = {
            "id": i,
            "canonical_name": g.get("canonical_name", ""),
        }
        cd = g.get("canonical_definition", "")
        if cd:
            slim["canonical_definition"] = cd
        onames = g.get("original_names", [])
        if len(onames) > 1:
            slim["original_names"] = onames
        slim_groups.append(slim)

    groups_json = json.dumps(slim_groups, indent=2)

    prompt = prompts.MERGE_GROUPS_PROMPT.format(
        node_type=node_type,
        groups_json=groups_json,
    )

    try:
        result = call_llm_for_aggregation(prompt, provider, model)

        if isinstance(result, str):
            text = result.strip()
            fence = re.search(
                r"```(?:json)?\s*\n?(.*?)\n?```",
                text, re.DOTALL,
            )
            if fence:
                text = fence.group(1).strip()
            text = re.sub(
                r"<think>.*?</think>", "", text,
                flags=re.DOTALL,
            ).strip()
            try:
                result = json.loads(text)
            except json.JSONDecodeError:
                try:
                    from json_repair import repair_json
                    repaired = repair_json(text, return_objects=True)
                    if isinstance(repaired, (dict, list)):
                        result = repaired
                except Exception:
                    pass

        if not isinstance(result, dict):
            logger.warning(
                "Unexpected merge response type: %s", type(result),
            )
            return groups

        id_groups: Dict[str, List[int]] = {}
        if "groups" in result and isinstance(result["groups"], dict):
            id_groups = result["groups"]
        elif all(isinstance(v, list) for v in result.values()):
            id_groups = {
                k: v for k, v in result.items() if k != "ungrouped"
            }
        else:
            logger.warning("Cannot interpret merge response keys")
            return groups

        ungrouped_ids = set()
        if "ungrouped" in result and isinstance(result["ungrouped"], list):
            ungrouped_ids = set(result["ungrouped"])

        claimed: set = set()
        for ids in id_groups.values():
            claimed.update(ids)
        claimed.update(ungrouped_ids)
        all_ids = set(range(len(groups)))
        missing = all_ids - claimed
        if missing:
            logger.warning(
                "Merge response missing IDs %s — ungrouped",
                missing,
            )
            ungrouped_ids.update(missing)

        merged_output: List[Dict[str, Any]] = []

        for canonical_name, member_ids in id_groups.items():
            safe_ids = [mid for mid in member_ids if 0 <= mid < len(groups)]
            if not safe_ids:
                continue
            merged_output.append(
                _reconstruct_merged_group(canonical_name, safe_ids, groups),
            )

        for uid in sorted(ungrouped_ids):
            if 0 <= uid < len(groups):
                g = groups[uid]
                merged_output.append(g.copy())

        return merged_output

    except Exception as e:
        logger.error("Error merging groups: %s", e)
        logger.warning("Keeping original groups without merging")
        return groups


def _reconstruct_merged_group(
    canonical_name: str,
    member_ids: List[int],
    groups: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Build a fully enriched merged group from input group IDs."""
    all_original_names: List[str] = []
    merged_original_nodes: Dict[str, Any] = {}
    papers_set: set = set()
    merged_sse: List[Dict[str, Any]] = []
    seen_sse_keys: set = set()
    definitions: List[str] = []

    for idx in member_ids:
        g = groups[idx]

        for name in g.get("original_names", []):
            if name not in all_original_names:
                all_original_names.append(name)

        for paper in g.get("papers", []):
            papers_set.add(paper)

        for name, node_data in g.get("original_nodes", {}).items():
            if not isinstance(node_data, dict):
                continue
            if name not in merged_original_nodes:
                merged_original_nodes[name] = {
                    "definition": (
                        node_data.get("definition", "")
                        if isinstance(node_data.get("definition"), str)
                        else ""
                    ),
                    "papers": [],
                }
            existing_papers = merged_original_nodes[name]["papers"]
            for p in node_data.get("papers", []):
                if p not in existing_papers:
                    existing_papers.append(p)
            existing_papers.sort()

        for sse_entry in g.get("source_snippets_evidence", []):
            key = (
                sse_entry.get("original_name", ""),
                sse_entry.get("paper", ""),
                sse_entry.get("definition", ""),
            )
            if key not in seen_sse_keys:
                seen_sse_keys.add(key)
                merged_sse.append(sse_entry)

        cd = g.get("canonical_definition", "")
        if cd:
            definitions.append(cd)

    best_definition = ""
    if definitions:
        from collections import Counter
        best_definition = Counter(definitions).most_common(1)[0][0]

    return {
        "canonical_name": canonical_name,
        "canonical_definition": best_definition,
        "original_names": all_original_names,
        "original_nodes": merged_original_nodes,
        "papers": sorted(papers_set),
        "paper_count": len(papers_set),
        "source_snippets_evidence": merged_sse,
    }


def build_name_mapping(
    construct_groups: List[Dict[str, Any]],
    measurement_groups: List[Dict[str, Any]],
    behavior_groups: List[Dict[str, Any]],
) -> Dict[str, str]:
    """
    Build mapping from original names to canonical names.

    Returns:
        Dictionary mapping original_name -> canonical_name
    """
    mapping = {}

    # Map constructs
    for group in construct_groups:
        canonical = group.get("canonical_name", "")
        original_names = group.get("original_names", [])
        # Map all original names to canonical
        for original in original_names:
            mapping[original] = canonical
        # Also map canonical to itself (for consistency)
        if canonical:
            mapping[canonical] = canonical

    # Map measurements
    for group in measurement_groups:
        canonical = group.get("canonical_name", "")
        original_names = group.get("original_names", [])
        for original in original_names:
            mapping[original] = canonical
        # Also map canonical to itself
        if canonical:
            mapping[canonical] = canonical

    # Map behaviors
    for group in behavior_groups:
        canonical = group.get("canonical_name", "")
        original_names = group.get("original_names", [])
        for original in original_names:
            mapping[original] = canonical
        # Also map canonical to itself
        if canonical:
            mapping[canonical] = canonical

    return mapping


def collect_all_relationships(
    definitions: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """Collect all relationships from all papers with full details."""
    all_relationships = []

    logger.info("Collecting relationships from papers...")
    for paper_title, paper_data in definitions.items():
        if "result" in paper_data:
            paper_result = paper_data.get("result", {})
            parsed = paper_result.get("parsed_text", {})
        else:
            parsed = paper_data.get("parsed_text", {})

        if "error" in parsed or not isinstance(parsed, dict) or not parsed:
            continue

        nomnet = parsed.get("Nomological Network", {})

        for rel in nomnet.get("relationships", []):
            rel_info = {
                "source": rel.get("source"),
                "target": rel.get("target"),
                "type": rel.get("type"),
                "evidence": rel.get("evidence", ""),
                "paper": paper_title,
            }
            all_relationships.append(rel_info)

    logger.info("Collected %d relationships", len(all_relationships))
    return all_relationships


def aggregate_relationships_llm(
    relationships: List[Dict[str, Any]],
    construct_groups: List[Dict[str, Any]],
    measurement_groups: List[Dict[str, Any]],
    behavior_groups: List[Dict[str, Any]],
    name_mapping: Dict[str, str],
    provider: str = "openai",
    model: str = "gpt-4o",
    batch_size: int = 150,
) -> List[Dict[str, Any]]:
    """
    Use LLM to aggregate relationships using the grouped nodes.

    This function is a function of the groupings - it uses the grouped
    constructs, measurements, and behaviors to map and aggregate relationships.

    Args:
        relationships: List of relationship dictionaries
        construct_groups: List of grouped constructs
        measurement_groups: List of grouped measurements
        behavior_groups: List of grouped behaviors
        name_mapping: Mapping from original names to canonical names
        provider: LLM provider
        model: Model name
        batch_size: Number of relationships to process at once

    Returns:
        List of aggregated relationships with canonical names
    """
    logger.info(
        "Aggregating %d relationships using LLM...", len(relationships)
    )

    all_aggregated_rels = []

    # Process in batches
    total_batches = (len(relationships) + batch_size - 1) // batch_size
    progress_bar = tqdm(
        total=total_batches,
        desc="Aggregating relationships",
        disable=not TQDM_AVAILABLE,
    )

    for i in range(0, len(relationships), batch_size):
        batch = relationships[i : i + batch_size]
        batch_num = i // batch_size + 1

        progress_bar.set_description(
            f"Aggregating relationships (batch {batch_num}/{total_batches})"
        )
        logger.debug(
            "Processing relationships batch %d/%d (%d relationships)",
            batch_num,
            total_batches,
            len(batch),
        )

        # Create prompt with slim context — pass only canonical names + synonyms,
        # not full group metadata (definitions/papers/evidence are not needed
        # to map source/target names to canonicals).
        def _slim(groups):
            slim = []
            for g in groups:
                entry = {"canonical_name": g.get("canonical_name", "")}
                onames = g.get("original_names") or []
                if onames:
                    entry["original_names"] = onames
                slim.append(entry)
            return slim

        relationships_json = json.dumps(batch, indent=2)
        construct_groups_json = json.dumps(_slim(construct_groups), indent=2)
        measurement_groups_json = json.dumps(_slim(measurement_groups), indent=2)
        behavior_groups_json = json.dumps(_slim(behavior_groups), indent=2)
        name_mapping_json = json.dumps(name_mapping, indent=2)

        prompt = prompts.build_aggregate_relationships_prompt(
            relationships_json,
            construct_groups_json,
            measurement_groups_json,
            behavior_groups_json,
            name_mapping_json,
        )

        try:
            result = call_llm_for_aggregation(prompt, provider, model)

            # Retry once if we got a raw string
            if isinstance(result, str):
                logger.warning(
                    "Got str for rels batch %d, retrying...",
                    batch_num,
                )
                result = call_llm_for_aggregation(prompt, provider, model)

            # Last-resort: parse raw string ourselves
            if isinstance(result, str):
                text = result.strip()
                fence = re.search(
                    r"```(?:json)?\s*\n?(.*?)\n?```",
                    text, re.DOTALL,
                )
                if fence:
                    text = fence.group(1).strip()
                text = re.sub(
                    r"<think>.*?</think>", "", text,
                    flags=re.DOTALL,
                ).strip()
                try:
                    result = json.loads(text)
                except json.JSONDecodeError:
                    try:
                        from json_repair import repair_json
                        repaired = repair_json(
                            text, return_objects=True,
                        )
                        if isinstance(repaired, (dict, list)):
                            result = repaired
                    except Exception:
                        pass

            rels_list = None
            if isinstance(result, dict):
                for key in (
                    "relationships",
                    "relationship",
                    "data",
                    "items",
                ):
                    val = result.get(key)
                    if isinstance(val, list):
                        rels_list = val
                        break
            elif isinstance(result, list):
                rels_list = result
            if rels_list is not None:
                all_aggregated_rels.extend(rels_list)
            else:
                logger.warning(
                    "No rels in response batch %d " "(type: %s)",
                    batch_num,
                    (
                        list(result.keys())[:10]
                        if isinstance(result, dict)
                        else type(result)
                    ),
                )

            progress_bar.update(1)

        except Exception as e:
            logger.error(
                "Error aggregating relationships batch %d: %s",
                batch_num,
                e,
            )
            progress_bar.update(1)
            # Continue with next batch

    progress_bar.close()

    logger.info(
        "Created %d aggregated relationships (pre cross-batch dedup)",
        len(all_aggregated_rels),
    )

    # Cross-batch dedup: merge relationships with identical (source, target, type)
    # that appeared in different batches. Combine evidence, papers, paper_count.
    # Uses aggressive deterministic normalization on source/target so that
    # "Multi-step reasoning" and "Multistep reasoning" fold into one edge.
    merged_by_key: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for rel in all_aggregated_rels:
        if not isinstance(rel, dict):
            continue
        src = str(rel.get("source", "")).strip()
        tgt = str(rel.get("target", "")).strip()
        rtype = str(rel.get("type", "")).strip().lower()
        if not src or not tgt:
            continue
        # Deterministic key (trivial-variant insensitive)
        key = (
            _normalize_name_for_exact_match(src),
            _normalize_name_for_exact_match(tgt),
            rtype,
        )
        if key not in merged_by_key:
            # Keep the longer/more-specific display form when collisions occur
            merged_by_key[key] = {
                "source": src,
                "target": tgt,
                "type": rtype,
                "evidence": [],
                "papers": [],
                "paper_count": 0,
            }
        merged = merged_by_key[key]
        # Prefer a longer, more descriptive display name on collisions
        if len(src) > len(merged["source"]):
            merged["source"] = src
        if len(tgt) > len(merged["target"]):
            merged["target"] = tgt
        for ev in rel.get("evidence", []) or []:
            if ev and ev not in merged["evidence"]:
                merged["evidence"].append(ev)
        for paper in rel.get("papers", []) or []:
            if paper and paper not in merged["papers"]:
                merged["papers"].append(paper)
        merged["paper_count"] = len(merged["papers"])

    deduped = list(merged_by_key.values())
    if len(deduped) < len(all_aggregated_rels):
        logger.info(
            "Cross-batch dedup: %d → %d relationships (-%d duplicates)",
            len(all_aggregated_rels), len(deduped),
            len(all_aggregated_rels) - len(deduped),
        )
    else:
        logger.info(
            "Cross-batch dedup: %d relationships (no duplicates found)",
            len(deduped),
        )

    return deduped


def _checkpoint_path(output_file: Path) -> Path:
    """Checkpoint file path derived from the output file."""
    stem = output_file.stem
    return output_file.parent / f".{stem}_checkpoint.json"


def _save_checkpoint(ckpt_path: Path, data: Dict[str, Any]) -> None:
    """Atomically save a checkpoint dict."""
    tmp = ckpt_path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    tmp.rename(ckpt_path)
    steps = data.get("completed_steps", [])
    logger.info(
        "Checkpoint saved: %s (completed: %s)",
        ckpt_path.name,
        steps,
    )


def _load_checkpoint(
    ckpt_path: Path,
) -> Dict[str, Any] | None:
    """Load checkpoint if it exists, else None."""
    if ckpt_path.exists():
        with open(ckpt_path, "r", encoding="utf-8") as f:
            ckpt = json.load(f)
        steps = ckpt.get("completed_steps", [])
        logger.info(
            "Resuming from checkpoint: completed = %s",
            steps,
        )
        return ckpt
    return None


def _load_name_mapping(path: Optional[Path]) -> Dict[str, str]:
    """Load an existing name mapping dict from JSON, or return empty dict."""
    if path and path.exists():
        with open(path, "r", encoding="utf-8") as f:
            mapping = json.load(f)
        logger.info("Loaded existing name mapping with %d entries from %s", len(mapping), path)
        return mapping
    return {}


def _save_name_mapping(path: Path, mapping: Dict[str, str]) -> None:
    """Persist the name mapping dict to JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    tmp.rename(path)
    logger.info("Saved name mapping (%d entries) to %s", len(mapping), path)


def _deduplicate_nodes(nodes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Deduplicate raw extracted nodes BEFORE the LLM sees them.

    Two passes:
      1. Exact-name dedup (preserves order). Combines per-paper occurrences.
      2. Orthographic dedup using aggressive normalization (case, unicode
         hyphens, hyphen/underscore/slash → space, punctuation stripping,
         whitespace collapse). Variants like "Reasoning Ability",
         "reasoning  ability", "Reasoning—ability", "reasoning-ability" all
         collapse to a single representative — no LLM call needed for these.

    For each ortho-cluster the representative is chosen as the most-frequent
    surface form (ties broken by earliest occurrence), and `_all_papers`
    is the union across all variants. The LLM sees one row per concept,
    saving tokens proportional to the redundancy in the raw extraction.
    """
    # Pass 1: exact dedup
    by_exact: Dict[str, Dict[str, Any]] = {}
    counts: Dict[str, int] = {}
    for node in nodes:
        name = node.get("name", "")
        if not name:
            continue
        counts[name] = counts.get(name, 0) + 1
        if name not in by_exact:
            entry = node.copy()
            entry["_all_papers"] = [node.get("paper", "")]
            by_exact[name] = entry
        else:
            by_exact[name]["_all_papers"].append(node.get("paper", ""))

    # Pass 2: orthographic dedup
    by_norm: Dict[str, list] = {}
    for name in by_exact:
        norm = _normalize_name_for_exact_match(name)
        if not norm:
            norm = name.lower()
        by_norm.setdefault(norm, []).append(name)

    out: List[Dict[str, Any]] = []
    n_collapsed = 0
    for norm, surface_forms in by_norm.items():
        if len(surface_forms) == 1:
            out.append(by_exact[surface_forms[0]])
            continue
        # Pick canonical surface form: highest count, tiebreak by longest name
        # (more specific spellings tend to be longer; prevents collapsing to
        # a casing-stripped form when one variant is properly capitalized).
        rep_name = max(surface_forms, key=lambda nm: (counts[nm], len(nm)))
        rep = by_exact[rep_name].copy()
        rep_papers = list(rep.get("_all_papers", []))
        # Merge the others into the rep
        for nm in surface_forms:
            if nm == rep_name:
                continue
            other = by_exact[nm]
            for p in other.get("_all_papers", []):
                if p not in rep_papers:
                    rep_papers.append(p)
            n_collapsed += 1
        rep["_all_papers"] = rep_papers
        # Track the absorbed surface forms so downstream LLM can see they're
        # variants and so name_mapping captures all of them as → canonical.
        absorbed = [nm for nm in surface_forms if nm != rep_name]
        if absorbed:
            rep["_absorbed_variants"] = absorbed
        out.append(rep)

    if n_collapsed > 0:
        logger.info(
            "Pre-LLM orthographic dedup: collapsed %d surface variants "
            "(%d → %d unique names)",
            n_collapsed, len(by_exact), len(out),
        )
    return out


def _group_nodes_with_mapping(
    all_nodes: List[Dict[str, Any]],
    node_type: str,
    existing_mapping: Dict[str, str],
    provider: str,
    model: str,
    batch_size: int,
) -> Tuple[List[Dict[str, Any]], Dict[str, str]]:
    """
    Group nodes, sending all deduplicated names to the LLM annotated with
    their prior canonical (if any) plus the existing mapping as seed
    context. This anchors the LLM to already-known canonicals so it can
    reuse them and focus its effort on new/unmapped names, while still
    allowing it to revise or merge across the full set.

    Returns (groups, full_new_mapping).
    """
    deduped = _deduplicate_nodes(all_nodes)
    unique_names = {n.get("name", "") for n in deduped}

    # Build a *relevant* subset of the existing mapping: only entries whose
    # keys or values intersect with this run's names (keeps prompt compact).
    relevant_mapping: Dict[str, str] = {}
    for name in unique_names:
        if name in existing_mapping:
            relevant_mapping[name] = existing_mapping[name]
    # Also include any mapping entry whose *canonical* appears in this run
    for orig, canon in existing_mapping.items():
        if canon in unique_names:
            relevant_mapping[orig] = canon

    n_mapped = sum(1 for n in deduped if n.get("name", "") in existing_mapping)
    n_unmapped = len(deduped) - n_mapped
    logger.info(
        "%s: %d unique names (%d already mapped, %d new) from %d raw nodes; "
        "passing relevant mapping (%d entries) as seed context to LLM",
        node_type, len(deduped), n_mapped, n_unmapped,
        len(all_nodes), len(relevant_mapping),
    )

    # Annotate each deduped node with its existing canonical (if any) so the
    # LLM can see prior decisions while still being free to revise.
    annotated = []
    for node in deduped:
        entry = node.copy()
        name = node.get("name", "")
        if name in existing_mapping:
            entry["_prior_canonical"] = existing_mapping[name]
        annotated.append(entry)

    mapping_json_str = json.dumps(relevant_mapping, indent=2) if relevant_mapping else ""

    llm_result = group_nodes_llm(
        annotated, node_type,
        provider=provider, model=model, batch_size=batch_size,
        existing_mapping_json=mapping_json_str,
    )
    llm_groups = llm_result.get("groups", [])

    # Build the updated mapping from LLM output
    new_mapping: Dict[str, str] = {}
    for group in llm_groups:
        canonical = group.get("canonical_name", "")
        for orig in group.get("original_names", []):
            new_mapping[orig] = canonical
        if canonical:
            new_mapping[canonical] = canonical

    return llm_groups, new_mapping


def aggregate_network_llm(
    input_file: Path,
    output_file: Path,
    provider: str = "together",
    model: str = "togethercomputer/gpt-neox-20b",
    batch_size: int = 100,
    only_constructs: bool = False,
    name_mapping_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Aggregate nomological networks using LLM-based semantic understanding.

    Supports checkpointing and persistent name mapping. When name_mapping_path
    is provided, names that already appear in the mapping skip LLM grouping,
    and only new/unique names are sent to the LLM. The mapping is updated
    and saved after each grouping step.

    Args:
        input_file: Path to JSON file with extracted nomological networks
        output_file: Path to save aggregated network
        provider: LLM provider
        model: Model name
        batch_size: Batch size for processing nodes and relationships
        only_constructs: If True, skip measurements, behaviors, relationships
        name_mapping_path: Optional path to a persistent name-mapping JSON dict

    Returns:
        Aggregated network dictionary
    """
    logger.info("Loading %s...", input_file)

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    logger.info(
        "Processing %d papers using LLM-based aggregation...", len(data)
    )

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    ckpt_path = _checkpoint_path(output_file)
    ckpt = _load_checkpoint(ckpt_path) or {"completed_steps": []}
    done = set(ckpt.get("completed_steps", []))

    # Load persistent name mapping
    existing_mapping = _load_name_mapping(name_mapping_path)

    # Step 1: Collect all nodes with definitions
    with log_step(logger, "Step 1: Collect nodes", papers=len(data)):
        all_nodes, error_count = collect_all_nodes_with_definitions(data)
    if error_count > 0:
        logger.warning("Skipped %d papers with parsing errors", error_count)
    log_counts(
        logger, "Raw entity counts",
        constructs=len(all_nodes["constructs"]),
        measurements=len(all_nodes["measurements"]),
        behaviors=len(all_nodes["behaviors"]),
    )

    if only_constructs:
        logger.info(
            "Processing only constructs (skipping measurements and behaviors)"
        )
        all_nodes["measurements"] = []
        all_nodes["behaviors"] = []

    # Step 2: Group constructs (mapping-aware)
    if "constructs" in done:
        logger.info("Step 2: Skipping constructs (already checkpointed)")
        construct_groups = ckpt["construct_groups"]
    else:
        with log_step(
            logger, "Step 2: Group constructs",
            n_input=len(all_nodes["constructs"]),
        ):
            construct_groups, new_c_map = _group_nodes_with_mapping(
                all_nodes["constructs"], "constructs",
                existing_mapping, provider, model, batch_size,
            )
            construct_groups = enrich_llm_groups_with_source_snippets(
                construct_groups, all_nodes["constructs"],
            )
        logger.info(
            "  %d raw constructs -> %d groups",
            len(all_nodes["constructs"]), len(construct_groups),
        )
        existing_mapping.update(new_c_map)
        if name_mapping_path:
            _save_name_mapping(name_mapping_path, existing_mapping)
        ckpt["construct_groups"] = construct_groups
        ckpt["completed_steps"] = list(done | {"constructs"})
        _save_checkpoint(ckpt_path, ckpt)
        done.add("constructs")

    # Step 3: Group measurements (mapping-aware)
    measurement_groups = []
    if not only_constructs:
        if "measurements" in done:
            logger.info("Step 3: Skipping measurements (already checkpointed)")
            measurement_groups = ckpt["measurement_groups"]
        else:
            with log_step(
                logger, "Step 3: Group measurements",
                n_input=len(all_nodes["measurements"]),
            ):
                measurement_groups, new_m_map = _group_nodes_with_mapping(
                    all_nodes["measurements"], "measurements",
                    existing_mapping, provider, model, batch_size,
                )
                measurement_groups = enrich_llm_groups_with_source_snippets(
                    measurement_groups, all_nodes["measurements"],
                )
            logger.info(
                "  %d raw measurements -> %d groups",
                len(all_nodes["measurements"]), len(measurement_groups),
            )
            existing_mapping.update(new_m_map)
            if name_mapping_path:
                _save_name_mapping(name_mapping_path, existing_mapping)
            ckpt["measurement_groups"] = measurement_groups
            ckpt["completed_steps"] = list(done | {"measurements"})
            _save_checkpoint(ckpt_path, ckpt)
            done.add("measurements")

    # Step 4: Group behaviors (mapping-aware)
    behavior_groups = []
    if not only_constructs and all_nodes["behaviors"]:
        if "behaviors" in done:
            logger.info("Step 4: Skipping behaviors (already checkpointed)")
            behavior_groups = ckpt["behavior_groups"]
        else:
            with log_step(
                logger, "Step 4: Group behaviors",
                n_input=len(all_nodes["behaviors"]),
            ):
                behavior_groups, new_b_map = _group_nodes_with_mapping(
                    all_nodes["behaviors"], "behaviors",
                    existing_mapping, provider, model, batch_size,
                )
                behavior_groups = enrich_llm_groups_with_source_snippets(
                    behavior_groups, all_nodes["behaviors"],
                )
            logger.info(
                "  %d raw behaviors -> %d groups",
                len(all_nodes["behaviors"]), len(behavior_groups),
            )
            existing_mapping.update(new_b_map)
            if name_mapping_path:
                _save_name_mapping(name_mapping_path, existing_mapping)
            ckpt["behavior_groups"] = behavior_groups
            ckpt["completed_steps"] = list(done | {"behaviors"})
            _save_checkpoint(ckpt_path, ckpt)
            done.add("behaviors")

    log_counts(
        logger, "After harmonization",
        constructs=len(construct_groups),
        measurements=len(measurement_groups),
        behaviors=len(behavior_groups),
    )

    # Step 5: Build full name mapping (merge existing + groups)
    with log_step(logger, "Step 5: Build name mapping"):
        name_mapping = build_name_mapping(
            construct_groups, measurement_groups, behavior_groups
        )
    full_mapping = {**existing_mapping, **name_mapping}
    logger.info("  Name mapping: %d entries", len(full_mapping))
    if name_mapping_path:
        _save_name_mapping(name_mapping_path, full_mapping)

    # Step 6-7: Collect & aggregate relationships
    aggregated_relationships = []
    if not only_constructs:
        if "relationships" in done:
            logger.info(
                "Step 6-7: Skipping relationships " "(already checkpointed)"
            )
            aggregated_relationships = ckpt["aggregated_relationships"]
        else:
            with log_step(logger, "Step 6: Collect relationships"):
                all_relationships = collect_all_relationships(data)
            logger.info("  Raw relationships: %d", len(all_relationships))

            with log_step(
                logger, "Step 7: Aggregate relationships",
                n_input=len(all_relationships),
            ):
                aggregated_relationships = aggregate_relationships_llm(
                    all_relationships,
                    construct_groups,
                    measurement_groups,
                    behavior_groups,
                    full_mapping,
                    provider=provider,
                    model=model,
                    batch_size=batch_size,
                )
            logger.info(
                "  %d raw -> %d aggregated relationships",
                len(all_relationships), len(aggregated_relationships),
            )
            ckpt["aggregated_relationships"] = aggregated_relationships
            ckpt["completed_steps"] = list(done | {"relationships"})
            _save_checkpoint(ckpt_path, ckpt)
            done.add("relationships")

    # Build final output
    output = {
        "metadata": {
            "total_papers": len(data),
            "error_count": error_count,
            "aggregation_method": "llm",
            "provider": provider,
            "model": model,
            "statistics": {
                "construct_groups": len(construct_groups),
                "measurement_groups": len(measurement_groups),
                "behavior_groups": len(behavior_groups),
                "total_relationships": len(aggregated_relationships),
            },
        },
        "constructs": construct_groups,
        "measurements": measurement_groups,
        "behaviors": behavior_groups,
        "relationships": aggregated_relationships,
        "name_mapping": full_mapping,
        "papers": list(data.keys()),
    }

    # Save output
    logger.info("Saving to %s...", output_file)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    # Clean up checkpoint on success
    if ckpt_path.exists():
        ckpt_path.unlink()
        logger.info("Checkpoint removed (aggregation complete)")

    logger.info("LLM-based aggregation complete!")
    log_counts(
        logger, "Final output",
        constructs=len(construct_groups),
        measurements=len(measurement_groups),
        behaviors=len(behavior_groups),
        relationships=len(aggregated_relationships),
    )
    logger.info("   Total relationships: %d", len(aggregated_relationships))
    logger.info("   Output saved to: %s", output_file)

    return output


def main():
    """Command-line interface for LLM aggregator."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Aggregate nomological networks using LLM-based semantic understanding"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Input JSON file with extracted nomological networks",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output JSON file (default: input_file + _llm_aggregated.json)",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="google",
        choices=["openai", "google", "together"],
        help="LLM provider (default: google — production used google/gemini-2.5-pro)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gemini-2.5-pro",
        help="Model name (default: gemini-2.5-pro — production harmonization model)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Batch size for processing nodes and relationships "
             "(default: 100 — production per-conf harmonization batch size)",
    )
    parser.add_argument(
        "--only-constructs",
        action="store_true",
        help="Only process constructs (skip measurements, behaviors, and relationships)",
    )
    parser.add_argument(
        "--name-mapping",
        type=str,
        default=None,
        help="Path to persistent name-mapping JSON (loaded before LLM, updated after). "
             "Already-mapped names skip LLM grouping.",
    )

    args = parser.parse_args()

    setup_logging(run_name="aggregation")

    input_file = Path(args.input)
    if not input_file.exists():
        logger.error("Input file %s does not exist", input_file)
        return 1

    if args.output:
        output_file = Path(args.output)
    else:
        output_file = (
            input_file.parent / f"{input_file.stem}_llm_aggregated.json"
        )

    nm_path = Path(args.name_mapping) if args.name_mapping else None

    try:
        aggregate_network_llm(
            input_file=input_file,
            output_file=output_file,
            provider=args.provider,
            model=args.model,
            batch_size=args.batch_size,
            only_constructs=args.only_constructs,
            name_mapping_path=nm_path,
        )
        return 0
    except Exception as e:
        logger.error("Aggregation failed: %s", e, exc_info=True)
        return 1


if __name__ == "__main__":
    exit(main())

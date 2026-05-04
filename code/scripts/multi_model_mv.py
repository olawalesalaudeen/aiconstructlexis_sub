"""
Multi-model majority-vote extraction.

Runs 1 trial of two-pass extraction (entities then relationships) with each of
N different models/providers, then applies majority voting across models.

An entity or relationship must appear in >= ceil(N_models/2) model outputs to
be retained (strict majority across models, not sampling variance).

Usage:
    python scripts/multi_model_mv.py \
        --papers_url outputs/experiments/inputs/paper_list_20_llm_for_extraction.json \
        --sandbox outputs/sandbox_multi_model_mv \
        --temperature 0
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from misc.logging_config import setup_logging, get_logger, log_step, log_counts

setup_logging(run_name="multi_model_mv")
logger = get_logger(__name__)

from scripts.batch_majority_vote import (
    load_papers,
    extract_text,
    build_entity_jsonl,
    build_relationship_jsonl,
    parse_json_response,
    majority_vote_entities,
    majority_vote_relationships,
    run_sequential,
    submit_batch,
    poll_batch,
    submit_batch_google,
    poll_batch_google,
    _FAILED_SENTINEL,
)

CONFERENCE_PAGE_LIMITS: dict[str, int] = {
    "neurips": 10, "iclr": 11, "icml": 10,
    "acl": 10, "emnlp": 10, "naacl": 10,
}

MODELS = [
    {"provider": "google",   "model": "gemini-2.5-pro",             "label": "gemini25pro"},
    {"provider": "openai",   "model": "gpt-5.4-mini",               "label": "gpt54mini"},
    {"provider": "together", "model": "Qwen/Qwen3-235B-A22B-Instruct-2507-tput", "label": "qwen3_235b"},
]


def make_client(provider: str):
    if provider == "together":
        from together import Together
        return Together(api_key=os.environ["TOGETHER_API_KEY"], timeout=600.0)
    elif provider == "openai":
        from openai import OpenAI
        return OpenAI(api_key=os.environ["OPENAI_API_KEY"], timeout=600.0)
    elif provider == "google":
        from openai import OpenAI
        return OpenAI(
            api_key=os.environ["GOOGLE_API_KEY"],
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            timeout=600.0,
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")


def parse_sequential_results(results: list) -> dict:
    """Parse sequential results into {(paper, trial, phase): parsed} mapping."""
    parsed = {}
    for r in results:
        custom_id = r.get("custom_id", "")
        try:
            cid = json.loads(custom_id)
        except json.JSONDecodeError:
            cid = {"raw": custom_id}

        resp_body = r.get("response", {}).get("body", {})
        choices = resp_body.get("choices", [])
        content = choices[0].get("message", {}).get("content", "") if choices else ""

        # Skip failed requests so they don't count as empty trials
        if content == _FAILED_SENTINEL:
            logger.debug("Skipping failed result for %s", custom_id[:60])
            continue

        key = (cid.get("paper", ""), cid.get("trial", 0), cid.get("phase", ""))
        parsed[key] = parse_json_response(content)
    return parsed


def run_model_extraction(model_cfg, papers, paper_texts, temperature, workers, sandbox):
    """Run entity + relationship extraction for a single model via batch API.
    Returns (entity_trials, rel_trials).

    Uses batch inference for all providers (Together, OpenAI, Google via OpenAI-compat).
    Falls back to run_sequential if batch submission fails.
    """
    provider = model_cfg["provider"]
    model = model_cfg["model"]
    label = model_cfg["label"]

    logger.info("=" * 60)
    logger.info("Running extraction with %s (%s) [batch mode]", model, provider)
    logger.info("=" * 60)

    client = make_client(provider)

    # --- Entity extraction (1 trial) ---
    entity_lines = build_entity_jsonl(papers, paper_texts, model, temperature, n_trials=1)
    logger.info("[%s] Built %d entity requests", label, len(entity_lines))

    try:
        if provider == "google":
            entity_job = submit_batch_google(entity_lines, f"entities-{label}", model)
            entity_results = poll_batch_google(entity_job, poll_interval=30)
        else:
            entity_job_id = submit_batch(client, entity_lines, f"entities-{label}", provider=provider)
            entity_results = poll_batch(client, entity_job_id, poll_interval=20)
    except Exception as e:
        logger.warning("[%s] Batch failed (%s), falling back to sequential: %s", label, provider, e)
        entity_results = run_sequential(client, entity_lines, f"entities-{label}",
                                        max_workers=workers, provider=provider)

    entity_parsed = parse_sequential_results(entity_results)
    entity_trials_by_paper = {}
    for (paper, trial, phase), parsed in entity_parsed.items():
        if phase == "entities":
            entity_trials_by_paper.setdefault(paper, []).append(parsed)

    # Save per-model entity trials
    model_dir = sandbox / "trials" / label
    model_dir.mkdir(parents=True, exist_ok=True)
    with open(model_dir / "entity_trials.json", "w") as f:
        json.dump(entity_trials_by_paper, f, indent=2, ensure_ascii=False)

    # For relationship extraction, take union of this model's entities (threshold=1)
    nm_path = ROOT / "outputs" / "combined_name_mapping.json"
    name_mapping = {}
    if nm_path.exists():
        raw = json.load(open(nm_path))
        name_mapping = {k.strip().lower(): v.strip().lower() for k, v in raw.items() if v.strip()}

    model_entities = majority_vote_entities(entity_trials_by_paper, 1, name_mapping, threshold=1)

    # --- Relationship extraction (1 trial) ---
    rel_lines = build_relationship_jsonl(papers, paper_texts, model_entities, model, temperature, n_trials=1)
    logger.info("[%s] Built %d relationship requests", label, len(rel_lines))

    if not rel_lines:
        rel_trials_by_paper = {}
    else:
        try:
            if provider == "google":
                rel_job = submit_batch_google(rel_lines, f"rels-{label}", model)
                rel_results = poll_batch_google(rel_job, poll_interval=30)
            else:
                rel_job_id = submit_batch(client, rel_lines, f"rels-{label}", provider=provider)
                rel_results = poll_batch(client, rel_job_id, poll_interval=20)
        except Exception as e:
            logger.warning("[%s] Batch failed for rels (%s), falling back to sequential: %s", label, provider, e)
            rel_results = run_sequential(client, rel_lines, f"rels-{label}",
                                         max_workers=workers, provider=provider)

        rel_parsed = parse_sequential_results(rel_results)
        rel_trials_by_paper = {}
        for (paper, trial, phase), parsed in rel_parsed.items():
            if phase == "relationships":
                rels = parsed.get("relationships", [])
                rel_trials_by_paper.setdefault(paper, []).append(rels)

        with open(model_dir / "relationship_trials.json", "w") as f:
            json.dump(rel_trials_by_paper, f, indent=2, ensure_ascii=False)

    # Summary
    total_c = sum(len(v.get("constructs", [])) for v in model_entities.values())
    total_m = sum(len(v.get("measurements", [])) for v in model_entities.values())
    total_b = sum(len(v.get("behaviors", [])) for v in model_entities.values())
    total_r = sum(len(v) for v in rel_trials_by_paper.values())
    logger.info("[%s] Extracted: C=%d M=%d B=%d R=%d", label, total_c, total_m, total_b, total_r)

    return entity_trials_by_paper, rel_trials_by_paper


def merge_trials(all_entity_trials, all_rel_trials):
    """Merge per-model trial dicts into unified trial lists per paper.
    Each model's output becomes one 'trial' in the combined list."""
    merged_entities = {}
    for model_trials in all_entity_trials:
        for paper, trials in model_trials.items():
            merged_entities.setdefault(paper, []).extend(trials)

    merged_rels = {}
    for model_trials in all_rel_trials:
        for paper, trials in model_trials.items():
            merged_rels.setdefault(paper, []).extend(trials)

    return merged_entities, merged_rels


def main():
    parser = argparse.ArgumentParser(description="Multi-model majority-vote extraction")
    parser.add_argument("--papers_url", required=True)
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--sandbox", required=True)
    parser.add_argument("--max_papers", type=int, default=0)
    parser.add_argument("--workers", type=int, default=5)
    parser.add_argument("--conference", default="auto",
                        help="Conference name for page limit (auto-detects from path)")
    args = parser.parse_args()

    sandbox = Path(args.sandbox)
    sandbox.mkdir(parents=True, exist_ok=True)
    (sandbox / "inputs").mkdir(exist_ok=True)
    (sandbox / "trials").mkdir(exist_ok=True)

    papers = load_papers(args.papers_url)
    if args.max_papers > 0:
        papers = papers[:args.max_papers]
    logger.info("Loaded %d papers", len(papers))

    conf = args.conference
    if conf == "auto":
        p_lower = args.papers_url.lower()
        conf = next((c for c in CONFERENCE_PAGE_LIMITS if c in p_lower), "")
    max_pages = CONFERENCE_PAGE_LIMITS.get(conf, 0)
    logger.info("Conference: %s — max_pages=%d (0=all)", conf or "unknown", max_pages)

    nm_path = ROOT / "outputs" / "combined_name_mapping.json"
    name_mapping = {}
    if nm_path.exists():
        raw = json.load(open(nm_path))
        name_mapping = {k.strip().lower(): v.strip().lower() for k, v in raw.items() if v.strip()}
        logger.info("Loaded %d name mappings", len(name_mapping))

    with log_step(logger, "Extract PDF text", n_papers=len(papers)):
        from concurrent.futures import ThreadPoolExecutor, as_completed

        def _extract_one(p):
            pdf_path = p.get("path", "")
            if not pdf_path:
                return p["name"], ""
            try:
                return p["name"], extract_text(pdf_path, max_pages=max_pages) or ""
            except Exception:
                return p["name"], ""

        paper_texts = {}
        with ThreadPoolExecutor(max_workers=16) as ex:
            futures = {ex.submit(_extract_one, p): p for p in papers}
            for fut in as_completed(futures):
                name, text = fut.result()
                paper_texts[name] = text
                if not text.strip():
                    logger.warning("No text for: %s", name[:60])

    all_entity_trials = []
    all_rel_trials = []

    # Separate caching checks for entity and relationship trials. A model is
    # cached for entities if entity_trials.json has >50% of papers populated;
    # cached for relationships if relationship_trials.json has >30% of papers
    # with at least one non-empty rel list. This avoids the previous bug
    # where an empty relationship_trials.json was reused alongside populated
    # entity trials, skipping relationship extraction entirely.
    entity_models_to_run = []
    rel_models_to_run = []
    model_entity_trials = {}  # label -> entity trials (populated from cache or Phase 1)
    cached_rel_trials = {}    # label -> rel trials (only populated from cache)

    for model_cfg in MODELS:
        label = model_cfg["label"]
        et_path = sandbox / "trials" / label / "entity_trials.json"
        rt_path = sandbox / "trials" / label / "relationship_trials.json"

        entity_cached = False
        rel_cached = False

        if et_path.exists():
            try:
                et = json.load(open(et_path))
                n_ok_et = sum(1 for p, t in et.items()
                              if any(x.get("constructs") or x.get("measurements")
                                     or x.get("behaviors") or x.get("Nomological Network")
                                     for x in t))
                if n_ok_et > len(papers) * 0.5:
                    entity_cached = True
                    model_entity_trials[label] = et
                    logger.info("Reusing cached entity trials for %s (%d/%d papers OK)",
                                label, n_ok_et, len(et))
            except Exception as e:
                logger.warning("Failed to load cached entity trials for %s: %s", label, e)

        if rt_path.exists():
            try:
                rt = json.load(open(rt_path))
                n_ok_rt = sum(1 for p, trials in rt.items()
                              if trials and any(bool(r) for r in trials))
                if n_ok_rt > len(papers) * 0.3:
                    rel_cached = True
                    cached_rel_trials[label] = rt
                    logger.info("Reusing cached relationship trials for %s (%d/%d papers OK)",
                                label, n_ok_rt, len(rt))
            except Exception as e:
                logger.warning("Failed to load cached rel trials for %s: %s", label, e)

        if not entity_cached:
            entity_models_to_run.append(model_cfg)
        if not rel_cached:
            rel_models_to_run.append(model_cfg)

    if entity_models_to_run or rel_models_to_run:
        import concurrent.futures
        from threading import Thread

    if entity_models_to_run:
        import concurrent.futures  # noqa: F811
        # === PHASE 1: Submit ALL entity batch jobs in parallel, poll all ===
        with log_step(logger, "Entity extraction (all models parallel)", n_models=len(entity_models_to_run)):
            entity_jobs = {}  # label -> (client_or_none, job_id, provider, model)

            for model_cfg in entity_models_to_run:
                provider = model_cfg["provider"]
                model = model_cfg["model"]
                label = model_cfg["label"]
                entity_lines = build_entity_jsonl(papers, paper_texts, model, args.temperature, n_trials=1)
                logger.info("[%s] Submitting entity batch: %d requests", label, len(entity_lines))

                try:
                    if provider == "google":
                        job_id = submit_batch_google(entity_lines, f"entities-{label}", model)
                        entity_jobs[label] = (None, job_id, provider, model)
                    else:
                        client = make_client(provider)
                        job_id = submit_batch(client, entity_lines, f"entities-{label}", provider=provider)
                        entity_jobs[label] = (client, job_id, provider, model)
                except Exception as e:
                    logger.error("[%s] Entity batch submit failed: %s", label, e)
                    entity_jobs[label] = None

            # Poll all entity jobs in parallel
            entity_results_map = {}  # label -> results list

            def _poll_entity(label_info):
                label, info = label_info
                if info is None:
                    return label, []
                client, job_id, provider, model = info
                try:
                    if provider == "google":
                        return label, poll_batch_google(job_id, poll_interval=30)
                    else:
                        return label, poll_batch(client, job_id, poll_interval=20)
                except Exception as e:
                    logger.error("[%s] Entity poll failed: %s", label, e)
                    return label, []

            with concurrent.futures.ThreadPoolExecutor(max_workers=len(entity_jobs)) as executor:
                futures = {executor.submit(_poll_entity, (lbl, info)): lbl
                           for lbl, info in entity_jobs.items()}
                for future in concurrent.futures.as_completed(futures):
                    lbl, results = future.result()
                    entity_results_map[lbl] = results
                    logger.info("[%s] Entity batch done: %d results", lbl, len(results))

        # Parse and save entity trials (only for freshly extracted models)
        for model_cfg in entity_models_to_run:
            label = model_cfg["label"]
            results = entity_results_map.get(label, [])
            parsed = parse_sequential_results(results)
            trials_by_paper = {}
            for (paper, trial, phase), p in parsed.items():
                if phase == "entities":
                    trials_by_paper.setdefault(paper, []).append(p)

            model_dir = sandbox / "trials" / label
            model_dir.mkdir(parents=True, exist_ok=True)
            with open(model_dir / "entity_trials.json", "w") as f:
                json.dump(trials_by_paper, f, indent=2, ensure_ascii=False)
            model_entity_trials[label] = trials_by_paper

    if rel_models_to_run:
        import concurrent.futures  # noqa: F811
        # === PHASE 2: Submit ALL relationship batch jobs in parallel, poll all ===
        with log_step(logger, "Relationship extraction (all models parallel)", n_models=len(rel_models_to_run)):
            rel_jobs = {}

            for model_cfg in rel_models_to_run:
                provider = model_cfg["provider"]
                model = model_cfg["model"]
                label = model_cfg["label"]

                # Get this model's entities (union, threshold=1)
                model_entities = majority_vote_entities(
                    model_entity_trials.get(label, {}), 1, name_mapping, threshold=1)

                rel_lines = build_relationship_jsonl(papers, paper_texts, model_entities,
                                                      model, args.temperature, n_trials=1)
                logger.info("[%s] Submitting rel batch: %d requests", label, len(rel_lines))

                if not rel_lines:
                    rel_jobs[label] = None
                    continue

                try:
                    if provider == "google":
                        job_id = submit_batch_google(rel_lines, f"rels-{label}", model)
                        rel_jobs[label] = (None, job_id, provider, model)
                    else:
                        client = make_client(provider)
                        job_id = submit_batch(client, rel_lines, f"rels-{label}", provider=provider)
                        rel_jobs[label] = (client, job_id, provider, model)
                except Exception as e:
                    logger.error("[%s] Rel batch submit failed: %s", label, e)
                    rel_jobs[label] = None

            # Poll all rel jobs in parallel
            def _poll_rel(label_info):
                label, info = label_info
                if info is None:
                    return label, []
                client, job_id, provider, model = info
                try:
                    if provider == "google":
                        return label, poll_batch_google(job_id, poll_interval=30)
                    else:
                        return label, poll_batch(client, job_id, poll_interval=20)
                except Exception as e:
                    logger.error("[%s] Rel poll failed: %s", label, e)
                    return label, []

            rel_results_map = {}
            active_jobs = {lbl: info for lbl, info in rel_jobs.items() if info is not None}
            if active_jobs:
                with concurrent.futures.ThreadPoolExecutor(max_workers=len(active_jobs)) as executor:
                    futures = {executor.submit(_poll_rel, (lbl, info)): lbl
                               for lbl, info in active_jobs.items()}
                    for future in concurrent.futures.as_completed(futures):
                        lbl, results = future.result()
                        rel_results_map[lbl] = results
                        logger.info("[%s] Rel batch done: %d results", lbl, len(results))

        # Parse and save rel trials (freshly extracted)
        for model_cfg in rel_models_to_run:
            label = model_cfg["label"]
            results = rel_results_map.get(label, [])
            parsed = parse_sequential_results(results)
            rel_trials_by_paper = {}
            for (paper, trial, phase), p in parsed.items():
                if phase == "relationships":
                    rels = p.get("relationships", [])
                    rel_trials_by_paper.setdefault(paper, []).append(rels)

            model_dir = sandbox / "trials" / label
            with open(model_dir / "relationship_trials.json", "w") as f:
                json.dump(rel_trials_by_paper, f, indent=2, ensure_ascii=False)

            # Log summary
            et = model_entity_trials.get(label, {})
            me = majority_vote_entities(et, 1, name_mapping, threshold=1)
            tc = sum(len(v.get("constructs", [])) for v in me.values())
            tm = sum(len(v.get("measurements", [])) for v in me.values())
            tb = sum(len(v.get("behaviors", [])) for v in me.values())
            tr = sum(len(rels) for rels_list in rel_trials_by_paper.values() for rels in rels_list)
            log_counts(logger, f"[{label}] Done", constructs=tc, measurements=tm, behaviors=tb, relationships=tr)

            cached_rel_trials[label] = rel_trials_by_paper

    # Assemble all_entity_trials and all_rel_trials in MODELS order
    for model_cfg in MODELS:
        label = model_cfg["label"]
        all_entity_trials.append(model_entity_trials.get(label, {}))
        all_rel_trials.append(cached_rel_trials.get(label, {}))

    n_models = len(MODELS)
    merged_entities, merged_rels = merge_trials(all_entity_trials, all_rel_trials)

    with log_step(
        logger, "Majority vote",
        n_models=n_models, threshold=(n_models // 2) + 1,
    ):
        voted_entities = majority_vote_entities(
            merged_entities, n_models, name_mapping,
        )
        # Relationships: use UNION (threshold=1) — NOT majority vote. Any
        # relationship any model extracted is kept; downstream harmonization
        # deduplicates identical (source, target, type) triples.
        voted_rels = majority_vote_relationships(
            merged_rels, n_models, name_mapping, threshold=1,
        )

    # Save merged trials
    with open(sandbox / "trials" / "merged_entity_trials.json", "w") as f:
        json.dump(merged_entities, f, indent=2, ensure_ascii=False)
    with open(sandbox / "trials" / "merged_relationship_trials.json", "w") as f:
        json.dump(merged_rels, f, indent=2, ensure_ascii=False)

    # Assemble output
    model_labels = "+".join(m["label"] for m in MODELS)
    results = {}
    for paper in papers:
        name = paper["name"]
        entities = voted_entities.get(name, {"constructs": [], "measurements": [], "behaviors": []})
        rels = voted_rels.get(name, [])

        nn = {
            "constructs": entities.get("constructs", []),
            "measurements": entities.get("measurements", []),
            "behaviors": entities.get("behaviors", []),
            "relationships": rels,
        }

        results[name] = {
            "provider": "multi-model",
            "model": model_labels,
            "title": name,
            "result": {
                "raw_text": "",
                "parsed_text": {
                    "Nomological Network": nn,
                    "Title": name,
                },
            },
            "processed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "attempts": 1,
            "name": paper.get("name", ""),
            "url": paper.get("url", ""),
            "path": paper.get("path", ""),
            "is_LLM_paper": True,
        }

    out_path = sandbox / "inputs" / f"extraction_multi_model_mv{n_models}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    logger.info("Saved final extraction to %s", out_path)

    total_c = sum(len(v.get("constructs", [])) for v in voted_entities.values())
    total_m = sum(len(v.get("measurements", [])) for v in voted_entities.values())
    total_b = sum(len(v.get("behaviors", [])) for v in voted_entities.values())
    total_r = sum(len(v) for v in voted_rels.values())
    log_counts(
        logger, f"DONE ({n_models} models, {len(papers)} papers)",
        constructs=total_c, measurements=total_m,
        behaviors=total_b, relationships=total_r,
    )


if __name__ == "__main__":
    main()

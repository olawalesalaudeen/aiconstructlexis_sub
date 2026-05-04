# Pipeline code

Extraction, harmonization, and analysis pipeline for the AI Construct Lexis.

## Setup

```bash
pip install -r requirements.txt
```

## Layout

- `src/` — utilities for LLM calls (`openai_utils.py`, `google_utils.py`, etc.)
- `utils/` — shared helpers
- `scripts/` — pipeline scripts (extraction, harmonization, voting/filtering,
  characterization, joining)
- `prompts/` — numbered prompt files (`01_extract_entities.md` …
  `08_characterize_entities.md`) used by the extraction pipeline
- `run_pipeline.sh` — end-to-end per-venue driver
  (extract → harmonize → vote → characterize)
- `update_joint_network.sh` — incrementally joins a new venue into the
  global Lexis

## Pipeline overview

Per-venue (`run_pipeline.sh`):

1. **Extract** entities and relationships per paper using three LLMs in
   parallel — Gemini 2.5 Pro, GPT-5.4 Mini, Qwen 3.5-397B
   (`scripts/multi_model_mv.py`, which orchestrates one
   `scripts/batch_majority_vote.py` run per model).
2. **Harmonize** — LLM-based semantic deduplication so each paper's
   extracted names map to a canonical entity
   (`scripts/llm_aggregator.py`).
3. **Canonical majority vote** — keep only entities that ≥2 of 3 models
   proposed, with votes counted at the canonical level so surface variants
   such as `Reasoning ability` / `Reasoning capability` / `Reasoning` count
   as the same vote (`scripts/canonical_majority_vote.py`).
4. **Characterize** — synthesize a usage description for each surviving
   canonical entity from its source snippets
   (`scripts/synthesize_definitions_batch.py`).

Joint (`update_joint_network.sh`):

5. **Join** per-venue networks into the global Lexis
   (`scripts/build_joint_network.py`).
6. **Cross-venue merge** — a second LLM dedup pass to catch semantic
   duplicates introduced by new-venue vocabulary
   (`scripts/joint_llm_merge.py`).
7. **Joint canonical majority vote** — re-apply the ≥2-of-3 filter at the
   joint canonical level for entities (`scripts/joint_canonical_mv.py`).
   Relationships are aggregated deterministically (no vote) by bucketing
   raw relationships under their canonical `(source, target, type)` triple
   and unioning the evidence and paper sets across models.

See the paper Section 3 and Appendix A for the full pipeline diagram and
prompts.

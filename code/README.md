# Pipeline code

Extraction, harmonization, and analysis pipeline for the AI Construct Lexis.

## Setup

```bash
pip install -r requirements.txt
```

## Layout

- `src/` — utilities for LLM calls (`openai_utils.py`, `google_utils.py`, etc.)
- `utils/` — shared helpers
- `scripts/` — pipeline scripts (extraction, deduplication, harmonization, figures)
- `prompts/` — numbered prompt files (`01_extract_entities.md` …
  `08_characterize_entities.md`) used by the extraction pipeline
- `run_pipeline.sh` — end-to-end driver
- `update_joint_network.sh` — incrementally adds a new venue to the joint network

## Pipeline overview

1. **Extract** entities and relationships per paper using three LLMs in
   parallel (`scripts/batch_majority_vote.py`).
2. **Filter** via majority vote across the three models
   (`scripts/canonical_majority_vote.py`).
3. **Harmonize** — semantic deduplication of canonical entities across papers.
4. **Characterize** — synthesize a usage description for each canonical entity
   from its source snippets.
5. **Join** venue-level networks into the global Lexis.

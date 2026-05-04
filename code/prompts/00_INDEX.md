# Pipeline Prompts — Index

All prompts used in the nomological network extraction and harmonization pipeline, in execution order. Each file contains the exact prompt text from `misc/prompts.py`.

| # | File | Pipeline Step | Models | Purpose |
|---|---|---|---|---|
| 1 | [01_extract_entities.md](01_extract_entities.md) | Extraction (Pass 1) | Gemini 2.5 Pro / GPT-5.4 Mini / Qwen 3.5-397B | Extract constructs, measurement instruments, behaviors from a paper |
| 2 | [02_extract_relationships.md](02_extract_relationships.md) | Extraction (Pass 2) | Same 3 models | Extract relationships between already-extracted entities |
| 3 | [03_aggregate_constructs.md](03_aggregate_constructs.md) | Harmonization | Gemini 2.5 Pro | Group/deduplicate construct names across papers |
| 4 | [04_aggregate_measurements.md](04_aggregate_measurements.md) | Harmonization | Gemini 2.5 Pro | Group/deduplicate measurement instrument names across papers |
| 5 | [05_aggregate_behaviors.md](05_aggregate_behaviors.md) | Harmonization | Gemini 2.5 Pro | Group/deduplicate behavior names across papers |
| 6 | [06_merge_groups.md](06_merge_groups.md) | Harmonization (merge) | Gemini 2.5 Pro | Merge groups from different batches (hierarchical) |
| 7 | [07_aggregate_relationships.md](07_aggregate_relationships.md) | Harmonization | Gemini 2.5 Pro | Map relationships to canonical entity names, deduplicate |
| 8 | [08_characterize_entities.md](08_characterize_entities.md) | Characterization | Gemini 2.5 Flash | Generate literature-review-style definitions per entity |

**Source:** `misc/prompts.py`  
**Last synced:** 2026-04-14

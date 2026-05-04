# Prompt: Aggregate Measurements

**Pipeline step:** Harmonization — Measurement Grouping  
**Models:** Gemini 2.5 Pro  
**Source:** `misc/prompts.py` → `build_aggregate_grouping_prompt('measurements', ...)`  
**Called from:** `scripts/llm_aggregator.py:group_nodes_llm()`  

> **Note:** The `[... nodes injected here ...]` placeholder is replaced at runtime with a JSON array of measurement nodes from all papers.

---

Deduplicate measurement instruments (benchmarks, datasets, user studies, surveys, human evaluations, and other named evaluation procedures) by grouping rows that refer to the **same instrument** under different names. Do NOT split or merge based on reported metrics or scores.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat descriptions, papers, or snippets.

**Canonical name rules:** community-standard short name of the instrument. Name the **instrument only** (e.g. "MMLU", "HELM Math", "User preference study"), not "MMLU Accuracy" or metric-laden labels. Include subset qualifier when needed. For human evaluations, use a descriptive label that captures the method.

**Grouping rules:**
- Group the same instrument referred to differently (e.g. "MMLU" and "Massive Multitask Language Understanding"; "User study" and "Human preference evaluation" when they clearly describe the same procedure)
- DO NOT group different subsets (e.g. "HELM Math" vs "HELM Code", "MMLU" vs "MMLU Math")
- DO NOT group distribution-shift variants as the parent (e.g. "ImageNet-A" ≠ "ImageNet")
- DO NOT merge dataset variants with different experimental conditions
- DO NOT merge distinct facets or modalities of an instrument (e.g. "HELM Math" and "HELM Code" are separate facets, not synonyms)
- DO NOT merge different types of human evaluation (e.g. "User preference study" ≠ "Expert annotation evaluation")
- When in doubt, keep separate

**Output format:**
```json
{"groups": {"MMLU": [0, 4], "HumanEval": [2], "User preference study": [6, 9]}, "ungrouped": [1, 3, 5]}
```
`ungrouped` lists IDs that don't match any other row. Every input ID must appear exactly once.

**Input rows:**
[... nodes injected here ...]

Return only the JSON object.
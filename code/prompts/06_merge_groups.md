# Prompt: Merge Groups Across Batches

**Pipeline step:** Harmonization — Hierarchical Merge  
**Models:** Gemini 2.5 Pro  
**Source:** `misc/prompts.py` → `MERGE_GROUPS_PROMPT`  
**Called from:** `scripts/llm_aggregator.py:_merge_groups_batch()`  

> **Note:** The `{node_type}` and `{output_example_json}` placeholders are filled at runtime. The groups JSON is appended after this template.

---

You are merging groups of {node_type} that were created from different batches. Some groups may refer to the same concept even though they were processed separately.

Each input group has an `id`. Output only the merge mapping as `{{canonical_name: [ids]}}`. All metadata (definitions, papers, snippets) is resolved from the IDs programmatically — do NOT repeat them.

**Task:**
Review all groups below and merge any that refer to the same concept.

**Canonical name rules:** Use the most specific/common community-standard name. Sentence case. For measurement instruments, include the subset if applicable.

**Merge rules:**
- ONLY merge groups that refer to the EXACT SAME concept (true synonyms)
- DO NOT merge hierarchical relationships — "Reasoning" and "Mathematical Reasoning" are DIFFERENT and should stay separate
- DO NOT merge parent-child relationships — keep specialized variants separate
- DO NOT merge distinct facets of a broader concept (e.g. "Mathematical reasoning" and "Commonsense reasoning" are separate facets, not synonyms)
- For measurement instruments: DO NOT merge different datasets, subsets, or evaluation types (e.g. "HELM Math" ≠ "HELM Code"; "MMLU" ≠ "MMLU Math"; "User preference study" ≠ "Expert annotation evaluation")
- Be VERY conservative: if unsure, keep them separate

**Output format:**
```json
{{"groups": {{"Reasoning": [0, 3], "Mathematical reasoning": [1], "MMLU": [2, 5]}}, "ungrouped": [4, 6]}}
```
`ungrouped` lists IDs that don't match any other group. Every input ID must appear exactly once.

**Input groups:**
{groups_json}

Return only the JSON object.
# Prompt: Aggregate Behaviors

**Pipeline step:** Harmonization — Behavior Grouping  
**Models:** Gemini 2.5 Pro  
**Source:** `misc/prompts.py` → `build_aggregate_grouping_prompt('behaviors', ...)`  
**Called from:** `scripts/llm_aggregator.py:group_nodes_llm()`  

> **Note:** The `[... nodes injected here ...]` placeholder is replaced at runtime with a JSON array of behavior nodes from all papers.

---

Deduplicate behaviors (observable tasks, outputs, performance outcomes, and non-task observable phenomena like hallucination, sycophancy, memorization — not latent constructs, not measurement instrument names) by grouping rows that name the **exact same behavior** under different wording.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat definitions, papers, or snippets.

**Canonical name rules:** concise, community-standard noun phrase. Sentence case.
- **Drop trailing filler words** "ability", "capability", "capacity", "skill" when they are a separate word: "Generation capability" → "Generation", "Prediction ability" → "Prediction"
- **Keep compound words** where the suffix is integral: "Interpretability", "Scalability" stay as-is

**Grouping rules:**
- Group the same observable outcome said differently (e.g. "Query Rephrasing" and "Search Query Rephrasing"; "Text Response Generation" and "Text Generation"; "Hate Speech Detection" and "Hateful Content Detection")
- DO NOT group behaviors that differ in their core action (e.g. "Robotic Action Prediction" ≠ "Robotic Action Generation" — predicting is not the same as generating)
- DO NOT group clearly distinct behaviors (e.g. "Code Generation" vs "Answer Generation"; "Instruction Following" vs "Text Generation")
- DO NOT merge specific task instances into a generic umbrella (e.g. "Moving Sliding Door" ≠ "Task Completion")
- DO NOT merge different methods/strategies into one (e.g. "Beam Search Decoding" ≠ "Monte Carlo Tree Search")
- DO NOT merge distinct facets of a broader behavior (e.g. "Mathematical problem solving" and "Code debugging" are separate facets, not synonyms)
- Test: if you swapped one name for the other in a results table, would the row describe the same experiment? If not, keep separate
- When in doubt, keep separate

**Output format:**
```json
{"groups": {"Code generation": [0, 4], "Question answering": [2]}, "ungrouped": [1, 3, 5]}
```
`ungrouped` lists IDs that don't match any other row. Every input ID must appear exactly once.

**Input rows:**
[... nodes injected here ...]

Return only the JSON object.
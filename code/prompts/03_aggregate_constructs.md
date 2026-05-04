# Prompt: Aggregate Constructs

**Pipeline step:** Harmonization — Construct Grouping  
**Models:** Gemini 2.5 Pro  
**Source:** `misc/prompts.py` → `build_aggregate_grouping_prompt('constructs', ...)`  
**Called from:** `scripts/llm_aggregator.py:group_nodes_llm()`  

> **Note:** The `[... nodes injected here ...]` placeholder is replaced at runtime with a JSON array of construct nodes from all papers.

---

Deduplicate constructs (latent LLM capabilities, risks, traits) by grouping rows that name the **exact same concept** under different wording.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat definitions, papers, or snippets.

**Canonical name rules:** concise, community-standard noun phrase. Sentence case.
- **Drop trailing filler words** "ability", "capability", "capacity", "skill" when they are a separate word: "Reasoning ability" → "Reasoning", "Self-evolution capability" → "Self-evolution", "Retrieval capability" → "Retrieval"
- **Keep compound words** where the suffix is integral: "Interpretability", "Editability", "Learnability", "Scalability" stay as-is

**Grouping rules:**
- Group the same concept said differently (e.g. "Reasoning" and "Reasoning Ability")
- DO NOT group similar but distinct concepts (e.g. "Reasoning" vs "Logical Reasoning")
- DO NOT group hierarchical variants (e.g. "Reasoning" vs "Mathematical Reasoning" — keep separate)
- DO NOT merge qualified/scoped variants into a bare parent (e.g. "Adversarial Robustness" ≠ "Robustness"; "In-context Learning" ≠ "Knowledge")
- DO NOT merge distinct facets of a broader concept (e.g. "Mathematical reasoning", "Spatial reasoning", "Commonsense reasoning" are each their own group — they are facets of "Reasoning", not synonyms)
- Test: would a domain expert use the two names *interchangeably*? If not, keep separate
- When in doubt, keep separate

**Output format:**
```json
{"groups": {"Reasoning": [0, 3], "Logical reasoning": [5]}, "ungrouped": [7, 12]}
```
WRONG canonical names (trailing filler word) → RIGHT:
- "Self-evolution capability" → "Self-evolution"
- "Generation capability" → "Generation"
- "Retrieval capability" → "Retrieval"
- "In-context learning ability" → "In-context learning"
- "Implicit knowledge base capacity" → "Implicit knowledge base"

`ungrouped` lists IDs that don't match any other row. Every input ID must appear exactly once.

**Input rows:**
[... nodes injected here ...]

Return only the JSON object.
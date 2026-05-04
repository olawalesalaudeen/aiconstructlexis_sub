# Prompt: Characterize Entities

**Pipeline step:** Characterization  
**Models:** Gemini 2.5 Flash  
**Source:** `misc/prompts.py` → `CHARACTERIZE_ENTITIES_PROMPT`  
**Called from:** `scripts/synthesize_definitions_batch.py` (production batch version; the older sync `scripts/synthesize_definitions.py` has been moved to `DEP/scripts/`).

> **Note:** The `{entities_json}` placeholder is replaced at runtime with a batch of entities and their paper-sourced definitions.

---

You are given a batch of entities from a nomological network of LLM research.
For each entity, you receive:
- its **canonical name** and **type** (construct, measurement instrument, or behavior/task)
- every **original definition** extracted from different papers (with paper titles)
- every **source snippet** (verbatim quotes from papers)
- every **relationship** this entity participates in, with evidence quotes

Your task: write a rich **summary of use** (4-8 sentences) for each entity that reads as a mini literature review — synthesizing how the field defines, operationalizes, and relates to this concept across the provided papers.

**Writing style:**
- Write as a field synthesis, NOT as a dictionary definition. Use language like "most commonly described as…", "some authors define it as…, though the prevailing usage…", "in the literature, this is typically operationalized via…", "across the surveyed work…"
- **Tone: descriptive and neutral — HARD CONSTRAINT.** NEVER use the words "crucial", "important", "essential", "significant", or "key" — even when paraphrasing a paper. Replace with frequency-based alternatives: "commonly", "widely", "frequently", "prevalent", "a recurring theme", "a popular instrument". If a paper says something is "crucial", paraphrase as "widely discussed" or "commonly targeted"
- Highlight agreement, disagreement, and dominant framings across papers
- Weave in **specific evidence**: quote or paraphrase key findings from the source snippets when they illuminate how the concept is used (e.g. "As one study notes, '…' (Paper Title)")
- Name **specific measurement instruments** (benchmarks, user studies, etc.) used to measure or operationalize the concept
- Describe the entity's **role in the broader network**: what it influences, what influences it, and what it is measured by — referencing the relationship evidence
- For entities with only one source paper, still provide a rich description drawing on all available definitions, snippets, and relationships
- Do NOT start with "X is…" as a flat definition. Start with how the field treats the concept.

Be precise and grounded in the evidence. Do not invent information not present in the inputs.

**Output format — JSON object mapping entity name to characterization string:**
```json
{{
  "Entity A": "Characterization text...",
  "Entity B": "Characterization text..."
}}
```

Return ONLY the JSON object.

**Entities to characterize:**
{entities_json}
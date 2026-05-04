# Prompt: Extract Relationships (Pass 2)

**Pipeline step:** Extraction — Phase 2  
**Models:** Same 3 models  
**Source:** `misc/prompts.py` → `EXTRACT_RELATIONSHIPS_PROMPT`  
**Called from:** `scripts/multi_model_mv.py` → `scripts/batch_majority_vote.py:build_relationship_jsonl()`  

> **Note:** The `{entities_json}` placeholder is replaced at runtime with the entities extracted in Phase 1.

---

Your task is to act as a research assistant. You are given an academic paper and a set of **already-extracted entities** (constructs, measurement instruments, behaviors). Extract **relationships** between these entities that are explicitly supported by the paper text.

## Already-Extracted Entities

{entities_json}

## Relationship Extraction Rules

- **ONLY use entities from the list above** as source and target. Do NOT introduce new entity names.
- **`type` must be exactly one of:**
  - `causes` — explicit or strong causal claim ("X improves Y", "X enables Y", "X leads to Y")
  - `correlates` — empirical association, regression, or "predicts" in the statistical sense ("X is associated with Y", "higher X corresponds to higher Y")
  - `measured_by` — a construct or behavior is evaluated/operationalized by a measurement instrument ("We evaluate X using benchmark Y", "We conducted a user study to assess X")
  - `related` — a stated conceptual or empirical link that is NOT merely co-occurrence. The paper must describe HOW or WHY the two entities are connected.

### Evidence Quality Rules (STRICT)

- **`evidence`:** must be a **quoted substring** from the paper that **directly describes the connection** between source and target — not just mentions both in the same sentence.
- **Do NOT extract a relationship just because two entities appear in the same list, table, or sentence.** Listing instruments together (e.g. "we evaluate on MMLU, HumanEval, and GSM8K") does NOT create relationships between those instruments.
- **Do NOT extract a relationship if the evidence only shows co-occurrence** (e.g. "We test reasoning and code generation" does NOT mean reasoning → code generation).
- The evidence must answer: **"What does the paper say about how/why these two entities are connected?"** If you cannot answer that from the quote, do not include the relationship.

WRONG — co-occurrence, no stated connection:
  source: "Reasoning", target: "Code generation", evidence: "We conduct experiments on reasoning tasks (language understanding, code generation, and mathematical reasoning)"

RIGHT — stated connection:
  source: "Reasoning", target: "Aesthetic understanding", evidence: "to make further development of aesthetic understanding, reasoning is essential"

RIGHT — measurement instrument relationship:
  source: "Bias", target: "PAIRS", type: "measured_by", evidence: "We use PAIRS to probe social biases in VLMs"

RIGHT — human evaluation relationship:
  source: "Helpfulness", target: "User preference study", type: "measured_by", evidence: "We conducted a user preference study with 200 participants to evaluate helpfulness"

- **Allowed source–target patterns** (any combination justified by the text):
  - construct ↔ construct
  - construct ↔ behavior
  - construct → measurement instrument (measured_by)
  - measurement instrument → behavior
  - measurement instrument ↔ measurement instrument (e.g. a benchmark suite contains a sub-benchmark, or two instruments measure overlapping domains)
  - behavior ↔ behavior

## Self-Check

After drafting, verify:
- Every source and target name **exactly matches** an entity name from the list above.
- Every evidence quote **appears** in the supplied paper text.
- The evidence **describes a connection**, not just co-occurrence.
- Direction and `type` match the paper's claims.
- Prefer fewer, higher-quality relationships over many weak ones.

## Output Format (JSON)

Return a single JSON object with exactly:
{{
  "relationships": [
    {{
      "source": "Entity Name (from above list)",
      "target": "Entity Name (from above list)",
      "type": "causes | correlates | measured_by | related",
      "evidence": "Quoted text from the paper that directly describes the connection (Section/Table ref)."
    }}
  ]
}}

If no relationships are supported, return `{{"relationships": []}}`.

Return only the JSON object, no additional text.
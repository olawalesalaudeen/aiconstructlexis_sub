# Prompt: Aggregate Relationships

**Pipeline step:** Harmonization — Relationship Mapping  
**Models:** Gemini 2.5 Pro  
**Source:** `misc/prompts.py` → `AGGREGATE_RELATIONSHIPS_PROMPT`  
**Called from:** `scripts/llm_aggregator.py:aggregate_relationships_llm()`  

> **Note:** The `{construct_groups_json}`, `{measurement_groups_json}`, `{behavior_groups_json}`, and `{name_mapping_json}` placeholders are filled at runtime with the harmonized entity groups. The raw relationships are appended after this template.

---

You are a research assistant harmonizing relationships between constructs, measurement instruments, and behaviors extracted from multiple academic papers. Your goal is to deduplicate relationships that describe the same connection under different wordings, resolving them to canonical forms.

**Faithfulness:** Do not invent relationships or nodes. Only map and consolidate what appears in the input relationships and canonical groups.

Given relationships from different papers, your task is to:
1. Map source and target names to their canonical names using the provided harmonized groups
2. Deduplicate relationships (same canonical source-target-type pairs expressed differently)
3. Consolidate evidence from multiple papers for each canonical relationship

There are three types of relationships allowed: `related`, `causal`, and `correlation` - related is basically NOT causal or correlated, but related and important to capture.

**Context - Canonical Groups:**

**Constructs:**
{construct_groups_json}

**Measurement Instruments:**
{measurement_groups_json}

**Behaviors:**
{behavior_groups_json}

**Name Mapping (original -> canonical):**
{name_mapping_json}

**Relationships to aggregate (JSON array):**
{relationships_json}

**Instructions:**
1. For each relationship, map the source and target to canonical names using:
   - First check the name_mapping dictionary (direct mapping)
   - If not found in mapping, search through the groups lists to find which canonical name it belongs to
   - Use the canonical_name from the matching group
2. If multiple relationships have the same canonical source-target-type combination, consolidate them:
   - Combine all evidence into a list
   - List all papers that mention this relationship
   - Count how many papers support this relationship
3. Preserve unique relationships (different canonical source-target-type combinations)

**Allowed relationship `type` values (exactly one):** `related`, `causes`, `correlates`. Preserve the type from the input when mapping to canonical names; if unclear, use `related`.

**Output Format (JSON):**
{{
  "relationships": [
    {{
      "source": "Canonical Construct Name",
      "target": "Canonical Measurement Name",
      "type": "related",
      "evidence": [
        "Quoted evidence from Paper1 (p. 5)",
        "Quoted evidence from Paper2 (Sec. 3)"
      ],
      "papers": ["Paper1", "Paper2"],
      "paper_count": 2
    }},
    {{
      "source": "MMLU",
      "target": "Jailbreak robustness",
      "type": "correlates",
      "evidence": ["Association reported in Paper3 (Table 2)."],
      "papers": ["Paper3"],
      "paper_count": 1
    }}
  ]
}}

Return only the JSON object, no additional text.
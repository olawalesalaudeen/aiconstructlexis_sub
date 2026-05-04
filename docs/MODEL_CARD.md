# Model Card — AI Construct Lexis Extraction Pipeline

**Release:** Beta (NeurIPS 2026 E&D submission)
**System:** Multi-model extraction → harmonization → canonical-MV → characterization → joint merge.
**Output:** the Lexis artifact (see the data card).

## What the system is

The Lexis pipeline is a chained LLM system that consumes published ML/NLP papers (PDF → text) and emits a structured nomological network of constructs, behaviors, and measurement instruments. It is not a single model; it is a sequence of LLM calls, each with a different role and prompt. This card documents what each stage does, which model runs it, and which failure modes the quality-control pass surfaced.

## Stages

| #   | Stage                   | Script                                                                              | Model                                                    | Decoding                                                                                                              |
| --- | ----------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1   | Multi-model extraction  | `code/scripts/multi_model_mv.py` (orchestrating `batch_majority_vote.py` per model) | Gemini 2.5 Pro · GPT-5.4 Mini · Qwen 3.5-397B (Together) | temperature=0, single trial per model per paper                                                                       |
| 2   | Simplify                | `simplify_extracted_results.py`                                                     | none (deterministic)                                     | —                                                                                                                     |
| 3   | Harmonize               | `llm_aggregator.py`                                                                 | Gemini 2.5 Pro                                           | temperature=0, hierarchical-merge group window 5,000                                                                  |
| 4   | Canonical majority vote | `canonical_majority_vote.py`                                                        | none (deterministic)                                     | threshold ≥2 of 3 models per paper, applied at the canonical level                                                    |
| 5   | Characterize            | `synthesize_definitions_batch.py`                                                   | Gemini 2.5 Pro (Google batch API)                        | temperature=0                                                                                                         |
| 6   | Build joint             | `build_joint_network.py`                                                            | none (deterministic)                                     | —                                                                                                                     |
| 7   | Cross-venue LLM merge   | `joint_llm_merge.py`                                                                | Gemini 2.5 Pro                                           | temperature=0                                                                                                         |
| 8   | Joint canonical-MV      | `joint_canonical_mv.py`                                                             | none (deterministic)                                     | threshold ≥2 of 3 models per paper, joint canonical level (entities only; relationships aggregated deterministically) |

Exact production parameters are recorded in `docs/PIPELINE.md`.

## Prompts

The extraction and aggregation prompts live in `docs/prompts/`:

- `01_extract_entities.md` — per-paper entity extraction
- `02_extract_relationships.md` — per-paper relationship extraction
- `03_aggregate_constructs.md` — semantic grouping of constructs
- `04_aggregate_measurements.md` — semantic grouping of measurement instruments
- `05_aggregate_behaviors.md` — semantic grouping of behaviors
- `06_merge_groups.md` — hierarchical group-merging during harmonization
- `07_aggregate_relationships.md` — relationship harmonization
- `08_characterize_entities.md` — usage characterization synthesis

## Quality control

Reported in detail in Section 3.1 of the paper (Figures 6 and 7). Headline numbers:

**Extraction precision and recall**, against six independent expert annotators on a 20-paper sample, evaluated three ways:

| Reference                                             | Overall P / R | Constructs P / R | Behaviors P / R | Instruments P / R |
| ----------------------------------------------------- | ------------- | ---------------- | --------------- | ----------------- |
| Expert–Expert (pairwise inter-rater)                  | 60 / 33       | 70 / 36          | 29 / 16         | 74 / 41           |
| Model–Expert (avg vs. single expert)                  | 84 / 62       | 85 / 59          | 84 / 47         | 84 / 75           |
| Model–Two-Experts (model vs. OR / AND of two experts) | 97 / 81       | 97 / 81          | 96 / 69         | 98 / 84           |

The pipeline reaches near-ceiling agreement with what two experts both endorse, and is systematically more conservative than any individual expert.

**Characterization ratings** from six experts on the top 20 entities:
- 82.5 % of 120 ratings on the agree side; 5.8 % disagree.
- Krippendorff's α = 0.78 (interval); above the conventional acceptable-reliability threshold.
- No entity receives a majority disagreement.

## Failure modes surfaced by QC

1. **Behaviors are the hardest category.** Even pairwise expert–expert recall on behaviors is only 47 % — there is genuine ambiguity in how tasks-as-behaviors are individuated. The pipeline's lower behavior recall partly inherits this.
2. **Long-tail under-extraction.** Recall trails precision throughout, indicating the pipeline omits idiosyncratic single-paper mentions rather than fabricating entities. Users should not treat absence as evidence of non-use.
3. **Anthropomorphic phrasing.** Some characterizations of cognitive constructs (notably *Reasoning*) describe them as "cognitive abilities," which a fraction of expert reviewers flagged as a belief, not a demonstrated property. Interpret characterizations as descriptive of literature usage, not as endorsement.
4. **Unsettled construct boundaries.** Generalization, Robustness, Safety, and Text generation drew the most expert push-back, often on whether the entity was correctly typed (construct vs. behavior vs. measure). These are the items where the literature itself disagrees.
5. **Surface-variant merging is imperfect.** Hierarchical harmonization may collapse near-synonyms or, conversely, leave variants un-merged when their phrasings diverge significantly. Inspect `original_names` for any canonical entity used in a downstream claim.
6. **Citation extraction is text-driven.** Source-snippet evidence is extracted from paper text; figures, tables, and appendices may yield weaker context than abstracts and method sections.

## Known biases of the model system itself

- **Frontier-LLM bias.** All three extraction models are large frontier or near-frontier LLMs trained on web-scale data; they share a common notion of "what counts as a construct" that may differ from social-science measurement theory.
- **English-only.** Prompts and source papers are English; non-English evaluation literature is not covered.
- **Cutoff bias.** Models' pre-training cutoffs influence their familiarity with specific benchmarks; very recent benchmarks (released late 2024 / 2025) may be extracted with lower fidelity than well-established ones.

## Ethical considerations and intended use

The pipeline does not produce model performance scores or rankings. It produces a structured map of evaluation vocabulary. Misuse risks are correspondingly low. The primary risk is over-reliance: treating the Lexis's canonical groupings or characterizations as authoritative when they are best understood as descriptive hypotheses.

## How to reproduce

See `code/README.md` and `docs/PIPELINE.md`. End-to-end reproduction requires API access to Google (Gemini 2.5 Pro), OpenAI (GPT-5.4 Mini), and Together (Qwen 3.5-397B), plus the source paper PDFs for each venue.

## License

MIT (pipeline code). Source-paper text is processed under fair-use rationale; the artifact ships only metadata and short verbatim quotations.

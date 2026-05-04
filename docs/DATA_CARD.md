# Data Card — AI Construct Lexis

**Release:** Beta (NeurIPS 2026 E&D submission)
**Artifact:** `network_data/joint_progressive/joint_v7_final.json`
**Headline counts:** 776 constructs · 653 behaviors · 1,608 measurement instruments · 5,891 relationships, derived from 8,000+ LLM-related papers across seven recent ML/NLP venues.

## Dataset summary

The Lexis is a structured nomological network linking three kinds of entities used to evaluate language models — *constructs* (abstract properties such as reasoning, robustness, safety), *behaviors* (observable phenomena such as text generation, hallucination), and *measurement instruments* (benchmarks, datasets, and protocols such as MMLU, GSM8k, human evaluation) — together with the *relationships* among them as they appear in the published literature. Each entity carries: a canonical name, the surface variants seen in source papers, the papers that reference it (with per-venue counts), source-snippet evidence, and an LLM-synthesized characterization of how the field uses it.

## Source venues (Table 1 of the paper)

| Venue   | Year | LLM-related papers / Total |
| ------- | ---- | -------------------------: |
| ICLR    | 2024 |                513 / 2,260 |
| NeurIPS | 2024 |                731 / 4,494 |
| ICLR    | 2025 |              1,365 / 3,703 |
| NAACL   | 2025 |                  551 / 638 |
| ACL     | 2025 |              1,420 / 1,602 |
| ICML    | 2025 |                992 / 3,330 |
| EMNLP   | 2025 |              2,767 / 3,618 |

LLM-relatedness was determined by an LLM screening pass over each venue's full proceedings.

## Composition

- **Entities:** every entity has a canonical name, a list of original surface variants, paper-of-occurrence pointers, per-venue paper counts, and a usage characterization synthesized from source snippets.
- **Relationships:** typed edges (e.g., `measured_by`, `related`, `enables`) between two canonical entities, with paper-of-occurrence and evidence snippets.
- **Languages:** English-only (the underlying papers are English).
- **Time span:** ICLR 2024 through EMNLP 2025.
- **Filtering:** at the canonical level, only entities for which ≥ 2 of 3 extraction models agreed survive into the final artifact. Relationships are aggregated deterministically by canonical `(source, target, type)` triple.

## Intended uses

- Audit and compare benchmark practices (jingle / jangle analysis).
- Generate falsifiable hypotheses about what existing benchmarks actually measure.
- Identify under-validated constructs, redundant benchmarks, and orphaned evaluation methods.
- Support meta-analyses and longitudinal studies of evaluation vocabulary.

## Out-of-scope uses

- The Lexis is descriptive of the *literature*, not prescriptive of *correct* construct definitions. It should not be used as a normative reference for construct meaning.
- It is not a leaderboard or benchmark scorecard — paper counts indicate frequency of mention, not quality or correctness of usage.
- It is not a substitute for reading the source papers when making strong scholarly claims about a specific construct.

## Known biases and limitations

- **Venue bias.** Coverage is restricted to seven recent ML/NLP conferences; ML4H, FAccT, AAAI, ACM, IEEE, and other venues are not included. Industry whitepapers, blog posts, and arXiv-only work are not represented.
- **Recency bias.** ICLR'24 onward; older constructs that have fallen out of vogue are under-represented.
- **Topic bias.** LLM-screening selects for LLM-related papers; constructs and instruments specific to non-LLM ML (vision, RL, tabular, fairness without LLM angle) appear only when they are referenced from an LLM paper.
- **Frontier-model bias.** Benchmarks designed for frontier LLMs (GSM8k, MMLU, HumanEval) dominate the measurement-instrument distribution; legacy NLP benchmarks are under-represented.
- **Extraction bias.** Three frontier LLMs propose entities; the canonical majority vote keeps only entities ≥ 2 models agree on. This is conservative — long-tail terms used by a single paper or named idiosyncratically may be dropped. Quality control measures this: see the model card.
- **Surface-variant resolution.** Harmonization may merge near-synonyms imperfectly; users should treat the canonical name as a *clustering hypothesis*, not a definitional claim.
- **Characterization is synthesized, not authoritative.** Each entity's usage characterization is an LLM-summary of source snippets; it captures how the literature uses the term but is not a peer-reviewed definition.

## Update cadence

The Lexis is designed for incremental release. New venues are appended via the joint update pipeline (see `code/update_joint_network.sh`) using the prior release's name mapping as a seed so canonical names align across releases. The changelog (`docs/CHANGELOG.md`) tracks added, removed, renamed, and re-typed entities between releases.

## Citation

Anonymous — to be added in the camera-ready version. Cite the NeurIPS 2026 E&D paper.

## License

MIT (see `LICENSE`). The underlying papers retain their original copyright; the Lexis ships only metadata and short verbatim quotations as evidence under fair-use rationale.

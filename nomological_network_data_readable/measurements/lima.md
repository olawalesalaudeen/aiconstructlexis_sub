# LIMA
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, LIMA is a natural language dataset with two distinct applications: model evaluation and model training. The most common use described in this set of papers is for evaluation, where it serves as an instrument to measure specific constructs. For instance, LIMA is used to measure `Memorization`, with one study employing it to "test the generalizability of findings" in a non-code domain. Another paper reports using LIMA to measure `Faithfulness`. A different line of work uses LIMA as a training resource. In this context, it is described as a dataset for "instruction fine-tuning" and is used for "additional training" of models, characterized as consisting of "curated prompts and responses designed to teach models to follow specific instructional formats."

## Sources

**[Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)**
> A natural language dataset used to study memorization in a non-code domain to test the generalizability of findings.

## Relationships

### → LIMA
- **Faithfulness** (constructs) — *measured_by*
  - [Data Selection via Optimal Control for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf)
- **Memorization** (constructs) — *measured_by*
  > Finally, we explore RLHF memorization on different task domains by studying memorization on natural language datasets, LIMA (Zhou et al., 2024) and Anthropic HH (Bai et al., 2022). (Section 5.5)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)

# Attribution
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Abstract concept understanding  

## State of the Field

Across the provided literature, 'Attribution' is used in two distinct ways. The most common framing defines it as a model's ability to support its claims with "traceable, source-aligned evidence," enabling auditability and verification. This perspective, concerned with whether a response is "grounded in credible evidence or is fabricated," connects attribution to factuality. In this context, attribution is studied in relation to `Hallucination` and is reported to be a cause of `Interpretability and explainability`. A different line of work, however, defines the concept as the "latent ability to recognize and associate visual content with non-literal, high-level semantic ideas" such as 'freedom' or 'justice'. This version of attribution, focused on abstract concept understanding, is operationalized and measured using the `AbsVis` benchmark, which evaluates how models and humans "associate images with abstract concepts". Thus, the term is used to describe both the grounding of claims in source material and the association of images with abstract ideas.

## Sources

**[TRUST-VL: An Explainable News Assistant for General Multimodal Misinformation Detection](https://aclanthology.org/2025.emnlp-main.285.pdf)**
> The ability of a model to support its claims with traceable, source-aligned evidence, enabling auditability and verification of reasoning steps.

**[2025.emnlp-main.417.checklist](https://aclanthology.org/attachments/2025.emnlp-main.417.checklist.pdf) (as "Abstract concept understanding")**
> The latent ability to recognize and associate visual content with non-literal, high-level semantic ideas such as 'freedom', 'justice', or 'happiness', which are not directly observable in pixel data.

## Relationships

### Attribution →
- **Interpretability and explainability** (constructs) — *causes*
  - [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.513.pdf)
- **AbsVis** (measurements) — *measured_by*
  > Paper title: AbsVis – Benchmarking How Humans and Vision-Language Models "See" Abstract Concepts in Images
  - [2025.emnlp-main.417.checklist](https://aclanthology.org/attachments/2025.emnlp-main.417.checklist.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)

# Self-evaluation
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Inconsistency identification, Self-review  

## State of the Field

Across the provided literature, self-evaluation is a behavior where a model assesses its own generated output, though it is operationalized in several distinct ways. One framing defines it as an LLM scoring the quality of its own summary, with a focus on measuring potential "self-evaluation bias," calculated as "the difference between an LLM’s evaluation score for its own summaries and the average score assigned by other evaluators" (KazMMLU: Evaluating Language Models onKazakh,Russian, and Regional Knowledge ofKazakhstan). Another approach, termed "inconsistency identification," operationalizes this behavior by prompting a model to "reflect on the discrepancies between generated responses and dialogue contexts" and explicitly categorize any inconsistencies it finds (PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support). A third conceptualization, called "self-review," treats it as a final check where an agent assesses the novelty of a generated abstract by comparing it against a database of existing papers (Parameter-Aware Contrastive Knowledge Editing: Tracing and Rectifying based on Critical Transmission Paths). In each case, the model's analytical capabilities are directed inward at its own productions, whether for quality scoring, consistency checking, or novelty assessment.

## Sources

**[KazMMLU: Evaluating Language Models onKazakh,Russian, and Regional Knowledge ofKazakhstan](https://aclanthology.org/2025.acl-long.702.pdf)**
> An LLM assessing the quality of its own generated summary, potentially exhibiting bias in scoring.

**[PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support](https://aclanthology.org/2025.acl-long.1050.pdf) (as "Inconsistency identification")**
> The observable behavior of a model analyzing its own output against a context and explicitly identifying and categorizing types of inconsistencies.

**[Parameter-Aware Contrastive Knowledge Editing: Tracing and Rectifying based on Critical Transmission Paths](https://aclanthology.org/2025.acl-long.1368.pdf) (as "Self-review")**
> A final check where an agent assesses the novelty of a generated abstract by comparing it against a database of existing papers.

## Relationships

### Self-evaluation →
- **Text generation** (behaviors tasks) — *causes*
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Entropy** (measurements) — *measured_by*
  - [AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf)

### Associated with
- **Evaluation** (behaviors tasks)
  - [Do LLMs estimate uncertainty well in instruction-following?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf)

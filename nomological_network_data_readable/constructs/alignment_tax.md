# Alignment tax
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

The construct of "Alignment tax" is consistently defined across the provided literature as the degradation of a model's general capabilities or performance on other tasks that results from alignment fine-tuning. This degradation is operationalized in at least two ways. One paper proposes measuring it by evaluating "how far our RLHF policy has drifted from its SFT initialization" ("Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models"). Another approach, noted in a different study, is to use the OpenLLM Leaderboard as a measurement instrument. The alignment tax is positioned within a network of related concepts; it is reported to be caused by a lack of output diversity and, in turn, is described as causing a reduction in a model's faithfulness. Additionally, it is studied in relation to a model's commonsense knowledge.

## Sources

**[Asynchronous RLHF: Faster and More Efficient Off-Policy RL for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b99315234cc95e6ef281f9155b68832-Paper-Conference.pdf)**
> The degradation of a model's general capabilities or performance on other tasks as a result of being fine-tuned to align with specific human preferences or safety objectives.

## Relationships

### Alignment tax →
- **OpenLLM Leaderboard** (measurements) — *measured_by*
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Factuality** (constructs) — *causes*
  - [Controlled Low-Rank Adaptation with Subspace Regularization for Continued Training on Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)

### → Alignment tax
- **Output diversity** (constructs) — *causes*
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)

### Associated with
- **Commonsense knowledge** (constructs)
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)

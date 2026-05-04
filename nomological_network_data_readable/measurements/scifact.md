# SciFact
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, SciFact is consistently described as a dataset or benchmark for scientific fact-checking. The task requires verifying claims against evidence from scientific literature, with the source of evidence most commonly defined as "evidence sentences from research papers," though a few papers specify "research abstracts." In this capacity, SciFact is used to measure the behavior of `Fact checking` and the construct of `Domain-specific knowledge`. One paper situates it among "medical datasets," highlighting its use in specialized domains. It is also characterized as a "challenging" dataset due to a high ratio of out-of-corpus terms and is noted as being part of the BEIR benchmark. One source specifies its size as containing "809 training, 300 test claims." More broadly, it serves as an instrument for the general `Evaluation` of models.

## Sources

**[AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.334.pdf)**
> Scientific fact-checking dataset where claims are verified using evidence sentences from research papers, often requiring citation context.

## Relationships

### → SciFact
- **Fact checking** (behaviors tasks) — *measured_by*
  - [CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Claim verification** (behaviors tasks) — *measured_by*
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)

# Databricks Dolly-15k
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Databricks-Dolly-15k, Dolly, Dolly-15k  

## State of the Field

Across the provided sources, Databricks Dolly-15k is consistently described as an open-source, human-generated, instruction-following dataset. One paper specifies that it is composed of 15,000 instruction-response pairs, with another noting its records span categories like brainstorming, question answering, and summarization. The dataset is used in two primary ways within the literature: for fine-tuning models and for evaluation. Several papers employ it for downstream adaptation and supervised fine-tuning, for example, to train models on instruction following or to test phenomena like attack durability and safety degradation. Other work uses it as an evaluation task for decoding experiments. As a measurement instrument, Databricks Dolly-15k is used to assess specific behaviors, with the provided data showing it measures both "Dialogue generation" and "Refusal to answer".

## Sources

**[Multi-Draft Speculative Sampling: Canonical Decomposition and Theoretical Limits](https://proceedings.iclr.cc/paper_files/paper/2025/file/04cdf500730af7733a6b13cbbc230206-Paper-Conference.pdf) (as "Databricks-Dolly-15k")**
> An instruction-following dataset used as an evaluation task for decoding experiments.

**[Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf) (as "Dolly")**
> An open-source dataset of human-generated instruction-following records used to fine-tune large language models for instruction following and dialogue generation.

**[Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf) (as "Dolly-15k")**
> An instruction-following dataset with records across categories like brainstorming and question answering, used for supervised fine-tuning to evaluate attack durability.

## Relationships

### → Databricks Dolly-15k
- **Refusal to answer** (behaviors tasks) — *measured_by*
  - [LT-Defense: Searching-free Backdoor Defense via Exploiting the Long-tailed Effect](https://proceedings.neurips.cc/paper_files/paper/2024/file/064f6bcd7d3c72fb187bfca35ba2bfd4-Paper-Conference.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  - [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf)

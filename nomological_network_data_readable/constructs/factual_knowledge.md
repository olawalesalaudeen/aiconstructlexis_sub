# Factual knowledge
**Type:** Construct  
**Referenced in:** 16 papers  

## State of the Field

Across the surveyed literature, factual knowledge is most commonly defined as the extent to which a model has encoded, stored, and can accurately retrieve verifiable information about the world. Some papers offer more specific framings; for instance, one line of work treats it as an internal representation of facts structured as subject-relation-object triples, while another describes it as a "latent store of accurate world knowledge encoded in a model's parameters." This knowledge is understood to be derived from pretraining data, with one paper tracing hallucinations back to the pretraining corpora. The construct is primarily studied through the "factual evaluation of the pretrained language models" using various benchmarks. Papers in this set operationalize factual knowledge using several measurement instruments, including the Massive Multitask Language Understanding (MMLU) dataset, the Zero-Shot Relation Extraction (ZSRE) dataset, and COUNTERFACT.

## Sources

**[SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)**
> The extent to which a model has encoded and can accurately retrieve factual information about the world.

## Relationships

### Factual knowledge →
- **MMLU** (measurements) — *measured_by*
  - [SelectIT: Selective Instruction Tuning for LLMs via Uncertainty-Aware Self-Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b130a5691815f550977e331f8bec08ae-Paper-Conference.pdf)
- **CounterFact** (measurements) — *measured_by*
  - [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
- **zs-RE** (measurements) — *measured_by*
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **TimeQA** (measurements) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
- **PopQA** (measurements) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)

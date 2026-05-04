# PubHealth
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, PubHealth is consistently defined as a fact verification dataset focused on the public health domain. Its primary application is to measure model capabilities related to factuality, with papers using it to assess constructs like fact checking and domain-specific knowledge. The dataset is composed of public health-related claims, and its use is frequently specified as a "closed-set factual verification" task, as described in "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection". Beyond these specific constructs, it is also used more broadly for general evaluation purposes. Some research also includes PubHealth alongside other datasets like PopQA and ASQA in ablation studies. The surveyed papers thus position PubHealth as an instrument for evaluating a model's ability to verify domain-specific information.

## Sources

**[Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)**
> A fact verification dataset about public health used to evaluate closed-set factual verification performance.

## Relationships

### → PubHealth
- **Domain-specific knowledge** (constructs) — *measured_by*
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Fact checking** (behaviors tasks) — *measured_by*
  - [CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf)

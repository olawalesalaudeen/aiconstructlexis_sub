# SQuAD v1.1
**Type:** Measurement  
**Referenced in:** 86 papers  
**Also known as:** SQuAD, SQuADv1.1, SQUAD, Squad  

## State of the Field

Across the provided literature, SQuAD v1.1 is consistently characterized as a benchmark for reading comprehension and question answering. The task is almost universally defined as extractive question answering, requiring a model to identify an answer as a direct "segment of text from a corresponding Wikipedia article" (Longhorn: State Space Models are Amortized Online Learners). Its most frequent application is to evaluate model performance on this task, with papers often reporting F1 and Exact Match scores. Beyond this primary function, SQuAD v1.1 is also used to measure a wider set of behaviors, including knowledge recall, language understanding, and generalization. It is commonly employed in the context of evaluating fine-tuned or compressed models. A less frequent use case, mentioned by one study, is leveraging the dataset as a source of prompts for model regularization. The data also shows it being paired with other datasets to assess continual learning.

## Sources

**[Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf) (as "SQuAD")**
> SQuAD (Stanford Question Answering Dataset) is an open-book question answering dataset used for evaluation.

**[Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf) (as "SQuADv1.1")**
> Stanford Question Answering Dataset version 1.1, a reading comprehension task where models identify answer spans in a passage given a question, used to evaluate question answering performance.

**[Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)**
> The Stanford Question Answering Dataset v1.1 is a reading comprehension benchmark for extractive question answering.

**[GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf) (as "SQUAD")**
> The Stanford Question Answering Dataset, a crowdsourced reading comprehension benchmark consisting of questions posed on a set of Wikipedia articles.

**[Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf) (as "Squad")**
> The Stanford Question Answering Dataset (SQuAD) is a reading comprehension benchmark where the answer to every question is a segment of text from a corresponding Wikipedia article.

**[A Lens into Interpretable Transformer Mistakes via Semantic Dependency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25n/dong25n.pdf) (as "SQuAD 1.1")**
> The Stanford Question Answering Dataset (version 1.1), a reading comprehension benchmark where answers are text spans extracted from a given Wikipedia article.

## Relationships

### → SQuAD v1.1
- **Question answering** (behaviors tasks) — *measured_by*
  > We apply our evaluation method to the Stanford Question Answering Dataset (SQuAD) 1.1 (Rajpurkar et al., 2016), which comprises context paragraphs extracted from Wikipedia articles, along with manually crafted questions and their corresponding correct answers.
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > “tasks including classification, multiple-choice questions, and content generation.”
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Continual learning** (constructs) — *measured_by*
  > “Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA to inject more complex, multi-hop reasoning data after simpler QA”
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  > To evaluate the fact recall ability of the adapted model, we use two question answering (QA) datasets, SQuAD (Rajpurkar et al., 2016) and StreamingQA (Liska et al., 2022)... (Section 4.1)
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  > Here, we consider the scenario where the model needs to adapt to new knowledge based on documents. ... we use two question answering (QA) datasets, SQuAD (Rajpurkar et al., 2016) and StreamingQA (Liska et al., 2022)
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Machine reading comprehension** (behaviors tasks) — *measured_by*
  - [Mutual-Taught](https://aclanthology.org/2025.acl-long.795.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [VMLUBenchmarks: A comprehensive benchmark toolkit forVietnameseLLMs](https://aclanthology.org/2025.acl-long.564.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [M+: Extending MemoryLLM with Scalable Long-Term Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25au/wang25au.pdf)
- **Factual question answering** (behaviors tasks) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Prompt engineering** (behaviors tasks) — *measured_by*
  - [Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf)

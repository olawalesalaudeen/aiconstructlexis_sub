# QQP
**Type:** Measurement  
**Referenced in:** 22 papers  

## State of the Field

Across the provided literature, QQP is consistently defined as a benchmark for evaluating whether two questions are semantically equivalent. Its primary and most common application is to measure the behavior of `paraphrase identification`, a task also referred to as duplicate question detection or recognition. The dataset, identified as the Quora Question Pairs dataset, is described as consisting of question pairs annotated with a binary value indicating if they are paraphrases. A recurring point across the sources is that QQP is a component of the GLUE benchmark, where it is frequently evaluated alongside other language understanding tasks. While its main use is for paraphrase detection, a few papers also employ QQP to measure other constructs. For instance, it is used to assess `adversarial robustness`, sometimes in an "adversarially perturbed form," and to evaluate model `generalization` on NLU tasks. The benchmark is applied in diverse evaluation settings, including the assessment of fine-tuned models, in-context learning, and language model distillation.

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)**
> A paraphrase identification benchmark used to evaluate whether two questions are semantically equivalent.

## Relationships

### → QQP
- **Paraphrase identification** (behaviors tasks) — *measured_by*
  > (5) Paraphrase Identification (QQP): determine if two questions are “equivalent” or “not equivalent” (Section 4.6)
  - [DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e016430ec3b2f02222ac8f9f93db2eb-Paper-Conference.pdf)
- **Paraphrase detection** (behaviors tasks) — *measured_by*
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > "Datasets. We adopt two datasets: SST-2 (Socher et al., 2013) is a sentiment classification task ... and QQP (Wang et al., 2019) is a task where we need to determine whether two sentences are paraphrases of each other."
  - [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > The first five datasets are used to evaluate performance against SSL baselines, while the remaining three assess generalization on NLU tasks. (Section 4.1)
  - [MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf)

### Associated with
- **GLUE** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): Sentiment Analysis (SST-2), Duplicate Question Detection (QQP)...
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)

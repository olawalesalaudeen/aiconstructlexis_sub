# Reading comprehension
**Type:** Construct  
**Referenced in:** 30 papers  

## State of the Field

Across the surveyed literature, reading comprehension is defined as the ability for "understanding and extracting information from written passages to answer questions or complete tasks" (CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation). This behavior is operationalized and measured through a wide variety of benchmarks. The most frequently cited instrument for this purpose is BoolQ, which papers explicitly use for assessing reading comprehension. Other commonly used benchmarks include RACE, SQuAD (both v1.1 and v2.0), and DROP. The field also employs a broad set of additional datasets for its evaluation, such as ARC, OpenBookQA, CoQA, and TyDi QA, with one paper specifying the use of "the Indonesian set from TyDi QA... based on Indonesian Wikipedia with human-written questions" (V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models). While most papers directly link these instruments to reading comprehension, one source snippet connects the RACE benchmark to "reading reasoning capabilities," suggesting a closely related framing. The behavior is also studied alongside other concepts like commonsense knowledge and faithfulness.

## Sources

**[CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation](https://aclanthology.org/2025.emnlp-main.37.pdf)**
> Understanding and extracting information from written passages to answer questions or complete tasks.

## Relationships

### Reading comprehension →
- **BoolQ** (measurements) — *measured_by*
  > BoolQ (Clark et al., 2019) for reading comprehension and binary question answering (Section 5.1.1).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **RACE** (measurements) — *measured_by*
  > “we define five fundamental LLM capabilities, namely Mathematical Reasoning, Reading Comprehension, Commonsense Reasoning, Scientific Reasoning, and Professional Expertise”
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **DROP** (measurements) — *measured_by*
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
- **SQuAD 2.0** (measurements) — *measured_by*
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **CoQA** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
- **Belebele** (measurements) — *measured_by*
  - [CoRAC: Integrating SelectiveAPIDocument Retrieval with Question Semantic Intent for Code Question Answering](https://aclanthology.org/2025.naacl-long.629.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **C3** (measurements) — *measured_by*
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
- **SQuAD v2.0** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
- **WikiHop** (measurements) — *measured_by*
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **CosmosQA** (measurements) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **MultiRC** (measurements) — *measured_by*
  - [Regress, Don’t Guess: A Regression-like Loss on Number Tokens for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zausinger25a/zausinger25a.pdf)
- **OBQA** (measurements) — *measured_by*
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **DocVQA** (measurements) — *measured_by*
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **SciQA** (measurements) — *measured_by*
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)
- **TyDi QA** (measurements) — *measured_by*
  > We adopt the Indonesian set from TyDi QA (Clark et al., 2020) for reading comprehension, which is based on Indonesian Wikipedia with human-written questions. (Section 3.3)
  - [V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models](https://aclanthology.org/2025.emnlp-main.881.pdf)

### Associated with
- **Commonsense knowledge** (constructs)
  - [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf)
- **Faithfulness** (constructs)
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)

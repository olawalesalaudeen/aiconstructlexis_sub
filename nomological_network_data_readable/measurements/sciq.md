# SciQ
**Type:** Measurement  
**Referenced in:** 75 papers  
**Also known as:** SCIQ  

## State of the Field

Across the provided literature, SciQ is consistently characterized as a benchmark for scientific question answering, composed of multiple-choice questions sourced from science exams. While its content is scientific, the benchmark is most frequently used to measure an LLM's `Commonsense understanding` and `Scientific reasoning`, with some sources noting it challenges models to "apply scientific concepts beyond mere fact recall." It is also commonly employed to evaluate a range of other capabilities, including general `Question answering`, `Natural language understanding`, `Text generation` with short responses, and `Generalization`. A smaller set of studies uses SciQ to assess more specific attributes like `Domain knowledge`, `Faithfulness`, and `Text classification`. The dataset is described as containing approximately 13,000 questions, with some papers highlighting its "rich annotations, including supporting evidence." In terms of evaluation protocol, SciQ is frequently used to report 0-shot accuracy and is included in standardized toolkits like the `LLM Evaluation Harness`. One study also leverages the dataset to analyze different types of model errors, distinguishing between inconsistent and self-consistent errors.

## Sources

**[LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)**
> A benchmark for scientific question answering, consisting of multiple-choice questions sourced from science exams.

**[ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf) (as "SCIQ")**
> A benchmark dataset with about 13,000 multiple-choice science questions.

## Relationships

### → SciQ
- **Commonsense reasoning** (constructs) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Calibrating Expressions of Certainty](https://proceedings.iclr.cc/paper_files/paper/2025/file/66b35d2e8d524706f39cc21f5337b002-Paper-Conference.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  > SciQ measures scientific reasoning, challenging models to apply scientific concepts beyond mere fact recall. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Open-ended question answering** (behaviors tasks) — *measured_by*
  - [LongReward: Improving Long-context Large Language Models withAIFeedback](https://aclanthology.org/2025.acl-long.188.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > PolyNorm outperforms SwiGLU on all tasks, with notable improvements, demonstrating superior generalization capabilities. (Section 4.3)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > The SciQ dataset (Welbl et al., 2017) is used, which contains 13,679 crowdsourced science exam questions about Physics, Chemistry and Biology, among others. (Section 5.1)
  - [Bayesian WeakS-to-Strong from Text Classification to Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/495e55f361708bedbab5d81f92048dcd-Paper-Conference.pdf)
- **Domain knowledge** (constructs) — *measured_by*
  > SciQ (Welbl et al., 2017) for science-related abilities. (Section 3.1)
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  > We include a set of tasks to evaluate the model’s core capabilities of natural language understanding, scientific knowledge, and reasoning. We report the zero-shot performance on ARC-challenge (Clark et al., 2018), ARC-easy (Clark et al., 2018), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PiQA (Bisk et al., 2020), LAMBADA-OpenAI (Paperno et al., 2016), and SciQ (Welbl et al., 2017).
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  > Therefore, we only test on tasks (ARC-easy, Hellaswag, PIQA, SciQ, LAMBADA) in lm-evaluation-harness. (Section 4.1)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)

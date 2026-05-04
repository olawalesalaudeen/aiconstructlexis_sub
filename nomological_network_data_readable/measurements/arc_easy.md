# ARC-Easy
**Type:** Measurement  
**Referenced in:** 192 papers  
**Also known as:** ARC Easy, ARC-easy, Arc-easy, ArcEasy, ARC-E, ARC-e, ARC_e, ARC (Easy), Arc Easy, ARCE, Arc-e, ARC_E  

## State of the Field

Across the provided literature, ARC-Easy is consistently characterized as a multiple-choice question-answering benchmark derived from the AI2 Reasoning Challenge (ARC), specifically containing its easier, grade-school-level science questions. The most prevalent use of this instrument is to measure commonsense reasoning and understanding, a framing supported by numerous definitions and its frequent inclusion in evaluation suites for this purpose. Beyond this primary focus, papers also use ARC-Easy to assess a range of other constructs, including scientific question answering, text generation, generalization, and basic factual knowledge. There is some variation in how the required cognitive process is described, with some papers defining the questions as answerable via "simple retrieval and text-matching," while others frame it more broadly as requiring reasoning. The dominant operationalization is zero-shot evaluation, with only a single mention of a few-shot setting. It is frequently evaluated alongside its more difficult counterpart, ARC-Challenge, as well as other common sense benchmarks like HellaSwag, PIQA, and WinoGrande. Several papers note that evaluations using ARC-Easy are conducted via the LM Evaluation Harness.

## Sources

**[Dynamic Sparse No Training:  Training-Free Fine-tuning for Sparse LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf) (as "ARC Easy")**
> AI2 Reasoning Challenge Easy subset used as a zero-shot question-answering benchmark.

**[Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf) (as "ARC-easy")**
> A subset of the AI2 Reasoning Challenge (ARC) dataset containing easier science questions, used to evaluate question answering ability in a zero-shot setting.

**[Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)**
> Science question answering dataset with easier multiple-choice questions that test basic factual knowledge.

**[Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf) (as "Arc-easy")**
> The easy set from the AI2 Reasoning Challenge (ARC), containing science questions that are answerable with simple retrieval and reasoning.

**[Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf) (as "ArcEasy")**
> A subset of the AI2 Reasoning Challenge (ARC) dataset containing easier science questions that can be answered with simple retrieval and text-matching.

**[Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf) (as "ARC-E")**
> The AI2 Reasoning Challenge (Easy Set), a multiple-choice question-answering dataset of science questions intended to test commonsense reasoning.

**[Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf) (as "ARC-e")**
> An AI2 Reasoning Challenge evaluation set used for zero-shot commonsense question answering.

**[SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf) (as "ARC_e")**
> The AI2 Reasoning Challenge (ARC) Easy Set, a collection of multiple-choice science questions designed to test reasoning.

**[Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf) (as "Arc Easy")**
> A benchmark for commonsense reasoning that features easier, grade-school-level science questions, complementing the Arc Challenge set.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "ARC (Easy)")**
> A multiple-choice question answering benchmark (AI2 Reasoning Challenge) focusing on easy questions.

**[Innovative Image Fraud Detection with Cross-Sample Anomaly Analysis: The Power ofLLMs](https://aclanthology.org/2025.acl-long.688.pdf) (as "ARCE")**
> The AI2 Reasoning Challenge (ARCE) is a multiple-choice question answering benchmark focusing on science questions for elementary and middle school students.

**[Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf) (as "Arc-e")**
> The AI2 Reasoning Challenge (Easy Set), a benchmark of grade-school science questions that are simpler than its challenge counterpart.

**[Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf) (as "ARC_E")**
> AI2 Reasoning Challenge (Easy) dataset containing science questions that require reasoning to answer correctly.

## Relationships

### → ARC-Easy
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  - [TODO: Enhancing LLM Alignment with Ternary Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/fef5607a9b826f1845533f923e308435-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **Scientific question answering** (behaviors tasks) — *measured_by*
  - [Debiasing the Fine-Grained Classification Task inLLMs with Bias-AwarePEFT](https://aclanthology.org/2025.acl-long.718.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We evaluated the trained models on public benchmarks (Fourrier et al., 2023; OpenCompass Contributors, 2023). Table 1 presents the evaluation results. ... These results demonstrate that both EDiT and A-EDiT exhibit strong convergence and generalization capabilities. (Section 4.2)
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **Zero-shot classification** (behaviors tasks) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > The commonsense reasoning tasks contain eight datasets, including six question-answering datasets (i.e., BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), ARC-e (Clark et al., 2018), ARC-c (Clark et al., 2018), and OBQA (Mihaylov et al., 2018))...
  - [STAREat the Structure: SteeringICLExemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **Out-of-distribution detection** (behaviors tasks) — *measured_by*
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **Overfitting** (constructs) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Functional linguistic competence** (constructs) — *measured_by*
  > To assess this, we use six benchmarks covering world knowledge (ARC-EASY, ARC-CHALLENGE (Clark et al., 2018)) (Section 3.3)
  - [Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  > We utilize the LM Eval Harness (Gao et al., 2023) for standardized performance evaluation. (Section 4.1)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)

# BoolQ
**Type:** Measurement  
**Referenced in:** 187 papers  
**Also known as:** Boolq, BOOLQ  

## State of the Field

Across the provided literature, BoolQ is consistently characterized as a question-answering benchmark composed of yes/no questions. The dataset's structure is typically described as consisting of a question, a corresponding passage, and a binary answer. The prevailing use of BoolQ is to evaluate a model's commonsense reasoning and reading comprehension, with many papers listing it as a standard benchmark for these capabilities. It is also frequently employed to assess broader constructs such as general language understanding, question answering, and knowledge retrieval. A recurring application is in the context of zero-shot evaluation, where models are tested on the benchmark without task-specific fine-tuning. In evaluation suites, BoolQ is commonly grouped with other commonsense benchmarks like PIQA, HellaSwag, WinoGrande, and ARC. While most papers use it for its primary purpose, a smaller number of studies adapt it for other uses, such as a text classification task to measure model calibration. Several sources also note that BoolQ is part of the SuperGLUE benchmark.

## Sources

**[AffineQuant: Affine Transformation Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ddfb58b61e7213dfb9e06c695475b2bd-Paper-Conference.pdf)**
> The Boolean Questions dataset, a benchmark for yes/no reading comprehension questions requiring commonsense reasoning.

**[BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf) (as "Boolq")**
> Boolean Questions (Boolq) is a question-answering dataset for yes/no questions where each example consists of a question, a passage, and a binary answer.

**[Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf) (as "BOOLQ")**
> Boolean Questions (Clark et al., 2019) is a question-answering dataset for yes/no questions that are naturally occurring and unprompted.

## Relationships

### → BoolQ
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  > BoolQ (Clark et al., 2019) for reading comprehension and binary question answering (Section 5.1.1).
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > “we evaluate the proposed MoEQuant on various reasoning tasks, including MMLU (Hendrycks et al., 2020), BoolQ (Clark et al., 2019), HellaSwag (Zellers et al., 2019), Openbookqa (Mihaylov et al., 2018), and MathQA (Amini et al., 2019).”
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > We evaluated these models on six different benchmarks ... including PIQA (Bisk et al., 2020), hellaswag (Zellers et al., 2019), BoolQ (Clark et al., 2019), ARC (Clark et al., 2018), winogrande (Sakaguchi et al., 2021) and SIQA (Sap et al., 2019). These tasks examine models’ language understanding, logical reasoning, knowledge utilization, and social awareness capabilities.
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  > “For zero-shot evaluation, we employ BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), WinoGrande (Keisuke et al., 2019), and TruthfulQA (Lin et al., 2022).” (Section 5.4)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
- **Short-context capability** (constructs) — *measured_by*
  > In Table 3, we compare Activation Beacon with the original LLM (Full) on popular benchmarks, including MMLU (Hendrycks et al., 2021), ARC-Challenge (Bhakthavatsalam et al., 2021), BoolQ (Clark et al., 2019), and GSM8K (Cobbe et al., 2021). We can observe that Activation Beacon leads to very little performance degradation on short-context tasks. In other words, the short-context capabilities are well preserved.
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks) — *measured_by*
  - [Path Drift in Large Reasoning Models: How First-Person Commitments Override Safety](https://aclanthology.org/2025.emnlp-main.991.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **Zero-shot classification** (behaviors tasks) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > “The tasks are categorized into five domains: • Knowledge: CommonsenseQA ... BoolQ ...”
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **Knowledge retrieval** (behaviors tasks) — *measured_by*
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **Overfitting** (constructs) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)

### Associated with
- **SuperGLUE** (measurements)
  > For question answering tasks, we utilize BoolQ (from SuperGLUE) (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements)
  > We utilize the LM Eval Harness (Gao et al., 2023) for standardized performance evaluation. (Section 4.1)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **Commonsense170k** (measurements)
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)

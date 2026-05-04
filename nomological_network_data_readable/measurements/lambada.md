# LAMBADA
**Type:** Measurement  
**Referenced in:** 98 papers  
**Also known as:** Lambada, LAMBADA-standard  

## State of the Field

Across the provided literature, LAMBADA is predominantly characterized as a language modeling benchmark designed to evaluate a model's ability to predict the final word of a passage. This task is consistently described as requiring an understanding of broad discourse context and is frequently used to assess a model's capacity to handle long-range dependencies; as one paper states, it is a "last word completion task... to test how models capture long-range dependencies in text." The evaluation is commonly conducted in a zero-shot setting, with accuracy and perplexity being the reported metrics. While its most prevalent application is to measure `Language modeling`, papers also use LAMBADA to assess related constructs such as `Contextual understanding` and `Natural language understanding`. A smaller set of studies frames it as a `Reading comprehension` benchmark, and it is often included in larger evaluation suites to measure general `Downstream task performance` or `Text generation`.

## Sources

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)**
> A language modeling task that evaluates the ability to predict the last word in a sentence requiring broad discourse context, used here to test length prediction reliability.

**[Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf) (as "Lambada")**
> A reading comprehension benchmark included in the expanded evaluation set.

**[MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duanmu25a/duanmu25a.pdf) (as "LAMBADA-standard")**
> The standard version of the LAMBADA dataset for evaluating a model's ability to predict the final word of a text passage.

## Relationships

### → LAMBADA
- **Language modeling** (behaviors tasks) — *measured_by*
  > On LAMBADA, we report ... suffix accuracy by masking all tokens of the last word and predicting all of them in a single forward pass
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > We evaluate quantized LLMs using ... zero-shot accuracy on the benchmarks ARC (Clark et al., 2018), LAMBADA (Paperno et al., 2016), MMLU (Hendrycks et al., 2020), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), and WinoGrande (Sakaguchi et al., 2021) (Section 4).
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf)
- **Contextual understanding** (constructs) — *measured_by*
  > These benchmarks assess different aspects of LLM emergent abilities: Lambada evaluates contextual comprehension, testing the model’s ability to understand long-range dependencies in text. (Section 4.2)
  - [Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > "We evaluate the distilled students on LAMBADA (Paperno et al., 2016) ... We find that SDTT preserves the natural language understanding performance of the teacher."
  - [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > These tasks assess the model performance on logical reasoning, language understanding, commonsense reasoning, and knowledge utilization. (Section 4.1)
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **Text understanding** (constructs) — *measured_by*
  - [Language Models Predict Empathy Gaps Between Social In-groups and Out-groups](https://aclanthology.org/2025.naacl-long.612.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)

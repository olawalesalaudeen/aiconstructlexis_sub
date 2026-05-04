# ARC-Challenge
**Type:** Measurement  
**Referenced in:** 234 papers  
**Also known as:** ARC Challenge, ARC-challenge, ARC-C, ARC-c, Arc-C, ARC (Challenge), ARC challenge, Arc Challenge, Arc-Challenge, Arc-challenge, ARC-easy/challenge, ArcChallenge, ARCC, ARC_C, Arc-c  

## State of the Field

Across the surveyed literature, ARC-Challenge is predominantly characterized as a measurement instrument comprising the difficult "challenge set" from the AI2 Reasoning Challenge. It consists of multiple-choice science questions, often described as grade-school level, that are designed to be hard to answer using simple retrieval or word co-occurrence methods. The benchmark is most frequently used to evaluate a model's reasoning capabilities, particularly `commonsense reasoning`, `scientific reasoning`, and general `question answering`. Papers operationalize this evaluation primarily in zero-shot or few-shot settings, with 3-shot, 10-shot, and 25-shot evaluations being explicitly mentioned. Beyond its core use, ARC-Challenge is also employed to assess broader constructs such as `generalization`, `natural language understanding`, and `downstream task performance`. However, there is a notable disagreement in its definition, with a small minority of papers using the name "ARC challenge" to refer to the "Abstraction and Reasoning Corpus," a benchmark of "novel visual puzzles." A few studies also raise concerns about potential data contamination within the benchmark, with one noting "slight evidence of contamination."

## Sources

**[Dynamic Sparse No Training:  Training-Free Fine-tuning for Sparse LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf) (as "ARC Challenge")**
> The challenge set of the AI2 Reasoning Challenge (ARC), a benchmark consisting of difficult, multiple-choice science questions that are hard to answer with simple retrieval or word co-occurrence.

**[SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf) (as "ARC-challenge")**
> A subset of the AI2 Reasoning Challenge (ARC) dataset containing difficult science questions, used to evaluate question answering ability in a zero-shot setting.

**[Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)**
> A multiple-choice reasoning dataset created from scientific exams used to evaluate closed-set reasoning performance.

**[Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf) (as "ARC-C")**
> The AI2 Reasoning Challenge (Challenge Set), a multiple-choice question-answering dataset of difficult science questions intended to test commonsense reasoning.

**[Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf) (as "ARC-c")**
> An AI2 Reasoning Challenge evaluation set used for zero-shot commonsense question answering.

**[OmnixR: Evaluating Omni-modality Language Models on Reasoning across Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa3e67220ca4cd50010165c950fc8056-Paper-Conference.pdf) (as "Arc-Challenge")**
> A question-answering benchmark based on science questions, considered as a potential source for the Omni×R suite but ultimately not used due to data contamination concerns.

**[Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf) (as "Arc-challenge")**
> Benchmark dataset used to evaluate science question answering.

**[Efficiently Learning at Test-Time: Active Fine-Tuning of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba942323c447c9bbb9d4b638eadefab9-Paper-Conference.pdf) (as "ARC challenge")**
> The Abstraction and Reasoning Corpus (ARC) is a benchmark designed to test abstract reasoning capabilities by requiring the solution of novel visual puzzles.

**[Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d022216357816e483433914204aa80ee-Paper-Conference.pdf) (as "Arc Challenge")**
> A benchmark for commonsense reasoning that features challenging, grade-school-level science questions.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "ARC (Challenge)")**
> AI2 Reasoning Challenge Challenge, a multiple-choice question-answering benchmark used to assess harder downstream reasoning performance.

**[Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f48b5133e89854a9e97cc22a6db83f25-Paper-Conference.pdf) (as "Arc-C")**
> The AI2 Reasoning Challenge (Challenge Set), a benchmark of difficult, grade-school level science questions used to evaluate a model's question answering and reasoning abilities.

**[Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf) (as "ARC-easy/challenge")**
> A multiple-choice science question benchmark used here to evaluate commonsense question answering and math reasoning-related performance.

**[LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf) (as "ArcChallenge")**
> ARC-Challenge benchmark used to evaluate LLM performance on science question answering.

**[Innovative Image Fraud Detection with Cross-Sample Anomaly Analysis: The Power ofLLMs](https://aclanthology.org/2025.acl-long.688.pdf) (as "ARCC")**
> The AI2 Reasoning Challenge - Challenge Set (ARCC) is a difficult subset of the ARC dataset, containing science questions that are hard to answer with simple retrieval-based methods.

**[Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf) (as "Arc-c")**
> Open benchmark assessing commonsense reasoning through challenge sets in science questions.

**[True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf) (as "ARC_C")**
> A benchmark from the Language Model Evaluation Harness used to evaluate zero-shot language understanding and reasoning.

## Relationships

### → ARC-Challenge
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Figure 4 shows the downstream performance on HellaSwag, MMLU Var3, ARC-Challenge, and SciQ. PolyNorm outperforms SwiGLU on all tasks, with notable improvements, demonstrating superior generalization capabilities.
  - [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/725f5e8036cc08adeba4a7c3bcbc6f2c-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019) for assessing the general language understanding and reasoning capabilities...
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We then evaluate it on question answering tasks: MMLU, ARC-Easy and ARC-Challenge. (Section 3.2)
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **Short-context capability** (constructs) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019)
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  - [DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [Selective Attention: Enhancing Transformer through Principled Context Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/14fc4a68da97a3d31eb11c642b0b10fc-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [MoE-SVD: Structured Mixture-of-Experts LLMs Compression via Singular Value Decomposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25az/li25az.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Zero-shot classification** (behaviors tasks) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Scientific question answering** (behaviors tasks) — *measured_by*
  - [Debiasing the Fine-Grained Classification Task inLLMs with Bias-AwarePEFT](https://aclanthology.org/2025.acl-long.718.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > ARC-Challenge introduces a multi-choice question answering dataset, composed of science exam questions from grade 3 to grade 9. (Section 4)
  - [STAREat the Structure: SteeringICLExemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **Out-of-distribution detection** (behaviors tasks) — *measured_by*
  > We fine-tune the LLMs on OBQA (as the ID dataset) and test them on ARC-C, ARC-E, and CSQA (as OOD dataset).
  - [Calibrating LLMs with Information-Theoretic Evidential Deep Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cbdd1e6613c42fe975337671790f406-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *measured_by*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > We evaluate the downstream task accuracy of models derived from the methodology outlined in §2.3 using the following datasets: ARC-Easy (Clark et al., 2018), ARC-Challenge (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2011), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), PIQA (Bisk et al., 2020), WinoGrande (Sakaguchi et al., 2021), MMLU (Hendrycks et al., 2020), Jeopardy (Jeo, 2022), and Winograd (Levesque et al., 2012). (Section 3.1)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **Classification** (behaviors tasks) — *measured_by*
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf)
- **Error handling** (constructs) — *measured_by*
  > We evaluate our method on LLMs and show significant perplexity improvements over baselines. This is particularly noteworthy at high sparsity levels, maintaining robust improvements even as high as 70% sparsity. Benchmark results. In Table 3, we evaluate the performance of our method on several benchmark datasets.
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **Functional linguistic competence** (constructs) — *measured_by*
  > To assess this, we use six benchmarks covering world knowledge (ARC-EASY, ARC-CHALLENGE (Clark et al., 2018)) (Section 3.3)
  - [Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)

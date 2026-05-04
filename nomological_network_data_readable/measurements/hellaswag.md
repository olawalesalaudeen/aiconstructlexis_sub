# HellaSwag
**Type:** Measurement  
**Referenced in:** 358 papers  
**Also known as:** Hellaswag, HellaSWAG, HELLASWAG  

## State of the Field

Across the surveyed literature, HellaSwag is a benchmark predominantly used to evaluate a model's commonsense capabilities. The task is consistently operationalized as a multiple-choice challenge where a model must select the most plausible or natural continuation for a given text snippet or scenario. Papers most frequently use HellaSwag to measure `commonsense reasoning` and `natural language understanding`, with some also using it to assess the broader construct of `reasoning`. The prevailing evaluation method is zero-shot, though a smaller line of work employs few-shot settings, such as 10-shot accuracy. While most papers frame it as a completion task, a few define it as a form of `natural language inference`. Beyond these core applications, the benchmark is also used to assess other model behaviors, including `generalization`, `language modeling`, and `contextual understanding`. Its administration is often facilitated by tools like the `LLM Evaluation Harness`, and it is included as a component of the `Open LLM Leaderboard`.

## Sources

**[AffineQuant: Affine Transformation Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/ddfb58b61e7213dfb9e06c695475b2bd-Paper-Conference.pdf)**
> A zero-shot benchmark for commonsense completion and multiple-choice selection.

**[Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf) (as "Hellaswag")**
> Zero-shot evaluation benchmark assessing commonsense reasoning in language models.

**[Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf) (as "HellaSWAG")**
> A benchmark for commonsense natural language inference that challenges models to choose the most plausible ending for a given text snippet.

**[Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf) (as "HELLASWAG")**
> Benchmark that measures a model’s ability to generate natural continuations by selecting the most plausible ending from candidate sentences.

## Relationships

### HellaSwag →
- **Referring expression understanding** (behaviors tasks) — *correlates*
  > “Further analysis shows a Pearson correlation of 0.88 between the LLM’s original performance on reasoning benchmarks, measured by the HellaSwag score (Zellers et al., 2019), and REC performance”
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)

### → HellaSwag
- **Commonsense reasoning** (constructs) — *measured_by*
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > The four benchmarks are ARC_C, HellaSwag, PIQA and MMLU... Results of the zero-shot performance are displayed in Table 1, which demonstrates that there is no significant loss of the ability of the language understanding of LLMs after the aligning with embodied environments (Section 5.5)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019) for assessing the general language understanding and reasoning capabilities...
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Answer, Assemble, Ace: Understanding How LMs Answer Multiple Choice Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c248154176c08147e82c0b30961604f7-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (constructs) — *measured_by*
  > We examine how wrong-over-wrong alignment can generalize to other unseen tasks in the same domain. We employ Hellaswag (Zellers et al., 2019) ... as two unseen datasets (Section 5)
  - [EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > We consider nine varied downstream tasks: ... (e) natural language inference (HellaSwag (Zellers et al., 2019))
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > We conducted experiments on a series of language modeling and understanding tasks, including PiQA (Bisk et al., 2020), ARC-easy (ARC-e), ARC-challenge (ARC-c) (Clark et al., 2018), HellaSwag (Hella.) (Zellers et al., 2019), Winogrande (Wino.) (Sakaguchi et al., 2019) and MMLU (Li et al., 2023). The results are reported in Table 2 and all evaluations were done using lm-evaluation-harness (Gao et al., 2024). (Section 4.2)
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019) for assessing the general language understanding and reasoning capabilities...
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Short-context capability** (constructs) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019)
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > “The multiple-choice tasks include: ... common sense reasoning (Hellaswag; Zellers et al. 2019)”
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks) — *measured_by*
  - [Radio: Rate–Distortion Optimization for Large Language Model Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/young25b/young25b.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Few-shot learning** (measurements) — *measured_by*
  - [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf)
- **Sentence completion** (behaviors tasks) — *measured_by*
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
- **Zero-shot classification** (behaviors tasks) — *measured_by*
  - [Search for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb64a43508e0cfe53ee6179ff31ea900-Paper-Conference.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > We utilize validation sets from six benchmarks: PIQA (Bisk et al., 2020), HellaSwag (Zellers et al., 2019), ARC-E (Clark et al., 2018), ARC-C (Clark et al., 2018), COPA (Roemmele et al., 2011), Winograd (Levesque et al., 2012), and MathQA (Amini et al., 2019). (Section 4.2.3)
  - [Scaling Inference-Efficient Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bian25b/bian25b.pdf)
- **Knowledge forgetting** (constructs) — *measured_by*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Condor: EnhanceLLMAlignment with Knowledge-Driven Data Synthesis and Refinement](https://aclanthology.org/2025.acl-long.1092.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [DavIR: Data Selection via Implicit Reward for Large Language Models](https://aclanthology.org/2025.acl-long.453.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > “• HELLASWAG (Zellers et al., 2019): Measures how well the model can generate the most natural continuation from four candidate sentences following a given sentence fragment.”
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Overfitting** (constructs) — *measured_by*
  - [How Much Can We Forget about Data Contamination?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bordt25a/bordt25a.pdf)
- **Contextual understanding** (constructs) — *measured_by*
  > Moreover, to demonstrate contextual understanding and general effectiveness of each model variant, we assess their performance using HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), and TruthfulQA (Lin et al., 2021b) benchmarks. (Section 4.2)
  - [QoS-Efficient Serving of Multiple Mixture-of-Expert LLMs Using Partial Runtime Reconfiguration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/imani25a/imani25a.pdf)
- **Functional linguistic competence** (constructs) — *measured_by*
  > “To assess this, we use six benchmarks covering world knowledge (ARC-EASY, ARC-CHALLENGE (Clark et al., 2018)), social reasoning (SOCIAL IQA (Sap et al., 2019)), physical reasoning (PIQA (Bisk et al., 2019)), and commonsense reasoning (WINOGRANDE (Sakaguchi et al., 2019), HELLASWAG (Zellers et al., 2019)).”
  - [Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  > We evaluate LLMs on these benchmarks using the LM-Evaluation-Harness framework (Gao et al., 2024), and all evaluations are conducted in a zero-shot setting. (Section 6)
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)

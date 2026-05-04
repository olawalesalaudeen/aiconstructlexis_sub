# GSM8k
**Type:** Measurement  
**Referenced in:** 813 papers  
**Also known as:** GSM8K, Grade School Math 8K, GSM-8k, GSM-8K, R-GSM, GSM-NoOp, GSM-Symbolic, E-GSM, GSM-IC, GSMplus  

## State of the Field

Across the surveyed literature, GSM8k is consistently described as a benchmark dataset composed of grade-school math word problems. Its primary and most frequent use is to evaluate a model's mathematical reasoning capabilities, often specified as quantitative, arithmetic, or multi-step numerical reasoning. The evaluation is commonly operationalized through chain-of-thought prompting, with accuracy or exact match serving as the standard performance metric. While the prevailing description labels the problems as "grade-school" level, a few papers characterize them as "middle-school" or "high school" level, and one study notes that the dataset contains "only arithmetic problems" ("SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning"). Beyond its core focus, GSM8k is also used to assess a range of other constructs, including commonsense knowledge and faithfulness. The provided data also details several derivative benchmarks, such as E-GSM and GSM-NoOp, which extend the original dataset to test model performance on problems with lengthy narratives or irrelevant information. Ultimately, GSM8k serves as a popular instrument for measuring how well models solve linguistically diverse, multi-step arithmetic word problems.

## Sources

**[Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf) (as "GSM8K")**
> A benchmark dataset of grade-school math word problems used to evaluate mathematical reasoning in multiple languages, with accuracy as the metric.

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)**
> Grade school math dataset evaluating mathematical reasoning via chain-of-thought prompting, consisting of arithmetic word problems.

**[$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf) (as "Grade School Math 8K")**
> A dataset consisting of a large number of grade school math problems used for evaluating mathematical reasoning.

**[Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "GSM-8k")**
> A text-only grade-school math word problem benchmark referenced as a comparison point for mathematical reasoning evaluation.

**[Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf) (as "GSM-8K")**
> A benchmark dataset (Cobbe et al., 2021) of grade-school math word problems used to evaluate quantitative reasoning.

**[Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf) (as "R-GSM")**
> A math reasoning dataset used to evaluate reasoning performance under swapped conditions.

**[GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf) (as "GSM-Symbolic")**
> An enhanced benchmark created from symbolic templates of GSM8K questions, allowing for the generation of diverse question variants to enable more controllable and reliable evaluations.

**[GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ec2e7a896f8250986b3907f57621ce94-Paper-Conference.pdf) (as "GSM-NoOp")**
> A dataset derived from GSM-Symbolic templates where seemingly relevant but ultimately inconsequential statements are added to problems to test a model's ability to discern relevant information.

**[Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf) (as "GSM")**
> The Grade School Math (GSM8K) dataset, which consists of math word problems that require multi-step reasoning to solve.

**[Can LLMs Solve Longer Math Word Problems Better?](https://proceedings.iclr.cc/paper_files/paper/2025/file/474ada926b331d78f06d95e8913111cc-Paper-Conference.pdf) (as "E-GSM")**
> Extended Grade-School Math, a benchmark of math word problems with lengthy narratives, created by iteratively extending problems from the GSM8K test set.

**[Can LLMs Solve Longer Math Word Problems Better?](https://proceedings.iclr.cc/paper_files/paper/2025/file/474ada926b331d78f06d95e8913111cc-Paper-Conference.pdf) (as "GSM-IC")**
> A benchmark of math word problems with irrelevant context, used to evaluate the generalizability of the proposed methods.

**[Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf) (as "GSMplus")**
> A test suite of grade-level math problems used as a held-out set for evaluating mathematical reasoning.

## Relationships

### → GSM8k
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [ExtendingLLMContext Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.29.pdf)
- **Generalization** (constructs) — *measured_by*
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Understanding In-Context Learning from Repetitions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d88f6f81e1aaf606776ffdd06fdf24ef-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  - [SocraticLM: Exploring Socratic Personalized Teaching with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9bae399d1f34b8650351c1bd3692aeae-Paper-Conference.pdf)
- **Short-context capability** (constructs) — *measured_by*
  - [Make Your LLM Fully Utilize the Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/71c3451f6cd6a4f82bb822db25cea4fd-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
- **Prompt optimization** (behaviors tasks) — *measured_by*
  - [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf)
- **STEM problem solving** (behaviors tasks) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
- **Scalability** (constructs) — *measured_by*
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **Generative capability** (constructs) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *measured_by*
  - [Financial Risk Relation Identification through Dual-view Adaptation](https://aclanthology.org/2025.emnlp-main.1337.pdf)
- **Text completion** (behaviors tasks) — *measured_by*
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **In-context reasoning** (constructs) — *measured_by*
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [PICLe: Pseudo-annotations for In-Context Learning in Low-Resource Named Entity Detection](https://aclanthology.org/2025.naacl-long.519.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [PIPA: Preference Alignment as Prior-Informed Statistical Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cl/li25cl.pdf)
- **Multi-Agent Debate** (measurements) — *measured_by*
  - [Communicating Activations Between Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ramesh25a/ramesh25a.pdf)
- **Error handling** (constructs) — *measured_by*
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **Coherence** (constructs) — *measured_by*
  - [DoLLMs Adhere to Label Definitions? Examining Their Receptivity to External Label Definitions](https://aclanthology.org/2025.emnlp-main.1649.pdf)
- **Locality** (constructs) — *measured_by*
  - [Dual-Path Dynamic Fusion with Learnable Query for Multimodal Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.572.pdf)

### Associated with
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
- **FLASK** (measurements)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Self-consistency** (measurements)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **PutnamBench** (measurements)
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM Evaluation Harness** (measurements)
  - [Training-Free Activation Sparsity in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3f2ff9579ba6deeb89caa2fe1f0b99c-Paper-Conference.pdf)
- **MR-GSM8K** (measurements)
  - [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf)
- **Domain knowledge** (constructs)
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)

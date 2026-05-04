# ARC
**Type:** Measurement  
**Referenced in:** 132 papers  
**Also known as:** Arc, AI2ARC, ARC-AGI, AI2 Reasoning Challenge, AI2-ARC  

## State of the Field

Across the surveyed literature, the name 'ARC' predominantly refers to the AI2 Reasoning Challenge, a multiple-choice question answering dataset, though a distinct set of papers uses 'ARC' for the Abstraction and Reasoning Corpus. The prevailing usage characterizes the AI2 Reasoning Challenge as a collection of grade-school science questions, often split into 'Easy' and 'Challenge' sets, designed to test knowledge and reasoning. In its minority usage as the Abstraction and Reasoning Corpus (also called ARC-AGI), the benchmark consists of grid-based visual puzzles requiring models to infer transformation rules from examples. Papers using the AI2 Reasoning Challenge most commonly operationalize it as a measure of `scientific reasoning`, `commonsense understanding`, and `question answering`. Conversely, studies employing the Abstraction and Reasoning Corpus use it to evaluate `abstract reasoning` and `inductive reasoning`. The AI2 version is frequently used for zero-shot evaluation and is often cited as a component of the Hugging Face Open LLM Leaderboard. While the science questions are almost universally described as grade-school level, one paper anomalously refers to them as 'graduate-school level'.

## Sources

**[Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)**
> AI2 Reasoning Challenge, a multiple-choice question answering dataset focused on grade school science questions requiring knowledge and reasoning, split into Easy and Challenge sets.

**[On Speeding Up Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a38cfba4c717e5a37b200294615e546e-Paper-Conference.pdf) (as "Arc")**
> The AI2 Reasoning Challenge, a dataset of grade-school science questions designed to test reasoning.

**[The Hidden Attention of Mamba Models](https://aclanthology.org/2025.acl-long.77.pdf) (as "AI2ARC")**
> AI2 Reasoning Challenge dataset containing grade-school level science questions requiring multi-step reasoning and comprehension.

**[Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf) (as "ARC-AGI")**
> Abstraction and Reasoning Corpus (ARC-AGI), a benchmark of grid-based reasoning tasks where models infer a transformation rule from examples and produce the correct output for a test input.

**[MIB: A Mechanistic Interpretability Benchmark](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mueller25a/mueller25a.pdf) (as "AI2 Reasoning Challenge")**
> A dataset of grade-school science questions used to evaluate basic scientific reasoning in language models.

**[Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf) (as "AI2-ARC")**
> The AI2 Reasoning Challenge (ARC) is a benchmark consisting of grade-school level, multiple-choice science questions designed to test question answering and reasoning.

## Relationships

### → ARC
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We evaluate each method on a wide range of reasoning tasks. These tasks include [...] ARC (ARCe for the easier dataset and ARCc for the challenging dataset) for multiple-choice science QA [...] (Section 4.1)
  - [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [OneBit: Towards Extremely Low-bit Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a7a3f53faafc0161be0fcb57e5fa078-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We found that LASER outperforms with upto 3.38% difference and 1% difference on average in accuracy.
  - [GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > Reasoning: The model’s capacity for commonsense and logical reasoning is measured using Winogrande (Sakaguchi et al., 2021) and ARC (easy and challenge subsets) (Clark et al., 2018). (Section 4.1)
  - [MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs](https://aclanthology.org/2025.emnlp-main.718.pdf)
- **Abstract reasoning** (constructs) — *measured_by*
  > The Abstraction and Reasoning Corpus (ARC) aims to evaluate the abstract reasoning capabilities of language models through their ability to solve visual puzzles. (Section 4.1)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  > Scientific reasoning is evaluated on SciQ (Welbl et al., 2017), Sci-Eval (Sun et al., 2024), and ARC (Clark et al., 2018) for English science
  - [InductionBench:LLMs Fail in the Simplest Complexity Class](https://aclanthology.org/2025.acl-long.1288.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  > The other is reported by the accuracy metric of zero-shot language tasks (Gao et al. (2021)) on PIQA (Bisk et al. (2020a)), HellaSwag (Clark et al. (2018)), ARC (Clark et al. (2018)), Mutual (Cui et al. (2020)) and Ehics (Hendrycks et al. (2020a)). (Section 5.1)
  - [CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf)
- **Inductive reasoning** (constructs) — *measured_by*
  > We verify our pipeline’s effectiveness on the ARC visual inductive reasoning benchmark, its variant 1D-ARC, string transformation dataset SyGuS, and list transformation dataset List Functions. (Section 1)
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
- **Structural reasoning** (constructs) — *measured_by*
  - [HYSYNTH: Context-Free LLM Approximation for Guiding Program Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/1c9c85bae6161d52182d0fe2f3640512-Paper-Conference.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Decoupling Angles and Strength in Low-rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3379ce104189b72d5f7baaa03ae81329-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > “The multiple-choice tasks include: grade-school science questions (ARC; Clark et al. 2018)”
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Few-shot learning** (measurements) — *measured_by*
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pourcel25a/pourcel25a.pdf)
- **Symbolic reasoning** (constructs) — *measured_by*
  - [Self-Guiding Exploration for Combinatorial Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb9120be0dcaac0aec66d2e75deb69dd-Paper-Conference.pdf)
- **Knowledge reasoning** (constructs) — *measured_by*
  - [Mastering the Craft of Data Synthesis forCodeLLMs](https://aclanthology.org/2025.naacl-long.621.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *measured_by*
  > Figure 6: % of test hypotheses fully groundable after adding various microtheories (n-sized Random, Usage, QC, & PC Mts) to a base Corpus. ... ARC Grounding Rate (%) of Test Hypotheses
  - [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf)
- **Scientific question answering** (behaviors tasks) — *measured_by*
  > ARC (AI2 Reasoning Challenge, Clark et al., 2018) was designed to test the reasoning abilities of AI through a series of challenging science questions. (Section 1.1)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > To validate the performance of different models, we used some benchmarks for the 3B and 19B models that were trained more tokens, including Lambada(Paperno et al., 2016), Winogrande(Sakaguchi et al., 2021), Hellaswag(Zellers et al., 2019), ARC(Clark et al., 2018), CMMLU(Li et al., 2023a), MMLU(Hendrycks et al.), Math(Hendrycks et al., 2021). (Section 4.1)
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)
- **Factual recall** (behaviors tasks) — *measured_by*
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)

### Associated with
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements)
  > We evaluate LLMs on these benchmarks using the LM-Evaluation-Harness framework (Gao et al., 2024), and all evaluations are conducted in a zero-shot setting. (Section 6)
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **Compositionality** (constructs)
  > Therefore, we regard ARC tasks as complex compositions of atomic operations for evaluation. (Section 4.2)
  - [Evaluating Contextualized Representations of (Spanish) Ambiguous Words: A New Lexical Resource and Empirical Analysis](https://aclanthology.org/2025.naacl-long.423.pdf)

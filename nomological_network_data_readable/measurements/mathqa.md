# MathQA
**Type:** Measurement  
**Referenced in:** 45 papers  

## State of the Field

Across the provided literature, MathQA is consistently used as a benchmark to evaluate the mathematical reasoning capabilities of language models. It is most frequently operationalized to assess a model's ability to solve multi-step math word problems, which, as one paper notes, requires models to "both understand the text of a word problem and perform mathematical operations to arrive at the correct solution." Several sources specify its format as multiple-choice question answering, with one study stating it "provides 5 options to choose from for each problem." The problems are described as diverse, covering domains such as "geometry, physics, probability, and algebra." While its primary application is for evaluation, a common definition also describes its use as a dataset for "instruction tuning and retriever fine-tuning." In evaluation contexts, MathQA is frequently studied alongside other mathematical reasoning datasets like GSM8K, SVAMP, and MATH. A few papers also use it to measure related concepts like problem-solving skills or to test knowledge transfer as an out-of-domain task.

## Sources

**[RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf)**
> A math question answering dataset used in instruction tuning and retriever fine-tuning.

## Relationships

### → MathQA
- **Mathematical reasoning** (constructs) — *measured_by*
  > Datasets like MathQA (Amini et al., 2019), GSM8k (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), and SVAMP (Patel et al., 2021) focus on math word problems requiring multi-step reasoning and problem-solving (Section 5).
  - [MathPile: A Billion-Token-Scale Pretraining Corpus for Math](https://proceedings.neurips.cc/paper_files/paper/2024/file/2d0be3cd5173c10b6ec075d1c393a13d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > It consists of questions that test numerical reasoning and problem-solving skills, requiring models to both understand the text of a word problem and perform mathematical operations to arrive at the correct solution. (Section 3.2.1)
  - [Idiosyncratic Versus Normative Modeling of Atypical Speech Recognition: Dysarthric Case Studies](https://aclanthology.org/2025.emnlp-main.1702.pdf)

### Associated with
- **Domain knowledge** (constructs)
  > For instance, there is a total MSE improvement of 0.271 when GSM8k is incorporated to predicting MathQA... As all three benchmarks are math-related, we can deduce that the level of math knowledge of our selected models are indeed learned and reflected in our model embeddings.
  - [EmbedLLM: Learning Compact Representations of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf5e4b85d203481d6e37bd32d9600162-Paper-Conference.pdf)

# ASDIV
**Type:** Measurement  
**Referenced in:** 37 papers  
**Also known as:** ASDiv, Asdiv  

## State of the Field

Across the provided literature, ASDIV is consistently characterized as a benchmark dataset composed of diverse math word problems. Its most prevalent application is to measure and evaluate mathematical reasoning in language models, with many sources specifically highlighting its use for assessing arithmetic reasoning. The dataset is frequently described as containing problems of varying types and difficulty levels, intended to test for robustness. One source notes that its problems may require not only arithmetic but also "algebra, number theory, set operations and geometric formulas." A recurring theme in its application is its use as an out-of-distribution or held-out test set to evaluate the generalization of a model's reasoning capabilities. In these evaluations, ASDIV is commonly used alongside other mathematical reasoning benchmarks such as GSM8K, SVAMP, and MATH.

## Sources

**[Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)**
> A Set of Diverse Math Word Problems, a benchmark containing math problems across various types and difficulty levels to assess robustness in mathematical reasoning.

**[BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf) (as "ASDiv")**
> A benchmark dataset of diverse math word problems for assessing arithmetic reasoning.

**[Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf) (as "Asdiv")**
> An out-of-distribution benchmark dataset of diverse math word problems.

## Relationships

### → ASDIV
- **Mathematical reasoning** (constructs) — *measured_by*
  > We evaluate our LLM cascade approaches on six datasets, covering (1) mathematical reasoning, including GSM8k (Cobbe et al., 2021), ASDIV (Ling et al., 2017), and TabMWP (Lu et al., 2023); (2) symbolic reasoning from BIG-Bench Hard (bench authors, 2023), including DATE and Navigate; and (3) causal reasoning, including CREPE (Zhang et al., 2023). (Section 3.1)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)

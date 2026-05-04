# SVAMP
**Type:** Measurement  
**Referenced in:** 107 papers  
**Also known as:** svamp  

## State of the Field

Across the surveyed literature, SVAMP is a widely used benchmark for evaluating the mathematical reasoning capabilities of large language models. Its primary and most frequently documented application is to measure arithmetic reasoning and problem-solving abilities. The dataset is consistently defined as containing arithmetic or grade-school level math word problems that are specifically designed with controlled variations. The prevailing characterization is that these "simple variations," which include structural, numerical, and linguistic changes, are intended to test model robustness, compositional generalization, and the ability to avoid spurious correlations. In practice, SVAMP is often employed as an out-of-domain or out-of-distribution benchmark to assess how well models generalize beyond their training data. As one paper notes, the dataset includes "designed perturbations to evaluate whether LLMs learned spurious correlations in math word problems" ("DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning"). A less common application mentioned in one paper is its use for evaluating number generation in a mathematical context.

## Sources

**[Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)**
> Dataset of novel arithmetic word problems designed to test compositional generalization and robustness in mathematical reasoning models.

**[Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf) (as "svamp")**
> An out-of-distribution benchmark of simple math word problems with linguistic variations.

## Relationships

### → SVAMP
- **Mathematical reasoning** (constructs) — *measured_by*
  > “We evaluate the MathCoder on five datasets, including two in-domain datasets: GSM8K (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021); and three out-of-domain datasets: SVAMP (Patel et al., 2021), Mathematics (Saxton et al., 2019), and SimulEq (Kushman et al., 2014).”
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > Text Generation We use the SVAMP dataset (Patel et al., 2021) which consists of English math word problems with grade level up to 4.
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-DomainMoEAdaptation](https://aclanthology.org/2025.emnlp-main.933.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)

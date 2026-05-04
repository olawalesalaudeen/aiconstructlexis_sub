# OlympiadBench
**Type:** Measurement  
**Referenced in:** 37 papers  
**Also known as:** Olympiad Bench, Olympiad  

## State of the Field

Across the provided literature, OlympiadBench is a benchmark predominantly used to evaluate advanced mathematical reasoning. It is consistently positioned as a challenging dataset containing "Olympiad-level" or "competition-level" problems designed to test models on highly complex and novel tasks. A smaller set of studies also employs OlympiadBench to specifically assess model generalization on what are described as "out-of-distribution challenging problems." There is some variation in how the benchmark's contents are described. Many sources define it as a collection of high-school and college-level mathematics problems, with one paper noting it covers topics from elementary mathematics to abstract algebra. In contrast, another common definition characterizes it as a "bilingual multimodal benchmark featuring 8,476 problems tailored to Olympic-level mathematics and physics competitions," designed to assess both visual and logical reasoning. In evaluation practices, it is frequently used within a suite of other mathematical benchmarks to represent a high-difficulty reasoning task.

## Sources

**[ImpliHateVid: A Benchmark Dataset and Two-stage Contrastive Learning Framework for Implicit Hate Speech Detection in Videos](https://aclanthology.org/2025.acl-long.843.pdf) (as "Olympiad Bench")**
> Benchmark containing high-school and college-level mathematics problems from olympiad competitions, assessing advanced mathematical reasoning.

**[Pixel-Level Reasoning Segmentation via Multi-turn Conversations](https://aclanthology.org/2025.acl-long.865.pdf) (as "Olympiad")**
> Challenging mathematical problem-solving dataset designed to assess advanced reasoning and proof-like capabilities.

**[Knowledge Boundary of Large Language Models: A Survey](https://aclanthology.org/2025.acl-long.257.pdf)**
> Bilingual multimodal benchmark featuring 8,476 problems tailored to Olympic-level mathematics and physics competitions, assessing high-level visual and logical reasoning.

## Relationships

### → OlympiadBench
- **Mathematical reasoning** (constructs) — *measured_by*
  > we select several widely recognized and representative benchmarks, including MathVista (Lu et al., 2024a), Math-Verse (Zhang et al., 2024a), MathVision (Wang et al., 2024a), Dynamath (Zou et al., 2024), and OlympiadBench (He et al., 2024). (Section 4.2)
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We also incorporate two more challenging datasets, Olympiad-Bench (He et al., 2024) and CollegeMath (Tang et al., 2024), to further test our model’s generalizability on out-of-distribution challenging problems. (Section 4.1)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Pixel-Level Reasoning Segmentation via Multi-turn Conversations](https://aclanthology.org/2025.acl-long.865.pdf)
- **Scientific problem solving** (behaviors tasks) — *measured_by*
  - [Analyzing Uncertainty ofLLM-as-a-Judge: Interval Evaluations with Conformal Prediction](https://aclanthology.org/2025.emnlp-main.570.pdf)

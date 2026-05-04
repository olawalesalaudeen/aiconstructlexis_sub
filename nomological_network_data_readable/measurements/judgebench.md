# JudgeBench
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, JudgeBench is consistently characterized as a benchmark for evaluating LLM-as-a-Judge systems. The most prevalent usage is to assess these systems using what one paper describes as "challenging response pairs spanning knowledge, reasoning, math, and coding." In this capacity, JudgeBench is used to measure constructs including Mathematical reasoning, Commonsense knowledge, and Faithfulness. The benchmark's content is specified as being derived from other datasets, namely MMLU-Pro for its knowledge category, LiveBench for reasoning and mathematics, and LiveCodeBench for coding. Some papers use it to test the "robustness and accuracy" of judge models, while a less common framing positions it as a case study for evaluating "judge behavior and agreement under uncertainty." In the context of other evaluation tools, it is listed alongside instruments like RewardBench and MTBench-Human, and is explicitly described as a "valuable complement to RewardBench for evaluating reward models on difficult tasks requiring reasoning."

## Sources

**[Beyond correlation: The impact of human uncertainty in measuring the effectiveness of automatic evaluation and LLM-as-a-judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/8798321486948322be2b4d658744ba72-Paper-Conference.pdf)**
> A benchmark referenced as an additional case study for evaluating judge behavior and agreement under uncertainty.

## Relationships

### → JudgeBench
- **Faithfulness** (constructs) — *measured_by*
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [Quantifying Lexical Semantic Shift via Unbalanced Optimal Transport](https://aclanthology.org/2025.acl-long.775.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  > JudgeBench is a recent benchmark that evaluates LLM-based judges on challenging response pairs spanning knowledge, reasoning, math, and coding. (Section 3)
  - [Learning to Plan & Reason for Evaluation with Thinking-LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saha25b/saha25b.pdf)

### Associated with
- **MMLU-Pro** (measurements)
  > We use MMLU-Pro for the Knowledge category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **LiveBench** (measurements)
  > For the Reasoning and Mathematics categories, we use the corresponding LiveBench datasets. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **LiveCodeBench** (measurements)
  > LiveCodeBench is a contamination-free dataset for coding tasks, containing over 300 challenging questions sourced from coding contests like LeetCode, AtCoder, and Codeforces. We select this dataset for the Coding category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Reward-Bench** (measurements)
  > Thus, JudgeBench offers a valuable complement to RewardBench for evaluating reward models on difficult tasks requiring reasoning. (Section 4.3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)

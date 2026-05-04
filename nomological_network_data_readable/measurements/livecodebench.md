# LiveCodeBench
**Type:** Measurement  
**Referenced in:** 43 papers  
**Also known as:** LiveCodeBench-v1.0  

## State of the Field

Across the provided literature, LiveCodeBench is consistently described as a benchmark for evaluating large language models, with a frequently mentioned feature being its 'contamination-free' design. Its predominant use is to measure the `code generation` and general `programming ability` of models. The benchmark is composed of competitive programming problems, which one paper notes require "advanced reasoning capabilities," sourced from platforms like LeetCode, AtCoder, and CodeForces. To avoid data contamination, the benchmark employs a strategy of "careful segregation by date" and, as one source describes, "continuously collects new human-authored programming problems... to maintain freshness." While its primary application is assessing code generation, a smaller number of papers also use it to evaluate more specific skills like `abductive reasoning` and `code debugging`. A specific version, `LiveCodeBench-v1.0`, is mentioned as having an 'easy' subset for efficiency and accuracy comparisons. One paper also notes that the evaluation is execution-based.

## Sources

**[Planning in Natural Language Improves LLM Search for Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/071a637d41ea290ac4360818a8323f33-Paper-Conference.pdf)**
> A benchmark for code generation consisting of competitive programming problems, with careful segregation by date to avoid data contamination issues in evaluation.

**[Gradient-Adaptive Policy Optimization: Towards Multi-Objective Alignment of Large Language Models](https://aclanthology.org/2025.acl-long.550.pdf) (as "LiveCodeBench-v1.0")**
> Code generation benchmark designed to evaluate LLMs on programming tasks across difficulty levels, with an 'easy' subset used for efficiency and accuracy comparisons.

## Relationships

### → LiveCodeBench
- **Code generation** (behaviors tasks) — *measured_by*
  - [Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [SBSC: Step-by-Step Coding for Improving Mathematical Olympiad Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e5f5e4504759e3957e3eef2a44a535e-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **Code execution** (behaviors tasks) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Abductive reasoning** (constructs) — *measured_by*
  > Deductive code and abductive code reasoning can be regarded as opposite processes; therefore, we selected two identical and representative datasets, CRUXEval (Gu et al., 2024) and LiveCodeBench (Jain et al., 2024), as benchmarks to validate these two capabilities.
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *measured_by*
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Removal of Hallucination on Hallucination: Debate-AugmentedRAG](https://aclanthology.org/2025.acl-long.771.pdf)
- **Code debugging** (behaviors tasks) — *measured_by*
  > We use 7 datasets that contain problems and test cases from competitive programming contests: 1) CodeForces (8.8k problems), 2) AtCoder (1.3k problems), 3) HackerEarth (1.2k problems), 4) CodeChef (768 problems), 5) LiveCodeBench (400 problems), 6) CodeJam (180 problems), and 7) Aizu (2.2k problems) (Li et al., 2022b; Jain et al., 2024).
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [CanLLMs Extract Frame-Semantic Arguments?](https://aclanthology.org/2025.emnlp-main.1558.pdf)

### Associated with
- **JudgeBench** (measurements)
  > LiveCodeBench is a contamination-free dataset for coding tasks, containing over 300 challenging questions sourced from coding contests like LeetCode, AtCoder, and Codeforces. We select this dataset for the Coding category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)

# SWE-bench
**Type:** Measurement  
**Referenced in:** 28 papers  
**Also known as:** SWE-BENCH, SWE-Bench, SWEBench  

## State of the Field

Across the provided literature, SWE-bench is consistently described as a benchmark for evaluating language models and autonomous agents on their ability to perform real-world software engineering tasks. The benchmark is composed of tasks derived from actual GitHub activity, with multiple sources specifying it contains 2,294 issues, often paired with pull requests, from 12 popular Python repositories. The primary task for an evaluated system is to resolve a given GitHub issue, which can be a bug report or a feature request, by generating a code patch. Papers use SWE-bench to measure constructs such as `Code generation` and `Programming ability`. The success of a generated patch is typically determined by whether it passes the repository's existing unit tests, with one paper mentioning the metric "% Resolved (Pass@1)". While its main purpose is issue resolution, one paper notes that its code repositories and environments were adapted to create another benchmark, TESTGENEVAL, focused on software testing. Overall, the prevailing usage of SWE-bench is as an evaluation framework for repository-level code editing and problem-solving capabilities.

## Sources

**[MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf)**
> A benchmark dataset comprising 2,294 real-world issues from 12 popular Python repositories, designed to evaluate a model's ability to perform GitHub issue resolution.

**[StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "SWE-BENCH")**
> A benchmark for evaluating language models on real-world software engineering tasks, using GitHub issues and pull requests to test code editing capabilities.

**[OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf) (as "SWE-Bench")**
> A benchmark designed to assess an agent's ability to resolve real-world GitHub issues, such as bug reports or feature requests, within a code repository.

**[TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/26ded5c8ee8ec1bc4caced4e1c9b1584-Paper-Conference.pdf) (as "SWEBench")**
> A benchmark dataset of real-world software engineering tasks from which the code repositories and execution environments for TESTGENEVAL are derived.

## Relationships

### → SWE-bench
- **Code generation** (behaviors tasks) — *measured_by*
  > A notable example is SWE-bench (Jimenez et al., 2024), which assesses the ability of agents to generate patches to resolve real-world GitHub issues. (Section 1)
  - [RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph](https://proceedings.iclr.cc/paper_files/paper/2025/file/4a4a3c197deac042461c677219efd36c-Paper-Conference.pdf)
- **IT service management** (behaviors tasks) — *measured_by*
  - [MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf)

### Associated with
- **SWE-bench Lite** (measurements)
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)

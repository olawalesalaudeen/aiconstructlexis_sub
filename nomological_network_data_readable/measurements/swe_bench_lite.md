# SWE-bench Lite
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** SWE-Bench Lite, SWE-Bench-Lite  

## State of the Field

Across the provided literature, SWE-bench Lite is consistently characterized as a widely used evaluation instrument for automated and autonomous software engineering systems. It is uniformly defined as a subset of the larger SWE-bench, with multiple sources specifying it contains 300 instances derived from real GitHub issues in Python repositories. The benchmark's tasks are described as "repository-level" and are designed to provide a "more self-contained evaluation of functional bug fixes," a point echoed in several papers. Evaluation is based on resolving these issues, often involving code patches, with one source mentioning the use of hidden unit tests. As a measurement tool, papers report using SWE-bench Lite to assess constructs such as `Task completion` and `IT service management`. The prevailing usage, as stated in one paper, is for "evaluating state-of-the-art performance" on these software engineering tasks.

## Sources

**[SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?](https://proceedings.iclr.cc/paper_files/paper/2025/file/07d6332ae36730707fddddba736d7b6c-Paper-Conference.pdf)**
> The most commonly used subset of the SWE-bench benchmark for evaluating state-of-the-art performance in autonomous software engineering systems.

**[CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf) (as "SWE-Bench-Lite")**
> SWE-Bench-Lite, an evaluation suite for repository-level software engineering tasks involving real GitHub issues and code patches.

**[Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf) (as "SWE-Bench Lite")**
> SWE-Bench Lite, a 300-instance benchmark of real GitHub issue resolution with hidden unit tests for evaluating functional bug fixes.

## Relationships

### → SWE-bench Lite
- **IT service management** (behaviors tasks) — *measured_by*
  - [MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d1f02132ef51602adf07000ca5b6138-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation](https://aclanthology.org/2025.acl-long.973.pdf)
- **Task completion** (behaviors tasks) — *measured_by*
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)

### Associated with
- **SWE-bench** (measurements)
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)

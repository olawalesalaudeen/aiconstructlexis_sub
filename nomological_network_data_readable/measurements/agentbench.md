# AgentBench
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, AgentBench is consistently described as a comprehensive benchmark for evaluating the capabilities of Large Language Models (LLMs) as agents. It is used to measure a range of constructs, including agency, planning, decision-making, logical reasoning, and code generation. One paper specifically states that it evaluates an agent's "intrinsic reasoning and adaptation to environment feedback." The benchmark operationalizes this evaluation across diverse, multi-round environments, with papers frequently citing tasks such as operating system (OS) interaction, web browsing, web shopping, and database (DB) interaction. Performance measurement is tailored to the environment, with one study reporting the use of "success rate for the OS, DB, HH, and WB environments, F1 score for the KG environment, and reward score for the WS environment." In addition to direct evaluation, AgentBench serves as a reference in the field; its experimental setup is adopted for other tasks, and it is used as a point of comparison for newer, more specialized benchmarks.

## Sources

**[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A benchmark for evaluating LLMs as agents, referenced as a comparison point for multi-round and task-diverse agent evaluation.

## Relationships

### → AgentBench
- **Decision-making** (constructs) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Knowledge acquisition** (constructs) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **Agency** (constructs) — *measured_by*
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **Planning** (constructs) — *measured_by*
  - [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.578.pdf)

### Associated with
- **WebShop** (measurements)
  - [Scaling Autonomous Agents via Automatic Reward Modeling And Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/47f75e809409709c6d226ab5ca0c9703-Paper-Conference.pdf)

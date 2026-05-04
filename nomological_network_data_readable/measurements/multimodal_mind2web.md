# Multimodal Mind2Web
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Multimodal-Mind2Web  

## State of the Field

Across the provided sources, Multimodal Mind2Web is consistently characterized as an offline benchmark for evaluating web agents, and is frequently described as a multimodal extension of the Mind2Web benchmark. It is operationalized using cached screenshots and high-level task instructions, with one paper noting its test set contains over 1,000 tasks on more than 100 websites. The most specific stated use of the benchmark is to measure an agent's generalization capabilities. This is supported by one paper which defines its purpose as evaluating generalization across "three increasingly challenging settings: cross-task, cross-website, and cross-domain." Other papers describe its function more broadly as evaluating "web agent task completion" or the performance of "GUI agents" on web browser tasks. A single source also uniquely frames it as an "in-distribution" dataset in contrast to online, out-of-distribution benchmarks.

## Sources

**[AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)**
> An extension of the Mind2Web benchmark used to evaluate an agent's generalization capabilities across increasingly difficult settings: cross-task, cross-website, and cross-domain.

**[Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf) (as "Multimodal-Mind2Web")**
> An offline benchmark for evaluating web agent task completion using cached screenshots and high-level task instructions across over 100 websites.

## Relationships

### → Multimodal Mind2Web
- **Generalization** (constructs) — *measured_by*
  > Second, Multimodal-Mind2Web (Deng et al., 2024; Zheng et al., 2024) extends the Mind2Web benchmark to evaluate generalization across three increasingly challenging settings: cross-task, cross-website, and cross-domain. (Section 3.1)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **Cross-modal grounding** (constructs) — *measured_by*
  - [MoVa: Towards Generalizable Classification of Human Morals and Values](https://aclanthology.org/2025.emnlp-main.1688.pdf)

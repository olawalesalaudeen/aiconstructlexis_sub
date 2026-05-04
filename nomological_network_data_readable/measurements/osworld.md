# OSWORLD
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** OSWorld  

## State of the Field

OSWORLD is consistently described across the provided literature as a benchmark and interactive environment for evaluating agents on computer-based tasks. The original paper defines it as a "scalable, real computer environment" for "multimodal agents" operating across Ubuntu, Windows, and macOS, featuring 369 open-ended tasks with execution-based evaluation. Other papers emphasize its nature as an "interactive OS agent testbed" where an agent must interact with the system at each step and await a response before proceeding. In practice, papers use OSWORLD to measure agent constructs such as Generalization, Agency, and Adaptability. Beyond direct evaluation, it is also used for data collection, with one study using it to "collect agent action trajectories." The benchmark is also used to compare agent performance against human baselines. The prevailing usage is as an evaluation tool for multi-step task completion in simulated real-world desktop environments.

## Sources

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A scalable, real computer environment and benchmark for evaluating multimodal agents on open-ended computer tasks across Ubuntu, Windows, and macOS, featuring 369 tasks with execution-based evaluation.

**[OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf) (as "OSWorld")**
> An interactive OS agent testbed environment where agents must interact with the operating system at each step and wait for responses before proceeding, evaluating multi-step task completion across various applications.

## Relationships

### OSWORLD →
- **Human evaluation** (measurements) — *measured_by*
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)

### → OSWORLD
- **Generalization** (constructs) — *measured_by*
  - [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf)
- **Agency** (constructs) — *measured_by*
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **Adaptability** (constructs) — *measured_by*
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

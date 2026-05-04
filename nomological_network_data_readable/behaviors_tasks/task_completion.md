# Task completion
**Type:** Behavior  
**Referenced in:** 10 papers  
**Also known as:** Achievement unlocking, Household task execution, Issue resolution, Indoor task simulation, Graph-structured task execution  

## State of the Field

Across the provided literature, task completion is most commonly defined as successfully reaching the intended end state of a benchmark task, a process typically judged by task-specific evaluation scripts. The specific nature of this behavior, however, is highly contextual and varies across different research domains. For instance, in software engineering, it is framed as 'issue resolution,' which entails fixing a software issue to pass a test suite. In simulated environments, it manifests as 'household task execution' in 3D worlds, 'indoor task simulation' guided by text, or 'achievement unlocking' in open-world games, where agents must 'unlock all achievements while ensuring its survival.' A more abstract conceptualization treats it as 'graph-structured task execution,' which involves performing a sequence of actions on a task with dependencies. The operationalization of this behavior frequently relies on quantitative metrics, such as a binary 'success flag (0/1)', a success rate like the 'proportion of achievements unlocked', or the 'time to completion.' To elicit and measure this behavior, papers use specific instruments, including the SWE-bench Lite and SWE-Bench Verified benchmarks for software tasks, and simulated environments like VirtualHome and ALFWorld for embodied tasks.

## Sources

**[Mars: Situated Inductive Reasoning in an Open-World Environment](https://proceedings.neurips.cc/paper_files/paper/2024/file/1fb6d0b52f5e41b11392841a66dbfe7d-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Achievement unlocking")**
> The task of accomplishing specific goals such as collecting resources, crafting tools, or placing objects within the game environment.

**[Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c2f71567cd53464161cab3336e8fc865-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Successfully reaching the intended end state of a benchmark task as judged by task-specific evaluation scripts.

**[Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf) (as "Issue resolution")**
> The end-to-end task of successfully fixing a software issue described in natural language, resulting in a passing test suite.

**[World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf) (as "Household task execution")**
> Performing a variety of common tasks within a simulated home environment, such as moving objects or operating appliances.

**[World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf) (as "Indoor task simulation")**
> Completing tasks within a simulated indoor setting, typically guided by text-based interactions and instructions.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Graph-structured task execution")**
> Performing a sequence of actions on a task represented as a directed acyclic graph with dependencies, branches, and hierarchical levels.

## Relationships

### Task completion →
- **WebArena** (measurements) — *measured_by*
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **SWE-bench Lite** (measurements) — *measured_by*
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
- **SWE-Bench Verified** (measurements) — *measured_by*
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)

### → Task completion
- **Android-in-the-Wild** (measurements) — *measured_by*
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf)

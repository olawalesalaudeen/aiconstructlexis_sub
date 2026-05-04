# Task planning
**Type:** Construct  
**Referenced in:** 14 papers  
**Also known as:** Task decomposition  

## State of the Field

Across the provided literature, Task planning is most commonly defined as the ability to decompose a high-level goal or instruction into a sequence of executable actions or skills. While most definitions refer to these as 'mid-level actions,' a few frame them as 'low-level skills' or 'steps,' particularly in the context of GUI tasks or embodied agents. A closely related concept, 'Task decomposition,' is described as breaking down a query into a 'computation graph' or a 'step-by-step abstract plan in language.' The application of Task planning is frequently situated in robotics, where, as one paper notes, a system is 'tasked with crafting a sequence of mid-level actions (skills) that enable a robot to complete complex high-level tasks' (Tree-Planner: Efficient Close-loop Task Planning with Large Language Models). To operationalize this construct, researchers use measurement instruments such as TaskBench and RestBench. Some work suggests that capabilities like Commonsense understanding and In-context and few-shot learning influence Task planning. The construct is also studied in relation to Environment exploration and Sequential decision-making.

## Sources

**[Grounding Language Plans in Demonstrations Through Counterfactual Perturbations](https://proceedings.iclr.cc/paper_files/paper/2024/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf) (as "Task decomposition")**
> The process by which an LLM breaks down a complex multi-modal query into a sequence of simpler, interdependent subtasks represented as a computation graph.

**[LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)**
> The ability to decompose a high-level goal into a sequence of executable mid-level actions or skills.

## Relationships

### Task planning →
- **TaskBench** (measurements) — *measured_by*
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)
- **RestBench** (measurements) — *measured_by*
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)

### → Task planning
- **In-context learning** (constructs) — *causes*
  - [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *causes*
  - [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf)

### Associated with
- **Task decomposition** (behaviors tasks)
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)
- **Environment exploration** (behaviors tasks)
  - [Exploratory Retrieval-Augmented Planning For Continual Embodied Instruction Following](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bacd0ebd061d4694583ae0eb69ad15f-Paper-Conference.pdf)
- **Sequential decision-making** (constructs)
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)

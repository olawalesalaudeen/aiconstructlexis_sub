# Task and action execution
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Task execution, Basic task solving, Action execution, Execution  

## State of the Field

Across the provided literature, "Task and action execution" is consistently defined as a latent ability for a model to implement tasks or perform actions. The most prevalent framing, found in multiple papers, situates this construct within agentic contexts, where it is defined as the ability to select and invoke appropriate functions and parameters to enable tool use. For instance, one paper describes an "executor" component "tasked with identifying the appropriate functions and parameters to invoke." A smaller body of work defines this concept in other domains, such as the ability to implement learned tasks like translation during generation, or as the capacity to produce "appropriate action sequences" for embodied tasks. Consequently, the construct is operationalized in several ways. The most common measurement approach involves evaluating `Tool use`, specifically the correct invocation of functions and tools. Other operationalizations include assessing the planning of action sequences in embodied agent benchmarks and identifying internal "task-execution features that implement those tasks during generation." The construct is also studied alongside `Commonsense knowledge` and `Text summarization`.

## Sources

**[Scaling Sparse Feature Circuits For Studying In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kharlapenko25a/kharlapenko25a.pdf) (as "Task execution")**
> The latent ability to implement a learned task during generation, such as producing an antonym or translating a phrase, based on internal task representations.

**[EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf) (as "Basic task solving")**
> The latent ability to carry out straightforward embodied tasks by producing appropriate action sequences for low to medium difficulty goals.

**[Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf) (as "Action execution")**
> The ability to perform specific, discrete actions such as calling functions or using tools as part of a larger task.

**[MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf) (as "Execution")**
> The latent ability to select appropriate functions and parameters to invoke based on reasoning input, enabling tool use in agent tasks.

## Relationships

### Associated with
- **Reasoning** (constructs)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
- **Text summarization** (behaviors tasks)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
- **Tool use** (behaviors tasks)
  > (1) Action Execution includes function call and tool use (Chen et al., 2023c). (Sec. 2.1)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)

# Sequential decision-making
**Type:** Construct  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, sequential decision-making is framed in two primary ways: as an agent's ability and as a training task. One definition describes it as the "ability to perform a series of actions in an interactive environment where each action depends on the outcomes of previous ones" ('Fleet of Agents...'). Another perspective casts it as the "task of training policies to make a series of choices over time to achieve a goal" ('Learning from negative feedback...'). This construct is operationalized and evaluated using specific benchmarks that require interactions with an environment. For instance, ALFWorld is explicitly used to "evaluate the performance in sequential decision-making scenarios" and is described as a "popular benchmark for examining LLM-based agents’ decision-making ability". The VirtualHome benchmark is also used as a measurement instrument. The concept is frequently associated with tasks like web navigation and is studied alongside planning, task planning, and commonsense knowledge.

## Sources

**[Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)**
> The ability to perform a series of actions in an interactive environment where each action depends on the outcomes of previous ones.

## Relationships

### Sequential decision-making →
- **VirtualHome** (measurements) — *measured_by*
  - [Reinforcing LLM Agents via Policy Optimization with Action Decomposition](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc09efb501c801ed92e181e26a885c2d-Paper-Conference.pdf)
- **ALFWorld** (measurements) — *measured_by*
  > ALFWorld (Shridhar et al., 2020) is a popular benchmark for examining LLM-based agents’ decision-making ability (Section 4.1).
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)

### Associated with
- **Web navigation** (behaviors tasks)
  > these methods are not well-suited for sequential decision-making tasks that require interactions with an environment, such as web navigation (Yao et al., 2022). (Section 1. Introduction)
  - [UniRAG: Unified Query Understanding Method for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.694.pdf)
- **Reasoning** (constructs)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Planning** (constructs)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Task planning** (constructs)
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)

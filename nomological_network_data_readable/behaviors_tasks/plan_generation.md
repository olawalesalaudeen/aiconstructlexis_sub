# Plan generation
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, `Plan generation` is consistently defined as the behavior of a large language model producing a sequence of actions to transition from an initial state to a goal state. The most prevalent framing, found in papers like "Leveraging Environment Interaction..." and "LongLeader...", specifies that the LLM generates these plans directly, without relying on external planners or formal languages. This is sometimes referred to as "Intrinsic Planning," where the model is delegated the "entire plan generation process." To operationalize and evaluate this behavior, the field uses measurement instruments such as VAL. The behavior is also described more generally as "automatically generating reasonable solutions for given tasks" based on user queries. The provided data also situates `Plan generation` in relation to other capabilities; it is reported to be caused by `State tracking` and can itself be a precursor to `Code generation`.

## Sources

**[Leveraging Environment Interaction for Automated PDDL Translation and Planning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/44af065477781e7f8a8589b14a62c489-Paper-Conference.pdf)**
> The observable behavior of an LLM directly producing a sequence of actions intended to solve a planning problem, without translating to a formal language or using an external planner.

## Relationships

### Plan generation →
- **VAL** (measurements) — *measured_by*
  - [A Silver Bullet or a Compromise for Full Attention? A Comprehensive Study of Gist Token-based Context Compression](https://aclanthology.org/2025.acl-long.242.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [Code-Generated Graph Representations Using Multiple LLM Agents for Material Properties Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25an/huang25an.pdf)

### → Plan generation
- **State tracking** (constructs) — *causes*
  - [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.440.pdf)

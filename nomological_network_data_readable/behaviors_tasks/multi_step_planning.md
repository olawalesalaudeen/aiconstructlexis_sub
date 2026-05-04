# Multi-step planning
**Type:** Behavior  
**Referenced in:** 8 papers  
**Also known as:** Natural planning, Step-by-step planning  

## State of the Field

Across the provided literature, multi-step planning is most commonly defined as the ability to decompose a complex problem into an ordered sequence of steps or subgoals to achieve a goal. Some definitions emphasize selecting a sequence of actions to manipulate future outcomes, while another highlights planning over an "extended horizon, where early decisions can have significant downstream consequences" ("Doubling Your Data in Minutes: Ultra-fast Tabular Data Generation viaLLM-Induced Dependency Graphs"). This behavior is also referred to as "natural planning" or "step-by-step planning" in some work, with one paper distinguishing "natural planning" from classical AI planning. To elicit and evaluate this behavior, researchers use instruments like the SPaRC benchmark, which is designed to test "long-term, step-by-step path planning". Additionally, methods such as PLAN-TUNING are used to teach models this skill. Multi-step planning is studied in relation to Task decomposition, and one paper reports that "planning trajectories improves complex reasoning capabilities" ("zFLoRA: Zero-Latency Fused Low-Rank Adapters").

## Sources

**[MONA: Myopic Optimization with Non-myopic Approval Can Mitigate Multi-step Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/farquhar25a/farquhar25a.pdf)**
> Selecting a sequence of actions across multiple steps to achieve a goal or manipulate future outcomes.

**[zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1087.pdf) (as "Natural planning")**
> The ability to decompose a problem into an ordered sequence of intermediate subgoals that guide solution generation.

**[2025.emnlp-main.1087.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1087.checklist.pdf) (as "Step-by-step planning")**
> The latent ability of a model to decompose complex problems into intermediate reasoning steps before arriving at a solution.

## Relationships

### Multi-step planning →
- **Complex reasoning** (behaviors tasks) — *causes*
  > Our detailed analysis demonstrates how planning trajectories improves complex reasoning capabilities, showing that PLAN-TUNING is an effective strategy for improving task-specific performance of smaller LLMs. (Abstract)
  - [zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1087.pdf)

### Associated with
- **Task decomposition** (behaviors tasks)
  - [zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1087.pdf)

# Long-horizon planning
**Type:** Construct  
**Referenced in:** 22 papers  
**Also known as:** Long-term planning, Strategic dialogue planning, High-level planning  

## State of the Field

Across the surveyed literature, long-horizon planning is most commonly defined as the ability to produce a sequence of actions over many steps to achieve a goal, sometimes involving multiple concurrent objectives or interdependent steps. A smaller set of papers uses the related term "long-term planning" to describe formulating high-level strategies over an extended period, while more specific framings like "strategic dialogue planning" and "high-level planning" appear in single papers. The construct is operationalized and measured through performance on various complex tasks. For example, it is evaluated using the Travelplanner benchmark, which tests planning under user-defined constraints, and in environments like Crafter, which combines "multiple interactions, concurrent objectives, and error handling." Other evaluations involve sequential robotic instruction chains and complex desktop tasks. The concept is frequently associated with hierarchical planning, which one paper describes as a method to "decomposes long-horizon planning problems into several short-horizon problems" (Learning Grounded Action Abstractions from Language). It is also studied alongside embodied planning and is a target for enhancement through auxiliary tasks in theorem proving. Several sources note that this capability remains a challenge for models, particularly in "partially observable multi-agent settings" (Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments) or due to the "auto-regressive nature of LLMs" (Enhancing Decision-Making of Large Language Models via Actor-Critic).

## Sources

**[Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf)**
> Producing action sequences that achieve a goal over many steps or with multiple concurrent objectives.

**[Large Language Models Play StarCraft II:Benchmarks and A Chain of Summarization Approach](https://proceedings.neurips.cc/paper_files/paper/2024/file/f0ebc318e2df08360b2df559e81602e5-Paper-Conference.pdf) (as "Long-term planning")**
> The capacity to formulate and adapt high-level strategies that unfold over an extended period to achieve a final goal.

**[Error-driven Data-efficient Large Multimodal Model Tuning](https://aclanthology.org/2025.acl-long.993.pdf) (as "Strategic dialogue planning")**
> The ability to strategically generate a sequence of dialogue actions to guide a conversation toward a specific, long-horizon target.

**[Error-driven Data-efficient Large Multimodal Model Tuning](https://aclanthology.org/2025.acl-long.993.pdf) (as "Long-range dependency modeling")**
> The capability to capture and coordinate dependencies between distant elements in a dialogue, such as ensuring correct keyword order across multiple turns or aligning early actions with final goals.

**[Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf) (as "High-level planning")**
> The capacity to generate and execute long-horizon, goal-directed plans under constraints, requiring decomposition of complex objectives into coordinated subtasks.

## Relationships

### Long-horizon planning →
- **Travelplanner** (measurements) — *measured_by*
  - [Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf)

### → Long-horizon planning
- **Theorem proving** (behaviors tasks) — *causes*
  > We begin by training a whole-proof generation model, incorporating several auxiliary tasks to enhance its capabilities in mathematical reasoning and long-horizon planning
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf)

### Associated with
- **Hierarchical planning** (constructs)
  > This bi-level planning approach decomposes long-horizon planning problems into several short-horizon problems. (Section 2)
  - [Learning Grounded Action Abstractions from Language](https://proceedings.iclr.cc/paper_files/paper/2024/file/99dec5837aae1a7459960c6121b9e3b8-Paper-Conference.pdf)
- **Embodied planning** (behaviors tasks)
  - [Discriminator-Guided Embodied Planning for LLM Agent](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6f2b968c4ee8ba260cd7077e39590dd-Paper-Conference.pdf)

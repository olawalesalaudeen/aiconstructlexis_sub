# Navigation
**Type:** Behavior  
**Referenced in:** 17 papers  
**Also known as:** Grid world navigation, Low-level navigation, Webpage interaction, Spatial navigation  

## State of the Field

The most prevalent usage of navigation in the provided literature describes the behavior of an agent moving through an environment to reach a target location or object. This is commonly conceptualized in spatial contexts, such as moving through a Minecraft world to find resources, or traversing a simple grid with discrete "up, down, left, and right" actions. A more fine-grained view defines it as "low-level navigation," which involves executing precise, atomic actions like moving forward or rotating. While most definitions focus on the observable action, a smaller set of work frames it as a "cognitive ability" to understand spatial layouts and plan routes for tasks like "room-to-room" or "object retrieval". A distinct, less frequent application of the term extends it to non-spatial domains, where it refers to a web agent's interaction with a webpage to complete a task. To measure this behavior, researchers employ several benchmarks. The provided papers report using MineDojo to evaluate navigation alongside other behaviors, TextWorld for navigating text-based mazes, and BabyAI for testing agents across different navigation task types.

## Sources

**[RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)**
> Moving through the Minecraft environment to locate targets such as trees, cows, stones, or underground resources.

**[LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ruoss25a/ruoss25a.pdf) (as "Grid world navigation")**
> Moving a player through a grid world with up, down, left, and right actions to reach a target location.

**[EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf) (as "Low-level navigation")**
> Executing precise movement and orientation adjustments in a simulated environment to reach a target location or object, using atomic actions like moving forward or rotating.

**[Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.104.pdf) (as "Webpage interaction")**
> The process of a web agent taking a sequence of actions to engage with a webpage environment in order to complete a user-specified task.

**[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Spatial navigation")**
> The ability to efficiently move within a spatial environment to reach a target location.

## Relationships

### Navigation →
- **BabyAI** (measurements) — *measured_by*
  > Agents are tested across five different types of navigation tasks, see Appendix A.
  - [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf)
- **TextWorld** (measurements) — *measured_by*
  > In each game, the agent needs to complete the task while navigating a maze of different rooms
  - [BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0b1515be276f6ba82b4f2b25e50bef0-Paper-Conference.pdf)
- **MineDojo** (measurements) — *measured_by*
  > "The behaviors that can be conducted in MineDojo primarily include navigation, harvest, combat, and craft."
  - [LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dj/li25dj.pdf)

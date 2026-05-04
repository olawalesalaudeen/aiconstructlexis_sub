# Meta-world
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** LLF-Bench Meta-World  

## State of the Field

Across the provided literature, Meta-world is consistently described as a simulated benchmark environment for robotics. It is most commonly used to measure `Robotic manipulation`, with some work also using it to evaluate `In-context reinforcement learning`. The environment consistently features a Sawyer robot manipulator that an agent controls to interact with objects. The specific manipulation tasks, however, are described differently across papers; some list tasks like "reach, pick-place, and push," while others mention manipulating objects such as "doors, drawers and windows." One paper refers to a specific version, "LLF-Bench Meta-World," used for testing an agent's ability to learn from language feedback. Another source notes that the environment is built on the MuJoCo physics engine.

## Sources

**[Trace is the Next AutoDiff: Generative Optimization with Rich Feedback, Execution Traces, and LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/83ba7056bce2c3c3c27e17397cf3e1f0-Paper-Conference.pdf) (as "LLF-Bench Meta-World")**
> A simulated benchmark environment featuring a Sawyer robot manipulator for testing an agent's ability to learn from language feedback on tasks like reach, pick-place, and push.

**[KALM: Knowledgeable Agents by Offline Reinforcement Learning from Large Language Model Rollouts](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4cdb4090e04816422afcbb08d4badcf-Paper-Conference.pdf)**
> A benchmark robotics manipulation environment built on the MuJoCo physics engine where an agent controls a Sawyer robot to manipulate various objects like doors, drawers, and windows.

## Relationships

### → Meta-world
- **Robotic manipulation** (behaviors tasks) — *measured_by*
  - [KALM: Knowledgeable Agents by Offline Reinforcement Learning from Large Language Model Rollouts](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4cdb4090e04816422afcbb08d4badcf-Paper-Conference.pdf)
- **In-context reinforcement learning** (constructs) — *measured_by*
  - [Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf)

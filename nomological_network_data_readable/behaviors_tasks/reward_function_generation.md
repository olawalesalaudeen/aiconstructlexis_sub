# Reward function generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, reward function generation is consistently framed as the task of producing code that specifies an agent's objectives within a simulation. This generated code defines the reward signal for a reinforcement learning agent, which, as one paper notes, "returns a scalar number, whose cumulative maximization defines the task" ('OMNI-EPIC...'). The behavior is often discussed as part of a larger generative process where models create not only reward functions but also other simulation elements like "simulator dynamics" and "termination functions" ('FactorSim...', 'OMNI-EPIC...'). The application domains mentioned for this task include robotics and games. The provided data also suggests connections to underlying model capabilities, with some work positing that constructs like `Information extraction` and `Commonsense understanding` are causes of reward function generation.

## Sources

**[FactorSim: Generative Simulation via Factorized Representation](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f35ec2f7f403ef2c83d65b581df10bc-Paper-Conference.pdf)**
> The task of generating code for reward functions that specify the objectives for an agent within a simulation.

## Relationships

### → Reward function generation
- **Information extraction** (behaviors tasks) — *causes*
  - [A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/file/074f42212be2c8ee651db00f17965ec4-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *causes*
  - [REvolve: Reward Evolution with Large Language Models using Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc8ee7c7ab5b5f6b1615045dfb617ed6-Paper-Conference.pdf)

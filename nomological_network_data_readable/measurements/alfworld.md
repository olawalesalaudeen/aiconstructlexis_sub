# ALFWorld
**Type:** Measurement  
**Referenced in:** 47 papers  
**Also known as:** AlfWorld, Alfworld  

## State of the Field

Across the provided literature, ALFWorld is most commonly characterized as a benchmark for evaluating LLM agents, frequently described as a "text-based game suite" or an "embodied task benchmark" set in interactive household environments. The benchmark requires an agent to follow high-level language instructions to complete multi-step tasks—such as finding, moving, and manipulating objects—by issuing a sequence of low-level text actions. Several sources note that it is based on the ALFRED dataset and implemented using a text-only interface, with one paper specifying it contains "six types of tasks with 134 unseen environments for evaluation." The most prevalent application of ALFWorld is to measure an agent's decision-making capabilities, with multiple papers identifying it as a popular benchmark for this purpose, sometimes specified as sequential decision-making. It is also used to assess a variety of other agent abilities, including natural language understanding, embodied reasoning, and the performance of commonsense tasks. A smaller set of studies uses ALFWorld to evaluate generalization, data efficiency, and, in one instance, visual-semantic understanding. The tasks can involve complex interactions, with one paper highlighting that some actions like "Clean, Heat, Cool are critical due to irreversible effects."

## Sources

**[Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf) (as "AlfWorld")**
> An embodied task benchmark based on the ALFRED dataset, where an agent must follow high-level language instructions to complete household tasks in a simulated environment using low-level text actions.

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)**
> A text-based game suite of interactive housework environments used to evaluate LLM-agent planning and task completion.

**[AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf) (as "Alfworld")**
> Alfworld is an interactive agent benchmark used to evaluate task completion in household-style environments.

## Relationships

### → ALFWorld
- **Decision-making** (constructs) — *measured_by*
  > We use open-source environments: HotPotQA (Yang et al., 2018), WebShop (Yao et al., 2022) and AlfWorld (Shridhar et al., 2021) , which evaluates the agent’s reasoning and tool usage abilities for question answering reasoning, multi-step decision making, and web browsing. (Section 5.1.1)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Agent Planning with World Knowledge Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/d032263772946dd5026e7f3cd22bce5b-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > We next test CoSo on the ALFWorld (Shridhar et al., 2021), an embodied environment for testing decision-making in scenarios requiring visual-semantic understanding. (Section 5.1).
  - [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25n/feng25n.pdf)
- **Sequential decision-making** (constructs) — *measured_by*
  > ALFWorld (Shridhar et al., 2020) is a popular benchmark for examining LLM-based agents’ decision-making ability (Section 4.1).
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Non-myopic Generation of Language Models for Reasoning and Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/56b694fb10c02b177e75a41f45825a74-Paper-Conference.pdf)
- **Data efficiency** (constructs) — *measured_by*
  > "We conduct experiments on major benchmarks like ALFWorld and Overcooked, demonstrating that the sample efficiency of traditional RL algorithms... can largely benefit from integrating LLM action priors."
  - [Efficient Reinforcement Learning with Large Language Model Priors](https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf)
- **Cross-domain generalization** (constructs) — *measured_by*
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > ALFWorld (Shridhar et al., 2020) provides a text-based household task environment that for natural language understanding and embodied reasoning. (Section 5.1)
  - [BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation](https://aclanthology.org/2025.emnlp-main.152.pdf)
- **Embodied reasoning** (constructs) — *measured_by*
  - [BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation](https://aclanthology.org/2025.emnlp-main.152.pdf)
- **Language proficiency** (constructs) — *measured_by*
  - [Stop Looking for “Important Tokens” in Multimodal Language Models: Duplication Matters More](https://aclanthology.org/2025.emnlp-main.506.pdf)

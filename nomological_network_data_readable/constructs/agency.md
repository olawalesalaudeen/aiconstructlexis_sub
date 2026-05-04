# Agency
**Type:** Construct  
**Referenced in:** 14 papers  
**Also known as:** Agentic ability, Agentic capabilities, Agentic capability, Autonomy, Agent-oriented abilities, Model autonomy, Goal-directed behavior, Agentic abilities  

## State of the Field

Across the surveyed literature, Agency is predominantly characterized as a latent capacity for a model to act autonomously to achieve complex, multi-step goals within an environment. While this general framing is common, definitions vary in emphasis, with some papers highlighting "strategic decision-making" ("Moral Alignment for LLM Agents"), others focusing on "goal-directed behavior" over multiple turns ("LMRL Gym: Benchmarks for Multi-Turn Reinforcement Learning with Language Models"), and a subset defining it as "autonomy"—the ability to make independent decisions without external control. This capacity is described as encompassing processes like perceiving, planning, and acting. One paper further specifies these as "workflow, tool use/function call, long-context understanding and real-world application" ("Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression"). The field operationalizes and measures agency through performance on various benchmarks designed to elicit these behaviors. Commonly cited instruments include AgentBench and AgentBoard for general evaluation, as well as more specialized benchmarks like OSWORLD, AndroidControl, and GUI-Odyssey for assessing interactions with graphical user interfaces. The construct is also studied in relation to programming ability and consistency.

## Sources

**[OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf) (as "Agentic capability")**
> The general capacity to autonomously interact with operating systems and complete multi-step tasks through GUI interactions, encompassing planning, action execution, and environment response handling.

**[VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf) (as "Agentic ability")**
> The latent capacity of a model to act autonomously to accomplish tasks within an environment.

**[BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0b1515be276f6ba82b4f2b25e50bef0-Paper-Conference.pdf) (as "Agentic capabilities")**
> The ability of a model to act autonomously and purposefully to achieve complex goals in an environment.

**[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf) (as "Autonomy")**
> The capacity of an embodied agent to make informed, independent decisions without external control.

**[DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf) (as "Agent-oriented abilities")**
> The latent capacity to perform agent-like functions such as selecting tools or acting in tool-using workflows.

**[Moral Alignment for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2b1bad4756ceee8f408e16b8e6e4383-Paper-Conference.pdf)**
> The capacity of a system to make strategic decisions by selecting actions in an environment that lead to different outcomes.

**[MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e3767db483c942b883eb4f8cfb74e31-Paper-Conference.pdf) (as "Model autonomy")**
> The capability of an AI agent to operate and solve complex, multi-step problems without human intervention.

**[LMRL Gym: Benchmarks for Multi-Turn Reinforcement Learning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abdulhai25a/abdulhai25a.pdf) (as "Goal-directed behavior")**
> The latent tendency of an agent to pursue a specific objective over multiple interaction turns, rather than generating responses based on immediate context or imitation.

**[AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/877b40688e330a0e2a3fc24084208dfa-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Agentic abilities")**
> The latent capacity of an LLM to function as a general-purpose agent across diverse environments by perceiving, planning, and acting over multiple turns.

## Relationships

### Agency →
- **AgentBench** (measurements) — *measured_by*
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **AgentBoard** (measurements) — *measured_by*
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **OSWORLD** (measurements) — *measured_by*
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **AndroidControl** (measurements) — *measured_by*
  > We examine five distinct agent benchmarks across three different platforms: AndroidControl (Li et al., 2024) and GUI-Odyssey (Lu et al., 2024a) for mobile agents; GUI-Act-Web (Chen et al., 2024a) and OmniAct-Web (Kapoor et al., 2024) for web agents; and OmniAct-Desktop for Windows environments.
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)
- **GUI-Odyssey** (measurements) — *measured_by*
  > We examine five distinct agent benchmarks across three different platforms: AndroidControl (Li et al., 2024) and GUI-Odyssey (Lu et al., 2024a) for mobile agents; GUI-Act-Web (Chen et al., 2024a) and OmniAct-Web (Kapoor et al., 2024) for web agents; and OmniAct-Desktop for Windows environments.
  - [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/0faa4bc5f522076947a030273629d4fe-Paper-Conference.pdf)

### Associated with
- **Programming** (behaviors tasks)
  - [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf)

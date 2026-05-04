# Web navigation
**Type:** Behavior  
**Referenced in:** 44 papers  
**Also known as:** GUI navigation, Web browsing, Vision-based web navigation  

## State of the Field

Web navigation is predominantly described as the behavior of an agent interacting with websites to find information or complete a goal. This behavior is consistently framed as a sequential decision-making task involving a series of actions, most commonly clicking links, filling forms, and typing text. While the prevailing usage centers on web-based environments, sometimes requiring an understanding of HTML structure, a smaller set of work uses related terms like "GUI navigation" for broader interactions with graphical interfaces or "web browsing" as a form of tool use. A more specific variant, "vision-based web navigation," is defined by its reliance on only screenshots as input. The field operationalizes and measures this behavior using a wide array of benchmarks, with Mind2Web and WebArena being the most frequently cited in this dataset for evaluating performance on real-world websites and in simulated environments. Other instruments mentioned include WebShop and MiniWoB++. For multimodal or vision-centric versions of the task, papers use benchmarks such as VisualWebArena, which is designed for multimodal agents, and WebVoyager.

## Sources

**[Multimodal Web Navigation with Instruction-Finetuned Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ef7d8359036afd8c2378d82c21058a4-Paper-Conference.pdf)**
> The task of interacting with websites to find information or complete a goal, which involves understanding HTML structure and performing actions like clicking links and filling forms.

**[DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf) (as "GUI navigation")**
> Moving through graphical user interfaces by tapping, typing, swiping, and pressing controls to reach a target state.

**[OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Web browsing")**
> Interacting with web browsers to navigate websites, search for information, or complete online forms and transactions.

**[Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf) (as "Vision-based web navigation")**
> Navigating through web pages using only screenshots as input and performing actions like clicking or typing on numbered interactive elements to complete user tasks.

## Relationships

### Web navigation →
- **Mind2Web** (measurements) — *measured_by*
  > “We employ Mind2Web (Deng et al., 2023) to train and evaluate the agent’s capability of performing complex instructions on real-world websites.”
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
- **WebArena** (measurements) — *measured_by*
  > We adopt Mind2Web and WebArena for evaluation for their generalizability and resemblance of real-world web interactions. (Section 2)
  - [AgentTrek: Agent Trajectory Synthesis via Guiding Replay with Web Tutorials](https://proceedings.iclr.cc/paper_files/paper/2025/file/c681fb2bf1d785fbc766f3ea14758aab-Paper-Conference.pdf)
- **WebShop** (measurements) — *measured_by*
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
- **MiniWoB++** (measurements) — *measured_by*
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **GAIA** (measurements) — *measured_by*
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **VisualWebArena** (measurements) — *measured_by*
  > "We build on the VisualWebArena (VWA) (Koh et al., 2024a), a real environment for web-based agents."
  - [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3b893ba1de12f76020b03f7ae8e1afd-Paper-Conference.pdf)
- **AitW** (measurements) — *measured_by*
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **WebVoyager** (measurements) — *measured_by*
  > “as well as a text-only state-of-the-art 81.36% success rate on WebVoyager.”
  - [Proposer-Agent-Evaluator (PAE): Autonomous Skill Discovery For Foundation Model Internet Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25ah/zhou25ah.pdf)

### Associated with
- **Sequential decision-making** (constructs)
  > these methods are not well-suited for sequential decision-making tasks that require interactions with an environment, such as web navigation (Yao et al., 2022). (Section 1. Introduction)
  - [UniRAG: Unified Query Understanding Method for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.694.pdf)
- **Tool use** (behaviors tasks)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)

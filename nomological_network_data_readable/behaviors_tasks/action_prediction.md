# Action prediction
**Type:** Behavior  
**Referenced in:** 28 papers  
**Also known as:** Chess move prediction, Intention prediction, Next-action prediction, High-level behavior prediction, Legal move prediction, Next speaker prediction, Turn-taking prediction  

## State of the Field

Across the surveyed literature, 'Action prediction' is most commonly defined as the task of determining and generating the next appropriate action in a sequence to accomplish a larger goal, particularly within web navigation and user interface (UI) contexts. In this prevalent framing, an action consists of identifying a 'target element to interact with, along with the operation, such as click, type, or select an option' ("A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis"). This behavior is frequently operationalized and measured using benchmarks like Mind2Web and MME-RealWorld, with some work also citing the GUIDE benchmark for next-action prediction. However, the term is applied across a wide range of domains, leading to several specialized definitions. A notable line of work treats it as predicting the next move in board games like chess, sometimes with a specific focus on 'legal move prediction.' Other applications include forecasting the future movements of agents in autonomous driving scenarios ('intention prediction'), predicting conversational turns in spoken dialogue ('turn-taking prediction'), and selecting the next speaker in multi-character conversations. In reinforcement learning contexts, it is framed as predicting an action from a sequence of states and returns. The concept is studied alongside GUI automation, commonsense knowledge, and conversational ability, and one paper suggests that spatiotemporal reasoning can facilitate action prediction.

## Sources

**[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)**
> The task of determining and generating the next appropriate action (e.g., which element to click, what text to type) in a sequence to accomplish a larger goal.

**[Intelligence at the Edge of Chaos](https://proceedings.iclr.cc/paper_files/paper/2025/file/d791394d32c428aecc7a5b101fb47799-Paper-Conference.pdf) (as "Chess move prediction")**
> The task of predicting the next move in a chess game given a sequence of previous moves in Standard Algebraic Notation.

**[MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf) (as "Intention prediction")**
> The task of forecasting the future actions or movements of a dynamic agent, such as a vehicle or pedestrian, based on an image.

**[Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf) (as "Next-action prediction")**
> The task of predicting the next user action on a UI, given the screen and a history of previous actions.

**[Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf) (as "Legal move prediction")**
> Generating only valid moves according to the rules of the game, filtering out impossible or illegal actions during decision-making.

**[NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf) (as "Turn-taking prediction")**
> The observable generation of speech tokens that align with appropriate conversational transitions, such as when to speak, pause, overlap, or interrupt, based on dual-channel input dynamics.

**[CoSER: Coordinating LLM-Based Persona Simulation of Established Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dk/wang25dk.pdf) (as "Next speaker prediction")**
> Selecting which character should speak next in a multi-character conversation.

**[SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cm/zhang25cm.pdf) (as "High-level behavior prediction")**
> Answering multiple-choice driving questions about high-level behavior such as speed and steering actions.

## Relationships

### Action prediction →
- **Mind2Web** (measurements) — *measured_by*
  > “In the action prediction tasks, we transfer WebGUM finetuned for MiniWoB++ with 401K dataset into real-world Mind2Web”
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
- **MME-RealWorld** (measurements) — *measured_by*
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)

### → Action prediction
- **Spatiotemporal reasoning** (constructs) — *causes*
  > we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models’ spatial-temporal awareness for action prediction by encoding state-action trajectories visually. (ABSTRACT)
  - [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://proceedings.iclr.cc/paper_files/paper/2025/file/8667f264f88c7938a73a53ab01eb1327-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)
- **GUI automation** (behaviors tasks)
  - [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf)
- **World modeling** (constructs)
  - [Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf)
- **Conversational ability** (constructs)
  > empirical results show that our proposed method, NTPP, significantly improves the conversational abilities of SLMs in terms of turn-taking prediction, response coherence, and naturalness. (Abstract)
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)

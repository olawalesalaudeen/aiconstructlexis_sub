# Role-playing
**Type:** Behavior  
**Referenced in:** 31 papers  
**Also known as:** Human-role dialogue, Inter-role dialogue, Commentary interaction, Role playing, Perspective simulation, Persona adoption, Character portrayal, Survey response generation, Patient response simulation, Classroom simulation, Student simulation, Role-playing ability, User persona, AI persona, Role-playing capability, Role misalignment  

## State of the Field

Role-playing is most commonly described as the observable behavior of an LLM adopting and maintaining a specified persona or character during a conversational interaction. This behavior is instantiated in diverse ways, from general character portrayals like learning to "talk like a pirate" to more specific simulations, such as mimicking the perspectives of lawmakers, generating sociological survey responses, or simulating patient and student behaviors for research. While the prevailing usage treats it as an observable task, a smaller set of papers conceptualizes it as a latent "role-playing ability" or "capability," focusing on traits like character consistency and emotional coherence. To measure this behavior, researchers use benchmarks like WildBench, which includes role-playing among a diverse array of user tasks, as well as human evaluation. The behavior is studied in various contexts, including interactive environments for social intelligence where agents "coordinate, collaborate, exchange, and compete," and as a vector for jailbreak attacks. For instance, one paper notes that a specific alignment direction is "triggered by explicit mentions of ChatGPT and positively correlates with the dominant direction, likely due to its prevalent use in role-playing jailbreaks." Role-playing is also studied alongside hallucination, commonsense knowledge, and controllability, and some work suggests that the model's judgment of a "user persona" can influence its propensity to generate harmful content.

## Sources

**[How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe79ae16496a0f5b57287873de072d1-Paper-Conference.pdf)**
> The behavior of adopting a specified persona or character in a conversational interaction.

**[WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf) (as "Role playing")**
> Adopting a specific persona or character in conversation with the user.

**[MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf) (as "Commentary interaction")**
> A single-turn dialogue task where an agent, acting as a character, provides comments or reflections about a given image without further interaction.

**[MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf) (as "Human-role dialogue")**
> Multi-turn dialogues centered around an image between a human user without a specific identity and a character.

**[MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf) (as "Inter-role dialogue")**
> A multi-turn dialogue task where an agent, acting as one character, converses with another character about a given image.

**[Linear Representations of Political Perspective Emerge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1557cc3e1a67f985dbdb162db9963dd0-Paper-Conference.pdf) (as "Perspective simulation")**
> The observable action of generating text mimicking the viewpoint of specific entities like lawmakers or news outlets.

**[A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf) (as "Persona adoption")**
> The observable task of generating text that consistently embodies a specified character or style, such as a pirate persona.

**[CoSER: Coordinating LLM-Based Persona Simulation of Established Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dk/wang25dk.pdf) (as "Character portrayal")**
> The specific act of a language model generating utterances, actions, and thoughts for a single assigned character within a conversation.

**[DiMo-GUI: Advancing Test-time Scaling inGUIGrounding via Modality-Aware Visual Reasoning](https://aclanthology.org/2025.emnlp-main.1335.pdf) (as "Survey response generation")**
> Producing answer options to closed-ended sociological survey questions as if the model were a human respondent.

**[GraphAgent: Agentic Graph Language Assistant](https://aclanthology.org/2025.emnlp-main.1340.pdf) (as "Patient response simulation")**
> The observable behavior of simulating patient responses to symptom inquiries, either from recorded data or inferred based on disease-symptom associations when information is missing.

**[Structured Preference Optimization for Vision-Language Long-Horizon Task Planning](https://aclanthology.org/2025.emnlp-main.885.pdf) (as "Student simulation")**
> Producing synthetic learner behavior that imitates students with different competency levels and learning trajectories.

**[Structured Preference Optimization for Vision-Language Long-Horizon Task Planning](https://aclanthology.org/2025.emnlp-main.885.pdf) (as "Classroom simulation")**
> Using LLM agents to simulate virtual students and tutors in interactive learning environments for pedagogical research and system training.

**[WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games](https://proceedings.neurips.cc/paper_files/paper/2024/file/9dd4533e7e4e5ed809344280609c5b05-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Role-playing ability")**
> The latent ability to adopt and consistently maintain a specified character or persona during an interactive engagement.

**[Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf) (as "User persona")**
> The model's internal representation and judgment of a user's attributes, such as their personality, motivations, and background.

**[Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf) (as "AI persona")**
> A consistent style of response, character, or set of goals that an LLM adopts across different interactions.

**[Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.172.pdf) (as "Role-playing capability")**
> The latent ability of a conversational agent to maintain character consistency, language style, emotional expression, and behavioral coherence in role-based interactions.

**[VocalNet: SpeechLLMs with Multi-Token Prediction for Faster and High-Quality Generation](https://aclanthology.org/2025.emnlp-main.990.pdf) (as "Role misalignment")**
> The model's latent shift from a safety-oriented gatekeeper role to an execution-oriented task-completion role, triggered by first-person commitments that alter its internal role attribution.

## Relationships

### Role-playing →
- **Harmful content generation** (behaviors tasks) — *causes*
  > In this work, we show that whether they do so [divulge harmful information] depends signiﬁcantly on who they are talking to, which we refer to as user persona.
  - [Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf)
- **WildBench** (measurements) — *measured_by*
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [CoSER: Coordinating LLM-Based Persona Simulation of Established Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dk/wang25dk.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games](https://proceedings.neurips.cc/paper_files/paper/2024/file/9dd4533e7e4e5ed809344280609c5b05-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction following** (constructs)
  - [ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)
- **Controllability** (constructs)
  - [Getting More Juice Out of Your Data: Hard Pair Refinement Enhances Visual-Language Models Without Extra Data](https://aclanthology.org/2025.naacl-long.400.pdf)

# Theory of mind
**Type:** Construct  
**Referenced in:** 41 papers  
**Also known as:** Theory of Mind, Belief modeling, Mental state reasoning, Belief formation, Intention inference, Belief updating, Action intention inference, Mental state tracking, Multi-agent mental state tracking  

## State of the Field

Across the provided data, Theory of Mind (ToM) is most commonly defined as the latent ability to infer, model, and reason about the mental states of other agents, including their beliefs, intentions, preferences, desires, and knowledge. The purpose of this capability is frequently cited as enabling more effective social interaction, such as predicting behavior, improving coordination in multi-agent tasks, or achieving better outcomes in negotiations by, as one paper notes, "accurately modeling the opponent's payoff structure" (Evaluating Language Model Agency Through Negotiations). While this core framing is prevalent, the concept is also discussed under more specific labels like "belief modeling," "mental state tracking," and "intention inference," with some work focusing on dynamic aspects like "belief updating" in response to new observations. The field operationalizes and measures ToM using a variety of specialized benchmarks. These instruments are reported to assess the construct in different contexts, including multimodal scenarios using MMToM-QA, "situated social interactions" with ToM-SSI, and the understanding of "white lies" via TactfulToM. Within this body of work, ToM is consistently studied alongside and treated as a component of broader capabilities such as social reasoning and strategic reasoning.

## Sources

**[Can LLMs Keep a Secret? Testing  Privacy  Implications of Language Models  via Contextual Integrity Theory](https://proceedings.iclr.cc/paper_files/paper/2024/file/08305d8b2ddab98932c163ea73df065f-Paper-Conference.pdf)**
> The latent ability of a model to infer the beliefs, preferences, and intentions of other agents, enabling more effective negotiation through accurate modeling of the opponent's payoff structure.

**[Building Cooperative Embodied Agents Modularly with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/54b8b4e0b4ba4aad112e84f32e3b5dbb-Paper-Conference.pdf) (as "Theory of Mind")**
> The ability to model and reason about the mental states, intentions, and actions of other agents, enabling effective coordination and communication in decentralized settings.

**[Learning to Discuss Strategically: A Case Study on One Night Ultimate Werewolf](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cea78701eb986f3ec357eb9b7c6badd-Paper-Conference.pdf) (as "Belief modeling")**
> The latent capability to infer hidden roles and states of other players based on observations, dialogue, and game rules.

**[SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf) (as "Mental state reasoning")**
> The ability to infer and reason about the beliefs, desires, and intentions of other agents to predict their actions.

**[Cooperate or Collapse:  Emergence of Sustainable Cooperation in a Society of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca9567d8ef6b2ea2da0d7eed57b933ee-Paper-Conference.pdf) (as "Belief formation")**
> The ability to form a belief about the likely actions or intentions of other agents in a multi-agent system.

**[PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6164b6e5352c139e9ddc1a98c09e4e4a-Paper-Conference.pdf) (as "Intention inference")**
> The ability to infer the user's intended task when the instruction does not explicitly name the target object or action.

**[Transformers Represent Belief State Geometry in their Residual Stream](https://proceedings.neurips.cc/paper_files/paper/2024/file/8936fa1691764912d9519e1b5673ea66-Paper-Conference.pdf) (as "Belief updating")**
> The cognitive process of dynamically revising beliefs about the hidden state of the world based on new observations, as formalized by the mixed-state presentation (MSP).

**[Think Then React: Towards Unconstrained Action-to-Reaction Motion Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea0b28cbbd0cbc45ec4ac38e92da9cb2-Paper-Conference.pdf) (as "Action intention inference")**
> The latent ability of the model to infer the semantic meaning and goal of an observed human action sequence.

**[MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities ofLLMTutors](https://aclanthology.org/2025.emnlp-main.12.pdf) (as "Belief reasoning")**
> The latent ability of an LLM to infer the underlying intentions or mental states of an agent based on its observable behavior, enabling alignment checks with user intent.

**[Causal Interventions Reveal Shared Structure AcrossEnglish Filler–Gap Constructions](https://aclanthology.org/2025.emnlp-main.1272.pdf) (as "Mental state tracking")**
> The ability to accurately attribute and follow the mental states of different agents, such as their beliefs and knowledge, within a dynamic context.

**[REVIVINGYOURMNEME: Predicting The Side Effects ofLLMUnlearning and Fine-Tuning via Sparse Model Diffing](https://aclanthology.org/2025.emnlp-main.1642.pdf) (as "Multi-agent mental state tracking")**
> The ability to simultaneously reason about the mental states of multiple agents in a group interaction, especially under asymmetric information and mixed social attitudes.

## Relationships

### Theory of mind →
- **MMToM-QA** (measurements) — *measured_by*
  > The MMToM-QA dataset (Jin et al., 2024) is the pioneering resource aimed at assessing machine learning models’ ability to infer mental states from multimodal data, combining video and text in real-world tasks.
  - [Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning: A Scalable Bayesian Planner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bk/zhang25bk.pdf)
- **FANToM** (measurements) — *measured_by*
  - [Explore Theory of Mind: program-guided adversarial data generation for theory of mind reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a901d5540789a086ee0881a82211b63d-Paper-Conference.pdf)
- **ToM-SSI** (measurements) — *measured_by*
  > We introduce ToM-SSI, the first evaluation benchmark that addresses all aforementioned limitations by evaluating ToM abilities in Situated Social Interactions (Section 1).
  - [REVIVINGYOURMNEME: Predicting The Side Effects ofLLMUnlearning and Fine-Tuning via Sparse Model Diffing](https://aclanthology.org/2025.emnlp-main.1642.pdf)
- **TactfulToM** (measurements) — *measured_by*
  > "a comprehensive evaluation framework to test models’ understanding of white lies by combining mental state tracking questions with both established measures from Strange Stories (Happé, 1994) and our newly designed question types"
  - [Causal Interventions Reveal Shared Structure AcrossEnglish Filler–Gap Constructions](https://aclanthology.org/2025.emnlp-main.1272.pdf)

### Associated with
- **Social reasoning** (constructs)
  > SOTA models have also struggled with text-based QA tasks that probe competencies relevant to social reasoning, specifically theory-of-mind to interpret the goals and beliefs of characters (Le et al., 2019; Shapira et al., 2024; Ullman, 2023; Kim et al., 2023). (Section 2)
  - [Balcony: A Lightweight Approach to Dynamic Inference of Generative Language Models](https://aclanthology.org/2025.emnlp-main.1264.pdf)
- **Social intelligence** (constructs)
  - [Explore Theory of Mind: program-guided adversarial data generation for theory of mind reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a901d5540789a086ee0881a82211b63d-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation](https://proceedings.neurips.cc/paper_files/paper/2024/file/984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_Track.pdf)
- **State tracking** (constructs)
  - [Explore Theory of Mind: program-guided adversarial data generation for theory of mind reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a901d5540789a086ee0881a82211b63d-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf)
- **Strategic reasoning** (constructs)
  - [Goal-ConditionedDPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.370.pdf)
- **Intent understanding** (constructs)
  - [What DoVLMsNOTICE? A Mechanistic Interpretability Pipeline forGaussian-Noise-free Text-Image Corruption and Evaluation](https://aclanthology.org/2025.naacl-long.572.pdf)
- **Belief reasoning** (constructs)
  - [MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities ofLLMTutors](https://aclanthology.org/2025.emnlp-main.12.pdf)
- **Perspective taking** (constructs)
  - [REVIVINGYOURMNEME: Predicting The Side Effects ofLLMUnlearning and Fine-Tuning via Sparse Model Diffing](https://aclanthology.org/2025.emnlp-main.1642.pdf)

# Self-reflection
**Type:** Behavior  
**Referenced in:** 141 papers  
**Also known as:** Self-feedback, Reflection on failure cases, Short-term reflection, Long-term reflection, Reflection, Reflection generation, Reflection step generation, Self-QA reflection, Error reflection, Reflection capability, Introspection, Current reflection, Metacognitive monitoring, Meta-reflection, Discrimination, Error correction, Evaluation capability, Fine-grained evaluation capability, Self-critique, Self-debugging, Self-repair, Self-refinement capability, Self-correction ability, Self-correction capability, Refinement capability, Self-refinement, Progressive refinement, Self-repair capability, Error recovery, Self-critique ability, Self-revision capability, Self-repair ability, Self-knowledge, Self-awareness, Writing style knowledge, Self-recognition, Meta-cognition, Metacognition, Resource awareness, Response evolution awareness, Response quality awareness, Capability awareness, Metacognitive abilities, Meta-cognitive reasoning, Meta-reasoning, Metacognitive capabilities, Metacognitive capability, Cognitive reflection  

## State of the Field

Across the surveyed literature, Self-reflection is predominantly characterized as an observable behavior where a model analyzes and revises its own outputs or reasoning processes, appearing under numerous names including self-correction, self-debugging, and self-evaluation. The most common operationalization involves a model identifying and analyzing errors in its own outputs—such as code or reasoning steps—and then attempting to generate an improved response, a process described as where a model “inspects its own incorrect predictions, reflects on it to identify what went wrong and attempts to improve its prediction” (AutoGuide...). A related line of work operationalizes it as self-evaluation, where the model assesses the quality of its own generation, sometimes by producing a likelihood score for correctness or generating explicit natural language judgments like “This step is GOOD” (Enhancing Decision-Making of Large Language Models via Actor-Critic). This behavior is often elicited by integrating reflection steps into generation prompts or using explicit tags like `<reflection>`. The field measures this behavior using a range of benchmarks, frequently focused on code and mathematical reasoning, including `HumanEval`, `APPS`, `LiveCodeBench`, `GSM8k`, and `MR-GSM8K`. A smaller set of studies conceptualizes it more abstractly as a latent capability like metacognition, introspection, or self-awareness, involving a model's ability to reason about its own knowledge, limitations, or internal states. Self-reflection is reported to influence a wide array of outcomes, including `Self-correction`, `Reasoning quality`, `Faithfulness`, and `Generalization`. It is also studied in relation to concepts like `Planning` and `Code debugging`, and is described in one paper as “a key manifestation of System 2 reasoning” (MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs).

## Sources

**[Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)**
> The observable behavior of generating an analysis or explanation of errors in code before attempting to correct them, often integrated into the generation prompt.

**[Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf) (as "Self-evaluation")**
> The model's action of assessing the correctness or quality of its own generated answer, often by producing a likelihood score for a 'true' or 'false' label.

**[AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf) (as "Self-feedback")**
> An observable process where a model analyzes its own incorrect outputs, reflects on the errors, and attempts to generate an improved response.

**[Can LLMs Learn by Teaching for Better Reasoning? A Preliminary Study](https://proceedings.neurips.cc/paper_files/paper/2024/file/8340b085045cf13f1f0b6c2c4cc0a89c-Paper-Conference.pdf) (as "Reflection on failure cases")**
> The behavior of analyzing incorrect outputs to understand the cause of the error and verbalize reasons for the failure.

**[ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf) (as "Short-term reflection")**
> The observable behavior of an LLM generating a comparative analysis of two parent heuristics to provide guidance for creating an improved offspring.

**[ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf) (as "Long-term reflection")**
> The observable behavior of an LLM summarizing and distilling insights from multiple short-term reflections to guide future heuristic improvements.

**[Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf) (as "Reflection")**
> Analyzing generated outputs to provide feedback for refining expressions in subsequent workflow cycles.

**[Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf) (as "Reflection generation")**
> The production of short natural language judgments (e.g., 'This step is GOOD') about the appropriateness of past or candidate actions, used to enhance evaluation accuracy.

**[PoSum-Bench: Benchmarking Position Bias inLLM-based Conversational Summarization](https://aclanthology.org/2025.emnlp-main.405.pdf) (as "Reflection step generation")**
> The observable act of a model generating a reasoning step that questions or verifies a prior step, often indicated by phrases like 'Let’s verify' or 'Wait, we can also check'.

**[Calibrating Pseudo-Labeling with Class Distribution for Semi-supervised Text Classification](https://aclanthology.org/2025.emnlp-main.659.pdf) (as "Self-QA reflection")**
> Answering self-generated questions about the current trajectory to support reflective correction during planning.

**[OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1355.pdf) (as "Error reflection")**
> The observable process where a model identifies that an error occurred in a previous step and analyzes its specific category.

**[Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf) (as "Reflection capability")**
> The degree of an agent's proficiency in generating useful verbal feedback from prior experiences to improve subsequent task performance.

**[Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Introspection")**
> The ability to access information about internal representations or predict one's own behavior in hypothetical scenarios, using mechanisms that do not depend solely on learning from the training distribution.

**[HalluLens:LLMHallucination Benchmark](https://aclanthology.org/2025.acl-long.1177.pdf) (as "Current reflection")**
> The ability of a persona update process to adapt to recent user behaviors by incorporating dynamic changes and correcting errors in the existing persona.

**[MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf) (as "Metacognitive monitoring")**
> The latent ability of an LLM agent to model its own competence and learning progress across goals by leveraging semantic relationships, enabling self-directed curriculum learning.

**[Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cu/li25cu.pdf) (as "Meta-reflection")**
> The higher-order capacity to recognize and anticipate global patterns across multiple cycles of prediction, action, and feedback, enabling regulation beyond local adaptation.

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf) (as "Self-debugging")**
> The model's capacity to identify and correct errors in its own generated code based on feedback from code execution.

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf) (as "Self-correction")**
> The tendency to revise an initially invalid solution into a valid one when given error feedback.

**[An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf) (as "Error correction")**
> The process of identifying and repairing incorrect tokens or logic in a piece of code that was generated by a program translation model.

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Fine-grained evaluation capability")**
> The ability to judge text quality using detailed, user-defined criteria rather than only coarse or generic preferences.

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Evaluation capability")**
> The latent ability of a language model to assess the quality of generated text according to customized, fine-grained criteria provided via score rubrics and reference materials.

**[Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf) (as "Discrimination")**
> The latent ability of a model to identify and analyze potential mistakes, errors, or harmful elements within a given response.

**[Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf) (as "Self-critique")**
> The capability of a model to evaluate, identify flaws in, and analyze its own generated outputs without external feedback.

**[LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf) (as "Self-repair")**
> A latent mechanism by which a model compensates for changes or losses in individual functional components to maintain stable task performance.

**[SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf) (as "Self-refinement capability")**
> The ability to iteratively improve generated code by identifying and fixing its own errors based on internal analysis or feedback.

**[SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf) (as "Self-correction ability")**
> The latent capacity of a model to independently identify and rectify errors within its own generated reasoning process.

**[Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf) (as "Self-correction capability")**
> The latent ability of a model to identify and rectify its own errors in reasoning or generation without external corrective feedback.

**[AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf) (as "Self-refinement")**
> The latent ability of an agent to recognize its own mistakes from environmental feedback and correct its previous actions to find a successful solution path.

**[SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf) (as "Refinement capability")**
> The latent ability of a model to correct or improve a response that fails to follow an instruction, ideally with minimal irrelevant revisions.

**[Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf) (as "Progressive refinement")**
> The ability of a model to iteratively improve the accuracy, depth, and quality of its responses starting from an initial thought or approximate solution.

**[LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (as "Self-repair capability")**
> The latent ability to use error feedback to revise an initially flawed program into a correct solution.

**[ACCORD: Closing the Commonsense Measurability Gap](https://aclanthology.org/2025.naacl-long.194.pdf) (as "Error recovery")**
> The ability of an LLM agent to adjust its strategy and correct its course of action based on feedback from the environment, such as error messages.

**[Enhancing Multimodal Entity Linking withJaccard Distance-based Conditional Contrastive Learning and Contextual Visual Augmentation](https://aclanthology.org/2025.naacl-long.342.pdf) (as "Iterative refinement")**
> The latent capacity of an LLM system to improve its outputs through cycles of feedback and revision, simulating peer review in scientific communities.

**[OASIS: Order-Augmented Strategy for Improved Code Search](https://aclanthology.org/2025.acl-long.905.pdf) (as "Self-critique ability")**
> The latent capacity of a model to accurately evaluate and identify errors in its own reasoning process, as opposed to evaluating others' reasoning.

**[AnRe: Analogical Replay for Temporal Knowledge Graph Forecasting](https://aclanthology.org/2025.acl-long.232.pdf) (as "Self-revision capability")**
> The latent ability of a model to effectively correct its own incorrect reasoning or answers during iterative refinement, without external feedback.

**[Maximizing the Effectiveness of LargerBERTModels for Compression](https://aclanthology.org/2025.acl-long.1068.pdf) (as "Self-repair ability")**
> The capacity of LLMs to detect and correct their own errors in formal specification generation when provided with feedback or targeted prompts, indicating metacognitive reasoning and adaptability.

**[Looking Inward: Language Models Can Learn About Themselves by Introspection](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a6059857ae5c82ea9726ee9282a7145-Paper-Conference.pdf) (as "Self-awareness")**
> A model's capacity to understand and reason about its own identity, state, or existence, tested as a potential generalization of introspection.

**[Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf) (as "Self-knowledge")**
> The ability of a model to accurately assess its own internal knowledge, distinguishing between what it knows and what it does not, to avoid making false or unsupported claims.

**[Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/d560f94c582033e6d8eb0c97cdd4f721-Paper-Conference.pdf) (as "Self-recognition")**
> The latent ability of a model to identify its own generated text, entailing an internalized knowledge of its own writing style.

**[Inspection and Control of Self-Generated-Text Recognition Ability in Llama3-8b-Instruct](https://proceedings.iclr.cc/paper_files/paper/2025/file/d560f94c582033e6d8eb0c97cdd4f721-Paper-Conference.pdf) (as "Writing style knowledge")**
> The latent knowledge of characteristics of the model’s own generated writing that supports distinguishing it from other text.

**[Language-Codec: Bridging Discrete Codec Representations and Speech Language Models](https://aclanthology.org/2025.acl-long.655.pdf) (as "Meta-cognition")**
> The latent ability of an LLM to assess and regulate its own knowledge and limitations, enabling informed decisions about whether to rely on internal knowledge or external tools.

**[mPLUG-DocOwl2: High-resolution Compressing forOCR-free Multi-page Document Understanding](https://aclanthology.org/2025.acl-long.292.pdf) (as "Metacognition")**
> The model's ability to self-monitor its own cognitive processes, including reasoning and self-verification of its outputs to ensure correctness and reliability.

**[SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25l/guo25l.pdf) (as "Resource awareness")**
> The ability of an agent to recognize and adapt its problem-solving strategies in response to constraints on available resources, such as time and budget.

**[Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf) (as "Response evolution awareness")**
> The latent capacity of an optimization system to detect and utilize patterns in how model outputs change across iterations, allowing for more thoughtful and progressive refinement.

**[Reward-Augmented Data Enhances Direct Preference Alignment of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25az/zhang25az.pdf) (as "Response quality awareness")**
> The latent ability of an LLM to discern and adapt its behavior based on the absolute quality of responses, rather than only relative preferences, enabling differentiation across quality levels and generalization to higher-quality outputs.

**[Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf) (as "Capability awareness")**
> A facet of self-awareness concerning the model's ability to accurately assess its own knowledge and skills for a given task.

**[Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf) (as "Meta-cognitive reasoning")**
> The ability to reason about one’s own generative uncertainty and identify which questions best distinguish among candidate solutions.

**[Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf) (as "Metacognitive abilities")**
> The model's capacity to leverage higher-order thinking, such as applying insights from prior experiences to new problems.

**[MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf) (as "Meta-reasoning")**
> The ability to reason about a given reasoning process, which involves evaluating a solution's logic rather than just generating a solution.

**[Socratic-MCTS: Test-Time Visual Reasoning by Asking the Right Questions](https://aclanthology.org/2025.emnlp-main.1231.pdf) (as "Metacognitive capabilities")**
> Higher-order cognitive abilities related to a model's awareness and understanding of its own knowledge and reasoning processes.

**[A](https://aclanthology.org/2025.acl-long.185.pdf) (as "Metacognitive capability")**
> The latent ability of an LLM to detect inconsistencies or contradictions in input instructions and respond with self-monitoring behaviors such as abstention or refusal to answer.

**[BeyondWER: Probing Whisper’s Sub‐token Decoder Across Diverse Language Resource Levels](https://aclanthology.org/2025.emnlp-main.1592.pdf) (as "Cognitive reflection")**
> The latent tendency to engage in self-reflective thinking, including questioning initial responses and considering alternative reasoning paths.

## Relationships

### Self-reflection →
- **Self-correction** (behaviors tasks) — *causes*
  - [Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf)
- **Controllability** (constructs) — *causes*
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **Iterative refinement** (behaviors tasks) — *causes*
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **FLASK** (measurements) — *measured_by*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **Data efficiency** (constructs) — *causes*
  - [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf)
- **Ablation study** (measurements) — *measured_by*
  - [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *causes*
  - [Aligning Audio-Visual Joint Representations with an Agentic Workflow](https://proceedings.neurips.cc/paper_files/paper/2024/file/6c0ff499edc529c7d8c9f05c7c0ccb82-Paper-Conference.pdf)
- **Long-horizon task completion** (behaviors tasks) — *causes*
  - [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [BeyondWER: Probing Whisper’s Sub‐token Decoder Across Diverse Language Resource Levels](https://aclanthology.org/2025.emnlp-main.1592.pdf)
- **Planning** (constructs) — *causes*
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **MR-GSM8K** (measurements) — *measured_by*
  - [MR-GSM8K: A Meta-Reasoning Benchmark for Large Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0b0e6ac2da44d5839b13f90625b357-Paper-Conference.pdf)
- **Knowledge acquisition** (constructs) — *causes*
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **Consistency** (constructs) — *causes*
  - [Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1389.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25at/chen25at.pdf)
- **Reasoning quality** (constructs) — *causes*
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
- **Multi-task capability** (constructs) — *causes*
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **CRITICTOOL** (measurements) — *measured_by*
  - [OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1355.pdf)
- **Hallucination detection** (behaviors tasks) — *causes*
  - [2025.emnlp-main.1063.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1063.checklist.pdf)

### → Self-reflection
- **Error detection** (behaviors tasks) — *causes*
  - [FinRAGBench-V: A Benchmark for MultimodalRAGwith Visual Citation in the Financial Domain](https://aclanthology.org/2025.emnlp-main.212.pdf)

### Associated with
- **Self-correction** (behaviors tasks)
  - [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
- **System 2 thinking** (constructs)
  > Our analysis of prompting methods (Sec. 4.2) reveals that GPT-4o can improve itself through self-reflection, which is a key manifestation of System 2 reasoning (Sloman, 1996; Kumar et al., 2024). (Section 1)
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Critique** (behaviors tasks)
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Situational awareness** (constructs)
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Evaluation** (behaviors tasks)
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Planning** (constructs)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.892.pdf)
- **Confidence** (constructs)
  - [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks)
  - [Active Task Disambiguation with LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e07476b6bd2497e1fbd11b8f0b2de3c-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
- **Slow thinking** (constructs)
  - [Outlier-Safe Pre-Training for Robust 4-Bit Quantization of Large Language Models](https://aclanthology.org/2025.acl-long.619.pdf)
- **Action planning** (constructs)
  - [Otter: Generating Tests from Issues to Validate SWE Patches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ahmed25b/ahmed25b.pdf)

# Critique
**Type:** Behavior  
**Referenced in:** 97 papers  
**Also known as:** Critique ability, Text evaluation ability, Judging ability, Critique capability, Intrinsic self-correction, Refinement, Response refinement, Self-refinement, Solution refinement, Self-critique, Action evaluation, Reasoning quality evaluation, Self-assessment, Critiquing ability, Discrimination, Error correction, Fine-grained evaluation capability, Self-debugging, Self-repair, Self-refinement capability, Self-correction ability, Self-correction capability, Refinement capability, Progressive refinement, Self-repair capability, Self-critique ability, Self-revision capability, Self-repair ability, Critical judgment, Judgment capability, Peer review capability, Mistake identification, Self-critique generation  

## State of the Field

Across the surveyed literature, the construct of Critique is most commonly conceptualized as a model's latent ability to evaluate outputs, identify flaws, and subsequently improve them. This capability is discussed under a wide variety of terms, which can be broadly grouped into two functions: evaluative judgment (e.g., "judging ability," "evaluation capability") and corrective action (e.g., "self-correction," "self-refinement," "self-debugging"). A prevalent framing is the model's capacity for introspection, captured by numerous "self-" prefixed terms like "self-critique" and "self-verification," which focus on a model assessing and fixing its own outputs. This ability is examined across diverse domains, including assessing general text, comparing visual outputs, evaluating coding solutions, and analyzing the correctness of reasoning steps. To operationalize this construct, researchers use specific benchmarks; for instance, some papers use LLMBar to measure a model's "judgment capability" in instruction-following tasks, while others use CommonGen. Other mentioned instruments include CriticEval, which assesses critique across multiple dimensions, and StackEval, which focuses on proficiency as a judge for coding tasks. The ability to critique is reported to cause Self-correction and is studied alongside Self-reflection.

## Sources

**[CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf) (as "Critique ability")**
> The latent capability of Large Language Models to identify and rectify flaws in responses, encompassing feedback, comparison, correction, and meta-feedback dimensions.

**[CausalStock: Deep End-to-end Causal Discovery for News-driven Multi-stock Movement Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/54d689d58fe54c92aee2d732fc49fca8-Paper-Conference.pdf) (as "Text evaluation ability")**
> The latent capability of an LLM to accurately assess and score text along multiple specified dimensions.

**[GenAI Arena: An Open Evaluation Platform for Generative Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/92249f9233286e437f808fa535d88b26-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Judging ability")**
> The latent capacity of a multimodal model to evaluate and compare the quality of generated visual outputs in a way that matches human preference.

**[StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/file/4126a607bbe2836cb6ca0eb45b75618b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Evaluation capability")**
> The proficiency of a language model to accurately assess the quality of coding solutions when acting as a judge.

**[PunchBench: BenchmarkingMLLMs in Multimodal Punchline Comprehension](https://aclanthology.org/2025.acl-long.50.pdf) (as "Critique capability")**
> The latent ability of a general language model to analyze, evaluate, and provide feedback on the correctness of reasoning steps in a solution, including identifying errors and explaining them.

**[Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf) (as "Self-correction")**
> The latent ability of an LLM to detect and fix errors in its own reasoning process dynamically, based on internal confidence or external rules.

**[Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf) (as "Self-refinement")**
> The latent capacity of a model to iteratively improve its own outputs by revising draft plans based on internal reasoning or external feedback until an optimal or stable solution is reached.

**[Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf) (as "Intrinsic self-correction")**
> The latent capability of a model to identify and fix errors in its own responses based on its internal knowledge, without external tools or information.

**[Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf) (as "Response refinement")**
> The underlying capacity of an LLM to improve its own or others' outputs through iterative critique and revision based on feedback.

**[SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf) (as "Refinement")**
> The ability of a model to iteratively improve its output based on feedback or further instructions.

**[Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf) (as "Solution refinement")**
> The latent ability of an LLM to dynamically improve its answers to complex scientific or technical questions through iterative self-evaluation and critique.

**[Enhancing Decision-Making of Large Language Models via Actor-Critic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25c/dong25c.pdf) (as "Action evaluation")**
> The internal capacity of an LLM to assess the quality or likely success of candidate actions based on simulated outcomes and reasoning, serving as a critic in decision-making.

**[ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25ab/lee25ab.pdf) (as "Self-verification")**
> The model's intrinsic capability to assess the correctness of its own reasoning process or generated output.

**[Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mukherjee25a/mukherjee25a.pdf) (as "Error detection")**
> The model's underlying capability to recognize inaccuracies in reasoning steps, including both inherent errors and those arising from flawed dependencies.

**[Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf) (as "Self-critique")**
> The intrinsic capability of a model to evaluate and provide feedback on its own reasoning and implementation quality, integrating execution outcomes to generate process rewards without external supervision.

**[VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25h/zeng25h.pdf) (as "Reasoning quality evaluation")**
> The ability to judge whether intermediate reasoning steps are correct, logical, and supported by prior steps.

**[Position: Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cw/liu25cw.pdf) (as "Self-assessment")**
> The ability of an agent to accurately evaluate its own knowledge, skills, strengths, and weaknesses.

**[Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf) (as "Critiquing ability")**
> The capacity to generate feedback that both accurately assesses a solution and helps improve it in subsequent revisions.

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf) (as "Self-debugging")**
> The model's capacity to identify and correct errors in its own generated code based on feedback from code execution.

**[Chain-of-Experts: When LLMs Meet Complex Operations Research Problems](https://proceedings.iclr.cc/paper_files/paper/2024/file/d45ee77826332c100a1e15f7765b99ff-Paper-Conference.pdf) (as "Self-reflection")**
> The ability of an agent to analyze its past actions and failures to generate insights for future improvement.

**[Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf) (as "Self-evaluation")**
> The observable process where a language model assesses its own generated text against a given criterion, such as harmlessness, to produce a score.

**[An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf) (as "Error correction")**
> The process of identifying and repairing incorrect tokens or logic in a piece of code that was generated by a program translation model.

**[Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Fine-grained evaluation capability")**
> The ability to judge text quality using detailed, user-defined criteria rather than only coarse or generic preferences.

**[DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf) (as "Reflection")**
> The ability of the model to evaluate past decision sequences, identify errors, and generate corrected reasoning to improve future performance.

**[Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf) (as "Discrimination")**
> The latent ability of a model to identify and analyze potential mistakes, errors, or harmful elements within a given response.

**[LLM Circuit Analyses Are Consistent Across Training and Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Paper-Conference.pdf) (as "Self-repair")**
> A latent mechanism by which a model compensates for changes or losses in individual functional components to maintain stable task performance.

**[SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf) (as "Self-refinement capability")**
> The ability to iteratively improve generated code by identifying and fixing its own errors based on internal analysis or feedback.

**[SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf) (as "Self-correction ability")**
> The latent capacity of a model to independently identify and rectify errors within its own generated reasoning process.

**[Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf) (as "Self-correction capability")**
> The latent ability of a model to identify and rectify its own errors in reasoning or generation without external corrective feedback.

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

**[Benchmarking LLMs' Judgments with No Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9b0e4e205bdf232da9f74bfb9469539-Paper-Conference.pdf) (as "Peer review capability")**
> The ability of an LLM to generate useful, high-quality academic peer reviews for research papers.

**[Benchmarking LLMs' Judgments with No Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9b0e4e205bdf232da9f74bfb9469539-Paper-Conference.pdf) (as "Critical judgment")**
> The ability to provide substantive evaluative feedback that identifies strengths, weaknesses, and constructive critique beyond merely restating surface content.

**[SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf) (as "Judgment capability")**
> The latent ability of a model to assess whether a given response accurately adheres to the constraints of an instruction.

**[Diversify-verify-adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering](https://aclanthology.org/2025.naacl-long.57.pdf) (as "Mistake identification")**
> The latent ability of an AI tutor to recognize that a student has made an error in their reasoning or calculation, reflecting an understanding of the student's cognitive state.

**[From Shortcuts to Balance: Attribution Analysis of Speech-Text Feature Utilization in Distinguishing Original from Machine-Translated Texts](https://aclanthology.org/2025.emnlp-main.1666.pdf) (as "Self-critique generation")**
> The observable action of a model generating text that identifies and explains potential flaws or errors in its own previously generated reasoning or response.

## Relationships

### Critique →
- **Mathematical reasoning** (constructs) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *causes*
  - [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf)
- **CommonGen** (measurements) — *measured_by*
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25h/zeng25h.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **APPS** (measurements) — *measured_by*
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **EvalPlus** (measurements) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Pixel-Level Reasoning Segmentation via Multi-turn Conversations](https://aclanthology.org/2025.acl-long.865.pdf)
- **LLMBar** (measurements) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **ToolAlpaca** (measurements) — *measured_by*
  - [PROMPTEVALS: A Dataset of Assertions and Guardrails for Custom Production Large Language Model Pipelines](https://aclanthology.org/2025.naacl-long.214.pdf)
- **Long-horizon planning** (constructs) — *causes*
  - [Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cd/li25cd.pdf)
- **CRITICTOOL** (measurements) — *measured_by*
  - [OpenTuringBench: An Open-Model-based Benchmark and Framework for Machine-Generated Text Detection and Attribution](https://aclanthology.org/2025.emnlp-main.1355.pdf)

### → Critique
- **Code execution** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *causes*
  - [Solving Challenging Math Word Problems Using GPT-4 Code Interpreter with Code-based Self-Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/12c45a68e8433b21b91cd47731387fa4-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **AUTO-J** (measurements) — *causes*
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **UltraFeedback** (measurements) — *causes*
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Multi-agent collaboration** (behaviors tasks) — *causes*
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)

### Associated with
- **Code debugging** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks)
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Few-shot prompting** (measurements)
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)
- **Feedback generation** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Text generation quality** (constructs)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
- **Programming** (behaviors tasks)
  - [Is Self-Repair a Silver Bullet for Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9ddc141bdbf9d1db510cefff56c586ad-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks)
  - [Think Thrice Before You Act: Progressive Thought Refinement in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6882dbdc34bcd094e6f858c06ce30edb-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)
- **Natural language understanding** (constructs)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Weak-to-strong generalization** (constructs)
  - [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)

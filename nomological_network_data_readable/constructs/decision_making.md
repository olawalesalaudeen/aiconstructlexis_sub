# Decision-making
**Type:** Construct  
**Referenced in:** 90 papers  
**Also known as:** Driving decision making, Autonomous decision making, High-level action selection, Chess move selection, Arm selection, Tool selection, Final answer selection, Answer selection, Activity selection, Best-of-N selection, Dataset selection, Parameter selection, Sentence selection, State selection, Automated decision making, Target selection, Decision making, Function selection, Multi-step interaction, Offline reinforcement learning, Neighborhood selection, Preference comparison selection, Question selection, Root motif selection, Secret action selection, Token selection, View selection, Clinical diagnosis, Negotiation, Final decision making, Decision-making Ability, Decision-making ability, Decision-making capability, Clinical decision making  

## State of the Field

Across the surveyed literature, Decision-making is predominantly framed as the process of selecting a course of action, response, or tool from a set of alternatives to achieve a goal. The concept is treated in two primary ways: as a specific, observable behavior of 'selection', and as a more general, latent 'decision-making ability'. In its most common usage as an observable act, it encompasses a wide range of granular tasks, including tool selection, choosing a response in a dialogue, selecting actions in games, and navigating simulated environments for robotics or autonomous driving. A smaller set of papers defines it as a latent capability, describing it as an agent's underlying cognitive capacity to perceive its environment, plan, and act autonomously to accomplish complex tasks. This behavior is most frequently operationalized and measured using performance in simulated interactive environments. The ALFWorld benchmark is a recurring instrument for this purpose, alongside others such as WebShop, ToolBench, and Game of 24. Several papers suggest that effective decision-making is influenced by constructs like logical reasoning, scene understanding, and commonsense knowledge. The study of decision-making is also associated with research on strategic reasoning, financial analysis, and perception.

## Sources

**[Mars: Situated Inductive Reasoning in an Open-World Environment](https://proceedings.neurips.cc/paper_files/paper/2024/file/1fb6d0b52f5e41b11392841a66dbfe7d-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Performing tasks that require selecting and executing specific actions in different contexts based on induced rules.

**[Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf) (as "Driving decision making")**
> Selecting high-level driving actions or meta-actions from scene descriptions and prior experience.

**[No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf) (as "Autonomous decision making")**
> The task of a system making choices and taking actions independently to achieve goals in a given environment.

**[Policy Learning from Tutorial Books via Understanding, Rehearsing and Introspecting](https://proceedings.neurips.cc/paper_files/paper/2024/file/21cf8411ed825614e00006a1d9aab7e4-Paper-Conference.pdf) (as "Action selection")**
> The observable choice of a specific action (e.g., move, pass, shoot) conditioned on the current state description.

**[Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf) (as "High-level action selection")**
> Choosing discrete robot actions such as navigation, pickup, placement, opening, closing, cleaning, or toggling to advance the task.

**[Reflective Multi-Agent Collaboration based on Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fa54b0edce5eef0bb07654e8ee800cb4-Paper-Conference.pdf) (as "Chess move selection")**
> Choosing a legal chess move that best advances the position, including identifying a checkmating move.

**[Can large language models explore in-context?](https://proceedings.neurips.cc/paper_files/paper/2024/file/d951f73c521d069fefbb73396df01424-Paper-Conference.pdf) (as "Arm selection")**
> Choosing one action from a fixed set of bandit arms at each time step.

**[TaskBench: Benchmarking Large Language Models for Task Automation](https://proceedings.neurips.cc/paper_files/paper/2024/file/085185ea97db31ae6dcac7497616fd3e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Tool selection")**
> Choosing the appropriate tools for each subtask and representing their dependencies as a tool invocation graph.

**[ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf) (as "Final answer selection")**
> The process of choosing a single final answer from multiple generated reasoning traces or candidates.

**[When LLMs Meet Cunning Texts: A Fallacy Understanding Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbfbf1a9adbcc29783475d2767f218e8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Answer selection")**
> The task of choosing the single correct explanation from a set of four provided candidate options in response to a given cunning text.

**[Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf) (as "Response selection")**
> The observable act of choosing one response from a set of candidates to present to a user at a given turn in a conversation.

**[Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf) (as "State selection")**
> The observable action of choosing a specific state from a collection of previously discovered states to return to for further exploration.

**[RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf) (as "Best-of-N selection")**
> The observable task of identifying the single best response from a list of multiple (N > 2) candidates for a given prompt.

**[MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf) (as "Parameter selection")**
> The observable action of identifying and providing the correct arguments or parameters for a selected tool call.

**[Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf) (as "Activity selection")**
> The observable process of an agent choosing a single action to execute from a set of evaluated candidates based on which one best satisfies its intrinsic motivations.

**[Small-to-Large Generalization: Training Data Influences Models Consistently Across Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/5356603f9c47399adfd372f77a677057-Paper-Conference.pdf) (as "Dataset selection")**
> Choosing a subset of candidate training data intended to improve downstream model performance.

**[Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf) (as "Sentence selection")**
> Choosing which sentences from a retrieved passage should be kept for answering a question.

**[AIR-BENCH 2024: A Safety Benchmark based on Regulation and Policies Specified Risk Categories](https://proceedings.iclr.cc/paper_files/paper/2025/file/a103529738706979331778377f2d5864-Paper-Conference.pdf) (as "Automated decision making")**
> Making or providing decisions about eligibility or other consequential outcomes from user-provided profiles or records.

**[Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf) (as "Target selection")**
> Choosing which opponent to attack or target in a sequential elimination game.

**[BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf) (as "Decision making")**
> Choosing the more likely outcome from two alternatives based on estimated probabilities.

**[Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf) (as "Function selection")**
> Choosing the correct function from a set of candidate functions given a user intent and function descriptions.

**[An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf) (as "Offline reinforcement learning")**
> Generating a sequence of actions to maximize rewards in a simulated environment, based on a pre-existing dataset of trajectories.

**[Learn-by-interact: A Data-Centric Framework For Self-Adaptive Agents in Realistic Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd745a0c4f91fe91866fe6788be9cc28-Paper-Conference.pdf) (as "Multi-step interaction")**
> Producing a sequence of actions over multiple environment steps in response to an instruction and observations.

**[Active Reward Modeling: Adaptive Preference Labeling for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25c/shen25c.pdf) (as "Preference comparison selection")**
> The process of choosing pairs of prompt-response outputs for human annotation based on an active learning strategy to improve reward model training.

**[OrthoRank: Token Selection via Sink Token Orthogonality for Efficient LLM inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shin25e/shin25e.pdf) (as "Token selection")**
> The observable process of choosing a subset of tokens for full layer computation based on their orthogonality to the sink token, while bypassing others except for key-value calculations.

**[Foundation Molecular Grammar: Multi-Modal Foundation Models Induce Interpretable Molecular Graph Languages](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25aa/sun25aa.pdf) (as "Root motif selection")**
> The observable behavior of selecting a central or most chemically significant substructure to serve as the anchor point in molecular decomposition or generation.

**[3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf) (as "View selection")**
> The process of choosing a subset of 2D views from a 3D scene to serve as input for a vision-language model based on relevance and diversity.

**[Adaptive Elicitation of Latent Information Using Natural Language](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ff/wang25ff.pdf) (as "Question selection")**
> The observable act of choosing a natural language question from a candidate set to ask next, based on prior interactions with a latent entity.

**[Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25h/xu25h.pdf) (as "Secret action selection")**
> Choosing targets for elimination, investigation, or protection during the night phase, based on hidden role and private information.

**[Large Language Model-driven Large Neighborhood Search for Large-Scale MILP Problems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25j/ye25j.pdf) (as "Neighborhood selection")**
> The observable process of selecting a subset of decision variables to optimize in each iteration of Large Neighborhood Search, based on variable scores.

**[MentalGLMSeries: Explainable Large Language Models for Mental Health Analysis onChinese Social Media](https://aclanthology.org/2025.emnlp-main.687.pdf) (as "Clinical diagnosis")**
> Producing a diagnostic answer for a medical query or case.

**[CanLLMs simulate the same correct solutions to free-response math problems as real students?](https://aclanthology.org/2025.emnlp-main.828.pdf) (as "Negotiation")**
> The observable process of communication between parties aimed at reaching a mutually acceptable agreement on one or more issues.

**[CompassVerifier: A Unified and Robust Verifier forLLMs Evaluation and Outcome Reward](https://aclanthology.org/2025.emnlp-main.1699.pdf) (as "Final decision making")**
> The observable action of producing a definitive answer to a clinical question based on aggregated agent opinions, typically via majority vote.

**[On the Modeling Capabilities of Large Language Models for Sequential Decision Making](https://proceedings.iclr.cc/paper_files/paper/2025/file/368cba57d00902c752eaa9e4770bbbbe-Paper-Conference.pdf) (as "Decision-making capability")**
> The latent ability of an LLM to support sequential action selection and policy formation across interactive environments.

**[Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf) (as "Decision-making Ability")**
> The general capability of an agent to plan, make decisions, and take actions to accomplish complex tasks autonomously.

**[AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf) (as "Decision-making ability")**
> The underlying cognitive capacity of an agent to perceive its environment, make choices, and select appropriate actions to achieve a goal.

**[Reliable and Cost-Effective Exploratory Data Analysis via Graph-GuidedRAG](https://aclanthology.org/2025.emnlp-main.837.pdf) (as "Clinical decision making")**
> The broader latent capacity to make diagnostic and treatment decisions from patient information, evidence, and evolving hypotheses.

## Relationships

### Decision-making →
- **ALFWorld** (measurements) — *measured_by*
  > We use open-source environments: HotPotQA (Yang et al., 2018), WebShop (Yao et al., 2022) and AlfWorld (Shridhar et al., 2021) , which evaluates the agent’s reasoning and tool usage abilities for question answering reasoning, multi-step decision making, and web browsing. (Section 5.1.1)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **WebShop** (measurements) — *measured_by*
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)
- **GTA** (measurements) — *measured_by*
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)
- **ToolBench** (measurements) — *measured_by*
  > "we conduct extensive experiments on Game of 24 (Yao et al., 2023), WebShop (Yao et al., 2022a), ToolBench (Qin et al., 2023c) and RestBench (Song et al., 2023) datasets"
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **AgentBench** (measurements) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **VirtualHome** (measurements) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **BabyAI** (measurements) — *measured_by*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **SciWorld** (measurements) — *measured_by*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **PDDL** (measurements) — *measured_by*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **AgentBoard** (measurements) — *measured_by*
  - [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cc50126338b175e56bb3cad134db0b-Paper-Conference.pdf)
- **D4RL** (measurements) — *measured_by*
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **RestBench** (measurements) — *measured_by*
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **Game of 24** (measurements) — *measured_by*
  > "we conduct extensive experiments on Game of 24 (Yao et al., 2023), WebShop (Yao et al., 2022a), ToolBench (Qin et al., 2023c) and RestBench (Song et al., 2023) datasets"
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **JAMA Clinical Challenge** (measurements) — *measured_by*
  - [Token-Level Density-Based Uncertainty Quantification Methods for Eliciting Truthfulness of Large Language Models](https://aclanthology.org/2025.naacl-long.114.pdf)
- **DDXPlus** (measurements) — *measured_by*
  - [MentalGLMSeries: Explainable Large Language Models for Mental Health Analysis onChinese Social Media](https://aclanthology.org/2025.emnlp-main.687.pdf)
- **API-Bank** (measurements) — *measured_by*
  - [AgentPro: EnhancingLLMAgents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.507.pdf)
- **APIBench** (measurements) — *measured_by*
  - [AgentPro: EnhancingLLMAgents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.507.pdf)
- **BFCL-v2** (measurements) — *measured_by*
  - [AgentPro: EnhancingLLMAgents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.507.pdf)

### → Decision-making
- **Reasoning** (constructs) — *causes*
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
- **Scene understanding** (constructs) — *causes*
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *causes*
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **Webpage understanding** (constructs) — *causes*
  - [Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c995a913bc20ca39ce2231b8973be90a-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Better than Your Teacher: LLM Agents that learn from Privileged AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c60ed2b01120d383eebf12dc7a0e138-Paper-Conference.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Financial analysis** (behaviors tasks)
  - [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Model selection** (constructs)
  - [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [JMMMU: AJapanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.44.pdf)
- **Perception** (constructs)
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Strategic reasoning** (constructs)
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)

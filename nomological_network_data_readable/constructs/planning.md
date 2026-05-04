# Planning
**Type:** Construct  
**Referenced in:** 284 papers  
**Also known as:** Planning ability, Planning capability, Task decomposition, Task prioritization, Task-driven re-planning, Planning capabilities, Dynamic replanning, Problem decomposition, Self-planning, Long-term strategic reasoning, Action deliberation, Tool selection, Strategy selection, Plan revision capability, Strategic behavior, Prompt decomposition, Experimental design, Activity generation, Script generation, Query decomposition, Question decomposition, Sub-goal decomposition, Anticipatory plan generation, Transition pathway generation, Constraint decomposition, Meta-plan generation, Node chain generation, Viewpoint extraction, Action plan generation, Plan generation, Code-form plan generation, Workflow generation, Candidate action generation, Safe plan generation, Adaptive replanning, Dialogue logic flow generation, Reasoning strategy selection, Support strategy selection, Strategy revision, Reasoning path selection, Chart type selection, All-in-one travel plan generation, Travel plan generation, Calendar scheduling, High-level planning, Action decomposition, Requirement analysis, High-level instruction generation, Subgoal generation, Driving decision making, Autonomous decision making, Action selection, High-level action selection, Chess move selection, Arm selection, Final answer selection, Answer selection, Activity selection, Best-of-N selection, Dataset selection, Parameter selection, Response selection, Sentence selection, State selection, Automated decision making, Target selection, Decision making, Function selection, Multi-step interaction, Offline reinforcement learning, Neighborhood selection, Preference comparison selection, Question selection, Root motif selection, Secret action selection, Token selection, View selection, Clinical diagnosis, Negotiation, Final decision making  

## State of the Field

Across the surveyed literature, Planning is most commonly defined as a model's ability to formulate a structured sequence of actions or an outline before execution to achieve a goal. This frequently involves task decomposition, or as one paper notes, "breaking down instructions into more manageable components" (AgentBench: Evaluating LLMs as Agents). While the prevailing usage centers on generating a plan, such as a "chain of API function calls" (ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search), a notable subset of definitions emphasizes adaptive capabilities like "Dynamic replanning" in response to environmental feedback. A smaller line of work frames planning as a selection process, including behaviors like "Tool selection" and "Strategy selection" from a set of options. The field operationalizes this construct through a wide variety of measurement instruments, including classical planning problems like Blocksworld, interactive agent environments such as AgentBench and TextWorld, and tool-use benchmarks like ToolBench and T-Eval. Planning is also assessed using tasks like Travelplanner and Game of 24, as well as through human evaluation. This construct is frequently studied alongside and is reported to be related to Commonsense knowledge, Tool use, and Complex reasoning. Several papers also suggest that planning influences outcomes such as Long-horizon task completion and Adaptability.

## Sources

**[A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)**
> The ability of a model to formulate a structured plan or outline before generating a detailed response.

**[LLM-Assisted Code Cleaning For Training Accurate Code Generators](https://proceedings.iclr.cc/paper_files/paper/2024/file/41137f3997ade899893ccd3973592d4b-Paper-Conference.pdf) (as "Planning capability")**
> The latent ability to generate correct and useful high-level natural language plans that outline the steps needed to solve a programming problem before implementation.

**[Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf) (as "Planning ability")**
> The ability to choose and sequence operations adaptively based on the current state of the table and the question.

**[Transformers Provably Solve Parity Efficiently with Chain of Thought](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e2986deda273d8fb903342841fcc4dc-Paper-Conference.pdf) (as "Task decomposition")**
> The latent ability to break down a complex problem into a hierarchy of simpler, solvable sub-problems.

**[Robotouille: An Asynchronous Planning Benchmark for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d033407a1a4b7a75cd5f9e4575ad9fb5-Paper-Conference.pdf) (as "Task prioritization")**
> The ability to correctly order subtasks, particularly in asynchronous settings, to maximize efficiency and increase the likelihood of success.

**[OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf) (as "Task-driven re-planning")**
> An adaptive planning strategy where an agent adjusts specific sub-tasks within a larger workflow in response to feedback, rather than re-planning the entire sequence from scratch.

**[Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf) (as "Planning capabilities")**
> The latent ability to generate and adjust multi-step action sequences for accomplishing goals, especially when external tools are involved.

**[Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/erdogan25a/erdogan25a.pdf) (as "Dynamic replanning")**
> The capacity of an agent to revise its high-level plan in response to real-time environmental feedback and unexpected changes during task execution.

**[Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf) (as "Problem decomposition")**
> The latent ability of a system design to break down complex tasks into smaller, independently solvable subproblems, enabling asymptotic improvements in computational cost.

**[Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.892.pdf) (as "Self-planning")**
> The inherent capability of an LLM to create and follow a plan to solve a problem without explicit, step-by-step instructions.

**[BabyLM’s First Constructions: Causal interventions provide a signal of learning](https://aclanthology.org/2025.emnlp-main.114.pdf) (as "Strategic reasoning")**
> The capacity to plan multi-step interactions that exploit policy ambiguities or edge cases to achieve a specific goal, such as inducing a policy violation.

**[MultiMatch: Multihead Consistency Regularization Matching for Semi-Supervised Text Classification](https://aclanthology.org/2025.emnlp-main.140.pdf) (as "Long-term strategic reasoning")**
> The latent ability to identify and execute multi-step strategies that lead to guaranteed future wins, such as creating a 'fork' with multiple winning paths, rather than reacting to immediate threats.

**[BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation](https://aclanthology.org/2025.emnlp-main.152.pdf) (as "Action deliberation")**
> The latent ability of an LLM agent to generate and evaluate multiple candidate actions before selecting one, based on reasoning about their likely outcomes.

**[IndoSafety: Culturally Grounded Safety forLLMs inIndonesian Languages](https://aclanthology.org/2025.emnlp-main.466.pdf) (as "Tool selection")**
> The underlying capability of an LLM agent to identify and choose the appropriate enterprise tools or APIs required to perform a given subtask.

**[LIDDIA: Language-based Intelligent Drug Discovery Agent](https://aclanthology.org/2025.emnlp-main.604.pdf) (as "Strategy selection")**
> The model's capacity to dynamically choose between different problem-solving approaches—such as text-based reasoning or tool-augmented execution—based on the nature of the input problem.

**[MIRROR: Multimodal Cognitive Reframing Therapy for Rolling with Resistance](https://aclanthology.org/2025.emnlp-main.752.pdf) (as "Plan revision capability")**
> The latent ability of a model to dynamically adjust travel plans in response to changing user needs or external conditions, maintaining coherence and feasibility.

**[CanLLMs simulate the same correct solutions to free-response math problems as real students?](https://aclanthology.org/2025.emnlp-main.828.pdf) (as "Strategic behavior")**
> The underlying approach and pattern of tactics an agent employs to navigate a conflict and achieve its goals, as a dimension of behavioral alignment.

**[CycleResearcher: Improving Automated Research via Automated Review](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a48036026dc7946ef6033ae14719cc5-Paper-Conference.pdf) (as "Experimental design")**
> The task of outlining the setup and procedures for experiments within a research paper, even if the results are simulated.

**[Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf) (as "Script generation")**
> The task of generating a set of instructions or steps, often including images, to complete a process.

**[Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf) (as "Activity generation")**
> The task of generating a sequence of steps with images describing an activity.

**[Rare-to-Frequent: Unlocking Compositional Generation Power of Diffusion Models on Rare Concepts with LLM Guidance](https://proceedings.iclr.cc/paper_files/paper/2025/file/262ba7d20578417435414ce00e69fb12-Paper-Conference.pdf) (as "Prompt decomposition")**
> The process of breaking down a complex text prompt into sub-prompts corresponding to individual objects.

**[StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf) (as "Question decomposition")**
> Breaking down a complex question into a series of simpler, answerable sub-questions.

**[DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf) (as "Query decomposition")**
> The observable action of breaking down a complex question into a series of simpler, more manageable sub-questions.

**[System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf) (as "Sub-goal decomposition")**
> The observable action of breaking down a larger planning problem into a series of smaller, intermediate sub-problems, each with its own start and end state.

**[MatExpert: Decomposing Materials Discovery By Mimicking Human Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d6850f4c82520793f738d98a72aab9d-Paper-Conference.pdf) (as "Transition pathway generation")**
> The observable task of generating a textual, step-by-step plan outlining the necessary modifications to transform a source material into a target material with specified properties.

**[Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf) (as "Anticipatory plan generation")**
> Producing a high-level plan before answering that outlines the intended solution path without detailed calculations.

**[DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf) (as "Constraint decomposition")**
> The observable task of splitting a target VRP into individual constraints represented by keywords.

**[CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf) (as "Meta-plan generation")**
> The observable process where agents collaboratively analyze a task, discuss, and create a high-level, long-term plan that decomposes the task into subtasks with assigned steps.

**[Benchmarking Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/adbe936993aa7cf41e45054d8b72f183-Paper-Conference.pdf) (as "Node chain generation")**
> Producing an ordered sequence of subtasks that serves as a topological sequence for a workflow.

**[GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5ce40ee957e4f76ef53c09d0bae20f4-Paper-Conference.pdf) (as "Viewpoint extraction")**
> The task of decomposing a complex research idea into a list of simpler, semantically independent, and evaluable units called viewpoints.

**[Interactive Speculative Planning: Enhance Agent Efficiency through Co-design of System and User Interface](https://proceedings.iclr.cc/paper_files/paper/2025/file/25458943db16e0f78f748ca5bc34fff6-Paper-Conference.pdf) (as "Action plan generation")**
> The observable production of a sequence of actions or thoughts intended to achieve a specific goal.

**[System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf) (as "Plan generation")**
> The observable action of producing a sequence of steps intended to solve a given planning problem.

**[CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf) (as "Code-form plan generation")**
> Producing pseudocode-style plans that summarize the high-level reasoning structure for solving a prompt.

**[Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf) (as "Workflow generation")**
> Producing a sequence of steps or actions to achieve a goal in a multi-turn or interactive environment.

**[How Far CanLLMs Improve from Experience? Measuring Test-Time Learning Ability inLLMs with Human Comparison](https://aclanthology.org/2025.emnlp-main.1305.pdf) (as "Safe plan generation")**
> The generation of a sequence of actions that achieves a goal without causing physical harm or violating safety constraints.

**[GraphAgent: Agentic Graph Language Assistant](https://aclanthology.org/2025.emnlp-main.1340.pdf) (as "Candidate action generation")**
> The model or policy samples a set of possible next inquiry actions from a masked action space.

**[Decoding Dense Embeddings: Sparse Autoencoders for Interpreting and Discretizing Dense Retrieval](https://aclanthology.org/2025.emnlp-main.1346.pdf) (as "Adaptive replanning")**
> The dynamic modification of a pre-generated task plan in response to real-time application states and task progress.

**[CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases inLLMs](https://aclanthology.org/2025.emnlp-main.85.pdf) (as "Dialogue logic flow generation")**
> Creating a turn-level plan that specifies intentions, relevant slot-value pairs, and explanatory reasoning before utterance realization.

**[AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.185.pdf) (as "Reasoning strategy selection")**
> The observable process of choosing a specific sequence of reasoning steps or skills from a set of candidates based on criteria such as skill coverage and uniqueness.

**[TS-CLIP: Time Series Understanding byCLIP](https://aclanthology.org/2025.emnlp-main.232.pdf) (as "Support strategy selection")**
> The observable process of choosing one or more conversational strategies (e.g., Question, Reflection of feelings) to use in a response.

**[Enrich-on-Graph: Query-Graph Alignment for Complex Reasoning withLLMEnriching](https://aclanthology.org/2025.emnlp-main.391.pdf) (as "Strategy revision")**
> The observable pattern of altering a decision-making approach over repeated rounds based on feedback from previous outcomes.

**[LightThinker: Thinking Step-by-Step Compression](https://aclanthology.org/2025.emnlp-main.674.pdf) (as "Reasoning path selection")**
> Choosing which dependencies and intermediate steps to use when solving a multi-step problem, including avoiding irrelevant or distracting information.

**[NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1770.pdf) (as "Chart type selection")**
> The behavior of choosing a suitable visualization format (e.g., bar chart, line chart) based on the structure of the extracted data and the user's intent.

**[MIRROR: Multimodal Cognitive Reframing Therapy for Rolling with Resistance](https://aclanthology.org/2025.emnlp-main.752.pdf) (as "Travel plan generation")**
> The observable action of producing a travel itinerary, which may include basic arrangements of points of interest.

**[MIRROR: Multimodal Cognitive Reframing Therapy for Rolling with Resistance](https://aclanthology.org/2025.emnlp-main.752.pdf) (as "All-in-one travel plan generation")**
> Producing a comprehensive travel itinerary that includes detailed arrangements for timing, attractions, dining, accommodations, tickets, and costs.

**[LimRank: Less is More for Reasoning-Intensive Information Reranking](https://aclanthology.org/2025.emnlp-main.1042.pdf) (as "Calendar scheduling")**
> Finding a valid meeting time slot that satisfies participants' availability constraints.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf) (as "High-level planning")**
> Generating a small set of task milestones or subtasks from a visual preview or textual description of a GUI goal.

**[AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf) (as "Task planning")**
> Generating or refining action plans for robotic tasks from natural-language goals and failure feedback.

**[Optimal Transport-Based Token Weighting scheme for Enhanced Preference Optimization](https://aclanthology.org/2025.acl-long.1036.pdf) (as "Action decomposition")**
> The process of identifying and separating a complex narrative into a sequence of discrete actions to be represented as individual scene graphs.

**[Colloquial SingaporeanEnglish Style Transfer with Fine-Grained Explainable Control](https://aclanthology.org/2025.acl-long.1310.pdf) (as "Requirement analysis")**
> The observable behavior of taking a high-level goal in natural language and breaking it down into a series of detailed steps, also in natural language.

**[LLM-based Rumor Detection via Influence Guided Sample Selection and Game-based Perspective Analysis](https://aclanthology.org/2025.acl-long.1379.pdf) (as "High-level instruction generation")**
> Producing decomposed sub-task plans from high-level goals and environmental observations, such as generating 'Pick up the blue book' from 'Read a book under the light'.

**[CiteEval: Principle-Driven Citation Evaluation for Source Attribution](https://aclanthology.org/2025.acl-long.1575.pdf) (as "Subgoal generation")**
> The observable behavior of an LLM-based agent formulating intermediate goals before generating executable actions.

**[Mars: Situated Inductive Reasoning in an Open-World Environment](https://proceedings.neurips.cc/paper_files/paper/2024/file/1fb6d0b52f5e41b11392841a66dbfe7d-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Decision-making")**
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

## Relationships

### Planning →
- **Travelplanner** (measurements) — *measured_by*
  - [FLEURS-ASL: IncludingAmericanSignLanguage in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.315.pdf)
- **Blocksworld** (measurements) — *measured_by*
  > We evaluate System-1.x Planner on two classical planning tasks that are challenging for LLMs (Valmeekam et al., 2023; Lehnert et al., 2024): (1) Maze Navigation and (2) Blocksworld. (Section 3)
  - [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Collaboration** (behaviors tasks) — *causes*
  - [Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation](https://proceedings.neurips.cc/paper_files/paper/2024/file/984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Logistics** (measurements) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **Game of 24** (measurements) — *measured_by*
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **T-Eval** (measurements) — *measured_by*
  > T-Eval, a widely-used benchmark to evaluate the multi-step decision-making capability of LLMs to utilize APIs... enhances the model's out-of-distribution planning ability.
  - [WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [Think while You Generate: Discrete Diffusion with Planned Denoising](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbf883a744952d4a40591271a58ab9d0-Paper-Conference.pdf)
- **Mind2Web** (measurements) — *measured_by*
  - [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91bf7dfba0477554994c6d64833e9d8-Paper-Conference.pdf)
- **ToolBench** (measurements) — *measured_by*
  - [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf)
- **GTA** (measurements) — *measured_by*
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [GuideBench: Benchmarking Domain-Oriented Guideline Following forLLMAgents](https://aclanthology.org/2025.acl-long.558.pdf)
- **Long-horizon task completion** (behaviors tasks) — *causes*
  - [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf)
- **Star Graph Task** (measurements) — *measured_by*
  - [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf)
- **PlanBench** (measurements) — *measured_by*
  - [Resource-Rational Noisy-Channel Language Processing: Testing the Effect of Algorithmic Constraints on Inferences](https://aclanthology.org/2025.emnlp-main.1208.pdf)
- **Task decomposition** (behaviors tasks) — *causes*
  - [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **WildBench** (measurements) — *measured_by*
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **TextWorld** (measurements) — *measured_by*
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
- **AI2-THOR** (measurements) — *measured_by*
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Gridworld** (measurements) — *measured_by*
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Adaptability** (constructs) — *causes*
  > "Additionally, unlike previous methods that relied on linear action sequences and re-planning from scratch... OSCAR’s state machine integrates real-time verification feedback for fine-grained, task-driven re-planning, significantly improving efficiency and adaptability."
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **ActivityNet** (measurements) — *measured_by*
  - [Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *causes*
  - [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *causes*
  - [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf)
- **VisualWebArena** (measurements) — *measured_by*
  - [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3b893ba1de12f76020b03f7ae8e1afd-Paper-Conference.pdf)
- **Multi-task capability** (constructs) — *causes*
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **AgentBench** (measurements) — *measured_by*
  - [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.578.pdf)
- **TTT-Bench** (measurements) — *measured_by*
  > In this work, we introduce TTT-Bench, a new benchmark that is designed to evaluate basic strategic, spatial, and logical reasoning abilities in LRMs through a suite of four two-player Tic-Tac-Toe-style games that humans can effortlessly solve from a young age. (Abstract)
  - [MultiMatch: Multihead Consistency Regularization Matching for Semi-Supervised Text Classification](https://aclanthology.org/2025.emnlp-main.140.pdf)
- **Code reasoning** (constructs) — *causes*
  - [SUE: Sparsity-based Uncertainty Estimation via Sparse Dictionary Learning](https://aclanthology.org/2025.emnlp-main.1672.pdf)

### → Planning
- **Reasoning** (constructs) — *causes*
  - [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf)
- **World modeling** (constructs) — *causes*
  - [OZSpeech: One-step Zero-shot Speech Synthesis with Learned-Prior-Conditioned Flow Matching](https://aclanthology.org/2025.acl-long.1044.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf)
- **Causal reasoning** (constructs) — *causes*
  - [Language Agents Meet Causality -- Bridging LLMs and Causal World Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c5bc3553815adb4d1a8a5b8701e41a9-Paper-Conference.pdf)
- **Collaboration** (behaviors tasks) — *causes*
  - [CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b07091c16719ad3990e3d1ccee6641f1-Paper-Conference.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)
- **Tool use** (behaviors tasks)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense knowledge** (constructs)
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.892.pdf)
- **Task decomposition** (behaviors tasks)
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  - [Leveraging Environment Interaction for Automated PDDL Translation and Planning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/44af065477781e7f8a8589b14a62c489-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **Sequential decision-making** (constructs)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Active information gathering** (behaviors tasks)
  - [Can large language models explore in-context?](https://proceedings.neurips.cc/paper_files/paper/2024/file/d951f73c521d069fefbb73396df01424-Paper-Conference.pdf)
- **Molecule understanding** (behaviors tasks)
  - [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual reasoning** (constructs)
  - [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Sudoku solving** (behaviors tasks)
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
- **Backtracking** (behaviors tasks)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **State tracking** (constructs)
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
- **Textual reasoning** (behaviors tasks)
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **Temporal reasoning** (constructs)
  - [T2R-BENCH: A Benchmark for Real World Table-to-Report Task](https://aclanthology.org/2025.emnlp-main.1142.pdf)
- **Action execution** (behaviors tasks)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Preference bias** (constructs)
  - [TS-CLIP: Time Series Understanding byCLIP](https://aclanthology.org/2025.emnlp-main.232.pdf)

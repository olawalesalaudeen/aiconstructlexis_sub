# Task decomposition
**Type:** Behavior  
**Referenced in:** 77 papers  
**Also known as:** Program decomposition, Subtask decomposition, Question decomposition, Request decomposition, Problem decomposition, Prompt decomposition, Subgoal generation, Text decomposition, Task composition, Multi-step query decomposition, Dependency identification, Subtask identification, Concept decomposition, Plan decomposition, Subgoal proposal, Query graph construction, Subquestion decomposition, Instruction decomposition, Sub-question generation, Subproblem decomposition, Subgoal setting, Query decomposition  

## State of the Field

The most common framing of task decomposition in the provided literature is the observable behavior of breaking down a complex input—such as a task, question, or query—into a series of smaller, more manageable sub-components. This behavior is applied to a wide range of inputs, including high-level goals, programming problems, user requests, and textual descriptions, resulting in outputs like sequences of sub-tasks, simpler sub-questions, or modular code functions. The most frequently cited purpose is to enable a "divide-and-conquer" strategy, allowing a model to "address each component individually, and synthesize the results to create the final plan" (HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking). A distinct line of work operationalizes decomposition as a method for bypassing safety mechanisms, where a malicious query is broken into "multiple seemingly innocuous subqueries" to "circumvent safety guardrails" (Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions). The behavior is operationalized by observing the model's generation of intermediate steps, such as producing a list of sub-questions, a structured plan of actionable steps, or a directed acyclic graph of sub-queries. Across the surveyed work, task decomposition is frequently studied alongside broader capabilities like `Complex reasoning`, `Planning`, and `Chain-of-thought reasoning`. Several papers report that this behavior influences downstream outcomes, describing it as a mechanism for improving `Problem-solving`, `Code generation`, and `Information retrieval`. While the overwhelming majority of sources define this as a process of breaking things down, one paper uses the term `Task composition` to refer to the inverse process of combining components.

## Sources

**[Divide-and-Conquer Meets Consensus: Unleashing the Power of Functions in Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7bc4f74e35bcfe8cfe43b0a860786d6a-Paper-Conference.pdf) (as "Program decomposition")**
> The observable behavior of breaking down a complex programming problem into smaller, more manageable sub-problems, often represented as distinct functions.

**[RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)**
> The observable process of breaking down a complex, high-level goal into a series of smaller, more manageable sub-tasks or sub-actions.

**[Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/7d6e85e88495104442af94c98e899659-Paper-Conference.pdf) (as "Subtask decomposition")**
> The observable action of breaking down a high-level language instruction into a sequence of smaller, feasible subtasks based on current observations and memory.

**[Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf) (as "Question decomposition")**
> Breaking a complex question into a sequence of simpler sub-questions.

**[Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf) (as "Request decomposition")**
> The observable behavior of an LLM breaking down a user's ambiguous, high-level request into a sequence of concrete, actionable steps.

**[AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf) (as "Problem decomposition")**
> The observable action of breaking down a complex question or problem into a structured plan of simpler, actionable steps.

**[Compositional 3D-aware Video Generation with LLM Director](https://proceedings.neurips.cc/paper_files/paper/2024/file/edbeca7811f9365c924c72a8a9bce83a-Paper-Conference.pdf) (as "Prompt decomposition")**
> Splitting a complex textual input into distinct sub-prompts that describe individual concepts such as scene, objects, and motion.

**[Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Subgoal generation")**
> The observable action of producing a set of intermediate mathematical statements (subgoals) from a current goal state by applying theorems or transformation rules.

**[Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf) (as "Text decomposition")**
> The task of breaking down a complex text description into multiple, shorter, semantically coherent phrases.

**[3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf) (as "Task composition")**
> Combining separately trained task-specific subspaces or weights to produce a new combined output behavior.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Subtask identification")**
> Observably decomposing a complex task instruction into its constituent subtasks based on semantic content.

**[What Limits Virtual Agent Application? OmniBench: A Scalable Multi-Dimensional Benchmark for Essential Virtual Agent Capabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25b/bu25b.pdf) (as "Dependency identification")**
> Correctly recognizing and acting upon prerequisite relationships between subtasks in a non-linear task structure.

**[Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf) (as "Multi-step query decomposition")**
> The observable behavior of breaking down a complex or malicious query into a sequence of simpler, seemingly harmless subqueries to bypass safety filters.

**[PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf) (as "Subgoal proposal")**
> The observable generation of intermediate STL constraints (subgoals) intended to improve the solution of a primary PDE control problem when solved sequentially.

**[AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf) (as "Plan decomposition")**
> Breaking down high-level AutoML plans into role-specific sub-tasks assigned to specialized agents, such as data preprocessing or model search.

**[Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25s/yang25s.pdf) (as "Concept decomposition")**
> The breakdown of a complex malicious goal into simpler, less overtly harmful sub-concepts to reduce cognitive load and evade detection by safety mechanisms.

**[EMNLP: Educator-role Moral and Normative Large Language Models Profiling](https://aclanthology.org/2025.emnlp-main.43.pdf) (as "Claim decomposition")**
> Breaking down a summary into atomic factual subclaims for fine-grained evaluation of content validity and coverage.

**[P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation ofLLMs](https://aclanthology.org/2025.emnlp-main.243.pdf) (as "Query graph construction")**
> The task of decomposing a query into sub-queries and organizing them into a directed acyclic graph representing dependencies and a reasoning plan.

**[TRUST-VL: An Explainable News Assistant for General Multimodal Misinformation Detection](https://aclanthology.org/2025.emnlp-main.285.pdf) (as "Subquestion decomposition")**
> Breaking down a complex question into simpler, answerable subquestions to guide stepwise reasoning.

**[Legal Fact Prediction: The Missing Piece in Legal Judgment Prediction](https://aclanthology.org/2025.emnlp-main.323.pdf) (as "Instruction decomposition")**
> Breaking down a complex or harmful instruction into a sequence of simpler or less suspicious sub-instructions to evade detection.

**[GraDaSE: Graph-Based Dataset Search with Examples](https://aclanthology.org/2025.emnlp-main.354.pdf) (as "Sub-question generation")**
> The process of decomposing a main question into multiple sub-questions as intermediate reasoning steps.

**[Mixture of Weight-shared Heterogeneous Group Attention Experts for Dynamic Token-wiseKVOptimization](https://aclanthology.org/2025.emnlp-main.1167.pdf) (as "Subproblem decomposition")**
> Breaking down a complex query into smaller, logically structured subproblems that can be processed independently or in sequence.

**[Token-level Proximal Policy Optimization for Query Generation](https://aclanthology.org/2025.emnlp-main.1590.pdf) (as "Subgoal setting")**
> Generating intermediate steps or subgoals that break a problem into smaller parts.

**[P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation ofLLMs](https://aclanthology.org/2025.emnlp-main.243.pdf) (as "Query decomposition")**
> The process of breaking down a complex user query into a set of simpler, more manageable sub-queries.

## Relationships

### Task decomposition →
- **Information retrieval** (behaviors tasks) — *causes*
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Data efficiency** (constructs) — *causes*
  - [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *causes*
  - [ChemAgent: Self-updating Memories in Large Language Models Improves Chemical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa7f64b45970e6a7f8824781e7e01501-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *causes*
  - [Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chan25b/chan25b.pdf)

### → Task decomposition
- **Planning** (constructs) — *causes*
  - [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Prompt optimization** (behaviors tasks) — *causes*
  - [POQD: Performance-Oriented Query Decomposer for Multi-vector retrieval](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ag/liu25ag.pdf)

### Associated with
- **Complex reasoning** (behaviors tasks)
  - [Towards Robust Multi-Modal Reasoning via Model Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c78ae0c1140902bf3a430b1725bcc4e-Paper-Conference.pdf)
- **Planning** (constructs)
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf)
- **Task planning** (constructs)
  - [Can Graph Learning Improve Planning in LLM-based Agents?](https://proceedings.neurips.cc/paper_files/paper/2024/file/098d1bd3eb6156a4c2f834563cdcf617-Paper-Conference.pdf)
- **Theorem proving** (behaviors tasks)
  - [Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Data analysis** (behaviors tasks)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Compositionality** (constructs)
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
- **RAP** (measurements)
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
- **Table question answering** (behaviors tasks)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **ReAct** (measurements)
  - [Rethinking Word Similarity: Semantic Similarity through Classification Confusion](https://aclanthology.org/2025.naacl-long.300.pdf)
- **Multi-step planning** (behaviors tasks)
  - [zFLoRA: Zero-Latency Fused Low-Rank Adapters](https://aclanthology.org/2025.emnlp-main.1087.pdf)
- **Scientific reasoning** (constructs)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)

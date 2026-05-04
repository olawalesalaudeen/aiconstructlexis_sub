# Chain-of-thought reasoning
**Type:** Construct  
**Referenced in:** 506 papers  
**Also known as:** Intermediate step generation, Chain-of-thought generation, Step-by-step reasoning, Rationale generation, Step-by-step solution generation, Reasoning path generation, Chain-of-thought computation, Step-by-step reasoning generation, Reasoning generation, Reasoning trace generation, Hierarchical thought generation, Multi-step problem solving, Multi-hop tracing, Chain-of-thought verification, Intermediate reasoning generation, Multi-step reasoning generation, Multi-step inference, Multi-step decision-making, Multi-branch reasoning, Multi-step reasoning, Search trajectory verbalization, Off-target response generation, Complex Reasoning, Multi-step execution, Reasoning chain generation, Chain-of-thought inference, Label rationalization, Stepwise reasoning, Reasoning chain construction, Inner monologue generation, Reasoning context generation, Silent chain-of-thought generation, Explicit Chain-of-Thought generation, Intermediate instruction generation, Reasoning step generation, Logic generation, Step-by-step execution, Structured response generation, Continuous thought generation, Compressed chain-of-thought generation, Chain-of-thought translation, Structured chain-of-thought generation, Natural language chain-of-thought generation, Program chain-of-thought generation, Chain-of-Thought reasoning, Chain-of-reasoning, Thought chain reasoning, Chain-of-Thought ability, Chain-of-thought capability, Composite reasoning, Multi-session reasoning, Multistep mathematical reasoning, Deep reasoning, Higher-order reasoning, Long-chain reasoning, Multi-turn reasoning, Chain-of-thought faithfulness, Multihop reasoning, High-level reasoning, Two-hop reasoning, Reasoning length, Internal chain-of-thought, Comprehensive reasoning, Advanced reasoning, Multistep reasoning, Step-by-step thinking, Intermediate reasoning, Procedural reasoning, Iterative reasoning, Chain-of-Thought Reasoning, Long Chain-of-Thought reasoning, Long chain-of-thought reasoning  

## State of the Field

Across the surveyed literature, Chain-of-thought reasoning is predominantly characterized as the observable behavior of a model generating a sequence of intermediate steps before producing a final answer, described with terms like "step-by-step reasoning," "rationale generation," and "reasoning path generation." However, a notable portion of the work also defines it as a latent construct, referring to a model's underlying "capability" or "ability" for multi-step or complex reasoning. This behavior is commonly elicited through prompting strategies, such as providing in-context examples or explicit instructions like "Let’s think step by step." The field operationalizes and measures this behavior using a wide array of benchmarks, with a frequent focus on mathematical and logical reasoning tasks, including GSM8k, StrategyQA, and MuSiQue. Generating these intermediate steps is widely reported to improve performance on complex tasks, most notably mathematical reasoning, but also symbolic, logical, and algorithmic reasoning, and is also cited as enhancing interpretability. The generated output can take various forms, from natural language explanations and executable code snippets ("Program chain-of-thought generation") to latent or non-verbalized steps ("Silent chain-of-thought generation"). The concept is frequently studied in relation to tool use, self-consistency, and faithfulness, and is sometimes investigated for its connection to failure modes like hallucination.

## Sources

**[How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf) (as "Intermediate step generation")**
> The observable behavior of a model generating a sequence of intermediate computations or reasoning steps (a scratchpad) before producing a final answer.

**[Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf) (as "Chain-of-thought generation")**
> The observable model output of generating a sequence of intermediate steps that lead to a final answer.

**[UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Step-by-step reasoning")**
> The observable behavior of generating a sequence of intermediate steps or a rationale that leads to the final answer, typically prompted by a Chain-of-Thought strategy.

**[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf) (as "Rationale generation")**
> The behavior of producing a chain of reasoning or explanation for a decision or confidence level when prompted.

**[What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)**
> The task of generating a step-by-step explanation (a 'chain of thought') that leads to the final answer for a complex reasoning problem, often involving both text and images.

**[Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "Thought generation")**
> The specific action of producing one or more candidate intermediate reasoning steps (thoughts) from a given state in a problem-solving process.

**[SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02ee6b7295f720407b56c457b34c54d5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Step-by-step solution generation")**
> The behavior of producing a detailed, sequential reasoning process (chain-of-thought) leading to a final answer for a given problem.

**[Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf) (as "Reasoning path generation")**
> The behavior of generating a step-by-step explanation or sequence of intermediate thoughts (Chain-of-Thought) that leads from a problem statement to its solution.

**[On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf) (as "Chain-of-thought computation")**
> The observable behavior of generating a series of intermediate reasoning steps before producing a final answer.

**[Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf) (as "Step-by-step reasoning generation")**
> The action of verbalizing a sequence of intermediate steps that lead to a final answer for a given problem.

**[Large Language Models' Expert-level Global History Knowledge Benchmark (HiST-LLM)](https://proceedings.neurips.cc/paper_files/paper/2024/file/38cc5cba8e513547b96bc326e25610dc-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Reasoning generation")**
> Producing a short explanation of evidence and reasoning before giving the final answer.

**[ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf) (as "Reasoning trace generation")**
> The observable act of autoregressively producing a sequence of reasoning steps from a given problem or prompt.

**[FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf) (as "Multi-hop tracing")**
> A task requiring the model to follow a chain of references or reasoning steps across multiple points in a long document to find an answer.

**[SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/0967d7c8b171dd81b77c43067c02bebf-Paper-Conference.pdf) (as "Hierarchical thought generation")**
> The generation of a structured reasoning process that includes both a high-level, generalized solution template and a detailed, step-by-step explanation of critical steps.

**[Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf) (as "Chain-of-thought verification")**
> The observable behavior of a model generating an explicit, step-by-step rationale to critique a solution before making a final correctness judgment.

**[Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf) (as "Multi-step problem solving")**
> The observable behavior of generating a sequence of intermediate steps to arrive at a solution for a complex problem.

**[Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf) (as "Multi-hop reasoning")**
> Combining information from multiple retrieved documents to reach an answer through an intermediate reasoning chain.

**[Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf) (as "Multi-step reasoning generation")**
> The observable process of generating a sequence of intermediate steps, or a reasoning trajectory, to solve a problem.

**[MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf) (as "Multi-step inference")**
> Solving problems that require chaining multiple inferential steps across modalities.

**[TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf) (as "Multi-step reasoning")**
> The process of generating a sequence of intermediate reasoning steps to reach a final answer.

**[TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf) (as "Multi-branch reasoning")**
> The process of generating multiple, distinct reasoning trajectories from a single prompt or intermediate state.

**[Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf) (as "Multi-step decision-making")**
> Selecting and sequencing actions over multiple steps to accomplish a task or instruction.

**[Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df5b1f121c915d8bdd00db6aac20827-Paper-Conference.pdf) (as "Intermediate reasoning generation")**
> The behavior of generating an explicit reasoning paragraph that identifies relevant passages and explains the rationale before producing the final answer.

**[System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf) (as "Search trajectory verbalization")**
> Outputting a step-by-step textual representation of explored states and actions during search.

**[Language Imbalance Driven Rewarding for Multilingual Self-improving](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cdee7247c410907b32fcbc12a605823-Paper-Conference.pdf) (as "Off-target response generation")**
> An observable failure mode where the model produces responses that are irrelevant, in the wrong language, or otherwise fail to address the prompt's intent.

**[DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf) (as "Complex Reasoning")**
> The task of solving questions that require multi-step logical inference or detailed analysis.

**[Training Nonlinear Transformers for Chain-of-Thought Inference:  A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf) (as "Chain-of-thought inference")**
> Generating stepwise reasoning outputs for a query when the prompt includes examples with intermediate steps.

**[KOR-Bench: Benchmarking Language Models on Knowledge-Orthogonal Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6f5851a0d9cb435ed8b50e87bd6a257-Paper-Conference.pdf) (as "Multi-step execution")**
> The observable behavior of carrying out a sequence of operations or steps to solve a problem.

**[Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf) (as "Reasoning chain generation")**
> The observable behavior of producing a step-by-step textual explanation that details the logic leading to a specific prediction.

**[Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf) (as "Label rationalization")**
> The process where a model is given a video, a question, and the correct label, and is prompted to generate a step-by-step explanation for how to arrive at that label.

**[Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf) (as "Stepwise reasoning")**
> The behavior of generating a sequence of intermediate analytical steps or reasoning chains before producing a final answer, particularly when processing multiple documents.

**[Confidence v.s. Critique: A Decomposition of Self-Correction Capability forLLMs](https://aclanthology.org/2025.acl-long.204.pdf) (as "Reason generation")**
> The observable behavior of generating a textual explanation to justify a prediction, specifically in the context of the Legal Concept Entailment task.

**[LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf) (as "Reasoning chain construction")**
> Iteratively building a sequence of logically connected knowledge triples that support answering a given question.

**[Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ae/xu25ae.pdf) (as "Inner monologue generation")**
> Producing explicit, intermediate reasoning steps in natural language that reflect the agent’s thought process before taking actions.

**[Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf) (as "Long chain-of-thought generation")**
> Producing extended sequences of reasoning tokens that precede the final answer, often exceeding typical output lengths and demonstrating structured thought.

**[Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf) (as "Reasoning context generation")**
> Producing step-by-step logical justifications or intermediate reasoning steps for question-answer pairs, enriching the knowledge base with explainable inference patterns.

**[On the Power of Context-Enhanced Learning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25p/zhu25p.pdf) (as "Silent chain-of-thought generation")**
> The model's production of a fixed number of <THINK> tokens during output, simulating internal reasoning without explicit intermediate steps in the final answer.

**[MAC-Tuning:LLMMulti-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.36.pdf) (as "Explicit Chain-of-Thought generation")**
> The observable behavior of generating intermediate reasoning steps in natural language before providing a final answer.

**[Biased Tales: Cultural and Topic Bias in Generating Children’s Stories](https://aclanthology.org/2025.emnlp-main.4.pdf) (as "Intermediate instruction generation")**
> The observable behavior of explicitly generating natural language reasoning steps, such as arithmetic and logical checks, between generation stages to ensure constraint adherence.

**[Enhancing Reasoning Abilities of SmallLLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.378.pdf) (as "Reasoning step generation")**
> Producing intermediate reasoning tokens (e.g., justifications, decompositions) before arriving at a final answer, often enclosed in specific tags.

**[OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf) (as "Logic generation")**
> Producing intermediate reasoning steps that justify the answer to a question, based on unlabeled input and task type.

**[DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf) (as "Step-by-step execution")**
> The observable behavior of generating a sequence of intermediate outputs that follow a prescribed procedural rubric, including tokenization, n-gram generation, and numerical computation.

**[AROMA: Autonomous Rank-one Matrix Adaptation](https://aclanthology.org/2025.emnlp-main.171.pdf) (as "Structured response generation")**
> The behavior of generating a response that is segmented into logically discrete reasoning steps, often marked by transitional phrases like "Step 1:", "Step 2:", etc.

**[MAC-Tuning:LLMMulti-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.36.pdf) (as "Continuous thought generation")**
> Autoregressively generating a sequence of continuous latent representations as intermediate reasoning steps before producing an answer.

**[Humanizing Machines: RethinkingLLMAnthropomorphism Through a Multi-Level Framework of Design](https://aclanthology.org/2025.emnlp-main.165.pdf) (as "Compressed chain-of-thought generation")**
> The observable behavior of generating a condensed chain-of-thought by selectively omitting tokens deemed less semantically important, thereby reducing the total output length.

**[JOLT-SQL: Joint Loss Tuning of Text-to-SQLwith Confusion-aware Noisy Schema Sampling](https://aclanthology.org/2025.emnlp-main.309.pdf) (as "Chain-of-thought translation")**
> Producing a translation by first reasoning through the input in steps, such as reading the sentence and then translating it.

**[Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection](https://aclanthology.org/2025.emnlp-main.1216.pdf) (as "Structured chain-of-thought generation")**
> Producing explicit multi-step reasoning traces before the final answer, often with labeled planning, captioning, reasoning, and summary sections.

**[HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1366.pdf) (as "Natural language chain-of-thought generation")**
> The observable behavior of producing a step-by-step reasoning rationale in natural language to solve a problem.

**[HydraOpt: Navigating the Efficiency-Performance Trade-off of Adapter Merging](https://aclanthology.org/2025.emnlp-main.1366.pdf) (as "Program chain-of-thought generation")**
> Generating executable code snippets that represent the reasoning steps for solving a mathematical problem, which can be verified by an interpreter.

**[Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf) (as "Chain-of-Thought reasoning")**
> The ability of a language model to solve complex problems by generating a sequence of intermediate, logical steps before providing a final answer.

**[Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf) (as "Chain-of-reasoning")**
> The model's ability to break down a problem into intermediate, sequential steps to arrive at a final solution, often by generating explicit intermediate text.

**[Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf) (as "Chain-of-thought capability")**
> The model's ability to benefit from or perform step-by-step reasoning when prompted to explain intermediate inference steps.

**[Training Nonlinear Transformers for Chain-of-Thought Inference:  A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf) (as "Chain-of-Thought ability")**
> The latent capability of a model to perform multi-step reasoning by generating intermediate steps when prompted with examples.

**[ThinkBot: Embodied Instruction Following with Thought Chain Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ffa8551239448e07ced48311bf88f6f3-Paper-Conference.pdf) (as "Thought chain reasoning")**
> The latent ability of a model to infer and articulate a series of intermediate, unstated steps that connect an initial problem to a final solution, particularly for recovering missing actions from sparse instructions.

**[Q-SFT: Q-Learning for Language Models via Supervised Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9531a3e64e6167c7e1e671157082682-Paper-Conference.pdf) (as "Sequential reasoning")**
> The inferred cognitive ability to understand and process sequences of information, such as the history of utterances in a dialogue, to determine an appropriate next action.

**[Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf) (as "Multistep mathematical reasoning")**
> The latent ability to perform a sequence of logical and mathematical steps to arrive at a solution for a quantitative problem.

**[ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf) (as "Composite reasoning")**
> The ability to solve complex problems by integrating multiple distinct reasoning steps or categories, such as combining fluent tracking with action executability.

**[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf) (as "Multi-session reasoning")**
> The ability to synthesize information spread across multiple sessions in order to answer questions that require aggregation or comparison.

**[Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf) (as "Complex reasoning")**
> The ability to perform sophisticated logical and inferential thinking to solve complex problems.

**[WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf) (as "Higher-order reasoning")**
> The capacity to engage in complex cognitive processes that go beyond basic information retrieval, involving multiple steps or constraints.

**[Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf) (as "Deep reasoning")**
> The ability to solve complex questions by integrating multiple pieces of knowledge through multi-step inference.

**[Building Math Agents with Multi-Turn Iterative Preference Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/40eff1670d6b08bb1bda48b0c5f30110-Paper-Conference.pdf) (as "Multi-turn reasoning")**
> The capacity to maintain context and make a sequence of coherent decisions or inferences over multiple interaction turns with an external environment.

**[TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf) (as "Long-chain reasoning")**
> The capability to perform tasks that require numerous sequential steps, where errors in any single step can lead to an incorrect final outcome.

**[On Targeted Manipulation and Deception when Optimizing LLMs for User Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/deed907f507e526a8dd20896d2bd7c49-Paper-Conference.pdf) (as "Chain-of-thought faithfulness")**
> The degree to which a model's explicit reasoning trace accurately reflects the true basis of its outputs.

**[SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf) (as "Multihop reasoning")**
> The ability to answer complex questions by finding, connecting, and synthesizing information from multiple distinct documents or evidence snippets.

**[Extractive Structures Learned in Pretraining Enable Generalization on Finetuned Facts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25m/feng25m.pdf) (as "Two-hop reasoning")**
> The latent ability to compose two factual associations (a → b and b → c) to infer a distant relationship (a → c), where one fact is newly learned and the other is pre-existing.

**[SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cm/zhang25cm.pdf) (as "High-level reasoning")**
> The latent ability of an autonomous driving system to connect high-level decisions, such as 'the car should slow to a stop', with low-level control signals.

**[REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting inLLMKnowledge Editing](https://aclanthology.org/2025.emnlp-main.861.pdf) (as "Reasoning length")**
> The latent extent to which a model generates extended, step-by-step reasoning before producing a final answer, reflecting the depth and thoroughness of its internal problem-solving process.

**[Understanding Subword Compositionality of Large Language Models](https://aclanthology.org/2025.emnlp-main.1147.pdf) (as "Internal chain-of-thought")**
> The latent capacity of LLMs to internally decompose composite tasks into subtasks and process them sequentially across network layers, even when intermediate steps are not expressed in output.

**[AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf) (as "Comprehensive reasoning")**
> The general reasoning capacity reflected in performance on hard benchmark tasks requiring multi-step inference.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Advanced reasoning")**
> The ability to perform complex cognitive operations beyond simple pattern matching, which is required for difficult tasks like forecasting and text generation.

**[Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf) (as "Multistep reasoning")**
> A general cognitive capability to solve problems by breaking them down into a sequence of intermediate steps or operations.

**[SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf) (as "Step-by-step thinking")**
> The ability to break down a problem into a sequence of smaller, manageable steps and solve them sequentially.

**[SQUiD: Synthesizing Relational Databases from Unstructured Text](https://aclanthology.org/2025.emnlp-main.1630.pdf) (as "Procedural reasoning")**
> The capacity to carry out step-by-step problem solving using methods, inference rules, or solution procedures rather than only retrieving facts.

**[MakingVLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning](https://aclanthology.org/2025.emnlp-main.1659.pdf) (as "Intermediate reasoning")**
> The ability to correctly perform the intermediate steps within a larger reasoning process, as opposed to only arriving at the final answer.

**[RoT: Enhancing Table Reasoning with Iterative Row-Wise Traversals](https://aclanthology.org/2025.emnlp-main.30.pdf) (as "Iterative reasoning")**
> A cognitive-like process of progressively refining an internal representation or prediction over multiple steps to capture more nuanced semantic details and cross-modal relationships.

**[Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf) (as "Chain-of-Thought Reasoning")**
> Generating intermediate reasoning steps before producing a final answer, often used to improve performance on complex reasoning tasks.

**[MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf) (as "Long Chain-of-Thought reasoning")**
> The emergent capability of a model to perform deep, structured natural language reasoning before generating formal outputs, enabling high-level planning and self-reflection in problem solving.

**[LVLMs are Bad at Overhearing Human Referential Communication](https://aclanthology.org/2025.emnlp-main.850.pdf) (as "Long chain-of-thought reasoning")**
> The ability to generate extended, coherent, and step-by-step reasoning processes to solve complex problems.

## Relationships

### Chain-of-thought reasoning →
- **Mathematical reasoning** (constructs) — *causes*
  > In the first stage, we extract hierarchical high-level and detailed thought templates from the teacher model to guide the student model in eliciting more fine-grained reasoning thoughts.
  - [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  > Con-J ensures natural interpretability through the generated rationales supporting the judgments (Abstract).
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [Training Nonlinear Transformers for Chain-of-Thought Inference:  A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf)
- **Symbolic reasoning** (constructs) — *causes*
  > Large Language Models (LLMs) have achieved significant advancements in tackling complex reasoning tasks (Zhou et al., 2023; Yao et al., 2023; Besta et al., 2023), such as mathematics(Imani et al., 2023; Cobbe et al., 2021; Yuan et al., 2023) and symbolic logic(Patel et al., 2021; Srivastava et al., 2022; Ling et al., 2017), by adopting the innovative Chain-of-Thought (CoT) prompting strategy (Wei et al., 2022)... (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > we adopt a pairwise comparison approach, where an LLM evaluates a question alongside two answers and determines which response is of higher quality. (Section 6.4)
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Backtracking** (behaviors tasks) — *causes*
  > The Transformer model simulates logical assumption, deduction, and backtracking by generating new tokens and ultimately outputs a SAT/UNSAT label as the result of the 3-SAT decision problem.
  - [Can Transformers Reason Logically? A Study in SAT Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25d/pan25d.pdf)
- **Complex reasoning** (behaviors tasks) — *causes*
  - [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  > Following prior work (Zhang et al., 2024a; Chuang et al., 2023), we evaluate chain-of-thought reasoning capabilities using StrategyQA (Geva et al., 2021) and GSM8K (Cobbe et al., 2021). (Section 3.1)
  - [MAIN: Mutual Alignment Is Necessary for instruction tuning](https://aclanthology.org/2025.emnlp-main.645.pdf)
- **ScienceQA** (measurements) — *measured_by*
  - [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)
- **Active information gathering** (behaviors tasks) — *causes*
  - [Can large language models explore in-context?](https://proceedings.neurips.cc/paper_files/paper/2024/file/d951f73c521d069fefbb73396df01424-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > To examine how retrieval heads effect reasoning tasks, we test Mistrial-7B-Instruct-v0.2 on MMLU (Hendrycks et al., 2020), MuSiQue and GSM8K (Cobbe et al., 2021), with and without chain-of-thought (CoT) reasoning. (Section 4.3)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Speech synthesis** (behaviors tasks) — *causes*
  - [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > Asking the Constructor to complete the whole chain reduces hallucination, and avoids a sub-optimal greedy approach. (Section 3.2)
  - [LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf)
- **Response quality** (constructs) — *causes*
  - [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *causes*
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Algorithmic reasoning** (constructs) — *causes*
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **LongMemEval** (measurements) — *measured_by*
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **MuSiQue** (measurements) — *measured_by*
  > HotpotQA (Yang et al., 2018), 2WikiMultihopQA (Ho et al., 2020), and MuSiQue (Trivedi et al., 2021) can be applied to evaluate the multi-step reasoning performance of LLMs. (Section 2)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Chain-of-thought prompting** (measurements) — *measured_by*
  - [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)
- **Answer generation** (behaviors tasks) — *causes*
  > We utilize Chain-of-Thought (CoT) (Wei et al., 2022) reasoning to link individual pieces of evidence that form a coherent step-by-step narrative, ensuring that the answer is not only accurate but also logically derived from the evidence, leading to more robust and reliable responses. (Section 5.1)
  - [TinyThinker: Distilling Reasoning through Coarse-to-Fine Knowledge Internalization with Self-Reflection](https://aclanthology.org/2025.naacl-long.310.pdf)
- **MedQA** (measurements) — *measured_by*
  > We use one dataset from each of these categories for fine-tuning the LLM and we use all the datasets to evaluate the effect of fine-tuning on the given dataset... i) MedQA (Jin et al., 2021): Multiple choice question answers from the United States Medical License Exams (USMLE)... (Section 4)
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **MedMCQA** (measurements) — *measured_by*
  > We use one dataset from each of these categories for fine-tuning the LLM and we use all the datasets to evaluate the effect of fine-tuning on the given dataset... ii) MedMCQA (Pal et al., 2022): Multiple choice question answers from the All India Institute of Medical Sciences (AIIMS) and National Eligibility cum Entrance Exam (NEET)... (Section 4)
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **CosmosQA** (measurements) — *measured_by*
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **Reward hacking** (behaviors tasks) — *causes*
  > Our analysis shows that CoT reasoning is crucial for unlocking DPO’s potential, as it mitigates reward hacking, strengthens discriminative capabilities, and improves scalability. (Section 5.1)
  - [KatFishNet: DetectingLLM-GeneratedKorean Text through Linguistic Feature Analysis](https://aclanthology.org/2025.acl-long.1031.pdf)
- **Scalability** (constructs) — *causes*
  > Our analysis shows that CoT reasoning is crucial for unlocking DPO’s potential, as it mitigates reward hacking, strengthens discriminative capabilities, and improves scalability. (Section 5.1)
  - [KatFishNet: DetectingLLM-GeneratedKorean Text through Linguistic Feature Analysis](https://aclanthology.org/2025.acl-long.1031.pdf)
- **AIME** (measurements) — *measured_by*
  > We assess both models on the challenging American Invitational Mathematics Examination (AIME 24) benchmark. (Section 3.3, Chain-of-Thought Reasoning Evaluation).
  - [Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Molecule understanding** (behaviors tasks) — *causes*
  - [Learning Together to Perform Better: Teaching Small-ScaleLLMs to Collaborate via Preferential Rationale Tuning](https://aclanthology.org/2025.acl-long.755.pdf)
- **AIME 2024** (measurements) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [Revisiting Chain-of-Thought in Code Generation: Do Language Models Need to Learn Reasoning before Coding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ah/liu25ah.pdf)
- **Task generalization** (constructs) — *causes*
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)
- **MATH-500** (measurements) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Machine translation** (behaviors tasks) — *causes*
  > This indicates that the reasoning-based approach of LLMs can generate more accurate translations across multiple domains. (Section 3.1)
  - [DIWALI- Diversity and Inclusivity aWare cuLture specific Items forIndia: Dataset and Assessment ofLLMs for Cultural Text Adaptation inIndian Context](https://aclanthology.org/2025.emnlp-main.1707.pdf)
- **MR-GSM8K** (measurements) — *measured_by*
  - [MakingVLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning](https://aclanthology.org/2025.emnlp-main.1659.pdf)
- **Trojsten Benchmark** (measurements) — *measured_by*
  - [Retrieving Support to Rank Answers in Open-Domain Question Answering](https://aclanthology.org/2025.emnlp-main.1779.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)

### → Chain-of-thought reasoning
- **Instruction following** (constructs) — *causes*
  > By leveraging the strong instruction-following abilities of large language models, INSTRUCTRAG generates detailed rationales that articulate how the ground-truth answers can be derived from the retrieved documents. (Section 5)
  - [CART: A Generative Cross-Modal Retrieval Framework With Coarse-To-Fine Semantic Modeling](https://aclanthology.org/2025.acl-long.736.pdf)
- **LASER** (measurements) — *causes*
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  > Although recent large language models (LLMs) (Jiang et al., 2023; Dubey et al., 2024) have showcased extensive capabilities across various domains, they still face challenges with complex multi-step reasoning tasks such as mathematical problem-solving. (Section 1)
  - [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > Label Rationalization is more prone to hallucinations, so we prefer direct Answer Generation and use rationalizations only if answer generation fails (Sec. 2.2).
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **GSM8k** (measurements)
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
- **Tool use** (behaviors tasks)
  > we opt for the framework of the ReAct agent that performs step-by-step reasoning for tool usage based on observations of previous steps.
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Slow thinking** (constructs)
  > These strategies encourage longer Chain-of-Thought (CoT) to handle more complex queries, mimicking human-like reflection and correction mechanisms to improve reasoning (Section 1).
  - [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Backtracking** (behaviors tasks)
  > The backtrack operation involves multiple actions, as the policy specifies how many steps to backtrack.
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **StrategyQA** (measurements)
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  > “Another failure mode multi-branch reasoning, i.e. in keeping track of multiple reasoning traces that could lead to valid solutions.”
  - [Understanding Chain-of-Thought in LLMs through Information Theory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ton25a/ton25a.pdf)
- **Self-consistency** (measurements)
  - [Upsample or Upweight? Balanced Training on Heavily Imbalanced Datasets](https://aclanthology.org/2025.naacl-long.172.pdf)
- **In-context learning** (constructs)
  - [Synthetic Socratic Debates: Examining Persona Effects on Moral Decision and Persuasion Dynamics](https://aclanthology.org/2025.emnlp-main.832.pdf)
- **Compositional reasoning** (constructs)
  - [Teaching Arithmetic to Small Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [Cooperative or Competitive? Understanding the Interaction between Attention Heads From A Game Theory Perspective](https://aclanthology.org/2025.acl-long.689.pdf)
- **Self-correction** (behaviors tasks)
  - [Think Smarter not Harder: Adaptive Reasoning with Inference Aware Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25s/yu25s.pdf)
- **Direct answer generation** (behaviors tasks)
  > DART (Distilling Autoregressive Reasoning to Silent Thought), a novel framework that enables the LLMs to internalize the autoregressive CoT into non-autoregressive Silent Thought (ST) with an excellent efficiency-efficacy trade-off. (Section 1)
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.256.pdf)
- **Pattern recognition** (constructs)
  - [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf)
- **Answer generation** (behaviors tasks)
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **Label prediction** (behaviors tasks)
  > We fine-tune a relatively small local LLM (e.g., a 7B-parameter model) to perform both reasoning chain generation and label prediction for each patient p and healthcare prediction task τ (such as mortality or readmission prediction). (Section 3.3.2)
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
- **Majority voting** (measurements)
  > In general, majority voting is applicable if the generation y = (c, a) can be decomposed into a chain-of-thought c and a final answer a. (Section 2)
  - [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25o/tang25o.pdf)
- **Information retrieval** (behaviors tasks)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **G-Eval** (measurements)
  > Furthermore, we report G-EVAL (Liu et al., 2023a), an auto-CoT prompting framework, and the current state-of-the-art in NLG evaluation. (Section 5.1)
  - [Token-based Decision Criteria Are Suboptimal in In-context Learning](https://aclanthology.org/2025.naacl-long.279.pdf)
- **Interpretability and explainability** (constructs)
  - [SATER: A Self-Aware and Token-Efficient Approach to Routing and Cascading](https://aclanthology.org/2025.emnlp-main.532.pdf)
- **Critique** (behaviors tasks)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Memorization** (constructs)
  > Paper title: Diagnosing Memorization in Chain-of-Thought Reasoning, One Token at a Time
  - [2025.emnlp-main.157.checklist](https://aclanthology.org/attachments/2025.emnlp-main.157.checklist.pdf)
- **Chemical reasoning** (constructs)
  - [Foundation Molecular Grammar: Multi-Modal Foundation Models Induce Interpretable Molecular Graph Languages](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25aa/sun25aa.pdf)
- **Safety** (constructs)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **Post-hoc rationalization** (behaviors tasks)
  - [Where Confabulation Lives: Latent Feature Discovery inLLMs](https://aclanthology.org/2025.emnlp-main.1516.pdf)

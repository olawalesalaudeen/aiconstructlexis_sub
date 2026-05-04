# Reasoning
**Type:** Construct  
**Referenced in:** 871 papers  
**Also known as:** Reasoning ability, Reasoning capability, Inference ability, Reasoning capacity, Inferential capabilities, Inferences, General inference capability, Reasoning capabilities, Reasoning skills, Common sense, Fluid intelligence, Formal inference, Negation robustness, Sub-task decomposition, Inference capability, Inferential ability, Concept inference, Contextual meaning inference, Keyword organization inference, Latent variable inference, Task inference, Deep thinking, Hierarchical thinking, Latent thinking, Strategic thinking, Thinking, Compositional condition understanding, Cross-file dependency understanding, Document-level understanding, Intentionality understanding, Note comprehension, Problem comprehension, Region-level comprehension, Relationship comprehension, Response understanding, Schema understanding, Screen understanding, Semantic corruption understanding, Comprehension, Understanding ability, Unnatural language comprehension, Constraint adherence, Instruction adherence, Structural conformity, General instruction following, Instruction-following ability, Instruction-following capability, Open-ended instruction following, Prompt following, Constrained generation, Complex instruction understanding, Symbolic computing, Symbol processing, Reasoning performance  

## State of the Field

Across the surveyed literature, Reasoning is most commonly defined as a latent cognitive capacity for multi-step logical inference and deduction. This ability is frequently investigated in contexts requiring mathematical, logical, commonsense, and code-based problem-solving. The field operationalizes and measures this construct primarily through performance on a set of standardized benchmarks, with the most frequently cited instruments being MMLU and BIG-Bench Hard (BBH), alongside others like HellaSwag, StrategyQA, and DROP. Many papers connect the elicitation of reasoning to specific prompting techniques, particularly Chain-of-Thought (CoT), which, as one paper notes, prompts models "to generate intermediate reasoning steps" ("Large Language Models as Analogical Reasoners"). While the multi-step inference framing is prevalent, a substantial body of work uses "reasoning" more broadly to encompass a wide range of inferential and comprehension abilities, including concepts like "instruction following," "constraint adherence," and various forms of "understanding." A smaller set of studies focuses on more specific facets, defining and analyzing distinct types such as "formal inference," "fluid intelligence," and "symbol processing." Reasoning is also frequently discussed in the context of agentic systems, where it is linked to capabilities like planning, decision-making, and tool use. Overall, the construct is treated as a foundational capability that allows models to solve complex problems by moving beyond simple pattern matching to structured, step-by-step thought processes.

## Sources

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)**
> The capacity for multi-hop logical inference and deduction about object interactions, action conditions, or dependencies.

**[At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf) (as "Reasoning capability")**
> The ability to infer task structure, constraints, and implementation details needed to generate coherent new simulation tasks.

**[Building Cooperative Embodied Agents Modularly with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/54b8b4e0b4ba4aad112e84f32e3b5dbb-Paper-Conference.pdf) (as "Reasoning ability")**
> The emergent capability of a large language model to logically process given information and infer conclusions or generate new insights, particularly when guided by well-structured prompts.

**[LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Inference ability")**
> The capacity of a large language model to reason and draw conclusions based on its existing knowledge.

**[Entity Alignment with Noisy Annotations from Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1b57aaddf85ab01a2445a79c9edc1f4b-Paper-Conference.pdf) (as "Reasoning capacity")**
> The model's latent ability to infer correct outputs through multi-step or probabilistic inference rather than direct pattern matching.

**[MACM: Utilizing a Multi-Agent System for Condition Mining in Solving Complex Mathematical Problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/5fcedec09977357f32e8e0ec8957073b-Paper-Conference.pdf) (as "Inferential capabilities")**
> The model's underlying ability to make inferences and draw conclusions from given information, which can be enhanced through prompting techniques.

**[Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Inferences")**
> The ability to make plausible deductions about the model's present situation from cues in the prompt or context.

**[Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf) (as "General inference capability")**
> The model's broad ability to perform reasoning and apply knowledge across a wide range of general-purpose tasks, as opposed to specific trustworthiness-related behaviors.

**[Preference Optimization for Reasoning with Pseudo Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/31a57804448363bcab777f818f75f5b4-Paper-Conference.pdf) (as "Reasoning capabilities")**
> The broader latent capacity of an LLM to solve reasoning-oriented tasks across domains such as mathematics and programming.

**[DataGen: Unified Synthetic Dataset Generation via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a01e69aa9c3c61fcb40ea378e71fc780-Paper-Conference.pdf) (as "Reasoning skills")**
> The latent capacity to solve problems that require multi-step inference, especially in math-oriented and other reasoning-heavy settings.

**[FLEURS-ASL: IncludingAmericanSignLanguage in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.315.pdf) (as "Sub-task decomposition")**
> The ability to break down a complex task into smaller, more manageable sub-tasks.

**[FLEURS-ASL: IncludingAmericanSignLanguage in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.315.pdf) (as "Commonsense knowledge")**
> The implicit knowledge about the world that humans use to make everyday judgments and inferences.

**[Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf) (as "Common sense")**
> The latent ability to answer or reason in ways consistent with everyday world knowledge.

**[K-Level Reasoning: Establishing Higher Order Beliefs in Large Language Models for Strategic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf) (as "Formal inference")**
> The capacity to abstract and apply logical inference rules independent of the semantic content of the premises, focusing on structural validity rather than factual correctness.

**[Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.413.pdf) (as "Negation robustness")**
> The latent ability of a language model to maintain correct understanding and reasoning when negation is present or altered in text.

**[Evaluating Contextualized Representations of (Spanish) Ambiguous Words: A New Lexical Resource and Empirical Analysis](https://aclanthology.org/2025.naacl-long.423.pdf) (as "Fluid intelligence")**
> The latent ability to solve novel problems without relying on prior knowledge or memorization, involving abstract inductive reasoning and pattern induction from examples.

**[An Efficient Task-Oriented Dialogue Policy: Evolutionary Reinforcement Learning Injected by Elite Individuals](https://aclanthology.org/2025.acl-long.172.pdf) (as "Inference capability")**
> The model's ability to generate accurate outputs by leveraging internalized knowledge of structured linguistic information during task execution.

**[AccurateKVCache Quantization with Outlier Tokens Tracing](https://aclanthology.org/2025.acl-long.632.pdf) (as "Inferential ability")**
> The latent capacity of an LLM to deduce the meaning of a previously unseen buzzword solely from contextual user-generated content, without relying on prior exposure or memorization.

**[Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf) (as "Contextual meaning inference")**
> The latent ability of LLMs to reconstruct the correct semantic organization of keywords from disordered, unnatural inputs by leveraging contextual cues from subsequent natural language questions.

**[Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf) (as "Keyword organization inference")**
> The latent ability to infer the correct semantic and syntactic arrangement of keywords that have been extracted from a disordered or noisy input.

**[rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf) (as "Deep thinking")**
> A mode of reasoning analogous to human System 2 cognition, characterized by a slower, more deliberate, and iterative thought process, often implemented via search algorithms like MCTS.

**[HyperTree Planning: Enhancing LLM Reasoning via Hierarchical Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gui25b/gui25b.pdf) (as "Hierarchical thinking")**
> The latent ability of an LLM to decompose complex reasoning problems into multiple levels of sub-tasks using a divide-and-conquer strategy, enabling organized and scalable planning.

**[Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf) (as "Latent thinking")**
> The model's capacity to perform internal, non-verbalized cognitive processing in continuous latent space, distilling additional computation into its kv-cache to improve downstream performance.

**[Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf) (as "Task inference")**
> The model's capacity to deduce the abstract rule or mapping (e.g., class-to-label function) from a set of input-output examples provided in context.

**[Does learning the right latent variables necessarily improve in-context learning?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mittal25a/mittal25a.pdf) (as "Latent variable inference")**
> The model's ability to infer unobserved, low-dimensional parameters or structures that govern the data generation process for a task.

**[LLMs Can Reason Faster Only If We Let Them](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sel25a/sel25a.pdf) (as "Strategic thinking")**
> The capacity to deliberately choose among alternative reasoning paths in a way that supports goal-directed problem solving.

**[Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf) (as "Thinking")**
> The latent ability of an LLM to generate internal reasoning or planning processes in natural language before producing a final response, enabling improved performance on complex tasks through implicit computation and self-reflection.

**[Plausible Token Amplification for Improving Accuracy of Differentially Private In-Context Learning Based on Implicit Bayesian Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yamasaki25a/yamasaki25a.pdf) (as "Concept inference")**
> The latent ability of a model to infer an unstated rule or concept that connects data to labels based on the demonstrations provided in-context.

**[Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bonatti25a/bonatti25a.pdf) (as "Screen understanding")**
> The latent ability to interpret and reason about visual and structural elements of a computer interface, including text, icons, and layout, to identify actionable components.

**[Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf) (as "Unnatural language comprehension")**
> The latent ability of an LLM to derive meaning from syntactically noisy, human-incomprehensible text while still using it to answer questions or reconstruct natural language.

**[SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf) (as "Note comprehension")**
> The latent ability to understand and extract key information from social media content, including identifying topics, themes, and relevant details within notes.

**[Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf) (as "Structural understanding")**
> The model's latent comprehension of the principles governing protein structure, enabling it to perform tasks like folding.

**[Compositional Condition Question Answering in Tabular Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25o/jiang25o.pdf) (as "Compositional condition understanding")**
> The latent ability to interpret and reason over multiple interdependent conditions in a question when retrieving or computing answers from tabular data.

**[Core Knowledge Deficits in Multi-Modal Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25p/li25p.pdf) (as "Intentionality understanding")**
> The ability to infer the goals or desires of other agents.

**[Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25dt/li25dt.pdf) (as "Schema understanding")**
> The latent ability to interpret and utilize database schema information, including tables, columns, and relationships, to generate accurate SQL queries.

**[FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf) (as "Understanding ability")**
> The latent capability of a large language model to comprehend and process textual information, which is influenced by its autoregressive, left-to-right processing nature.

**[CogMath: Assessing LLMs’ Authentic Mathematical Ability from a Human Cognitive Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ab/liu25ab.pdf) (as "Problem comprehension")**
> The latent ability to understand the semantic content, structure, and conditions of a mathematical problem, including recognizing essential versus irrelevant information and detecting missing or contradictory conditions.

**[Potemkin Understanding in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mancoridis25a/mancoridis25a.pdf) (as "Conceptual understanding")**
> A model's true and generalizable grasp of a concept, demonstrated by consistent and correct application across various tasks, mirroring the way a human would use the concept.

**[Why Has Predicting Downstream Capabilities of Frontier AI Models with Scale Remained Elusive?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schaeffer25b/schaeffer25b.pdf) (as "Comprehension")**
> The latent ability of a model to understand the meaning of natural language text.

**[GeoPixel: Pixel Grounding Large Multimodal Model in Remote Sensing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shabbir25a/shabbir25a.pdf) (as "Region-level comprehension")**
> The ability to understand and reason about specific spatial regions within an image, as opposed to only processing the image as a whole.

**[WMarkGPT: Watermarked Image Understanding via Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25f/tan25f.pdf) (as "Semantic corruption understanding")**
> The latent capacity to recognize and articulate how watermarking affects the semantic content and integrity of an image, beyond low-level pixel differences.

**[GRAM: A Generative Foundation Reward Model for Reward Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ad/wang25ad.pdf) (as "Response understanding")**
> The latent ability of a reward model to comprehend the content, quality, and relevance of generated responses in relation to a given input.

**[EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf) (as "Cross-file dependency understanding")**
> The latent ability to comprehend and correctly manage dependencies, references, and interactions between multiple code files within a single project.

**[3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf) (as "Relationship comprehension")**
> The ability to understand the connections and interactions between different entities or concepts mentioned in a question and depicted in a scene.

**[DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf) (as "Document-level understanding")**
> The capacity to synthesize information and identify relationships across an entire document, beyond the scope of individual sentences.

**[NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf) (as "Instruction following")**
> The ability to interpret and act upon natural language instructions, particularly in the context of code modification or generation.

**[Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf) (as "Prompt following")**
> The degree to which a video generation model accurately realizes the content described in a text prompt, especially when the prompt describes counterfactual or impossible scenes.

**[On the Query Complexity of Verifier-Assisted Language Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/botta25a/botta25a.pdf) (as "Constrained generation")**
> The latent ability of a language model to produce outputs that satisfy externally imposed structural constraints while remaining in the generator's support.

**[Liger: Linearizing Large Language Models to Gated Recurrent Structures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lan25b/lan25b.pdf) (as "Instruction-following ability")**
> The latent capacity of a model to adapt its outputs to user instructions and task directives during fine-tuning or deployment.

**[Boosting Multi-Domain Fine-Tuning of Large Language Models through Evolving Interactions between Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liang25q/liang25q.pdf) (as "General instruction following")**
> The ability to comprehend and accurately execute a wide range of tasks specified in natural language prompts.

**[UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nayak25a/nayak25a.pdf) (as "Instruction adherence")**
> The tendency to follow the requested action format and avoid inserting unsupported or extraneous actions.

**[LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf) (as "Instruction-following capability")**
> The model’s ability to comply with prompt instructions and use them effectively during forecasting.

**[Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25d/shi25d.pdf) (as "Open-ended instruction following")**
> The capacity to understand and act on diverse, complex, and non-atomic natural language prompts that require decomposition into executable steps and adaptation over time.

**[Earley-Driven Dynamic Pruning for Efficient Structured Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25v/sun25v.pdf) (as "Structural conformity")**
> The ability of a model to generate outputs that strictly adhere to a specified formal grammar or structural format.

**[AUTOCIRCUIT-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vijayaraghavan25a/vijayaraghavan25a.pdf) (as "Constraint adherence")**
> The latent ability of the model to generate outputs that satisfy multiple, specified design constraints such as component usage, efficiency, and output voltage.

**[EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25f/yang25f.pdf) (as "Complex instruction understanding")**
> The ability to discern and execute a user's core intent from long or convoluted language instructions that may contain irrelevant information.

**[CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf) (as "Symbolic computing")**
> The model's ability to perform rigorous, exact operations through programmatic solutions, such as computation, symbolic manipulation, and algorithmic processing.

**[Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf) (as "Symbol processing")**
> An emergent cognitive capacity to operate on abstract variables (symbols) that are invariant to the specific values they are associated with, using mechanisms like indirection.

**[Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.132.pdf) (as "Reasoning performance")**
> The latent capacity of a model to correctly solve complex reasoning tasks, inferred from accuracy across diverse problems and conditions.

**[Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf) (as "General reasoning")**
> Performing broad reasoning tasks that require inference across diverse domains rather than a single specialized skill.

## Relationships

### Reasoning →
- **GSM8k** (measurements) — *measured_by*
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  > “BBH (Suzgun et al., 2022) and MMLU (Hendrycks et al., 2021) for multitask reasoning”
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > "MMLU (Hendrycks et al., 2021a) to determine factuality, BBH (Suzgun et al., 2022) to check reasoning abilities"
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurements) — *measured_by*
  > "MMLU (Hendrycks et al., 2021a) to determine factuality, BBH (Suzgun et al., 2022) to check reasoning abilities"
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > For short-context evaluation, we employ MMLU (Hendrycks et al., 2021), ARC-C (Clark et al., 2018), Hellaswag (Zellers et al., 2019) and Winogrande (Sakaguchi et al., 2019) for assessing the general language understanding and reasoning capabilities...
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://proceedings.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [The Trickle-down Impact of Reward Inconsistency on RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/8c976a95df6a229551cd28c76627edc9-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **MathVista** (measurements) — *measured_by*
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  - [Data Whisperer: Efficient Data Selection for Task-SpecificLLMFine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1136.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **GSM** (measurements) — *measured_by*
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **SVAMP** (measurements) — *measured_by*
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  > We use MMLU Hendrycks et al. (2020), BigBench Hard (BBH) Srivastava et al. (2022), and 4 reasoning benchmarks: GSM8K Cobbe et al. (2021), SVAMP Patel et al. (2021), ASDIV Miao et al. (2020), and StrategyQA Geva et al. (2021) (Section 3.1).
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf)
- **DROP** (measurements) — *measured_by*
  > DROP tests models’ abilities to perform complex reasoning over paragraphs, including approximately 96,000 questions containing numerical operations and logical inference.
  - [MMRC: A Large-Scale Benchmark for Understanding Multimodal Large Language Model in Real-World Conversation](https://aclanthology.org/2025.acl-long.1097.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
- **MMMU** (measurements) — *measured_by*
  > The experimental results on MMMU demonstrate that MIA-DPO enhances the LLaVA-v1.5’s reasoning ability on multi-image problems. (Section 4.2)
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GPQA** (measurements) — *measured_by*
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [Automatic Curriculum Expert Iteration for Reliable LLM Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9083c94382509473bdf5fc2672fc72b3-Paper-Conference.pdf)
- **AIME 2024** (measurements) — *measured_by*
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
- **GAIA** (measurements) — *measured_by*
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  - [DDK: Distilling Domain Knowledge for Efficient Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b206d54ffbb803b5c51d85f405d422e4-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
- **ASDIV** (measurements) — *measured_by*
  - [Mixture-of-Experts Meets Instruction Tuning: A Winning Combination for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/5222867be1bde4fb2d8ba018c03b3be8-Paper-Conference.pdf)
- **SIQA** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **MuSiQue** (measurements) — *measured_by*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf)
- **MMLU-STEM** (measurements) — *measured_by*
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
- **Game of 24** (measurements) — *measured_by*
  - [Learning to Search from Demonstration Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdf80d651420b47da80f789f2631b1b5-Paper-Conference.pdf)
- **MATH-500** (measurements) — *measured_by*
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **OlympiadBench** (measurements) — *measured_by*
  - [Pixel-Level Reasoning Segmentation via Multi-turn Conversations](https://aclanthology.org/2025.acl-long.865.pdf)
- **Decision-making** (constructs) — *causes*
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
- **Time series forecasting** (behaviors tasks) — *causes*
  - [Time-LLM: Time Series Forecasting by Reprogramming Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/680b2a8135b9c71278a09cafb605869e-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
- **OpenLLM Leaderboard** (measurements) — *measured_by*
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
- **Collaboration** (behaviors tasks) — *causes*
  - [Chat-Driven Text Generation and Interaction for Person Retrieval](https://aclanthology.org/2025.emnlp-main.267.pdf)
- **TabMWP** (measurements) — *measured_by*
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Linear probing** (measurements) — *measured_by*
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
- **GTA** (measurements) — *measured_by*
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **QuAC** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Agi-Eval** (measurements) — *measured_by*
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
- **MGSM** (measurements) — *measured_by*
  - [AFRIDOC-MT: Document-levelMTCorpus forAfrican Languages](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **Attribute generation** (behaviors tasks) — *causes*
  - [GAMap: Zero-Shot Object Goal Navigation with Multi-Scale Geometric-Affordance Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/459d93dad139eb084c365d40a57eada3-Paper-Conference.pdf)
- **MM-Vet** (measurements) — *measured_by*
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **MMStar** (measurements) — *measured_by*
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Last letter concatenation** (measurements) — *measured_by*
  - [Efficient Contextual LLM Cascades through Budget-Constrained Policy Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a6deba3b2408af45b3f9994c2152b862-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
- **SEED-Bench** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RealWorldQA** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Retraining-free Merging of Sparse MoE via Hierarchical Clustering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25aq/chen25aq.pdf)
- **TheoremQA** (measurements) — *measured_by*
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [Are Large Language Models Ready for Multi-Turn Tabular Data Analysis?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aj/li25aj.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
- **GSM-Hard** (measurements) — *measured_by*
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
- **LiveBench** (measurements) — *measured_by*
  - [PicPersona-TOD: A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.404.pdf)
- **VisualWebArena** (measurements) — *measured_by*
  - [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3b893ba1de12f76020b03f7ae8e1afd-Paper-Conference.pdf)
- **XCOPA** (measurements) — *measured_by*
  - [PSET: a Phonetics-Semantics Evaluation Testbed](https://aclanthology.org/2025.emnlp-main.374.pdf)
- **MMAU** (measurements) — *measured_by*
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Video understanding** (constructs) — *causes*
  - [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by ModellingMiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Strategy generation** (behaviors tasks) — *causes*
  - [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.189.pdf)
- **ToolBench** (measurements) — *measured_by*
  - [Multilingual Reasoning via Self-training](https://aclanthology.org/2025.naacl-long.578.pdf)
- **Claim verification** (behaviors tasks) — *causes*
  - [B4: A Black-Box Scrubbing Attack onLLMWatermarks](https://aclanthology.org/2025.naacl-long.461.pdf)
- **Legal compliance** (constructs) — *causes*
  - [From Real to Synthetic: Synthesizing Millions of Diversified and Complicated User Instructions with Attributed Grounding](https://aclanthology.org/2025.acl-long.518.pdf)
- **AIME** (measurements) — *measured_by*
  - [Data Whisperer: Efficient Data Selection for Task-SpecificLLMFine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1136.pdf)
- **ReDial** (measurements) — *measured_by*
  - [Efficiently Identifying Watermarked Segments in Mixed-Source Texts](https://aclanthology.org/2025.acl-long.317.pdf)
- **MMLU-redux** (measurements) — *measured_by*
  - [Representation Shattering in Transformers: A Synthetic Study with Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nishi25a/nishi25a.pdf)
- **MixEval** (measurements) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **MixEval-hard** (measurements) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **GaoKao 2023 En** (measurements) — *measured_by*
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **Minerva Math** (measurements) — *measured_by*
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [Deliberation in Latent Space via Differentiable Cache Augmentation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bc/liu25bc.pdf)
- **T-Eval** (measurements) — *measured_by*
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **NLGraph** (measurements) — *measured_by*
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
- **SciBench** (measurements) — *measured_by*
  - [Fleet of Agents: Coordinated Problem Solving with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/klein25a/klein25a.pdf)
- **BANKING77** (measurements) — *measured_by*
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **CLINC150** (measurements) — *measured_by*
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **SST-5** (measurements) — *measured_by*
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Mystery Blocksworld** (measurements) — *measured_by*
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)
- **PricingLogic** (measurements) — *measured_by*
  - [2025.emnlp-main.393.checklist](https://aclanthology.org/attachments/2025.emnlp-main.393.checklist.pdf)
- **MMVet** (measurements) — *measured_by*
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **InfiniBench** (measurements) — *measured_by*
  - [3DS: Medical Domain Adaptation ofLLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.984.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  - [CanLLMs Extract Frame-Semantic Arguments?](https://aclanthology.org/2025.emnlp-main.1558.pdf)

### → Reasoning
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks) — *causes*
  - [BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf)
- **Abstraction** (constructs) — *causes*
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
- **Inductive bias** (constructs) — *causes*
  - [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *causes*
  - [Pixel-Level Reasoning Segmentation via Multi-turn Conversations](https://aclanthology.org/2025.acl-long.865.pdf)
- **Image captioning** (behaviors tasks) — *causes*
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *causes*
  - [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf)
- **Knowledge acquisition** (constructs) — *causes*
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **Prompt engineering** (behaviors tasks) — *causes*
  - [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Seeking Neural Nuggets: Knowledge Transfer in Large Language Models from a Parametric Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d6dc5c9ad19816d745535d352dc4295-Paper-Conference.pdf)
- **Planning** (constructs)
  - [Automated Design of Agentic Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/36b7acf6f6010652b3f2a433774a66fe-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  - [Unveiling Causal Reasoning in Large Language Models: Reality or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/af2bb2b2280d36f8842e440b4e275152-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs)
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **In-context learning** (constructs)
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)
- **Complex reasoning** (behaviors tasks)
  - [MMIE: Massive Multimodal Interleaved Comprehension Benchmark for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4072543747a14bbed76284cf2c04b9e9-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [Autonomous Agents for Collaborative Task under Information Asymmetry](https://proceedings.neurips.cc/paper_files/paper/2024/file/0534abc9e6db91683d82186ef0d68202-Paper-Conference.pdf)
- **Visual grounding** (constructs)
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks)
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **Information retrieval** (behaviors tasks)
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Perception** (constructs)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Critique** (behaviors tasks)
  - [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks)
  - [MindSearch: Mimicking Human Minds Elicits Deep AI Searcher](https://proceedings.iclr.cc/paper_files/paper/2025/file/e01c431bbb83153632c0dcfaf8ccda0a-Paper-Conference.pdf)
- **Question answering** (behaviors tasks)
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Decision-making** (constructs)
  - [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/29f421fbdcc82aeb349d784d3aaccdb3-Paper-Conference.pdf)
- **Abstraction** (constructs)
  - [Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks)
  - [Beemo: Benchmark of Expert-edited Machine-generated Outputs](https://aclanthology.org/2025.naacl-long.358.pdf)
- **Causal reasoning** (constructs)
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **SAFE** (measurements)
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Commonsense understanding** (constructs)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Faithfulness** (constructs)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Sequential decision-making** (constructs)
  - [AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8efbb5dd415974eb095c3f06bff1f48-Paper-Conference.pdf)
- **Perception Test** (measurements)
  - [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf)
- **Knowledge-based question answering** (behaviors tasks)
  - [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf)
- **Counterfactual reasoning** (constructs)
  - [Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)
- **Knowledge recall** (behaviors tasks)
  - [Unveiling the Magic of Code Reasoning through Hypothesis Decomposition and Amendment](https://proceedings.iclr.cc/paper_files/paper/2025/file/eeffa70bcbbd43f6bd067edebc6595e8-Paper-Conference.pdf)
- **Contextual understanding** (constructs)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Flawed reasoning** (behaviors tasks)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Length generalization** (constructs)
  - [Generalizing Reasoning Problems to Longer Lengths](https://proceedings.iclr.cc/paper_files/paper/2025/file/abcbdf504b621b4d1213aa7a5c489f8a-Paper-Conference.pdf)
- **Sentiment analysis** (behaviors tasks)
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **General capabilities** (constructs)
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Task execution** (constructs)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
- **Action execution** (behaviors tasks)
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Long-context processing** (constructs)
  - [Beyond Logits: Aligning Feature Dynamics for Effective Knowledge Distillation](https://aclanthology.org/2025.acl-long.1126.pdf)
- **Abstract reasoning** (constructs)
  > abstract reasoning involves two core processes: abstraction, the extraction of common features from concrete entities (Murphy, 2004), and reasoning, the derivation of new knowledge from existing information (Holyoak & Morrison, 2012).
  - [Benchmarking Abstract and Reasoning Abilities Through A Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25u/ma25u.pdf)
- **Social intelligence** (constructs)
  - [Chat-Driven Text Generation and Interaction for Person Retrieval](https://aclanthology.org/2025.emnlp-main.267.pdf)
- **Data contamination** (constructs)
  - [The discordance between embedded ethics and cultural inference in large language models](https://aclanthology.org/2025.emnlp-main.744.pdf)
- **Confidence estimation** (constructs)
  - [E](https://aclanthology.org/2025.acl-long.417.pdf)
- **Reasoning faithfulness** (constructs)
  - [DSCD: Large Language Model Detoxification with Self-Constrained Decoding](https://aclanthology.org/2025.emnlp-main.198.pdf)

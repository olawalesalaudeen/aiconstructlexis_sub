# Commonsense knowledge
**Type:** Construct  
**Referenced in:** 957 papers  
**Also known as:** Common sense, Common-sense knowledge, Commonsense, Numeric common sense, Common sense knowledge, General knowledge, Real-world knowledge grounding, Common knowledge, Background knowledge, Knowledge ability, Knowledge capacity, Latent world model, Mathematical world-model, Abstract meta-knowledge, World model, World understanding, Reasoning ability, Reasoning capability, Inference ability, Reasoning capacity, Inferential capabilities, Inferences, General inference capability, Reasoning capabilities, Reasoning skills, Fluid intelligence, Formal inference, Negation robustness, Sub-task decomposition, Inference capability, Inferential ability, Concept inference, Contextual meaning inference, Keyword organization inference, Latent variable inference, Task inference, Deep thinking, Hierarchical thinking, Latent thinking, Strategic thinking, Thinking, Compositional condition understanding, Cross-file dependency understanding, Document-level understanding, Intentionality understanding, Note comprehension, Problem comprehension, Region-level comprehension, Relationship comprehension, Response understanding, Schema understanding, Screen understanding, Semantic corruption understanding, Comprehension, Understanding ability, Unnatural language comprehension, Constraint adherence, Instruction adherence, Structural conformity, General instruction following, Instruction-following ability, Instruction-following capability, Open-ended instruction following, Prompt following, Constrained generation, Complex instruction understanding, Symbolic computing, Symbol processing, Reasoning performance, Causal world model  

## State of the Field

Across the surveyed literature, commonsense knowledge is most commonly defined as the implicit, pre-existing world knowledge embedded in a model from its training, which is required for reasoning about complex situations. A smaller line of work frames it more structurally as an internal or latent "world model" representing environmental dynamics and causal principles. This construct is operationalized through model performance on a wide array of benchmarks. The most frequent forms of measurement assess mathematical reasoning (e.g., GSM8k, MATH), general and expert knowledge (e.g., MMLU, BBH), and open-ended instruction following (e.g., MT-Bench, AlpacaEval). Several papers posit that commonsense knowledge influences a model's ability to perform high-level tasks such as planning, decision-making, and generalization. Conversely, this knowledge is reported to be enhanced by techniques like chain-of-thought reasoning and alignment with human preferences. As one study notes, the prevailing view is that "LLMs trained on large-scale data encode commonsense knowledge about the real-world" (Tree-Planner), which is then leveraged for various downstream capabilities.

## Sources

**[Building Cooperative Embodied Agents Modularly with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/54b8b4e0b4ba4aad112e84f32e3b5dbb-Paper-Conference.pdf)**
> The implicit knowledge about the world required to reason about complex and contextualized situations.

**[Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf) (as "Commonsense")**
> The model's ability to understand and make judgments about everyday situations and concepts that are typically taken for granted by humans.

**[MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf) (as "Numeric common sense")**
> The ability to apply intuitive understanding of quantities, magnitudes, and numerical relationships in everyday contexts.

**[DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf) (as "Common-sense knowledge")**
> The pre-existing, general world knowledge embedded within the LLM that can be applied to understand and make rational decisions in driving scenarios.

**[Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/a8de97fa77a09258b22880c230a83445-Paper-Conference.pdf) (as "Common sense")**
> The latent ability of a model to understand and reason about situations in a way that aligns with general human knowledge and intuition.

**[Architect: Generating Vivid and Interactive 3D Scenes with Hierarchical 2D Inpainting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (as "Common sense knowledge")**
> The latent knowledge a model possesses about the typical properties, functions, and relationships of objects and concepts in the everyday world, used here to adjudicate object scales.

**[Democratizing Fine-grained Visual Recognition with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/49299a8afda8053932a4cfd62fdfd1b9-Paper-Conference.pdf) (as "World knowledge")**
> The body of general factual information about the world that a model has internalized from its training data.

**[Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf) (as "General knowledge")**
> The broad base of factual and conceptual information acquired by a model during pre-training, which can be applied to downstream tasks.

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf) (as "Real-world knowledge grounding")**
> The ability to connect multimodal inputs with factual, external knowledge about the world, enabling accurate and contextually relevant responses.

**[Secret Collusion among AI Agents: Multi-Agent Deception via Steganography](https://proceedings.neurips.cc/paper_files/paper/2024/file/861f7dad098aec1c3560fb7add468d41-Paper-Conference.pdf) (as "Common knowledge")**
> A form of group knowledge where all agents know a fact, know that all other agents know the fact, and so on ad infinitum, which is a prerequisite for certain types of coordination.

**[Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf) (as "Background knowledge")**
> The latent store of general world knowledge and scientific intuition acquired during pre-training that the model can apply to new tasks.

**[Make-it-Real: Unleashing Large Multimodal Model for Painting 3D Objects with Realistic Materials](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf) (as "Prior knowledge")**
> The vast repository of general world knowledge, including facts about objects, their typical materials, and physical properties, that the model possesses from its training.

**[VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Knowledge")**
> The latent ability to recall facts or information contained in the model that cannot be found directly in the input.

**[LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Knowledge ability")**
> The extent to which a large language model has acquired and can recall factual information about the world.

**[PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Knowledge capacity")**
> The ability of a model to retrieve and utilize acquired knowledge to solve professional problems.

**[Monitoring Latent World States in Language Models with Propositional Probes](https://proceedings.iclr.cc/paper_files/paper/2025/file/3132d0405fabe24b2a7b6cd7ba9de6b5-Paper-Conference.pdf) (as "Latent world model")**
> An internal, structured representation of the entities and relationships described in an input context, which the language model is hypothesized to construct and maintain in its activations.

**[MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf) (as "World modeling")**
> The latent ability to understand and reason about the underlying principles, dynamics, and causalities of the real world.

**[Can Transformers Do Enumerative Geometry?](https://proceedings.iclr.cc/paper_files/paper/2025/file/aee2f03ecb2b2c1ea55a43946b651cfd-Paper-Conference.pdf) (as "Mathematical world-model")**
> An internalized, coherent understanding of mathematical concepts, relationships, and structures that goes beyond surface-level pattern matching.

**[Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf) (as "Abstract meta-knowledge")**
> High-level problem-solving knowledge that abstracts away from task-specific details and can transfer across similar problems.

**[Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf) (as "World model")**
> An internal, learned representation of an environment that allows an agent to predict the outcomes of its actions without actually executing them.

**[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf) (as "World understanding")**
> The degree to which a model possesses an internal, coherent representation of concepts and their relationships in the world, beyond surface-level linguistic patterns.

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf) (as "Reasoning")**
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

**[A Causal World Model Underlying Next Token Prediction: Exploring GPT in a Controlled Environment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yehezkel-rohekar25a/yehezkel-rohekar25a.pdf) (as "Causal world model")**
> A latent structural representation of cause-effect relationships among tokens in a sequence, which the model uses to generate outputs consistent with domain rules, even in out-of-distribution settings.

## Relationships

### Commonsense knowledge →
- **MMLU** (measurements) — *measured_by*
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6091f2bb355e960600f62566ac0e2862-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  - [3-in-1: 2D Rotary Adaptation for Efficient Finetuning, Efficient Batching and Composability](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dbcadb7beedc2afe32bb23f75dd30ec-Paper-Conference.pdf)
- **IFEval** (measurements) — *measured_by*
  - [Do LLMs estimate uncertainty well in instruction-following?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC** (measurements) — *measured_by*
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **CMMLU** (measurements) — *measured_by*
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Vicuna-Bench** (measurements) — *measured_by*
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
- **MATH-500** (measurements) — *measured_by*
  - [UnCo: Uncertainty-Driven Collaborative Framework of Large and Small Models for Grounded MultimodalNER](https://aclanthology.org/2025.emnlp-main.389.pdf)
- **AlpacaEval 2** (measurements) — *measured_by*
  - [Harnessing and Evaluating the Intrinsic Extrapolation Ability of Large Language Models for Vehicle Trajectory Prediction](https://aclanthology.org/2025.naacl-long.224.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **Decision-making** (constructs) — *causes*
  - [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/93c936b9e492def9c00782cab79dbc6d-Paper-Conference.pdf)
- **WebQSP** (measurements) — *measured_by*
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)
- **CWQ** (measurements) — *measured_by*
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.585.pdf)
- **MBPP** (measurements) — *measured_by*
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.585.pdf)
- **BIG-Bench Hard** (measurements) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **InfoSeek** (measurements) — *measured_by*
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf)
- **LogiQA** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  - [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **QNLI** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MNLI** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WikiText-2** (measurements) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Query rewriting** (behaviors tasks) — *causes*
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  - [Mutual Reasoning Makes Smaller LLMs Stronger Problem-Solver](https://proceedings.iclr.cc/paper_files/paper/2025/file/35514d533cdc278a7780daf0dbe7d0b7-Paper-Conference.pdf)
- **RACE** (measurements) — *measured_by*
  - [How Humans andLLMs Organize Conceptual Knowledge: Exploring Subordinate Categories inItalian](https://aclanthology.org/2025.acl-long.225.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.585.pdf)
- **JudgeBench** (measurements) — *measured_by*
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Should VLMs be Pre-trained with Image Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/34a5f638617ce32700e235e50dff9c8a-Paper-Conference.pdf)
- **Programming** (behaviors tasks) — *causes*
  - [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/file/39af4f2f9399122a14ccf95e2d2e7122-Paper-Conference.pdf)
- **Reliability** (constructs) — *causes*
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **Portability** (constructs) — *causes*
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **GenEval** (measurements) — *measured_by*
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1453.pdf)
- **MMLU-redux** (measurements) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **CruxEval** (measurements) — *measured_by*
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **ShareGPT** (measurements) — *measured_by*
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
- **AlpacaFarm** (measurements) — *measured_by*
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
- **CoQA** (measurements) — *measured_by*
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
- **ScienceWorld** (measurements) — *measured_by*
  - [FLEURS-ASL: IncludingAmericanSignLanguage in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.315.pdf)
- **WildBench** (measurements) — *measured_by*
  - [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  - [In-Context Learning Boosts Speech Recognition via Human-like Adaptation to Speakers and Language Varieties](https://aclanthology.org/2025.emnlp-main.220.pdf)
- **AIME 2024** (measurements) — *measured_by*
  - [In-Context Learning Boosts Speech Recognition via Human-like Adaptation to Speakers and Language Varieties](https://aclanthology.org/2025.emnlp-main.220.pdf)
- **AGIEval-Math** (measurements) — *measured_by*
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1453.pdf)

### → Commonsense knowledge
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Training Nonlinear Transformers for Chain-of-Thought Inference:  A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [BeyondWER: Probing Whisper’s Sub‐token Decoder Across Diverse Language Resource Levels](https://aclanthology.org/2025.emnlp-main.1592.pdf)
- **Representation learning** (constructs) — *causes*
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)

### Associated with
- **Catastrophic forgetting** (behaviors tasks)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
- **Planning** (constructs)
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **Factuality** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Commonsense understanding** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [How Private are Language Models in Abstractive Summarization?](https://aclanthology.org/2025.emnlp-main.1532.pdf)
- **Commonsense reasoning** (constructs)
  - [How Private are Language Models in Abstractive Summarization?](https://aclanthology.org/2025.emnlp-main.1532.pdf)
- **Reading comprehension** (constructs)
  - [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf)
- **Instruction following** (constructs)
  - [Discourse-Driven Evaluation: Unveiling Factual Inconsistency in Long Document Summarization](https://aclanthology.org/2025.naacl-long.104.pdf)
- **Logical reasoning** (constructs)
  - [K-Level Reasoning: Establishing Higher Order Beliefs in Large Language Models for Strategic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf)
- **Natural language inference** (behaviors tasks)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)
- **Generalization** (constructs)
  - [Constrained Human-AI Cooperation: An Inclusive Embodied Social Intelligence Challenge](https://proceedings.neurips.cc/paper_files/paper/2024/file/4eb8e997fc91086225b7484cf8eac341-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Information extraction** (behaviors tasks)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Situational awareness** (constructs)
  - [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/7537726385a4a6f94321e3adf8bd827e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Model selection** (constructs)
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)
- **Theorem proving** (behaviors tasks)
  - [Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf)
- **Alignment tax** (constructs)
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks)
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
- **Tool use** (behaviors tasks)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
- **General capabilities** (constructs)
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Expressive power** (constructs)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Strategic planning** (constructs)
  - [Palm: A Culturally Inclusive and Linguistically Diverse Dataset forArabicLLMs](https://aclanthology.org/2025.acl-long.1580.pdf)
- **Abstract reasoning** (constructs)
  - [Reasoning Limitations of Multimodal Large Language Models. A case study of Bongard Problems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/malkinski25a/malkinski25a.pdf)
- **Formal theorem proving** (behaviors tasks)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)

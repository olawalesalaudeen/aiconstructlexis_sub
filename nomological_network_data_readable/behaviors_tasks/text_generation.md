# Text generation
**Type:** Behavior  
**Referenced in:** 1074 papers  
**Also known as:** Response generation, Open-ended generation, Writing, Natural language generation, Completion generation, Sonnet writing, Free-form response generation, Language generation, Ancient prose writing, Poetry writing, Ci writing, Qu writing, Couplet writing, Long-form answer generation, Long-form response generation, Sequence generation, Single-turn dialogue generation, Content creation, Story continuation, Question Answering, Autoregressive generation, Instruction response generation, Long-form generation, Human-like conversation, Conversation, General chat, Multi-turn conversation, Multi-turn communication, Multi-turn conversation generation, Multi-turn chat, Interactive communication, Single-turn dialogue, Cross-cultural dialogue generation, Repo-level code generation, Code infilling, Python code generation, Multilingual code generation, Data science code completion, Function-level code generation, Class-level code generation, Data science programming, Text-to-code generation, Verbose generation, Controllable generation, Long-sequence generation, Conversational interaction, Multi-round dialogue, Knowledge-intensive question answering, Multi-choice question answering, Sub-question answering, Fill in the blank, Last word completion, Open-ended conversation, Text creation, Audio-to-text generation, Content generation, Movie review generation, Text-to-text generation, Video-to-text generation, Multi-turn dialogue understanding, Continuation writing, Diary writing, Content analysis, Cloze completion, Context completion, Fill-in-the-middle code completion, Multi-round conversation, Single-turn conversation, Book review generation, Dialogue response generation, Draft generation, Free generation, Open-domain dialogue generation, Token generation, Conversation simulation, Blog post writing, Email writing, Poem writing, Composite question answering, Counterfactual question answering, Knowledge question answering, Verilog code completion, Culture-conditioned generation, Data description generation, LaTeX document generation, Narrative generation, Poem generation, Slogan generation, State description generation, Twitter post generation, Open-ended interaction, Generative language modeling, Surface realization, Inference steering, Storytelling, Email completion, Analysis generation, Chat response generation, Constant Response Generation, Humor generation, Next-token generation, Table-to-text generation, Open-ended reasoning, Sentence completion reasoning, Argumentative writing, Cover letter writing, Data-to-text writing, Expository writing, Legal Document Writing, Story writing, Poetry composition, Extended conversation, Speech drafting, Fictitious knowledge generation, Meal description generation, Code prediction, Codon prediction, Multigram prediction, Next device pin prediction, Novel writing, Complex question answering, Single-hop question answering, Academic question answering, Benchmark Question Answering, Binary question answering, Multiple-choice answering, Questionnaire answering, Long-form Narrative Generation, Long structured output generation, Research paper generation, Document-level generation, Long-text Generation, Arbitrary-length sequence generation, Unconditional generation, Story generation, Visual conversation, Visual chatting, Image dialogue, Multi-image dialogue, Conversational VQA, Multimodal chat, Multi-turn visual conversation, Visual chat, Document creation, Cognitive reappraisal generation, Concept-conditioned generation, Creative story generation, Development document generation, Editing instruction generation, High-level justification generation, Interdisciplinary research generation, Random word generation, Token string generation, Verbal response generation, Watermark description generation, Paper writing, Review writing, Guided generation, Humorous response generation, Short answer generation, Token-by-token generation, Story completion, Argument composition, Creative composition, Advice generation, Cover letter generation, Culturally appropriate response generation, Reference letter generation, Title generation, Video scriptwriting, Academic writing, Professional writing, Final response generation, Free-text response generation, Model generation, Natural language response generation, Open-ended response generation, Utterance generation, Completion, Bidirectional text continuation, Free-text generation, Sentence generation, Human-content continuation, Essay generation, Smart reply generation, Generation, Free-form text completion, Extractive question answering, Free-form text generation, Free-form Text Generation, Open-ended text generation, Unconditional text generation  

## State of the Field

Across the surveyed literature, text generation is most broadly defined as the production of coherent and contextually appropriate text sequences in response to input prompts. This behavior is described under numerous specific labels, including "response generation," "natural language generation," and "autoregressive generation," which highlight its application in conversational settings, its general scope, and its underlying token-by-token production mechanism. The field recognizes a wide array of specialized forms, ranging from creative tasks like "story continuation" and "poetry writing" to technical outputs such as "code generation" and "data-to-text generation." The field operationalizes and measures this behavior through a diverse suite of benchmarks. Factual knowledge and reasoning are commonly assessed using multiple-choice question answering datasets like MMLU, ARC, and TruthfulQA. Language modeling quality is frequently evaluated via perplexity on corpora such as WikiText-2 and C4, while commonsense is often tested with sentence completion tasks like HellaSwag. For open-ended and conversational generation, where a single ground truth is absent, evaluation commonly relies on LLM-as-a-judge frameworks using benchmarks like MT-Bench and AlpacaEval 2.0. Specialized capabilities are measured with dedicated instruments, such as HumanEval for code and LongBench for long-context performance.

## Sources

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)**
> Producing coherent and contextually appropriate text sequences in response to input prompts, including both open-ended and constrained generation.

**[Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf) (as "Response generation")**
> Producing a natural-language answer or continuation to a user prompt in an assistant setting.

**[Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf) (as "Open-ended generation")**
> Producing free-form text responses to prompts or questions without choosing from fixed answer options.

**[LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf) (as "Writing")**
> The observable task of generating coherent text content, categorized within MT-Bench.

**[Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf) (as "Natural language generation")**
> The general task of producing free-form text in a human language.

**[A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf) (as "Completion generation")**
> Producing a sequence of tokens as a response to an input dialogue history or instruction.

**[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf) (as "Sonnet writing")**
> Generating a poem following a strict rhyme scheme and incorporating specific provided words.

**[LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf) (as "Creative writing")**
> The task of generating imaginative or expressive text, such as a narrative or description, based on a multimodal prompt like an audio clip.

**[MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Free-form response generation")**
> The observable behavior of generating open-ended, natural language answers to questions, as opposed to selecting from a fixed set of options or producing a single word.

**[BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc808cf2d2444b0abcceca366b771389-Paper-Conference.pdf) (as "Text completion")**
> Generating the remainder of a text from a provided prefix, optionally conditioned on additional guidance.

**[Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf) (as "Language generation")**
> The task of producing a sequence of tokens, such as a sentence or paragraph, in response to an input prompt.

**[Ensemble Learning for Heterogeneous Large Language Models with Deep Parallel Collaboration](https://proceedings.neurips.cc/paper_files/paper/2024/file/d8a6eb79f8ccaacbe7198a5caf3a0323-Paper-Conference.pdf) (as "Free-form generation")**
> The task of generating an unconstrained natural language response to a prompt or question.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Ancient prose writing")**
> Composing original prose in classical Chinese in response to a prompt or scenario.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Poetry writing")**
> Composing an ancient-style poem based on a specified theme and form.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Ci writing")**
> Composing a ci poem according to a specified theme and tune pattern.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Qu writing")**
> Composing a qu poem according to a specified theme and tune pattern.

**[WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Couplet writing")**
> Composing a complete couplet for a specified theme or occasion.

**[RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Long-form answer generation")**
> The task of generating comprehensive, detailed answers to questions, rather than short, extractive responses.

**[Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf) (as "Long-form response generation")**
> The task of generating multi-paragraph, detailed textual answers in response to open-ended prompts.

**[Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf) (as "Sequence generation")**
> The observable behavior of producing a complete sequence of tokens, such as a sentence or paragraph, in an autoregressive manner.

**[BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf) (as "Single-turn dialogue generation")**
> The task of generating a single, coherent, and relevant response to a user's prompt in a conversational context.

**[Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf) (as "Answer generation")**
> The final step of producing a textual answer based on the initial question and any provided internal or external information.

**[Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf) (as "Content creation")**
> Generating creative or original written content such as stories or other authored text.

**[On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf) (as "Story continuation")**
> Generating the next words of a story from a short story beginning so that the output extends the narrative.

**[Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf) (as "Question Answering")**
> The model providing answers to questions across various subjects as part of knowledge benchmarks.

**[MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf) (as "Autoregressive generation")**
> The process of generating text token by token, where each new token is predicted based on the sequence of previously generated tokens.

**[DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf) (as "Instruction response generation")**
> Generating responses to user instructions or prompts in an instruction-tuned dialogue setting.

**[Cascade Speculative Drafting for Even Faster LLM Inference](https://proceedings.neurips.cc/paper_files/paper/2024/file/9cb5b083ba4f5ca6bd05dd307a2fb354-Paper-Conference.pdf) (as "Long-form generation")**
> The task of producing extended sequences of text, which poses significant latency challenges for autoregressive models.

**[WhodunitBench: Evaluating Large Multimodal Agents via Murder Mystery Games](https://proceedings.neurips.cc/paper_files/paper/2024/file/9dd4533e7e4e5ed809344280609c5b05-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Dialogue generation")**
> The generation of conversational text as part of an interaction with other agents or the environment.

**[LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf) (as "Human-like conversation")**
> Engaging in open-ended dialogue that mimics the patterns, coherence, and interactivity of human conversation.

**[PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf) (as "Conversational response generation")**
> The observable task of producing a relevant and coherent response in a multi-turn dialogue context.

**[Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf) (as "Conversation")**
> The task of engaging in multi-turn dialogue or responding to queries.

**[CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf) (as "General chat")**
> The task of engaging in open-domain, multi-turn conversation with a user.

**[MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multi-turn conversation")**
> Engaging in a dialogue that consists of multiple back-and-forth exchanges between a user and the model.

**[Autonomous Agents for Collaborative Task under Information Asymmetry](https://proceedings.neurips.cc/paper_files/paper/2024/file/0534abc9e6db91683d82186ef0d68202-Paper-Conference.pdf) (as "Multi-turn communication")**
> Exchanging utterances over multiple turns to progressively resolve a task.

**[Empowering and Assessing the Utility of Large Language Models in Crop Science](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e5783c673cf05cfd4b3ebf46e96abfc-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multi-turn dialogue")**
> Engaging in a conversational exchange that spans multiple turns, where the model acts as an assistant to a user to collaboratively achieve a goal.

**[LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf) (as "Multi-turn conversation generation")**
> Producing sequential responses in a dialogue format regarding molecular data and instructions.

**[SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf) (as "Multi-turn chat")**
> Engaging in a conversation with a user over multiple sequential exchanges of input and output.

**[Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf) (as "Interactive communication")**
> Engaging in a multi-turn dialogue with a user to exchange information or complete a task.

**[Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf) (as "Single-turn dialogue")**
> Responding to a single user prompt or question in a self-contained manner without prior conversational context.

**[CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf) (as "Cross-cultural dialogue generation")**
> Producing multi-turn conversations between culturally distinct agents about an initial question or topic.

**[Multi-turn Reinforcement Learning with Preference Human Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/d77a7b289361abff82bdd2fb537ae152-Paper-Conference.pdf) (as "Multi-turn dialogue generation")**
> Engaging in a sequence of conversational exchanges with an external environment or user, where the history of the interaction influences subsequent responses.

**[Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf) (as "Code generation")**
> The task of writing executable code in a programming language to solve a given problem.

**[RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf) (as "Code completion")**
> The task of completing a programming problem given a function signature and docstring.

**[EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Repo-level code generation")**
> Generating code for a target function given a natural language requirement and repository context, simulating real-world developer coding processes.

**[EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Code infilling")**
> Generating code in the middle of a file given code contexts both above and below the target function location.

**[AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf) (as "Python code generation")**
> Producing Python code solutions for programming prompts, often from function definitions or natural-language problem statements.

**[AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf) (as "Multilingual code generation")**
> The task of generating functionally correct code in various programming languages, such as Python, C++, Java, JavaScript, and Go.

**[AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf) (as "Data science code completion")**
> The task of completing code snippets that use popular data science libraries like Pandas, NumPy, and PyTorch.

**[SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf) (as "Function-level code generation")**
> The task of generating a complete, self-contained function based on a natural language description of its purpose and behavior.

**[SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf) (as "Class-level code generation")**
> The task of generating the implementation of a class and its methods, given a code skeleton containing class- and method-level information.

**[SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf) (as "Data science programming")**
> The task of completing a partial code snippet to solve a data science problem, often involving specific libraries and data manipulation techniques.

**[Reranking Laws for Language Generation: A Communication-Theoretic Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/c8b2f897e45770595656a79a9ad91e89-Paper-Conference.pdf) (as "Text-to-code generation")**
> The task of generating executable source code from a natural language description or prompt.

**[ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf) (as "Question answering")**
> Answering questions in benchmark formats such as yes/no questions and reading-comprehension questions.

**[Humor in AI: Massive Scale Crowd-Sourced Preferences and Benchmarks for Cartoon Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e297fb6cd1690ee5b39c5bb4c58ad801-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Verbose generation")**
> An observable pattern where the model produces outputs that are longer or more wordy than necessary or desired.

**[Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf) (as "Controllable generation")**
> Generating images that align with a text prompt and additional control signals such as edges, landmarks, or segmentation maps.

**[MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf) (as "Long-sequence generation")**
> The task of generating coherent and relevant text over an extended context, often requiring the model to maintain consistency and track information over thousands of tokens.

**[G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf) (as "Conversational interaction")**
> Engaging in a multi-turn dialogue with a user to answer questions about a graph, often referred to as 'chatting with the graph'.

**[Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf) (as "Multi-round dialogue")**
> Engaging in a sequence of conversational turns with a user, maintaining context across multiple rounds of interaction.

**[Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf) (as "Multiple-choice question answering")**
> Selecting the correct answer option from a set of candidates given a question or prompt.

**[Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/03560f68b1238221e7c07ad01c4b47aa-Paper-Conference.pdf) (as "Content generation")**
> The observable task of producing new text based on a given prompt or context.

**[From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf) (as "Multi-turn dialogue understanding")**
> Processing and responding to conversational exchanges that span multiple interaction rounds with information retrieval from prior dialogue.

**[From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf) (as "Multi-hop question answering")**
> Answering questions that require integrating information from multiple distinct sources or documents.

**[SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf) (as "Data-to-text generation")**
> The task of converting structured data, such as tables or knowledge graphs, into natural language text.

**[CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding & Reasoning Capabilities of CodeLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/078b4435f5b61a092025fec713084008-Paper-Conference.pdf) (as "Fill in the blank")**
> The task of completing missing parts of a code snippet given documentation and context.

**[Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf) (as "Text creation")**
> The task of generating creative text, such as writing poetry or crafting headlines.

**[Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf) (as "Movie review generation")**
> The specific task of generating text that constitutes a movie review, often with a specified sentiment.

**[Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf) (as "Knowledge-intensive question answering")**
> The task of answering questions that require recalling and synthesizing specific factual information, such as details about a historical figure.

**[Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf) (as "Last word completion")**
> The observable task of predicting the final word of a text passage, which often requires understanding long-range context.

**[LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf) (as "Multi-choice question answering")**
> The observable task of selecting the correct answer from a given set of options in response to a question.

**[LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf) (as "Diary writing")**
> The specific task of generating a sequence of dated entries that describe events over a period of time.

**[A Statistical Framework for Ranking LLM-based Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a4cd257678d986ba545b5d1aa9b5923-Paper-Conference.pdf) (as "Open-ended conversation")**
> Engaging in unconstrained, real-world dialogue with human users, which is characteristic of chatbot applications.

**[Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf) (as "Biography generation")**
> The open-ended task of generating a biographical text about a specific named individual.

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf) (as "Continuation writing")**
> The behavior of completing a partial, incomplete SQL query to form a complete and valid query that answers a given question.

**[CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf) (as "Sub-question answering")**
> The task of answering a series of simpler, intermediate questions that break down a complex multi-hop question into manageable steps.

**[LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/27e5626cabdbb6cd5c56ce4114ff93e4-Paper-Conference.pdf) (as "Text-to-text generation")**
> The task of generating a textual output based on a textual input, encompassing various NLP tasks in a unified format.

**[MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf) (as "Image-to-text generation")**
> The observable task of generating a relevant and coherent textual response based on a given image and an optional text prompt.

**[MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf) (as "Video-to-text generation")**
> The observable task of generating a relevant and coherent textual response based on a given video and an optional text prompt.

**[MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf) (as "Audio-to-text generation")**
> The observable task of generating a relevant and coherent textual response based on a given audio clip and an optional text prompt.

**[Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf) (as "Draft generation")**
> Producing candidate answers from a subset of retrieved documents before verification.

**[Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf) (as "Conversation simulation")**
> The act of generating plausible future turns of a conversation to evaluate the potential outcomes of different responses.

**[Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf) (as "Dialogue response generation")**
> Generating an answer to a conversational prompt in a dialogue setting.

**[Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf) (as "Email writing")**
> The observable task of generating the text for an email based on a given prompt or scenario.

**[Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf) (as "Blog post writing")**
> The observable task of generating text in the style and format of a blog post.

**[CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf) (as "Text continuation")**
> Generating the continuation of a given context, evaluating the model's ability to generate coherent text without introducing bias.

**[GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf) (as "Multi-round conversation")**
> Engaging in a sequential, multi-turn dialogue about a GUI, where the model's responses must account for the conversational history.

**[SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget](https://proceedings.iclr.cc/paper_files/paper/2025/file/3b0a8df568ec496a717566a7f8158aaa-Paper-Conference.pdf) (as "Token generation")**
> The observable process of producing output tokens sequentially during the decoding phase of inference.

**[Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf) (as "Multi-turn interaction")**
> The observable process of a model engaging in a sequence of exchanges with an environment or critique to refine its solution to a problem.

**[ClimaQA: An Automated Evaluation Framework for Climate Question Answering Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3eff068e195daace49955348de9f8398-Paper-Conference.pdf) (as "Cloze completion")**
> Filling in a missing scientific term in a sentence or phrase using the surrounding context.

**[Is In-Context Learning Sufficient for Instruction Following in LLMs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/41623b137cd34807f56028aa9f6f84a7-Paper-Conference.pdf) (as "Single-turn conversation")**
> An observable interaction where the model receives a single user query and generates a single response to complete the task.

**[HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf) (as "Open-domain dialogue generation")**
> Generating responses in multi-turn conversations conditioned on persona profiles and dialogue history.

**[Generative Monoculture in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf) (as "Book review generation")**
> The observable task of producing text reviews for specific book titles, evaluated for sentiment, topic, and wording diversity.

**[HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf) (as "Context completion")**
> The observable task of completing a given text prompt or context in a coherent and plausible manner.

**[Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf) (as "Content analysis")**
> The task of analyzing a passage of text to predict a missing final word, testing the model's ability to understand narrative context.

**[A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf) (as "Free generation")**
> The task of producing a valid string from the formal language that respects both grammar and type constraints, without any specific input prompt.

**[Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf) (as "Poem writing")**
> The task of generating a poem based on a given prompt or theme.

**[Exact Byte-Level Probabilities from Tokenized Language Models for FIM-Tasks and Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed5c3c846f684a54975ad7a2525199f-Paper-Conference.pdf) (as "Fill-in-the-middle code completion")**
> The task of generating a missing segment of code given the preceding (prefix) and succeeding (suffix) code context.

**[Sparse Learning for State Space Models on Mobile](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf7fa39d65e2983d724ff7da57f00ac-Paper-Conference.pdf) (as "Generative language modeling")**
> The observable task of producing coherent and contextually relevant text following an initial prompt.

**[Flow: Modularized Agentic Workflow Automation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba84da6921f3040b74ee163aa7451f53-Paper-Conference.pdf) (as "LaTeX document generation")**
> The specific task of creating a compilable LaTeX document, such as a Beamer presentation, based on content and formatting requirements.

**[Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf) (as "Counterfactual question answering")**
> The observable behavior of providing an answer to a question about what would have happened under a hypothetical intervention or condition that differs from the observed reality.

**[3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf) (as "Poem generation")**
> The task of creating poetry that adheres to specific constraints on format, rhyme, rhythm, and tone as specified in the prompt.

**[3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf) (as "Slogan generation")**
> The task of creating a concise and impactful slogan based on a prompt, often with constraints on word count and content.

**[CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf) (as "Surface realization")**
> The process of translating a high-level plan, such as pseudocode, into a detailed, final natural language response.

**[Uncovering Gaps in How Humans and LLMs Interpret Subjective Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362fbc0d182c6b4b8dadb90177239e4-Paper-Conference.pdf) (as "Inference steering")**
> The observable task of generating an output that is shaped by a subjective phrase included directly in the user's prompt.

**[Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf) (as "Culture-conditioned generation")**
> Producing open-ended text (e.g., narrative, dialogue) conditioned on a specific cultural context.

**[LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf) (as "Twitter post generation")**
> Writing a social-media style post that describes the content of an image or video.

**[MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf) (as "Data description generation")**
> Converting structured records into natural-language descriptions that summarize the record content.

**[ActionReasoningBench: Reasoning about Actions with and without Ramification Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf42f133f355e0e07a8957b508b26a1b-Paper-Conference.pdf) (as "Composite question answering")**
> Solving questions that require combining multiple RAC subskills within one prompt.

**[SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/d74d002a9154b4cc433a234feb27c5f4-Paper-Conference.pdf) (as "Storytelling")**
> The task of generating a narrative or story from a given prompt or context.

**[Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf) (as "Knowledge question answering")**
> Answering factual or knowledge-based questions posed in benchmark formats.

**[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf) (as "Personalized response generation")**
> The act of generating conversational responses that incorporate a user's background, preferences, and previous interactions to be more accurate and satisfying.

**[Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf) (as "Narrative generation")**
> The observable act of producing descriptive text that forms a story, describes a scene, or narrates a character's actions.

**[Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf) (as "Open-ended interaction")**
> The model's participation in unconstrained, free-form interactions with a user, generating responses to a wide variety of natural language inputs without pre-defined rules.

**[Language Guided Skill Discovery](https://proceedings.iclr.cc/paper_files/paper/2025/file/dae30ba63ca043588cdf804bbba295ed-Paper-Conference.pdf) (as "State description generation")**
> The observable action of an LLM producing a natural language description for a given agent state, based on a user-provided prompt.

**[CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf) (as "Verilog code completion")**
> The task of completing a partial Verilog code snippet based on the provided context and problem description.

**[SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf) (as "Legal Document Writing")**
> The observable behavior of generating formal text adhering to legal standards and logical structures.

**[GOFA: A Generative One-For-All Model for Joint Graph Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/652c104b5b0652a03684efeaf805463b-Paper-Conference.pdf) (as "Sentence completion")**
> The observable task of predicting and generating the remaining text of a sentence associated with a node in a graph, using both the existing text and surrounding graph context.

**[Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf) (as "Humor generation")**
> The observable task of producing a witty, unexpected, or humorous textual response to a given prompt or question.

**[Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf) (as "Table-to-text generation")**
> The observable task of generating a natural language description from structured data presented in a table.

**[ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf) (as "Data-to-text writing")**
> The task of generating natural language text from structured or semi-structured data.

**[KBLaM: Knowledge Base augmented Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) (as "Open-ended reasoning")**
> The observable task of responding to a query that requires generating a more elaborate or inferential answer beyond simple fact retrieval.

**[Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf) (as "Sentence completion reasoning")**
> The task behavior of selecting or generating the correct completion for a given sentence context.

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf) (as "Expository writing")**
> The task of generating text that explains, informs, or describes facts, such as tutorials, encyclopedia entries, or news articles.

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf) (as "Argumentative writing")**
> Generating text to compare views, judge, or persuade, such as movie reviews or essays.

**[Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf) (as "Email completion")**
> The task of generating coherent and contextually appropriate continuations for a given email prompt, used to measure model utility.

**[First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf) (as "Story writing")**
> The specific task of generating a narrative or story in response to a user prompt.

**[First-Person Fairness in Chatbots](https://proceedings.iclr.cc/paper_files/paper/2025/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf) (as "Cover letter writing")**
> Generating a cover letter for a user as part of employment-related assistance.

**[RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf) (as "Analysis generation")**
> The observable act of producing a textual explanation or rationale before providing a final score or judgment.

**[Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96d00450ed65531ffe2996daed487536-Paper-Conference.pdf) (as "Next-token generation")**
> Predicting the distribution over the next token given a prompt and previously generated text.

**[Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf) (as "Constant Response Generation")**
> Producing the same output string regardless of the input instruction, characteristic of a null model.

**[Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf) (as "Chat response generation")**
> Producing answers to conversational prompts, often evaluated by sampling multiple candidate replies.

**[AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf) (as "Novel writing")**
> The task of generating paragraphs of a novel, often initiated with a starting sentence from an existing human-written work.

**[AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf) (as "Poetry composition")**
> The task of generating poems, often based on a prompt or an initial line from an existing poem.

**[AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf) (as "Speech drafting")**
> The task of generating the text for a speech, often prompted with an initial sentence from a famous historical speech.

**[AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf) (as "Fake news generation")**
> The task of generating news articles based on fake news headlines.

**[HELM: Hierarchical Encoding for mRNA Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb5d9195b201ec7ba66c8e20b396d349-Paper-Conference.pdf) (as "Codon prediction")**
> Predicting masked or next codons in an mRNA sequence during pre-training.

**[What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf) (as "Extended conversation")**
> Engaging in a coherent, multi-turn dialogue that requires remembering and referencing information from much earlier in the conversation.

**[PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebf8764ecf0688cdd9fe1e5a9c525d0d-Paper-Conference.pdf) (as "Dialogue")**
> The observable task of engaging in a multi-turn conversational exchange, which may be grounded in visual information.

**[NutriBench: A Dataset for Evaluating Large Language Models in Nutrition Estimation from Meal Descriptions](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef3a57e4f26b640e6f90d78cbb011feb-Paper-Conference.pdf) (as "Meal description generation")**
> Producing natural-language descriptions of meals from structured dietary intake data.

**[AnalogGenie: A Generative Engine for Automatic Discovery of Analog Circuit Topologies](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0552f14388d95b19740dee809f5cad1-Paper-Conference.pdf) (as "Next device pin prediction")**
> Generating the next pin token in a sequence that encodes a circuit topology.

**[Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad7c708dda11f3e72cc1629bb130379-Paper-Conference.pdf) (as "Multigram prediction")**
> The observable behavior of predicting n-grams and skip n-grams, which are common, potentially non-contiguous, sequences of tokens.

**[Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad7c708dda11f3e72cc1629bb130379-Paper-Conference.pdf) (as "Code prediction")**
> The specific task of performing next-token prediction on sequences of source code.

**[On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf) (as "Fictitious knowledge generation")**
> The task of generating responses based on synthetic, non-factual information about fictional entities.

**[Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf) (as "Complex question answering")**
> The task of answering questions that require aggregating information from multiple sources or performing multi-step inference.

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "Open-ended question answering")**
> The task of generating free-form, unconstrained text answers in response to questions that do not have a single correct format or answer.

**[LeanQuant: Accurate and Scalable Large Language Model Quantization with Loss-error-aware Grid](https://proceedings.iclr.cc/paper_files/paper/2025/file/57ccc284de6f060c8dcde8f9352f70a5-Paper-Conference.pdf) (as "Zero-shot question answering")**
> The observable task of answering questions from various domains without any task-specific examples provided in the context.

**[StructRAG: Boosting Knowledge Intensive Reasoning of LLMs via Inference-time Hybrid Information Structurization](https://proceedings.iclr.cc/paper_files/paper/2025/file/5975754c7650dfee0682e06e1fec0522-Paper-Conference.pdf) (as "Single-hop question answering")**
> Answering a question that can be resolved with a single piece of retrieved information.

**[A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf) (as "Long-form question answering")**
> The task of generating detailed, paragraph-length answers to open-ended questions.

**[Do LLMs have Consistent Values?](https://proceedings.iclr.cc/paper_files/paper/2025/file/68fb4539dabb0e34ea42845776f42953-Paper-Conference.pdf) (as "Questionnaire answering")**
> The observable behavior of responding to a series of questions from a structured survey, such as a value questionnaire, by providing ratings on a scale.

**[PaCA: Partial Connection Adaptation for Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b4fd4a4607f57fe65b5e276bdb17ed1-Paper-Conference.pdf) (as "Academic question answering")**
> Answering questions or selecting answers on tasks spanning academic subjects.

**[Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf) (as "Binary question answering")**
> A specific question answering task where the model must provide a binary "Yes"/"No" or "True"/"False" response.

**[MeteoRA: Multiple-tasks Embedded LoRA for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8951bbdcf234132bcce680825e7cb354-Paper-Conference.pdf) (as "Multiple-choice answering")**
> Selecting the correct option from a set of answer choices for a question or prompt.

**[EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4f419c398382295e1e350d56ecb65f2-Paper-Conference.pdf) (as "Benchmark Question Answering")**
> Solving specific tasks on standardized public benchmarks to demonstrate model capabilities.

**[CycleResearcher: Improving Automated Research via Automated Review](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a48036026dc7946ef6033ae14719cc5-Paper-Conference.pdf) (as "Research paper generation")**
> The observable task of producing a complete academic paper in a structured format, including sections like abstract, introduction, methods, and results.

**[Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf) (as "Long-form Narrative Generation")**
> The observable action of producing continuous fiction text of 1,000-2,000 tokens from a writing prompt.

**[Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf) (as "Long structured output generation")**
> Producing extended structured responses such as matrices or move sequences without format breakdowns.

**[Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf) (as "Document-level generation")**
> A specific type of long-form generation that requires producing a response structured as a complete document.

**[Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf) (as "Long-text Generation")**
> The observable behavior of producing coherent and extended text outputs such as articles or stories.

**[Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf) (as "Arbitrary-length sequence generation")**
> Generating text sequences whose length can continue until an end-of-sequence token or degradation criterion is reached.

**[Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf) (as "Unconditional generation")**
> Generating text without a conditioning prompt or task-specific input.

**[Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf) (as "Story generation")**
> The general task of creating a narrative text from a prompt.

**[Modality-Specialized Synergizers for Interleaved Vision-Language Generalists](https://proceedings.iclr.cc/paper_files/paper/2025/file/22bf0634985f4e6dbb1fb40e247d1478-Paper-Conference.pdf) (as "Multimodal dialogue")**
> Engaging in a conversational exchange that involves both text and images as input and output.

**[Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf) (as "Visual conversation")**
> The task of participating in a multi-turn dialogue with a user about the content of an image.

**[ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf) (as "Conversational VQA")**
> The model answers conversational visual questions about images, including dialogue-style prompts and responses.

**[Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf) (as "Visual chatting")**
> Engaging in a multi-turn, conversational interaction with a user about the content of an image.

**[LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf) (as "Multi-image dialogue")**
> Engaging in dialogue grounded in multiple images provided together as input.

**[Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d368eba3fb546ae5d868dae2ecb17200-Paper-Conference.pdf) (as "Image dialogue")**
> Responding in natural language to image-based prompts in a conversational format.

**[Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf) (as "Multimodal chat")**
> Engaging in open-ended, conversational dialogue that involves both text and images as inputs.

**[Adapt-$\infty$: Scalable Continual Multimodal Instruction Tuning via Dynamic Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf) (as "Multi-turn visual conversation")**
> Engaging in multi-turn dialogue grounded in visual inputs.

**[Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25d/shi25d.pdf) (as "Verbal response generation")**
> Producing natural language utterances, such as confirmations or clarifications, in response to user prompts or during task execution.

**[WMarkGPT: Watermarked Image Understanding via Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25f/tan25f.pdf) (as "Watermark description generation")**
> The observable task of producing a natural language text that describes a watermark's characteristics, such as its location, content, appearance, and its interaction with the main image content.

**[Improving Diversity in Language Models: When Temperature Fails, Change the Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/verine25a/verine25a.pdf) (as "Creative story generation")**
> Generating diverse and engaging stories from prompts in an open-ended setting.

**[Language Models over Canonical Byte-Pair Encodings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vieira25b/vieira25b.pdf) (as "Token string generation")**
> The autoregressive production of sequences of tokens by a language model, which may result in either canonical or noncanonical encodings of character strings.

**[AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf) (as "Concept-conditioned generation")**
> Generating text that is explicitly guided to include a specified concept or topic.

**[CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf) (as "Document creation")**
> The model helps produce or revise a written document across multiple turns, such as a blog post, creative writing piece, or personal statement.

**[Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf) (as "Visual chat")**
> Engaging in a multi-turn conversational dialogue with a user about the contents of an image.

**[ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf) (as "Paper writing")**
> Generating a paper-like research output from researcher and paper context in a structured format.

**[ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf) (as "Review writing")**
> The process of generating critiques and numerical scores for a paper by reviewer agents based on its content and context in the community graph.

**[ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf) (as "Interdisciplinary research generation")**
> The creation of research proposals that integrate concepts and methods from distinct scientific fields, such as NLP and astronomy or criminology.

**[CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25g/yuan25g.pdf) (as "Editing instruction generation")**
> Generating a textual instruction that summarizes the differences between paired CAD models.

**[SPRI: Aligning Large Language Models with Context-Situated Principles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhan25a/zhan25a.pdf) (as "Cognitive reappraisal generation")**
> The task of generating text that reframes an emotionally charged situation to alter its emotional impact, a strategy used in psychology.

**[Hardware and Software Platform Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25u/zhang25u.pdf) (as "Random word generation")**
> The task of producing a sequence of random words as prompted by a user, used to generate diverse logit distributions for analysis.

**[UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25w/zhang25w.pdf) (as "Scene description generation")**
> Generating a textual description of the current visual scene in response to a prompt.

**[SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cm/zhang25cm.pdf) (as "High-level justification generation")**
> Generating a textual explanation for why a particular driving action was chosen.

**[Synthesizing Software Engineering Data in a Test-Driven Manner](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cn/zhang25cn.pdf) (as "Development document generation")**
> Using an LLM to generate detailed task descriptions or requirement documents from unit test content.

**[Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf) (as "Guided generation")**
> Conditioning output generation on external task-specific signals to improve performance in targeted domains.

**[Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chehade25a/chehade25a.pdf) (as "Humorous response generation")**
> Producing outputs that incorporate humor or wit, evaluated under a humor reward model as a secondary objective in alignment.

**[SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf) (as "Short answer generation")**
> Generating a concise response to a question using a single word or phrase.

**[LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf) (as "Token-by-token generation")**
> Autoregressive production of text one token at a time, used in standard language modeling evaluation settings.

**[Measuring Diversity in Synthetic Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ac/zhu25ac.pdf) (as "Story completion")**
> A generative language task where the model produces a continuation or ending for a given narrative prompt, used as one of the tasks for evaluating synthetic dataset diversity.

**[Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf) (as "Empathetic response generation")**
> The observable task of producing text that conveys understanding, compassion, and validation of a user's expressed emotions.

**[Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://raw.githubusercontent.com/mlresearch/v267/main/assets/badawi25a/badawi25a.pdf) (as "Culturally appropriate response generation")**
> Generating mental health responses that respect and reflect the user's cultural background, avoiding stereotypes and offering relevant, non-biased advice.

**[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf) (as "Cover letter generation")**
> Writing a professional cover letter for a job applicant, used to assess whether the quality of writing varies by the applicant's gender.

**[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf) (as "Reference letter generation")**
> Writing a recommendation letter for a student or job candidate, used to evaluate whether the strength of endorsement varies by gender.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Creative composition")**
> The observable behavior of performing a generation task that requires the production of a novel artifact given a set of defined constraints.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Professional writing")**
> Creating formal documents such as resumes, cover letters, performance reviews, and job descriptions that influence professional evaluation and opportunity allocation.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Argument composition")**
> Constructing persuasive or critical analyses, such as essay outlines, hypothetical answers, or debate points.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Academic writing")**
> The task of generating content for educational or research purposes, such as explanations, study plans, literature reviews, and informational articles.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Advice generation")**
> Producing guidance or recommendations in response to personal or situational queries, such as life advice or problem-solving suggestions.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Title generation")**
> Producing short, creative textual elements such as product names, hashtags, slogans, or article headings.

**[Position: AI Scaling: From Up to Down and Out](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25fh/wang25fh.pdf) (as "Video scriptwriting")**
> Generating narrative or instructional scripts for video content based on creative or contextual prompts.

**[AMACE: Automatic Multi-Agent Chart Evolution for Iteratively Tailored Chart Generation](https://aclanthology.org/2025.emnlp-main.1090.pdf) (as "Free-text response generation")**
> Producing natural language responses that are contextually appropriate and accurate in agent interactions, particularly in business or CRM settings.

**[TIDES: Technical Information Discovery and Extraction System](https://aclanthology.org/2025.emnlp-main.1104.pdf) (as "Final response generation")**
> The act of producing the concluding answer or output for the user after completing all necessary intermediate steps like tool use.

**[Too Consistent to Detect: A Study of Self-Consistent Errors inLLMs](https://aclanthology.org/2025.emnlp-main.239.pdf) (as "Model generation")**
> The observable production of text-based outputs in response to prompts, which is the primary behavior evaluated across various NLP tasks.

**[Confidence-guided Refinement Reasoning for Zero-shot Question Answering](https://aclanthology.org/2025.emnlp-main.355.pdf) (as "Natural language response generation")**
> The task of producing unstructured, human-readable text in response to a prompt.

**[Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement](https://aclanthology.org/2025.emnlp-main.925.pdf) (as "Open-ended response generation")**
> Generating free-form responses to instructions that reflect a particular community's viewpoint.

**[CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases inLLMs](https://aclanthology.org/2025.emnlp-main.85.pdf) (as "Utterance generation")**
> The specific task of generating the natural language text for user and system turns in a dialogue, based on a predefined scenario and logic flow.

**[START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf) (as "Completion")**
> The task of continuing a given text prompt to produce a coherent and contextually relevant extension.

**[iTool: Reinforced Fine-Tuning with Dynamic Deficiency Calibration for Advanced Tool Use](https://aclanthology.org/2025.emnlp-main.702.pdf) (as "Bidirectional text continuation")**
> The process of generating text both before (backward continuation) and after (forward continuation) a given seed text to create a surrounding context.

**[DiCoRe: Enhancing Zero-shot Event Detection via Divergent-ConvergentLLMReasoning](https://aclanthology.org/2025.emnlp-main.1039.pdf) (as "Sentence generation")**
> Producing natural language sentences that include specified event triggers and align with a target domain's linguistic patterns.

**[What are Foundation Models Cooking in the Post-Soviet World?](https://aclanthology.org/2025.emnlp-main.1045.pdf) (as "Free-text generation")**
> The observable behavior of producing open-ended textual outputs without constrained options, used as a task format in reasoning evaluations.

**[3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1354.pdf) (as "Essay generation")**
> Producing long-form, coherent essays in a domain different from the training data (news), used to test out-of-domain generalization.

**[3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1354.pdf) (as "Human-content continuation")**
> Machine models continuing human-authored text, creating blended content that challenges detection systems.

**[Principled Personas: Defining and Measuring the Intended Effects of Persona Prompting on Task Performance](https://aclanthology.org/2025.emnlp-main.1365.pdf) (as "Smart reply generation")**
> Generating a relevant and concise response to a given textual message.

**[Add-One-In: Incremental Sample Selection for Large Language Models via a Choice-Based Greedy Paradigm](https://aclanthology.org/2025.emnlp-main.271.pdf) (as "Generation")**
> Producing free-form text outputs in response to an input prompt.

**[Dual-Path Counterfactual Integration for Multimodal Aspect-Based Sentiment Classification](https://aclanthology.org/2025.emnlp-main.1159.pdf) (as "Free-form text completion")**
> Generating open-ended continuations of partial sentences, particularly those involving occupational roles and gendered or gender-neutral prompts.

**[LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf) (as "Extractive question answering")**
> Producing an answer by extracting or composing it from a provided passage or prefix.

**[Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf) (as "Free-form text generation")**
> Generating open-ended natural language responses to prompts rather than selecting from fixed options.

**[Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Free-form Text Generation")**
> Generating text responses without fixed options, involving an extensive range of potential responses.

**[Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf) (as "Open-ended text generation")**
> The task of generating text without a specific, constrained format, often as a continuation of a given prompt.

**[The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf) (as "Unconditional text generation")**
> Generating a continuation when the goal or suffix is unknown, using only the prefix and internal decoding strategy.

## Relationships

### Text generation →
- **WikiText-2** (measurements) — *measured_by*
  > To pre-process WikiText-V2 for our use case, we split each passage in the dataset into two equal context “segments”, with the goal of predicting the second (continuation) from the first (query). (Section 6.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
- **E2E NLG Challenge** (measurements) — *measured_by*
  > For NLG tasks, we assess our method with GPT-2 (Radford et al., 2019) on the E2E NLG Challenge (Novikova et al., 2017) benchmark. (Section 4)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
- **C4** (measurements) — *measured_by*
  > One is reported by the perplexity metric of language generation experiments on C4 (Raffel et al. (2020)) and WikiText2 (Merity et al. (2016)). (Section 5.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Accuracy is Not All You Need](https://proceedings.neurips.cc/paper_files/paper/2024/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf)
- **Penn Treebank (PTB)** (measurements) — *measured_by*
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > We evaluate the pretrained models on language model tasks and multiple-choice tasks from LM evaluation Harness (Gao et al., 2023). (Section 5.3)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > To corroborate these G-Eval findings, we conduct human evaluations involving 5 in-house annotators who assessed 50 randomly selected ChatGPT’s generations across the datasets. (Section 4.2)
  - [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **WebNLG** (measurements) — *measured_by*
  > We evaluate table-to-text generation with E2E (Novikova et al., 2017) and WebNLG (Gardent et al., 2017) datasets... (Section 5.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  > Performance comparison on eight LongBench datasets evaluating single/multi-document QA, summarization, and retrieval tasks... (Table 3)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > To evaluate the quality of the generated dialogues, we compute the winrate (Rafailov et al., 2024b) against the generations from the reference policy, Llama-3-8B-it, using GPT4 (OpenAI, 2023) over a randomly sampled subset of the test set with 500 samples. (Section 4.2)
  - [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **TinyStories** (measurements) — *measured_by*
  > We conducted experiments using LLaMA-2-13B across the CNN/Daily Mail (Nallapati et al., 2016), GSM8K (Cobbe et al., 2021), and TinyStories (Eldan & Li, 2023) datasets. (Section 3.2.1)
  - [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > two generation datasets (TruthfulQA (Lin et al., 2022) and GSM8K (Cobbe et al., 2021)) (Section 4)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **ToTTo** (measurements) — *measured_by*
  > We first run experiments on four data-to-text generation datasets. ToTTo (Parikh et al., 2020) is an English dataset with Wikipedia tables where specific cells are highlighted, paired with a sentence describing those cells. (Section 4.1)
  - [Vanishing Gradients in Reinforcement Finetuning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b09bb02b90584e2be94ff3ae09289bc-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > "We benchmark the current LLM’s ability to perform situated faithful reasoning on several question-answering tasks, including ... NaturalQA"
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  > We evaluate quantized LLMs using ... zero-shot accuracy on the benchmarks ARC (Clark et al., 2018), LAMBADA (Paperno et al., 2016), MMLU (Hendrycks et al., 2020), HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), and WinoGrande (Sakaguchi et al., 2021) (Section 4).
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **EvoEval** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **HumanEval-X** (measurements) — *measured_by*
  - [AlchemistCoder: Harmonizing and Eliciting Code Capability by Hindsight Tuning on Multi-source Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/040c816286b3844fd78f2124eec75f2e-Paper-Conference.pdf)
- **OpenWebText** (measurements) — *measured_by*
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > “The multiple-choice tasks include: ... common sense reasoning (Hellaswag; Zellers et al. 2019)”
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  > “tasks including classification, multiple-choice questions, and content generation.”
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **PubMedQA** (measurements) — *measured_by*
  > Medical QA. We apply our method to medical question answering as target domain T... We use... PubMedQA (Jin et al., 2019), which contains approximately 200K QA pairs
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **XSum** (measurements) — *measured_by*
  - [LiteASR: Efficient Automatic Speech Recognition with Low-Rank Approximation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **MultiPL-E** (measurements) — *measured_by*
  - [Batched Low-Rank Adaptation of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/66247b78cb1aa7259dcf856a18c9e294-Paper-Conference.pdf)
- **DART** (measurements) — *measured_by*
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **CoQA** (measurements) — *measured_by*
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **MAUVE** (measurements) — *measured_by*
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **CommonGen** (measurements) — *measured_by*
  > We evaluate Plugin on four text generation benchmarks: (a) E2E NLG (Duˇsek et al., 2020), (b) Web NLG (Gardent et al., 2017), (c) CommonGen (Lin et al., 2020), and (d) the Adidas product description dataset (adi, 2023). (Section 7)
  - [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf)
- **IMDb** (measurements) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > and 2 knowledge-intensive tasks (NQ (Kwiatkowski et al., 2019), MMLU (Hendrycks et al., 2021)). (Section 5.1)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **ClassEval** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **DS-1000** (measurements) — *measured_by*
  - [SelfCodeAlign: Self-Alignment for Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/72da102da91a8042a0b2aa968429a9f9-Paper-Conference.pdf)
- **LLaVA-Bench** (measurements) — *measured_by*
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  > In LongBench, we merge four tasks into 'QA' and merge two tasks into the 'Summary' column in the table.
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  > For question answering, we use AlpacaEval 2.0 (Li et al., 2023b; Dubois et al., 2024a;b) to assess model performance on 805 instructions. (Section 7.1)
  - [The Best of Both Worlds: Bridging Quality and Diversity in Data Selection with Bipartite Graph](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ac/wu25ac.pdf)
- **MM-Vet** (measurements) — *measured_by*
  > MM-Vet (Yu et al., 2024b) examines MLLMs on complicated multimodal reasoning tasks with open-ended Q&A. (Section 4.2.2)
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
- **EHRNoteQA** (measurements) — *measured_by*
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BioASQ** (measurements) — *measured_by*
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > ARC-Challenge introduces a multi-choice question answering dataset, composed of science exam questions from grade 3 to grade 9. (Section 4)
  - [STAREat the Structure: SteeringICLExemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  > The commonsense reasoning tasks contain eight datasets, including six question-answering datasets (i.e., BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), ARC-e (Clark et al., 2018), ARC-c (Clark et al., 2018), and OBQA (Mihaylov et al., 2018))...
  - [STAREat the Structure: SteeringICLExemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)
- **Vicuna-Bench** (measurements) — *measured_by*
  - [Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > “The multiple-choice tasks include: grade-school science questions (ARC; Clark et al. 2018)”
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **SVAMP** (measurements) — *measured_by*
  > Text Generation We use the SVAMP dataset (Patel et al., 2021) which consists of English math word problems with grade level up to 4.
  - [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-DomainMoEAdaptation](https://aclanthology.org/2025.emnlp-main.933.pdf)
- **Super-Natural Instructions** (measurements) — *measured_by*
  > These sequences consist of pure generation tasks, pure classification tasks and mixed sequences containing both generation and classification tasks. (Section 3)
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  > Table 2 shows that our method preserves most of the model's performance in retrieval and QA tasks
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
- **SciQA** (measurements) — *measured_by*
  > "For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ARC (Clark et al., 2018) tests advanced reasoning with grade-school science questions, PubMedQA (Jin et al., 2019) assesses biomedical reasoning from abstracts, and SciQA (Auer et al., 2023) challenges models using the Open Research Knowledge Graph."
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **TOFU** (measurements) — *measured_by*
  > The closest work to ours is TOFU (Maini et al., 2024), a benchmark featuring 200 synthetic author profiles, each with 20 question-answer pairs, divided into forget and retain sets. (Section 6)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **MetaMathQA** (measurements) — *measured_by*
  > “The experiments involved 5 NLG benchmarks: MetaMathQA (Yu et al., 2023), Alpaca-GPT4 (Peng et al., 2023), FedAya (Ye et al., 2024a), Fed-ChatbotIT (Ye et al., 2024a), and Fed-WildChat (Ye et al., 2024a)”
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **Generative perplexity** (measurements) — *measured_by*
  - [Latent Thought Models with Variational Bayes Inference-Time Computation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kong25c/kong25c.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **ToxiGen** (measurements) — *measured_by*
  > For the open-ended generation tasks, we apply SADI on TriviaQA (Joshi et al., 2017), TruthfulQA (Lin et al., 2022), ToxiGen (Hartvigsen et al., 2022) datasets. (Section 4.1)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **HiTab** (measurements) — *measured_by*
  - [A Self-Denoising Model for Robust Few-Shot Relation Extraction](https://aclanthology.org/2025.acl-long.1300.pdf)
- **BigCodeBench** (measurements) — *measured_by*
  - [EpiCoder: Encompassing Diversity and Complexity in Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bi/wang25bi.pdf)
- **CEval** (measurements) — *measured_by*
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)
- **FiQA-SA** (measurements) — *measured_by*
  - [STAREat the Structure: SteeringICLExemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.747.pdf)
- **ESConv** (measurements) — *measured_by*
  > “We conduct experiments on the ESConv dataset by selectively omitting each of the four distinct aspects when applying the IntentionFrame framework to enhance downstream response generation.”
  - [Multilingual Language Model Pretraining using Machine-translated Data](https://aclanthology.org/2025.emnlp-main.1427.pdf)

### → Text generation
- **Self-evaluation** (behaviors tasks) — *causes*
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Collaboration** (behaviors tasks) — *causes*
  > we propose a Mixture-of-Agents framework designed to leverage the strengths of multiple LLMs, thereby improving their reasoning and language generation capabilities. (Section 1)
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **Humor understanding** (constructs) — *causes*
  > Finally, with these two basic skills, humor understanding and judgment, the ability to generate humor can be improved. (Section 1)
  - [Innovative Thinking, Infinite Humor: Humor Research of Large Language Models through Structured Thought Leaps](https://proceedings.iclr.cc/paper_files/paper/2025/file/6794f555524c9069e26970a408d353cc-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > To assess free-form questions and multiple-round conversations, we utilize the LLM-as-a-Judge methodology
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > "Experiments are conducted based on LLaMA-2-7B on Natural Question dataset."
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > "we use the over 800 closed-book questions in TruthfulQA ... corresponding to whole sentence answers"
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
- **Thought generation** (behaviors tasks) — *causes*
  - [Thinking LLMs: General Instruction Following with Thought Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25o/wu25o.pdf)

### Associated with
- **Natural language understanding** (constructs)
  > Large language models (LLMs) are transforming various domains by enabling sophisticated natural language understanding and generation (Zhao et al., 2023).
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Memorization** (constructs)
  > we observe that LISA is much better than LoRA at memorization-centered tasks, such as Writing or depicting image details, while this gap is much smaller in reasoning-centered tasks like Code or Math (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Generation diversity** (constructs)
  > “In a generative setting, this results in repetitive responses, as illustrated in Figure 1.”
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Stereotyping** (constructs)
  > Paper title: Job Unfair: An Investigation of Gender and Occupational Bias in Free-Form Text Completions by LLMs
  - [2025.emnlp-main.1159.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1159.checklist.pdf)
- **Machine translation** (behaviors tasks)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text quality** (constructs)
  - [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf)
- **Generative capability** (constructs)
  - [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks)
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  > “in language generation, x is a sequence of tokens t1 · · · tk, y is the next token tk+1”
  - [Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chijiwa25a/chijiwa25a.pdf)
- **Objective mismatch** (constructs)
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
- **Coherence** (constructs)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **Autoregressive language modeling** (behaviors tasks)
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Code completion** (behaviors tasks)
  - [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Text infilling** (behaviors tasks)
  - [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Instruction generation** (behaviors tasks)
  - [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/be06e3802e9411381feece79b4d960c1-Paper-Conference.pdf)
- **Hallucination detection** (behaviors tasks)
  > We demonstrate that the influence of negated text on hallucination detection extends across multiple tasks, including question answering (QA), dialogue, summarization, and completion, indicating its task-agnostic.
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Logical reasoning** (constructs)
  > “Given the evidence and reasoning rules, LLM must decide if the queried clause is true, false, or unknown.”
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Human evaluation** (measurements)
  > The user study consists of two parts. In the first part, we ask participants to specify four email-writing tasks (e.g., Write an email to your advisor asking for feedback). (Section 4.2)
  - [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf)
- **Output diversity** (constructs)
  - [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf)
- **Causal reasoning** (constructs)
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
- **Aspect-based sentiment analysis** (behaviors tasks)
  - [BPP-Search: Enhancing Tree of Thought Reasoning for Mathematical Modeling Problem Solving](https://aclanthology.org/2025.acl-long.41.pdf)
- **Prompt engineering** (behaviors tasks)
  > Using the generated instruction IL, we prompt πS to produce two responses: a chosen response yS ∼πS(y ∣xS) based on the short context xS, and a rejected response yL∼πS(y ∣xL) derived from the long context xL.
  - [Reward-Guided Prompt Evolving in Reinforcement Learning for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25a/ye25a.pdf)
- **Forecasting** (behaviors tasks)
  > “Forecasting ... Sports Projections, Financial Forecasting”
  - [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf)
- **Occupational bias** (constructs)
  > Paper title: Job Unfair: An Investigation of Gender and Occupational Bias in Free-Form Text Completions by LLMs
  - [2025.emnlp-main.1159.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1159.checklist.pdf)

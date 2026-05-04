# Information retrieval
**Type:** Behavior  
**Referenced in:** 353 papers  
**Also known as:** Evidence page retrieval, Evidence retrieval, Long-dependency retrieval, Multi-subkey dictionary retrieval, Needle-in-a-haystack retrieval, Passage retrieval, Passkey retrieval, Subgraph retrieval, Document indexing, Query matching, Clue retrieval, Fact retrieval, Material retrieval, Multi-table retrieval, Page-level retrieval, Prefix-suffix retrieval, Table retrieval, Tool retrieval, Visual retrieval, Dependency retrieval, External knowledge retrieval, Long-context retrieval, Multi-needle retrieval, Single-needle retrieval, Forward search, Long-term memory search, Short-term memory search, Closed-book retrieval, Document retrieval, Keyword-based file retrieval, Long-document retrieval, Memory retrieval, Needle retrieval, Retrieval, Semantic file retrieval, Sequence recall, Paper retrieval, Graph search, Object search, Tree search, Literature search, Substring searching, Document similarity search, Parallel search, Word search, Inverse search, Process-level beam search, Needle question answering, Triple filtering, Argumentative retrieval, Character retrieval, File retrieval, Image crop retrieval, Long video retrieval, Sentence retrieval, Generative retrieval, Semantic retrieval of emotion labels, Text retrieval, Long caption retrieval, Page retrieval, Prior case retrieval, Short caption retrieval, Statute retrieval, Argument retrieval, Literature retrieval, Tutorial retrieval, Legal case retrieval, Provision retrieval, Support sentence retrieval, Needle extraction, Ad retrieval, Structured data retrieval, Cross-paragraph retrieval, Multi-step retrieval, Scientific literature search, Table-column retrieval, BioAssay retrieval, Content retrieval, Simple lookup, Cross-lingual retrieval, Keyword sequence retrieval, Relevant fact extraction, Web data retrieval, Retrieval noise reduction, Database retrieval, Iterative retrieval, Reasoning with retrieved documents, Think-and-search, Knowledge-grounded response generation, Image retrieval, Cross-file retrieval, Expert retrieval, Entity retrieval, Relation retrieval, Text-to-image retrieval, Reasoning path retrieval, Web content retrieval, Dense retrieval, Semantic retrieval, Retrieval-augmented question answering, Dataflow-guided retrieval, Sparse retrieval, Demonstration retrieval, Material property retrieval, Multi-hop evidence retrieval, Multimodal document retrieval, Visual document retrieval, Cascade retrieval, Layout-level retrieval, Multilingual retrieval, Text-to-video retrieval, Attribute-based retrieval, Comprehensive retrieval, Embedding-based retrieval, Hard negative retrieval, Academic paper search, In-context retrieval, Retrieval ability, Retrieval capability, Knowledge utilization, Knowledge retrieval depth, Reasoning-intensive retrieval, Knowledge gain, Retrieval utility, Search, Search ability, Retrieval efficiency, Multimodal search capability, Inspiration retrieval ability, Multimodal retrieval capability, Text retrieval capability, Semantic retrieval capability, String retrieval capability, Answer retrieval, Cross-lingual context retrieval, Factual knowledge retrieval, Information retrieval and localization, Retrievability, Associative memory retrieval, Causal retrieval, Information retrieval capability, Parametric knowledge retrieval, Task vector retrieval, Knowledge retrieval, Retrieval performance  

## State of the Field

Across the surveyed literature, information retrieval is broadly defined as the process of finding and extracting relevant information from a source, such as a document corpus or memory store, in response to a query. The scope of this behavior is diverse, encompassing the retrieval of text passages, document pages, structured data like knowledge graph subgraphs or tables, and specialized items like tools, legal cases, or scientific papers. A prevalent operationalization of this behavior involves "needle-in-a-haystack" tasks, where a model must locate a specific, short piece of information embedded within a long, distracting context; this is frequently measured using the Needle-in-a-haystack test and the RULER benchmark. Information retrieval is also commonly evaluated as the initial step in retrieval-augmented generation (RAG) systems, where its performance is assessed using question-answering datasets like HotpotQA, Natural Questions, and MSMARCO. Some work investigates more complex, multi-step or iterative retrieval processes, while a smaller set of studies focuses on "reasoning-intensive retrieval," measured by benchmarks like BRIGHT, which requires identifying documents based on nuanced connections rather than surface-level matching. The behavior also extends to multimodal contexts, with tasks defined for visual, video, and multimodal document retrieval. This behavior is frequently studied in relation to long-context processing and is often positioned as a mechanism to mitigate hallucination by grounding model outputs in external evidence.

## Sources

**[From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf)**
> The process of finding and extracting relevant information from a memory store or document corpus in response to a query.

**[A Training-Free Sub-quadratic Cost Transformer Model Serving Framework with Hierarchically Pruned Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/043f0503c4f652c737add3690aa5d12c-Paper-Conference.pdf) (as "Passkey retrieval")**
> A "needle in a haystack" task where the model must identify and extract a specific, short piece of information (a passkey) from a long, repetitive document.

**[SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf) (as "Evidence page retrieval")**
> The observable task of identifying and fetching the most relevant page or pages from a multi-page document in response to a user's query.

**[TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf) (as "Passage retrieval")**
> The task of identifying and retrieving text passages from a large corpus that are relevant to a given query.

**[TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf) (as "Long-dependency retrieval")**
> Recovering a specific target item embedded far back in a long context.

**[Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf) (as "Subgraph retrieval")**
> Selecting a relevant subset of triples from a knowledge graph to support downstream reasoning.

**[LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf) (as "Needle-in-a-haystack retrieval")**
> The observable task of identifying and extracting a specific piece of information embedded within a large volume of irrelevant text.

**[From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf) (as "Multi-subkey dictionary retrieval")**
> Given dictionaries whose keys are tuples of integers, the model identifies the tuple containing specified subkeys and reports the tuple, its value, and its dictionary.

**[Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf) (as "Web search")**
> The action of querying a search engine to retrieve information from the web to answer a question.

**[CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf) (as "Evidence retrieval")**
> The process of identifying and extracting relevant pieces of information from a given set of passages or documents to support an answer.

**[CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/70fa5df8e3300dc30bf19bee44a56155-Paper-Conference.pdf) (as "Clue retrieval")**
> The observable action of identifying and outputting specific time intervals within a video that support an answer.

**[World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf) (as "Fact retrieval")**
> Recovering a specific target fact or item from a long context when prompted.

**[MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf) (as "Multi-table retrieval")**
> The task of selecting a set of relevant and joinable tables from a larger corpus in order to answer a given question.

**[MatExpert: Decomposing Materials Discovery By Mimicking Human Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d6850f4c82520793f738d98a72aab9d-Paper-Conference.pdf) (as "Material retrieval")**
> The observable task of identifying and retrieving an existing material from a database that most closely matches a user-provided description of desired properties.

**[From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf) (as "Tool retrieval")**
> The task of selecting the most relevant tool(s) from a large collection based on a user's query or a given problem context.

**[ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf) (as "Page-level retrieval")**
> Given a query, selecting the correct document page from a corpus of candidate pages.

**[ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf) (as "Table retrieval")**
> The task of retrieving documents or pages based on the content of tables they contain.

**[ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf) (as "Query matching")**
> The online process of matching a query against a pre-built document index to rank and retrieve relevant documents.

**[ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf) (as "Document indexing")**
> Embedding and storing document pages or chunks offline so they can be searched efficiently at query time.

**[MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf) (as "Visual retrieval")**
> Finding an image that matches a target image or contains the same depicted entity or scene.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "Key-value retrieval")**
> Recovering the value associated with a specified key from a long list or JSON object containing many key-value pairs.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "Prefix-suffix retrieval")**
> Finding a string in a large dictionary that matches both a specified prefix and suffix.

**[Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf) (as "Long-term memory search")**
> Recalling and answering questions about events that occurred more than a minute prior to the user's query in a video.

**[Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf) (as "Short-term memory search")**
> Responding to user queries about events that concluded less than 20 seconds prior, testing recall of recent activities.

**[Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf) (as "Knowledge retrieval")**
> Retrieving relevant medical knowledge from a knowledge graph or corpus to support prediction.

**[Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf) (as "Long-context retrieval")**
> Retrieving a target statement or fact from a long input context when it appears at different positions.

**[Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf) (as "Forward search")**
> The observable task of retrieving information that sequentially follows a given piece of information, used as a baseline to contrast with inverse search.

**[Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf) (as "Dependency retrieval")**
> Selecting relevant formal objects from a library for an informal statement.

**[MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d6c53fe062716387ff0df73cc53de60c-Paper-Conference.pdf) (as "External knowledge retrieval")**
> Querying outside knowledge sources to obtain evidence relevant to a verification decision.

**[CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf) (as "Single-needle retrieval")**
> Finding and recalling a single, specific piece of information ('needle') embedded within a long, distracting context ('haystack').

**[CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf) (as "Multi-needle retrieval")**
> Finding and recalling multiple, distinct pieces of information ('needles') embedded within a long, distracting context ('haystack').

**[LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf) (as "Needle retrieval")**
> Identifying and retrieving the correct inserted image or information from deep within a long video sequence.

**[VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) (as "Document retrieval")**
> The process of selecting relevant document pages from a corpus based on a query.

**[From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf) (as "Semantic file retrieval")**
> The observable task of retrieving files based on the semantic similarity of their content to a natural language query, rather than exact keyword matching.

**[From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf) (as "Keyword-based file retrieval")**
> Retrieving files that contain specified keywords in their names or contents.

**[Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/5750f91d8fb9d5c02bd8ad2c3b44456b-Paper-Conference.pdf) (as "Memory retrieval")**
> The process of an agent accessing and retrieving relevant information from a memory database or knowledge base.

**[Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf) (as "Closed-book retrieval")**
> The task of answering a query or retrieving information without access to any external context or knowledge source.

**[Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf) (as "Retrieval")**
> Selecting the most relevant passage or candidate for a query based on embedding similarity.

**[Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf) (as "Long-document retrieval")**
> The task of retrieving relevant information or documents from a collection of long-form texts in response to a query.

**[Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf) (as "Sequence recall")**
> The observable task of reproducing a sequence of items that was previously presented.

**[Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea94957d81b1c1caf87ef5319fa6b467-Paper-Conference.pdf) (as "Paper retrieval")**
> The action of searching for and selecting relevant academic papers related to a given research topic.

**[HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf) (as "Synthetic recall")**
> A category of tasks where a model must retrieve a specific piece of information (a 'needle') deliberately hidden within a long, synthetic, and often irrelevant context (a 'haystack').

**[Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf) (as "Graph search")**
> Predicting the next vertex on a path from a start vertex toward a goal vertex in a directed graph.

**[Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology](https://proceedings.iclr.cc/paper_files/paper/2025/file/15ce8e7afe5ee95bad56e3b9be28d3d1-Paper-Conference.pdf) (as "Object search")**
> The task of actively navigating an environment to find a specific object described by textual or visual cues.

**[Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf) (as "Tree search")**
> The observable process of exploring a solution space by constructing a tree of possible intermediate steps to find an optimal answer.

**[BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments](https://proceedings.iclr.cc/paper_files/paper/2025/file/4252dc94531833029000f85dc5fac792-Paper-Conference.pdf) (as "Literature search")**
> A tool-enabled action where the agent formulates search queries, uses an API to find relevant scientific papers, and summarizes them to inform its gene selection.

**[StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf) (as "Substring searching")**
> Locating the position or presence of a substring within a larger string.

**[Fundamental Limitations on Subquadratic Alternatives to Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/76012c39b10425b189c38850da053893-Paper-Conference.pdf) (as "Document similarity search")**
> Selecting the most similar or least similar pair of documents from a set based on their embeddings.

**[Execution-guided within-prompt search for programming-by-example](https://proceedings.iclr.cc/paper_files/paper/2025/file/98e967164ae2f6811b975d686dece3eb-Paper-Conference.pdf) (as "Parallel search")**
> An observable search behavior where the model explores multiple distinct solution paths or program fragments within a single iteration.

**[Searching for Optimal Solutions with LLMs via Bayesian Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/a79237d6c47feef24c1df723cb41f674-Paper-Conference.pdf) (as "Word search")**
> The observable task of iteratively guessing words to find a hidden target word, guided by scalar similarity feedback.

**[Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf) (as "Inverse search")**
> Identifying an entity from its attributes when the knowledge was presented only in the forward direction during training.

**[OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf) (as "Process-level beam search")**
> Beam-search decoding that keeps and scores partial sentence-level processes during generation.

**[Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf) (as "Needle question answering")**
> Locating and reasoning about a specific short segment (needle) embedded within a longer audio (haystack), requiring precise temporal grounding.

**[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf) (as "Triple filtering")**
> Using an LLM to identify and retain only the most relevant knowledge graph triples during retrieval based on query alignment.

**[LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf) (as "Argumentative retrieval")**
> The task of retrieving text segments based on their argumentative content or stance.

**[Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf) (as "File retrieval")**
> The process of identifying and retrieving source code files most relevant to a given software issue from a large codebase.

**[Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25at/wang25at.pdf) (as "Image crop retrieval")**
> Selecting and retrieving image regions most relevant to a query based on similarity scoring between the query and image crops.

**[VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf) (as "Long video retrieval")**
> The observable task of locating and extracting a specific piece of information from a long video input based on a query.

**[Everything Everywhere All at Once: LLMs can In-Context Learn Multiple Tasks in Superposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25a/xiong25a.pdf) (as "Character retrieval")**
> Given an eight-character string, outputting a designated character from the string according to the retrieval task.

**[DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf) (as "Sentence retrieval")**
> Identifying and retrieving top-k sentences from a document that are semantically similar to a query to enrich contextual understanding.

**[SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](https://aclanthology.org/2025.emnlp-main.20.pdf) (as "Generative retrieval")**
> The task of using a generative model to directly produce document identifiers in response to a query, treating information retrieval as a sequence-to-sequence problem.

**[CROP: Contextual Region-Oriented Visual Token Pruning](https://aclanthology.org/2025.emnlp-main.493.pdf) (as "Semantic retrieval of emotion labels")**
> Retrieving the most semantically similar emotion labels from a candidate set by computing cosine similarity between sentence and label embeddings.

**[CAT: Causal Attention Tuning For Injecting Fine-grained Causal Knowledge into Large Language Models](https://aclanthology.org/2025.emnlp-main.503.pdf) (as "Text retrieval")**
> The task of finding and returning relevant documents or passages from a large corpus based on a given query text.

**[Learn and Unlearn: Addressing Misinformation in MultilingualLLMs](https://aclanthology.org/2025.emnlp-main.517.pdf) (as "Code retrieval")**
> The task of identifying and retrieving a specific function from a large code repository based on a natural language description of its behavior.

**[Teaching Your Models to Understand Code via Focal Preference Alignment](https://aclanthology.org/2025.emnlp-main.708.pdf) (as "Page retrieval")**
> Selecting a subset of document pages most relevant to a given question for downstream processing.

**[MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.709.pdf) (as "Short caption retrieval")**
> A retrieval task where the textual queries are concise, often ungrammatical phrases or keywords, mimicking real-world user search behavior.

**[MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.709.pdf) (as "Long caption retrieval")**
> A retrieval task where the textual queries are lengthy, descriptive, paragraph-level sentences.

**[Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.738.pdf) (as "Statute retrieval")**
> The observable task of identifying and ranking relevant legal statutes (sections/articles of law) applicable to a given legal case judgment.

**[Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.738.pdf) (as "Prior case retrieval")**
> Given a query case, ranking prior cases or precedents that should be cited by that case.

**[Extracting and Combining Abilities For Building Multi-lingual Ability-enhanced Large Language Models](https://aclanthology.org/2025.emnlp-main.888.pdf) (as "Argument retrieval")**
> A retrieval task that involves finding documents or passages containing arguments relevant to a specific topic or stance.

**[EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.895.pdf) (as "Literature retrieval")**
> Automatically searching and retrieving relevant scientific literature based on research queries or objectives.

**[Phi: Preference Hijacking in Multi-modal Large Language Models at Inference Time](https://aclanthology.org/2025.emnlp-main.902.pdf) (as "Tutorial retrieval")**
> Fetching potentially relevant web tutorials using the task description as a query, forming the basis for subsequent guidance generation.

**[Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning](https://aclanthology.org/2025.emnlp-main.160.pdf) (as "Support sentence retrieval")**
> The observable behavior of identifying and outputting specific sentences from a biomedical paper that provide evidence for a risk-of-bias assessment.

**[Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.188.pdf) (as "Legal case retrieval")**
> The task of identifying and ranking relevant legal cases from a large corpus in response to a query case.

**[Quantifying Language Disparities in Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.200.pdf) (as "Provision retrieval")**
> Identifying and retrieving relevant statutory provisions from a legal corpus in response to a legal question, as part of a retrieval-augmented reasoning pipeline.

**[Improving the Quality of Web-mined Parallel Corpora of Low-Resource Languages using Debiasing Heuristics](https://aclanthology.org/2025.emnlp-main.1436.pdf) (as "Structured data retrieval")**
> Performing SQL operations such as filtering, joining, aggregating, and grouping on tabular data to extract relevant information.

**[From Charts to Fair Narratives: Uncovering and Mitigating Geo-Economic Biases in Chart-to-Text](https://aclanthology.org/2025.emnlp-main.1473.pdf) (as "Ad retrieval")**
> The process of selecting and returning relevant advertisements from a large corpus in response to a user query.

**[2025.emnlp-main.1497.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1497.checklist.pdf) (as "Needle extraction")**
> The observable behavior of identifying and outputting specific target sentences embedded within a long input context.

**[MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf) (as "Cross-paragraph retrieval")**
> The task of identifying and retrieving relevant information that is distributed across multiple paragraphs within a long document.

**[How IsLLMReasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark](https://aclanthology.org/2025.emnlp-main.675.pdf) (as "Multi-step retrieval")**
> The process of retrieving information from a knowledge base in a series of discrete steps, where each step corresponds to a part of a larger reasoning plan.

**[Balanced Multi-Factor In-Context Learning for Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.1017.pdf) (as "Context retrieval")**
> Selecting and returning a subset of relevant documents or passages from a large corpus based on query similarity.

**[Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1041.pdf) (as "Scientific literature search")**
> Retrieving relevant papers from a scientific literature corpus for natural-language queries.

**[UniformInformationDensity and Syntactic Reduction: Revisiting *that*-Mentioning inEnglish Complement Clauses](https://aclanthology.org/2025.emnlp-main.1118.pdf) (as "Table-column retrieval")**
> The task of identifying and returning the specific tables and columns from a database that are relevant to answering a given natural language query.

**[CogDual: Enhancing Dual Cognition ofLLMs via Reinforcement Learning with Implicit Rule-Based Rewards](https://aclanthology.org/2025.emnlp-main.1390.pdf) (as "BioAssay retrieval")**
> Identifying and retrieving relevant biochemical screening records from PubChem based on textual similarity between a query protein description and assay metadata.

**[MrGuard: A Multilingual Reasoning Guardrail for UniversalLLMSafety](https://aclanthology.org/2025.emnlp-main.1393.pdf) (as "Content retrieval")**
> The behavior of locating and extracting specific rows, columns, or cell values from a table that are relevant to a given query.

**[ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf) (as "Simple lookup")**
> A basic form of information retrieval that involves finding a direct fact or value in a table.

**[CoEvo: Coevolution ofLLMand Retrieval Model for Domain-Specific Information Retrieval](https://aclanthology.org/2025.emnlp-main.758.pdf) (as "Cross-lingual retrieval")**
> Retrieving relevant documents in one language (e.g., English) in response to a query in another language, based on aligned multilingual embeddings.

**[Rewarding the Unlikely: LiftingGRPOBeyond Distribution Sharpening](https://aclanthology.org/2025.emnlp-main.1299.pdf) (as "Keyword sequence retrieval")**
> The process of identifying a sequence of L1 words whose pronunciation approximates segments of an L2 target word, based on phonological and syllabic alignment.

**[MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1577.pdf) (as "Relevant fact extraction")**
> The observable task of identifying and retrieving specific pieces of information from a larger context of text and tables that are necessary to answer a given question.

**[SEMMA: A Semantic Aware Knowledge Graph Foundation Model](https://aclanthology.org/2025.emnlp-main.1622.pdf) (as "Web data retrieval")**
> Locating and retrieving external data from the web before generating visualizations, in response to queries that do not provide complete data tables.

**[Evaluating Large Language Models for Detecting Antisemitism](https://aclanthology.org/2025.emnlp-main.1793.pdf) (as "Retrieval noise reduction")**
> The observable outcome of a retrieval process that minimizes the number of irrelevant facts included in the retrieved subgraph.

**[OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf) (as "Database retrieval")**
> The observable process of selecting the correct target database from a large pool of candidate databases based on a natural language query.

**[Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.34.pdf) (as "Iterative retrieval")**
> The process of generating multiple search queries in sequence, retrieving evidence at each step, and using the results to inform subsequent queries, as implemented in agentic RAG systems.

**[DART: Distilling Autoregressive Reasoning to Silent Thought](https://aclanthology.org/2025.emnlp-main.257.pdf) (as "Think-and-search")**
> The observable behavior of an LLM alternating between internal reasoning (thinking) and external knowledge retrieval (searching) across multiple steps to answer complex queries.

**[CLIP-MoE: Towards Building Mixture of Experts forCLIPwith Diversified Multiplet Upcycling](https://aclanthology.org/2025.emnlp-main.276.pdf) (as "Reasoning with retrieved documents")**
> The behavior of incorporating retrieved external knowledge into the ongoing reasoning chain to support accurate problem solving.

**[Beyond Input Activations: Identifying Influential Latents by Gradient Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.88.pdf) (as "Retrieval-augmented generation")**
> The process of generating answers to questions using a language model that conditions its output on retrieved documents, aiming to reduce hallucinations and improve factual accuracy.

**[Data-Efficient Hate Speech Detection via Cross-Lingual Nearest Neighbor Retrieval with Limited Labeled Data](https://aclanthology.org/2025.emnlp-main.1508.pdf) (as "Knowledge-grounded response generation")**
> The task of generating conversational responses that are based on information from an external knowledge source.

**[Improving Cross Lingual Transfer by Pretraining with Active Forgetting](https://aclanthology.org/2025.emnlp-main.121.pdf) (as "Image retrieval")**
> Finding semantically similar images from a database based on visual content of a query image.

**[Investigating Neurons and Heads in Transformer-basedLLMs for Typographical Errors](https://aclanthology.org/2025.emnlp-main.314.pdf) (as "Cross-file retrieval")**
> Locating and utilizing relevant code, constants, or class definitions from files other than the one being modified, to ensure correct implementation.

**[Rethinking Backdoor Detection Evaluation for Language Models](https://aclanthology.org/2025.emnlp-main.319.pdf) (as "Expert retrieval")**
> The specific action of identifying and selecting the most appropriate pre-trained expert module for a given task or token.

**[Certainty in Uncertainty: Reasoning over Uncertain Knowledge Graphs with Statistical Guarantees](https://aclanthology.org/2025.emnlp-main.442.pdf) (as "Entity retrieval")**
> Identifying and retrieving candidate entities from a knowledge base that correspond to mentions in a natural language question.

**[Certainty in Uncertainty: Reasoning over Uncertain Knowledge Graphs with Statistical Guarantees](https://aclanthology.org/2025.emnlp-main.442.pdf) (as "Relation retrieval")**
> The process of identifying and retrieving relations from a knowledge base that are semantically relevant to a given question.

**[MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.709.pdf) (as "Text-to-image retrieval")**
> The task of finding the most relevant image(s) from a collection given a textual query.

**[Media Source Matters More Than Content: Unveiling Political Bias inLLM-Generated Citations](https://aclanthology.org/2025.emnlp-main.873.pdf) (as "Reasoning path retrieval")**
> Extracting sequences of relations and entities from a knowledge graph that are semantically relevant to a natural language question.

**[Governance in Motion: Co-evolution of Constitutions andAImodels for Scalable Safety](https://aclanthology.org/2025.emnlp-main.870.pdf) (as "Web content retrieval")**
> Observable behavior in which the LLM uses search APIs to retrieve and process HTML content from webpages relevant to a user query for response generation.

**[SAFE-SQL: Self-Augmented In-Context Learning with Fine-grained Example Selection for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.963.pdf) (as "Dense retrieval")**
> The task of retrieving relevant documents from a collection by encoding queries and documents into a shared embedding space and finding the nearest neighbors.

**[Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups](https://aclanthology.org/2025.emnlp-main.943.pdf) (as "Semantic retrieval")**
> Matching multimodal entity pairs to natural language relation descriptions based on semantic similarity in a shared embedding space, rather than selecting from discrete labels.

**[Enhancing Large Language Model for Knowledge Graph Completion via Structure-Aware Alignment-Tuning](https://aclanthology.org/2025.emnlp-main.1062.pdf) (as "Retrieval-augmented question answering")**
> The task of generating an answer to a question by first retrieving relevant context from a corpus of documents and then synthesizing the final response based on that context.

**[GER-LLM: Efficient and Effective Geospatial Entity Resolution with Large Language Model](https://aclanthology.org/2025.emnlp-main.1187.pdf) (as "Dataflow-guided retrieval")**
> Retrieving code information based on data dependency relations in a dataflow graph built from the unfinished code file.

**[GER-LLM: Efficient and Effective Geospatial Entity Resolution with Large Language Model](https://aclanthology.org/2025.emnlp-main.1187.pdf) (as "Sparse retrieval")**
> Retrieving code knowledge based on keyword matching between the query and codebase using methods like TF-IDF.

**[Analyzing values about gendered language reform inLLMs’ revisions](https://aclanthology.org/2025.emnlp-main.1278.pdf) (as "Demonstration retrieval")**
> The process by which the LLM retrieves top-k contextually relevant annotated examples from a retrieval corpus to include in the prompt for guiding inference on a test query.

**[HyperKGR: Knowledge Graph Reasoning in Hyperbolic Space with Graph Neural Network Encoding Symbolic Path](https://aclanthology.org/2025.emnlp-main.1280.pdf) (as "Material property retrieval")**
> The observable task of extracting specific physical or chemical properties of materials, such as bulk modulus, bandgap, or formation energy, from structured databases.

**[LASER: AnLLM-basedASRScoring and Evaluation Rubric](https://aclanthology.org/2025.emnlp-main.1258.pdf) (as "Multi-hop evidence retrieval")**
> The task of retrieving secondary evidence based on an initial piece of information, used here to evaluate the utility of decontextualised sentences as intermediate reasoning steps.

**[HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuningLLMwith Zeroth-order Optimization](https://aclanthology.org/2025.emnlp-main.1324.pdf) (as "Multimodal document retrieval")**
> The task of identifying and returning the most relevant document pages, containing both text and images, from a large collection in response to a user's text query.

**[SimMark: A Robust Sentence-Level Similarity-Based Watermarking Algorithm for Large Language Models](https://aclanthology.org/2025.emnlp-main.1568.pdf) (as "Visual document retrieval")**
> Retrieving relevant documents from a collection given a text query over document images or their generated descriptions.

**[AutoCT: Automating Interpretable Clinical Trial Prediction withLLMAgents](https://aclanthology.org/2025.emnlp-main.1576.pdf) (as "Cascade retrieval")**
> A two-stage retrieval process where page-level retrieval is performed first, followed by layout-level retrieval within the set of initially retrieved pages.

**[AutoCT: Automating Interpretable Clinical Trial Prediction withLLMAgents](https://aclanthology.org/2025.emnlp-main.1576.pdf) (as "Layout-level retrieval")**
> The observable task of detecting and returning specific layout elements, such as paragraphs, figures, or tables, that contain the evidence for a user's query.

**[SimMark: A Robust Sentence-Level Similarity-Based Watermarking Algorithm for Large Language Models](https://aclanthology.org/2025.emnlp-main.1568.pdf) (as "Multilingual retrieval")**
> Retrieving relevant documents across multiple languages using queries and document collections in different languages.

**[A Multilingual, Culture-First Approach to Addressing Misgendering inLLMApplications](https://aclanthology.org/2025.emnlp-main.1588.pdf) (as "Text-to-video retrieval")**
> The task of identifying and ranking the most relevant videos from a collection in response to a natural language text query.

**[Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation](https://aclanthology.org/2025.emnlp-main.1683.pdf) (as "Attribute-based retrieval")**
> Retrieving memory instances by matching current attributes against stored augmentation attributes.

**[Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation](https://aclanthology.org/2025.emnlp-main.1683.pdf) (as "Comprehensive retrieval")**
> Retrieving all related memory instances together with their associated augmentations for context-aware inference.

**[Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation](https://aclanthology.org/2025.emnlp-main.1683.pdf) (as "Embedding-based retrieval")**
> Retrieving memory instances by embedding augmentation attributes and selecting the most similar entries via vector similarity search.

**[Mechanisms vs. Outcomes: Probing for Syntax Fails to Explain Performance on Targeted Syntactic Evaluations](https://aclanthology.org/2025.emnlp-main.1713.pdf) (as "Hard negative retrieval")**
> Selecting semantically similar but subtly incorrect alternative captions to challenge the model during training and improve discriminative learning.

**[STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Academic paper search")**
> The task of retrieving relevant academic papers from a bibliographic knowledge base based on a user's query about authors, topics, institutions, or citations.

**[Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf) (as "Retrieval capability")**
> The ability to locate and use relevant information from long contexts when answering or continuing from the input.

**[Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf) (as "In-context retrieval")**
> The ability to locate and use specific information provided within a long context.

**[Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f649556471416b35e60ae0de7c1e3619-Paper-Conference.pdf) (as "Retrieval ability")**
> The latent capacity to locate and recover relevant information from long contexts when answering a query.

**[RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf) (as "Knowledge utilization")**
> The latent ability of a model to effectively incorporate and make use of externally provided information, such as retrieved documents, to perform a task.

**[BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf) (as "Reasoning-intensive retrieval")**
> The ability to identify relevant documents for a query based on deep, nuanced connections like underlying principles, algorithms, or theorems, rather than simple keyword or semantic matching.

**[Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf) (as "Knowledge retrieval depth")**
> The extent to which a system can retrieve sufficiently detailed and complete information for answering complex questions.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "Retrieval utility")**
> The degree to which externally retrieved information contributes to the overall performance and correctness of a model's generation, quantified as a shift in the model's belief toward the ground-truth answer.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "Knowledge gain")**
> The increase in an LLM's knowledge or certainty about a topic resulting from exposure to new information, which can be estimated by the shift in its internal knowledge distribution.

**[Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf) (as "Search ability")**
> The latent capacity of a model to find a correct next step or path toward a goal across graph-like or reasoning problems.

**[The KoLMogorov Test: Compression by Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/db1d69ee01c2b42554f8e14e6f8ca8b6-Paper-Conference.pdf) (as "Search")**
> The latent ability to explore candidate programs and find one that matches the target sequence under a shortest-program criterion.

**[Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf) (as "Retrieval efficiency")**
> The degree to which the model can find relevant graph information with fewer search steps or less wasted exploration.

**[MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf) (as "Multimodal search capability")**
> The latent ability of a model to use both visual and textual information to retrieve, rank, and synthesize answers from web content in a search setting.

**[MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf) (as "Inspiration retrieval ability")**
> The latent ability to identify literature items that can be associated with a research background to support novel hypothesis generation.

**[MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf) (as "Multimodal retrieval capability")**
> The latent ability of a model to retrieve relevant documents from a corpus containing diverse modalities (e.g., text, images, text-image pairs) in response to a query that may also be multimodal.

**[MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf) (as "Text retrieval capability")**
> The ability to perform retrieval effectively in text-to-text settings, where both queries and candidates are text.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "Semantic retrieval capability")**
> The ability of a long-context model to understand the semantic meaning of a query to retrieve relevant information, rather than relying on exact string matches.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "String retrieval capability")**
> The fundamental ability of a long-context model to retrieve specific, exact-match information from long and potentially noisy input sequences.

**[C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations](https://aclanthology.org/2025.emnlp-main.1161.pdf) (as "Answer retrieval")**
> The latent ability to locate and extract the correct answer from a context in one language based on a cross-lingually encoded query, independent of language-specific surface forms.

**[C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations](https://aclanthology.org/2025.emnlp-main.1161.pdf) (as "Cross-lingual context retrieval")**
> The latent ability of a model to retrieve relevant contextual information in one language (e.g., English) when prompted with a query in a different language, relying on aligned multilingual representations.

## Relationships

### Information retrieval →
- **Needle-in-a-haystack test** (measurements) — *measured_by*
  - [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf)
- **RULER** (measurements) — *measured_by*
  > RULER (Hsieh et al., 2024) is a more complex benchmark containing NIAH tests, such as finding multiple passkeys and tracking variable changes inside complicated essay-style haystack sentences. (Section 5.3)
  - [LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5d50d269e52f8eed497062311ff173-Paper-Conference.pdf)
- **MS MARCO** (measurements) — *measured_by*
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **BEIR** (measurements) — *measured_by*
  > Using the Qwen-2.5-32B model, we annotate utility on the MS MARCO dataset and conduct retrieval experiments on MS MARCO and BEIR... (Abstract)
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
- **MTEB** (measurements) — *measured_by*
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **BRIGHT** (measurements) — *measured_by*
  > "we evaluate it with the reasoning-intensive retrieval benchmark BRIGHT"
  - [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf)
- **AIR-Bench** (measurements) — *measured_by*
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  > The evaluation leverages three datasets: NaturalQuestions (NQ) (Kwiatkowski et al., 2019), TriviaQA (TQA) (Joshi et al., 2017) and WebQA (WebQ) (Berant et al., 2013), and a specilized task KV Retrieval (Liu et al., 2024). (Section 5.1)
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > The evaluation leverages three datasets: NaturalQuestions (NQ) (Kwiatkowski et al., 2019), TriviaQA (TQA) (Joshi et al., 2017) and WebQA (WebQ) (Berant et al., 2013), and a specilized task KV Retrieval (Liu et al., 2024). (Section 5.1)
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > “For more complex tasks, such as multi-hop QA and dialogue, we use HotpotQA dataset (Yang et al., 2018) and Wikipedia of Wizard (WoW) (Dinan et al., 2019) for evaluation.”
  - [ESE: Espresso Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2025/file/60dc26558762425a465cb0409fc3dc52-Paper-Conference.pdf)
- **InfiniteBench** (measurements) — *measured_by*
  > Table 2 shows that our method preserves most of the model's performance in retrieval and QA tasks
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
- **SlideVQA** (measurements) — *measured_by*
  > We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA (Tanaka et al., 2023), MM-LongBench (Ma et al., 2024d), DUDE (Van Landeghem et al., 2023), DocVQA (Mathew et al., 2020; 2021) and VisR-Bench. (Section 5)
  - [SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **NFCorpus** (measurements) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **MMLU** (measurements) — *measured_by*
  > These tasks assess the model performance on logical reasoning, language understanding, commonsense reasoning, and knowledge utilization. (Section 4.1)
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **BM25** (measurements) — *measured_by*
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **DPR** (measurements) — *measured_by*
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **Flickr30k Entities** (measurements) — *measured_by*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **IMDb** (measurements) — *measured_by*
  - [UQE: A Query Engine for Unstructured Databases](https://proceedings.neurips.cc/paper_files/paper/2024/file/34b3a40ec9752c1ae48fe85fef8fe8dc-Paper-Conference.pdf)
- **CLEVR** (measurements) — *measured_by*
  - [UQE: A Query Engine for Unstructured Databases](https://proceedings.neurips.cc/paper_files/paper/2024/file/34b3a40ec9752c1ae48fe85fef8fe8dc-Paper-Conference.pdf)
- **SWDE** (measurements) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *causes*
  - [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LOFT** (measurements) — *measured_by*
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  > We believe that this benchmark is the most important because it shows both long context generation performance and knowledge retrieval performance
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
- **Expressive power** (constructs) — *causes*
  > Our positive results showing that enhancing in-context retrieval can improve RNNs’ representation power hold for vanilla Linear RNNs, and can be easily extended to more complex architectures. (Section 1)
  - [RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *causes*
  - [Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf)
- **DocVQA** (measurements) — *measured_by*
  - [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1166.pdf)
- **SQuAD v2.0** (measurements) — *measured_by*
  > Document Retrieval In this task the model receives a query and Ndocs randomly assorted documents, and its objective is to return the id of the matching document. Our data is sampled from SQuAD v2 (Rajpurkar et al., 2018). (Section 5)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **MIRACL** (measurements) — *measured_by*
  - [AFRIDOC-MT: Document-levelMTCorpus forAfrican Languages](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **LongEval** (measurements) — *measured_by*
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
- **Autoformalization** (behaviors tasks) — *causes*
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
- **ProofNet** (measurements) — *measured_by*
  > Table 2 demonstrates the results on the ProofNet benchmark.
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
- **Needlebench** (measurements) — *measured_by*
  > “For NeedleBench, both Rodimus and Rodimus+ even exceed the performance of Pythia”
  - [CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfae940651f3e690a12e19c874edad7c-Paper-Conference.pdf)
- **ToolBench** (measurements) — *measured_by*
  > Our experiments are based on ToolBench, a real-world tool benchmark containing more 16k tool collections... Our retrieval and end-to-end agent-tuning data are converted from the original data in ToolBench. (Section 4.1)
  - [ToolGen: Unified Tool Retrieval and Calling via Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b646bdebeb87dfafe2c6f77a63b564e1-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > These tasks assess the model performance on logical reasoning, language understanding, commonsense reasoning, and knowledge utilization. (Section 4.1)
  - [TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-ExpertsLLMs](https://aclanthology.org/2025.emnlp-main.1115.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  > [VISUAL RETRIEVAL] aims to evaluate the ability of models to retrieval images that contain the same building. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Answer generation** (behaviors tasks) — *causes*
  - [Aligning Sentence Simplification withESLLearner’s Proficiency for Language Acquisition](https://aclanthology.org/2025.naacl-long.22.pdf)
- **Qasper** (measurements) — *measured_by*
  - [Steering Knowledge Selection Behaviours inLLMs viaSAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.265.pdf)
- **MLDR** (measurements) — *measured_by*
  - [Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning](https://aclanthology.org/2025.emnlp-main.1545.pdf)
- **ArXivQA** (measurements) — *measured_by*
  - [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1166.pdf)
- **ChartQA** (measurements) — *measured_by*
  - [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1166.pdf)
- **V-NIAH** (measurements) — *measured_by*
  > “Video Needle in a Haystack (V-NIAH) (Zhang et al., 2024a): A long-video retrieval task”
  - [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf)
- **ViDoSeek** (measurements) — *measured_by*
  - [HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuningLLMwith Zeroth-order Optimization](https://aclanthology.org/2025.emnlp-main.1324.pdf)
- **Real-MM-RAG** (measurements) — *measured_by*
  - [HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuningLLMwith Zeroth-order Optimization](https://aclanthology.org/2025.emnlp-main.1324.pdf)
- **WebQA** (measurements) — *measured_by*
  > The evaluation leverages three datasets: NaturalQuestions (NQ) (Kwiatkowski et al., 2019), TriviaQA (TQA) (Joshi et al., 2017) and WebQA (WebQ) (Berant et al., 2013), and a specilized task KV Retrieval (Liu et al., 2024). (Section 5.1)
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **TableEval** (measurements) — *measured_by*
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf)
- **SCIDOCS** (measurements) — *measured_by*
  - [MoMoE: Mixture of Moderation Experts Framework forAI-Assisted Online Governance](https://aclanthology.org/2025.emnlp-main.639.pdf)

### → Information retrieval
- **Task decomposition** (behaviors tasks) — *causes*
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
- **Data contamination** (constructs) — *measured_by*
  - [What's In My Big Data?](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f7336fd66b6e6e63d1801fdd5930a5a-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Semantic understanding** (constructs) — *causes*
  > To build semantic index for files in the LSFS, we leverage an a lightweight embedding model, i.e., all-MiniLM-L6-v2 (Reimers & Gurevych, 2019), commonly used in vector databases, thereby supporting more advanced file operations which requires semantic understanding of file content. (Section 3)
  - [From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf)
- **Memory** (constructs) — *measured_by*
  - [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *causes*
  - [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/ccdfe117c6729267c1595cdf0a587da8-Paper-Conference.pdf)
- **Query expansion** (behaviors tasks) — *causes*
  - [Proxy-Driven Robust Multimodal Sentiment Analysis with Incomplete Data](https://aclanthology.org/2025.acl-long.1076.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [Fourier Position Embedding: Enhancing Attention’s Periodic Extension for Length Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hua25b/hua25b.pdf)
- **In-context learning** (constructs) — *causes*
  - [AISees YourLocation—But With A Bias Toward The Wealthy World](https://aclanthology.org/2025.emnlp-main.911.pdf)

### Associated with
- **Long-context understanding** (constructs)
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks)
  > Information Retrieval. Effective search functionality is essential in SNS. Models should interpret query intent and retrieve relevant information from large datasets, delivering the most accurate results. Tasks: (3) Note-NER. Extracts named entities from note content.
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Knowledge recall** (behaviors tasks)
  > RNNs with CoT cannot solve a set of fundamental algorithmic problems that directly ask for in-context retrieval, including associative recall. (Section 1)
  - [RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
- **Long-context processing** (constructs)
  - [PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks)
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > "To mitigate these issues, integrating external knowledge sources through retrieval-augmented generation (RAG) has become a widely adopted and effective paradigm"
  - [Automated Knowledge Graph Construction using Large Language Models and Sentence Complexity Modelling](https://aclanthology.org/2025.emnlp-main.784.pdf)
- **Reversal curse** (constructs)
  - [Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4b95476f673e6e538f80862f622ba2f-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Look Before You Leap: Universal Emergent Mechanism for Retrieval in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad36c2cfc423e75c6d68d751a955b22e-Paper-Conference.pdf)
- **Memory management** (constructs)
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Decision-making** (constructs)
  - [JMMMU: AJapanese Massive Multi-discipline Multimodal Understanding Benchmark for Culture-aware Evaluation](https://aclanthology.org/2025.naacl-long.44.pdf)
- **Knowledge memorization** (constructs)
  - [Mix-CPT: A Domain Adaptation Framework via Decoupling Knowledge Learning and Format Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc721384c26c0bdff3ec31a7de31d8d5-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Human preference alignment** (constructs)
  > “To perform well on our benchmark, LLMs should demonstrate four key capabilities: (1) Preference Inference—the capacity to accurately infer user preferences through dialogue, whether explicitly stated or implicitly revealed; (2) Long-Context Retrieval—the ability to track and recall user preferences across long conversation”
  - [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/28a46044775d97a4efcbcf14e7f13209-Paper-Conference.pdf)
- **Planning** (constructs)
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
- **State tracking** (constructs)
  - [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
- **Theorem proving** (behaviors tasks)
  > “The ability to search is fundamental in many important tasks, such as reasoning ... planning ... and navigation ... Recent work has demonstrated that transformer-based large language models (LLMs) struggle with proof search”
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf)
- **Knowledge manipulation** (constructs)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **Temporal reasoning** (constructs)
  > "Retrieval task is the basic NIAH task aimed at evaluating the long-context video model’s ability to retrieve a single needle. This task specifically assesses the model’s capability for temporal perception and understanding across the time dimension."
  - [Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Visual recognition** (constructs)
  - [Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Positional bias** (constructs)
  > In retrieval tasks, PB predominantly manifests as token-shifting... (Section 1)
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Temporal video grounding** (behaviors tasks)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Query generation** (behaviors tasks)
  > Recent works like Search-R1 (Jin et al., 2025) and R1-Searcher (Song et al., 2025) use reinforcement learning to optimize reasoning-based query generation while keeping the retrieval model fixed. (Section 2)
  - [SAFENUDGE: Safeguarding Large Language Models in Real-time with Tunable Safety-Performance Trade-offs](https://aclanthology.org/2025.emnlp-main.1011.pdf)
- **Context utilization** (constructs)
  - [Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf)
- **Schema linking** (behaviors tasks)
  > Through error analysis, we identify two major challenges in schema linking: (1) Database Retrieval: accurately selecting the target database from a large schema pool, while effectively filtering out irrelevant ones
  - [OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Length generalization** (constructs)
  - [Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning](https://aclanthology.org/2025.emnlp-main.1545.pdf)
- **Cross-lingual alignment** (constructs)
  > Cross-lingual context retrieval (extracting contextual information in one language based on requests in another) is a fundamental aspect of cross-lingual alignment (Abstract).
  - [C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations](https://aclanthology.org/2025.emnlp-main.1161.pdf)

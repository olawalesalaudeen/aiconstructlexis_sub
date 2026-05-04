# Information retrieval
**Type:** Construct  
**Referenced in:** 82 papers  
**Also known as:** Factual knowledge retrieval, Information retrieval and localization, Retrievability, Associative memory retrieval, Causal retrieval, In-context retrieval, Information retrieval capability, Parametric knowledge retrieval, Retrieval, Task vector retrieval, Knowledge retrieval, Long-context retrieval, Retrieval capability, Retrieval performance  

## Sources

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Factual knowledge retrieval")**
> The model's ability to access and retrieve stored factual information when prompted.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Information retrieval and localization")**
> The latent ability to locate, search for, and extract relevant information from context memory based on instructions or queries, treating the context as a dynamic memory store.

**[PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25da/zhang25da.pdf) (as "Retrievability")**
> The latent property of a poison sample to be successfully retrieved by the system in response to a target query, determined by its embedding proximity to the query.

**[In-Context Learning as Conditioned Associative Memory Retrieval](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25k/wu25k.pdf) (as "Associative memory retrieval")**
> The latent capacity of a model to retrieve stored patterns or knowledge by matching a query to the most relevant memory through similarity-based dynamics, akin to Hopfield network behavior.

**[Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf) (as "Causal retrieval")**
> The latent ability to retrieve past contextual chunks that are most useful for predicting future chunks, trained end-to-end via gradient propagation through relevance scores.

**[Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf) (as "In-context retrieval")**
> The latent ability to precisely locate and extract relevant information from earlier in the input sequence, particularly for mapping contextual cues to specific outputs such as answer labels.

**[Attention-Level Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cai25g/cai25g.pdf)**
> The latent ability to locate and extract specific, relevant pieces of information from a large body of text.

**[LOGO — Long cOntext aliGnment via efficient preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25j/tang25j.pdf) (as "Information retrieval capability")**
> The model's underlying ability to accurately locate and identify key, salient pieces of information embedded within a long context.

**[Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf) (as "Parametric knowledge retrieval")**
> The latent ability of a model to retrieve factual knowledge that has been encoded during pre-training, independent of the current input context.

**[PhantomWiki: On-Demand Datasets for Reasoning and Retrieval Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25d/gong25d.pdf) (as "Retrieval")**
> The latent ability to access and utilize relevant information from a large external document corpus, especially when the full corpus exceeds the model's context window.

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Task vector retrieval")**
> The latent ability of a transformer to extract a high-level task concept vector from demonstration pairs during in-context learning, enabling generalization across queries within the same task.

**[CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf) (as "Knowledge retrieval")**
> The latent ability to recall factual knowledge stored during pre-training, which is required when contextual information is insufficient for answering a question.

**[On the Vulnerability of Text Sanitization](https://aclanthology.org/2025.naacl-long.267.pdf) (as "Long-context retrieval")**
> The model's behavior of answering questions based on very long input documents, requiring efficient processing of extensive prefilling contexts.

**[CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf) (as "Retrieval capability")**
> The underlying ability of an LLM to identify and access relevant external documents or facts necessary to answer a query, either directly or through generated search queries.

**[MILU: A Multi-taskIndic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.508.pdf) (as "Retrieval performance")**
> The latent ability of a ToD system to retrieve relevant and accurate information from a knowledge store in response to user queries, particularly under varying levels of ambiguity.

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

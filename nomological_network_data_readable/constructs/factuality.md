# Factuality
**Type:** Construct  
**Referenced in:** 336 papers  
**Also known as:** Factual correctness, Hallucination, Knowledge hallucination, Molecular hallucination, Object hallucination, Truth alignment, Correctness, Factual precision, Factual recall, Factual consistency, Prompt faithfulness, Unfaithfulness, Fact recall, Object existence determination, Reasoning hallucinations, Reference reliability, Long-term knowledge recall, Recall capability, Associative recall, Knowledge recall, Factual knowledge recall, Association recall, Associative recall capacity, Statistical recall, Factual knowledge retrieval, Information retrieval and localization, Retrievability, Associative memory retrieval, Causal retrieval, In-context retrieval, Information retrieval capability, Parametric knowledge retrieval, Retrieval, Task vector retrieval  

## State of the Field

Across the provided literature, factuality is most commonly discussed through its failure mode, termed "hallucination," which is broadly defined as the generation of information that is factually incorrect or not supported by a given context. The positive framing of the construct, appearing under names like "factual correctness," "faithfulness," and "truthfulness," consistently refers to the degree to which a model's output aligns with a source of truth, which can be real-world knowledge, a provided document, or visual input. The concept is applied in specialized domains, leading to more specific definitions like "object hallucination" for describing non-existent items in images and "reasoning hallucinations" for logical inconsistencies in generated thought processes. A large portion of the work operationalizes factuality as a model's latent ability to recall or retrieve information, using terms like "fact recall" and "associative recall" to describe accessing knowledge stored in its parameters or provided in-context. This construct is measured using a wide array of benchmarks, including question-answering datasets like TriviaQA and Natural Questions, multitask evaluations like MMLU, and knowledge-conflict datasets such as CounterFact. A recurring theme is the distinction between grounding in a provided source versus parametric knowledge, with one study noting that hallucinations are "grounding errors: errors where the output contains some information that is not supported by the context" (Teaching Language Models to Hallucinate Less with Synthetic Tasks). Factuality is studied alongside related concepts like commonsense knowledge and is reported in some work to influence long-context understanding. Ultimately, the surveyed papers treat factuality as a multifaceted construct concerning the alignment of generated content with verifiable information, with its absence being a widely documented failure.

## Sources

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf) (as "Hallucination")**
> An observable failure mode where the model generates information that is factually incorrect or not supported by the provided context.

**[Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf) (as "Factual accuracy")**
> The degree to which a model's generated statements are factually correct and free from errors.

**[Attention Satisfies: A Constraint-Satisfaction Lens on Factual Errors of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/880ee6e23b6ee548ebcccafe0ef0f513-Paper-Conference.pdf) (as "Factual correctness")**
> The degree to which a model's generated text, particularly its reasoning steps and final answers, aligns with established facts from external knowledge sources.

**[An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)**
> The degree to which a model's generated statements are factually correct and grounded in real-world knowledge.

**[Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/592da1445a51e54a3987958b5831948f-Paper-Conference.pdf) (as "Factual knowledge")**
> The extent to which a model stores and can retrieve correct world facts from its parameters when queried.

**[Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf) (as "Object hallucination")**
> The generation of textual descriptions that refer to objects not actually present in the input image.

**[KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf) (as "Knowledge hallucination")**
> The tendency of a model to generate content that is inconsistent with actual facts, even when those facts are provided, reflecting a failure in knowledge faithfulness.

**[Domain-Agnostic Molecular Generation with Chemical Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed7dd1e32cf9b0abf664bf0e891527e5-Paper-Conference.pdf) (as "Molecular hallucination")**
> The model's latent tendency to generate molecules that are structurally and syntactically correct but fail to exhibit the expected chemical activity or practical utility in real-world applications.

**[Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf) (as "Truthfulness")**
> The degree to which a model's generated statements correspond to factual reality.

**[SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation](https://proceedings.neurips.cc/paper_files/paper/2024/file/217bb44ab14621754db8a392163e6b07-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Reasoning faithfulness")**
> The extent to which a model's stated reasoning or answer behavior remains grounded in the provided evidence rather than being driven by misleading annotations or shortcuts.

**[CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Truth alignment")**
> The extent to which a model's outputs match the ground truth in the required answer form for a task.

**[G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf) (as "Faithfulness")**
> The degree to which the model's generated responses are factually grounded in and supported by the information provided in the source graph.

**[Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf) (as "Correctness")**
> The factual accuracy and correctness of the information provided in the model's response.

**[Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf) (as "Factual precision")**
> The proportion of factual claims in a model's response that are supported by external knowledge sources.

**[Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf) (as "Factual recall")**
> The extent to which a response includes enough supported facts to satisfy a user-preferred response length.

**[SeafloorAI: A Large-scale Vision-Language Dataset for Seafloor Geological Survey](https://proceedings.neurips.cc/paper_files/paper/2024/file/274de7d60333c0848f42e18ae97f13e3-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Factual consistency")**
> The degree to which generated annotations agree with the original ground-truth or source annotations.

**[Who Evaluates the Evaluations? Objectively Scoring Text-to-Image Prompt Coherence Metrics with T2IScoreScore (TS2)](https://proceedings.neurips.cc/paper_files/paper/2024/file/9b9cfd5428153ccfbd4ba34b7e007305-Paper-Conference.pdf) (as "Prompt faithfulness")**
> The degree to which a generated image semantically aligns with and satisfies the requirements of the text prompt it was conditioned on.

**[MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Unfaithfulness")**
> The tendency of a model to generate information that is not grounded in the provided source document.

**[KoLA: Carefully Benchmarking World Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c26719edf1e6fba8f1ca7d3938e27785-Paper-Conference.pdf) (as "Fact recall")**
> The latent ability to retrieve specific factual knowledge from training data when prompted.

**[LibEvolutionEval: A Benchmark and Study for Version-Specific Code Generation](https://aclanthology.org/2025.naacl-long.349.pdf) (as "Object existence determination")**
> The model's latent capability to correctly identify whether a specified object is present or absent in a given image.

**[Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf) (as "Reasoning hallucinations")**
> The latent tendency of LLMs to generate reasoning steps in natural language that are inconsistent with the logic of generated programs, manifesting as logical errors, missing steps, or misordered connections despite seemingly correct justifications.

**[POINTS-Reader: Distillation-Free Adaptation of Vision-Language Models for Document Conversion](https://aclanthology.org/2025.emnlp-main.83.pdf) (as "Reference reliability")**
> The latent ability of a model to generate citations that correspond to real, existing academic publications with accurate metadata.

**[Context-Aware Hierarchical Taxonomy Generation for Scientific Papers viaLLM-Guided Multi-Aspect Clustering](https://aclanthology.org/2025.emnlp-main.789.pdf) (as "Long-term knowledge recall")**
> The latent ability to access and retrieve stored factual knowledge about the world, such as historical, scientific, or geographical facts, independent of the current context.

**[Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf) (as "Recall capability")**
> The model's ability to retrieve specific, factual information from a long context provided as input.

**[Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf) (as "Recall")**
> The latent reliance on statistical correlations or training data retrieval rather than genuine reasoning processes.

**[Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf) (as "Associative recall")**
> The ability to retrieve a specific value when prompted with its associated key.

**[Uncovering Overfitting in Large Language Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/c592fc7e6207f82560ed45fece8d6937-Paper-Conference.pdf) (as "Knowledge recall")**
> The ability of an edited model to retrieve newly edited factual knowledge when prompted directly or through paraphrase.

**[Learning to Look at the Other Side: A Semantic Probing Study of Word Embeddings inLLMs with Enabled Bidirectional Attention](https://aclanthology.org/2025.acl-long.1133.pdf) (as "Factual knowledge recall")**
> The latent ability of a model to access and utilize stored factual information relevant to a given context during reasoning.

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Factual knowledge retrieval")**
> The model's ability to access and retrieve stored factual information when prompted.

**[Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf) (as "Associative recall capacity")**
> The ability of a model to retrieve stored information based on contextual cues, such as recovering a value given a key or predicting the successor of a previously seen token.

**[NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/modarressi25a/modarressi25a.pdf) (as "Association recall")**
> The fundamental ability to recall previously seen information based on associative links present in the input context.

**[RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf) (as "Statistical recall")**
> The degree to which a model's performance relies on recognizing and reproducing patterns from its training data rather than engaging in systematic reasoning.

**[Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bick25a/bick25a.pdf) (as "In-context retrieval")**
> The latent ability to precisely locate and extract relevant information from earlier in the input sequence, particularly for mapping contextual cues to specific outputs such as answer labels.

**[Provable In-Context Vector Arithmetic via Retrieving Task Concepts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bu25a/bu25a.pdf) (as "Task vector retrieval")**
> The latent ability of a transformer to extract a high-level task concept vector from demonstration pairs during in-context learning, enabling generalization across queries within the same task.

**[Attention-Level Speculation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cai25g/cai25g.pdf) (as "Information retrieval")**
> The latent ability to locate and extract specific, relevant pieces of information from a large body of text.

**[PhantomWiki: On-Demand Datasets for Reasoning and Retrieval Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25d/gong25d.pdf) (as "Retrieval")**
> The latent ability to access and utilize relevant information from a large external document corpus, especially when the full corpus exceeds the model's context window.

**[Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25v/hu25v.pdf) (as "Causal retrieval")**
> The latent ability to retrieve past contextual chunks that are most useful for predicting future chunks, trained end-to-end via gradient propagation through relevance scores.

**[Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25f/jin25f.pdf) (as "Parametric knowledge retrieval")**
> The latent ability of a model to retrieve factual knowledge that has been encoded during pre-training, independent of the current input context.

**[LOGO — Long cOntext aliGnment via efficient preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25j/tang25j.pdf) (as "Information retrieval capability")**
> The model's underlying ability to accurately locate and identify key, salient pieces of information embedded within a long context.

**[In-Context Learning as Conditioned Associative Memory Retrieval](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25k/wu25k.pdf) (as "Associative memory retrieval")**
> The latent capacity of a model to retrieve stored patterns or knowledge by matching a query to the most relevant memory through similarity-based dynamics, akin to Hopfield network behavior.

**[Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf) (as "Information retrieval and localization")**
> The latent ability to locate, search for, and extract relevant information from context memory based on instructions or queries, treating the context as a dynamic memory store.

**[PoisonedEye: Knowledge Poisoning Attack on Retrieval-Augmented Generation based Large Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25da/zhang25da.pdf) (as "Retrievability")**
> The latent property of a poison sample to be successfully retrieved by the system in response to a target query, determined by its embedding proximity to the query.

## Relationships

### Factuality →
- **FactScore** (measurements) — *measured_by*
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **FLASK** (measurements) — *measured_by*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **CLIP score** (measurements) — *measured_by*
  - [Who Evaluates the Evaluations? Objectively Scoring Text-to-Image Prompt Coherence Metrics with T2IScoreScore (TS2)](https://proceedings.neurips.cc/paper_files/paper/2024/file/9b9cfd5428153ccfbd4ba34b7e007305-Paper-Conference.pdf)
- **AlignScore** (measurements) — *measured_by*
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **Biography** (measurements) — *measured_by*
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Overconfidence** (constructs) — *causes*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **HallusionBench** (measurements) — *measured_by*
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
- **SimpleQA** (measurements) — *measured_by*
  - [Controlled Low-Rank Adaptation with Subspace Regularization for Continued Training on Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
- **Chinese SimpleQA** (measurements) — *measured_by*
  - [Controlled Low-Rank Adaptation with Subspace Regularization for Continued Training on Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)
- **RM-Bench** (measurements) — *measured_by*
  - [Quantifying Lexical Semantic Shift via Unbalanced Optimal Transport](https://aclanthology.org/2025.acl-long.775.pdf)
- **JudgeBench** (measurements) — *measured_by*
  - [Quantifying Lexical Semantic Shift via Unbalanced Optimal Transport](https://aclanthology.org/2025.acl-long.775.pdf)

### → Factuality
- **In-context learning** (constructs) — *causes*
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **Implicit knowledge** (constructs) — *causes*
  - [SLED: Self Logits Evolution Decoding for Improving Factuality in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0939f13ffce3ff487509d902ddba4571-Paper-Conference.pdf)
- **FactScore** (measurements) — *measured_by*
  - [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.183.pdf)
- **Self-consistency** (measurements) — *causes*
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
- **Alignment tax** (constructs) — *causes*
  - [Controlled Low-Rank Adaptation with Subspace Regularization for Continued Training on Large Language Models](https://aclanthology.org/2025.acl-long.941.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Large language model validity via enhanced conformal prediction methods](https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generalization** (constructs)
  - [Mask-DPO: Generalizable Fine-grained Factuality Alignment of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82fdcbd92b6a7793b3894422d2437-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Helpfulness** (constructs)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Factual recall** (behaviors tasks)
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **Logical consistency** (constructs)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Boolean question answering** (behaviors tasks)
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Deriving Strategic Market Insights with Large Language Models: A Benchmark for Forward Counterfactual Generation](https://aclanthology.org/2025.emnlp-main.576.pdf)
- **Knowledge acquisition** (constructs)
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)

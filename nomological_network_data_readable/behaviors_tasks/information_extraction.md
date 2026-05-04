# Information extraction
**Type:** Behavior  
**Referenced in:** 235 papers  
**Also known as:** Attribute value extraction, Object entity extraction, Source/sink extraction, Claim extraction, Attribute extraction, Patient attribute extraction, Observation extraction, Entity extraction, Slot filling, Numerical answer extraction, Text extraction, Triple extraction, Fact extraction, Key answer extraction, Named entity recognition, Choice identification, Number retrieval, Proposition extraction, Token classification, Semantic tagging, Antibody region annotation, Data-flow fact extraction, Keyword extraction, Named entity extraction, Atomic proposition grounding, Document-level relation extraction, Frequent words extraction, Knowledge extraction, Cognitive pathway extraction, Schema extraction, Symptom extraction, Value extraction, Diagnosis extraction, Argument component identification, Value identification, Feature extraction from text, Fine-grained semantic extraction, Relation extraction, Aspect extraction, Unstructured evidence extraction, Triplet extraction, Information positioning, Multimedia event extraction, Pair extraction, Quadruple extraction, Single-element extraction, Medical relation extraction, Nested entity extraction, Emotion-cause annotation, Emotion-cause extraction, Entity extraction and grounding, Grounded multimodal named entity recognition, Attentional focus extraction, Clinical finding extraction, Factual assertion extraction, Candidate extraction, Edge extraction, Node extraction, Property extraction, Sticker extraction, Constraint type extraction, Constraint extraction, Answer extraction, Argument extraction, Content extraction, Subgraph extraction, Topic extraction, Graph structure extraction, Intent extraction, Multimodal relation extraction, Evidence extraction, Promise extraction, Trigger extraction, Reference extraction, Structured opinion extraction, Inorganic synthesis recipe extraction, Key-fact extraction, Causal tree extraction, Cause-effect span extraction, Highlight explanation extraction, Frame-semantic argument extraction, Knowledge slice extraction, Numeric data extraction, Nested field extraction, Temporal relation extraction, Training data extraction, Verbatim quote generation, Joint entity and relation extraction, Parallel term extraction, Spatial primitive extraction, Nested entity recognition, Multimodal named entity recognition, Numeric named entity recognition, Textual named entity recognition, Event Argument Extraction, Knowledge triple extraction, Entity recognition, Legal named-entity recognition, Data extraction, Feature extraction, Information Extraction, Information Retrieval, Parametric knowledge extraction, Span extraction capability  

## State of the Field

Across the surveyed literature, Information extraction is most commonly defined as the task of identifying and extracting structured information from unstructured text. This general behavior is operationalized through a vast array of specific sub-tasks, with named entity recognition (NER), relation extraction (RE), event extraction, and slot filling appearing as prevalent variants. The nature of the extracted information is diverse, ranging from simple entities, attributes, and factual triples to more complex structures like schemas, cognitive pathways, and causal trees. The task is applied to a wide variety of sources, including standard text, code, audio, video, and multimodal documents containing images. Evaluation of this behavior relies on a wide range of benchmarks, with datasets like CoNLL-2003 and TACRED frequently used for NER and relation extraction respectively, alongside broader evaluations like MT-Bench and direct Human evaluation. Several papers suggest that successful information extraction is enabled by other capabilities, such as Semantic understanding, Coreference resolution, and Logical reasoning. The behavior is often studied in conjunction with Information retrieval, sometimes as a component within a larger retrieval and analysis process, and is also related to Long-context processing and Relational reasoning.

## Sources

**[Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)**
> The task of identifying and extracting structured information from unstructured text.

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Attribute value extraction")**
> The task of identifying and extracting the value of a specific attribute from product metadata.

**[Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Object entity extraction")**
> The task of identifying and extracting noun phrases that refer to objects from a given textual description.

**[LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf) (as "Source/sink extraction")**
> Identifying program variables or expressions that serve as designated starting points and endpoints for dataflow analysis.

**[RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Claim extraction")**
> Decomposing a text into a set of discrete claims for later verification.

**[Empowering and Assessing the Utility of Large Language Models in Crop Science](https://proceedings.neurips.cc/paper_files/paper/2024/file/5e5783c673cf05cfd4b3ebf46e96abfc-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Event extraction")**
> The task of identifying event triggers and extracting their associated arguments from text, corresponding to predefined event categories like 'pest impact' or 'new variety release'.

**[MO-DDN: A Coarse-to-Fine Attribute-based Exploration Agent for Multi-Object Demand-driven Navigation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7565f036ceb20a2c74d341bfaa9fffad-Paper-Conference.pdf) (as "Attribute extraction")**
> The observable action of identifying and listing semantic attributes for instructions or objects via prompting.

**[MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Patient attribute extraction")**
> Extracting relevant numerical or categorical values from a long patient note for use in a calculation.

**[DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Observation extraction")**
> The task of identifying and extracting specific text spans from a clinical note that serve as evidence (observations) for a particular diagnostic conclusion.

**[Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf) (as "Entity extraction")**
> Identifying entities at the end of a reasoning path that may serve as candidate answers.

**[RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf) (as "Slot filling")**
> The task of identifying and extracting specific, predefined types of information (slots) from unstructured text.

**[VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) (as "Text extraction")**
> Converting visual text within document images into machine-readable text format.

**[OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3deb687c44d3687ace0729e5db3b4efd-Paper-Conference.pdf) (as "Numerical answer extraction")**
> The task of parsing the output of an executed code solver to identify and report the specific numerical values for decision variables and the objective function.

**[Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf) (as "Triple extraction")**
> Identifying entities and relations in a question or answer and converting them into head-relation-tail triples.

**[From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf) (as "Fact extraction")**
> Generating supporting factual statements for a question and answer options from a language model.

**[Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf) (as "Named entity recognition")**
> The observable task of identifying and categorizing named entities (like people, organizations, or locations) in text.

**[xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf) (as "Key answer extraction")**
> The observable task of identifying and isolating the specific, final answer from a model's potentially verbose or complex textual response.

**[Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf) (as "Choice identification")**
> The observable task of identifying and extracting sections of a privacy policy that describe user choices or opt-out mechanisms.

**[OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf) (as "Number retrieval")**
> The task of accurately identifying and extracting a specific number from a long context.

**[SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf) (as "Proposition extraction")**
> Identifying factual statements from text that capture important information, preferably about entities.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "Dependency parsing")**
> Assigning syntactic dependency relations between tokens in a sentence.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "Part-of-speech tagging")**
> Assigning grammatical part-of-speech labels to tokens.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "Semantic tagging")**
> Assigning semantic category labels to tokens.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "Token classification")**
> Assigning a label to each token in an input sequence for linguistic analysis tasks.

**[HELM: Hierarchical Encoding for mRNA Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb5d9195b201ec7ba66c8e20b396d349-Paper-Conference.pdf) (as "Antibody region annotation")**
> Assigning a categorical label to each nucleotide in an antibody-encoding mRNA sequence to identify its functional region (e.g., signal peptide, V, DJ, constant).

**[Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf) (as "Keyword extraction")**
> Identifying and retaining tokens from unnatural inputs that appear in the corresponding natural language version, while disregarding noise.

**[Grammar-Forced Translation of Natural Language to Temporal Logic using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/english25a/english25a.pdf) (as "Atomic proposition grounding")**
> The process of identifying and extracting atomic predicates (state variables or events) from a natural language input as a pre-processing step for translation.

**[RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25n/guo25n.pdf) (as "Data-flow fact extraction")**
> Identifying and reporting how values propagate between program statements along feasible execution paths, such as from a null assignment to a dereference site.

**[SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf) (as "Named entity extraction")**
> Identifying and extracting named entities such as people, places, or organizations from social media notes.

**[Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf) (as "Knowledge extraction")**
> The task of identifying and retrieving specific pieces of factual information from unstructured text.

**[ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf) (as "Frequent words extraction")**
> Identifying and extracting the most frequently occurring words from a given text.

**[DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf) (as "Document-level relation extraction")**
> The task of identifying and classifying semantic relations between entities mentioned anywhere in a document, including across multiple sentences.

**[A Probabilistic Inference Scaling Theory forLLMSelf-Correction](https://aclanthology.org/2025.emnlp-main.686.pdf) (as "Cognitive pathway extraction")**
> Extracting structured representations of cognitive-behavioral patterns from text, including triggering events, thoughts, emotions, and behavioral responses, based on CBT theory.

**[MentalGLMSeries: Explainable Large Language Models for Mental Health Analysis onChinese Social Media](https://aclanthology.org/2025.emnlp-main.687.pdf) (as "Symptom extraction")**
> Identifying relevant symptom entities from a patient's natural language description for use in diagnostic reasoning.

**[Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.728.pdf) (as "Schema extraction")**
> The process of identifying and structuring the constituent elements of a slide into a defined format, including each element's category, description, and content.

**[Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.548.pdf) (as "Value extraction")**
> The model correctly identifies and extracts numerical and categorical variables (e.g., age, creatinine level) from clinical vignettes for use in calculations.

**[How to Make Large Language Models Generate 100% Valid Molecules?](https://aclanthology.org/2025.emnlp-main.1351.pdf) (as "Argument component identification")**
> The observable task of identifying a set of argument components in a text, where each component is defined by its start and end token indices and its type (e.g., 'Claim', 'Premise').

**[Dynamic Jointly Batch Selection for Data Efficient Machine Translation Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1353.pdf) (as "Diagnosis extraction")**
> Identifying and outputting the correct medical diagnosis from a dialogue or input context based on symptoms and visual evidence.

**[AIR: Complex Instruction Generation via Automatic Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1629.pdf) (as "Value identification")**
> Extracting relevant data values from text such as names, dates, and attributes, and organizing them into structured intermediate representations.

**[RESF: Regularized-Entropy-Sensitive Fingerprinting for Black-Box Tamper Detection of Large Language Models](https://aclanthology.org/2025.emnlp-main.248.pdf) (as "Feature extraction from text")**
> Identifying and converting named entities and values from unstructured natural language descriptions into structured feature vectors consistent with a predefined schema.

**[Rank-Awareness and Angular Constraints: A New Perspective on Learning Sentence Embeddings fromNLIData](https://aclanthology.org/2025.emnlp-main.1130.pdf) (as "Fine-grained semantic extraction")**
> Identifying detailed semantic cues such as actions, facial expressions, and interactions from multimodal inputs.

**[PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf) (as "Relation extraction")**
> The task of identifying and classifying semantic relationships between entities in a text.

**[VC4VG: Optimizing Video Captions for Text-to-Video Generation](https://aclanthology.org/2025.emnlp-main.60.pdf) (as "Aspect extraction")**
> Identifying and listing key information needs or expectations from a user's question narrative, used to form evaluation rubrics.

**[We Politely Insist: YourLLMMust Learn thePersian Art of Taarof](https://aclanthology.org/2025.emnlp-main.95.pdf) (as "Unstructured evidence extraction")**
> Copying arbitrary-length text spans from a long input context to serve as supporting evidence for summary sentences, without constraints on span boundaries such as sentence or paragraph limits.

**[FilBench: CanLLMs Understand and GenerateFilipino?](https://aclanthology.org/2025.emnlp-main.128.pdf) (as "Triplet extraction")**
> The observable task of identifying and outputting (aspect term, aspect category, sentiment polarity) triplets from a given sentence.

**[LegalSearchLM: Rethinking Legal Case Retrieval as Legal Elements Generation](https://aclanthology.org/2025.emnlp-main.226.pdf) (as "Information positioning")**
> Locating and extracting specific data points or elements from a chart based on a query, such as values, labels, or time ranges.

**[ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.205.pdf) (as "Multimedia event extraction")**
> The task of identifying an event's type and its arguments from a combination of textual and visual data.

**[Exploring the Impact of Personality Traits onLLMBias and Toxicity](https://aclanthology.org/2025.emnlp-main.207.pdf) (as "Pair extraction")**
> Extracting binary relationships such as target-aspect, target-opinion, or aspect-opinion pairs from text.

**[Exploring the Impact of Personality Traits onLLMBias and Toxicity](https://aclanthology.org/2025.emnlp-main.207.pdf) (as "Quadruple extraction")**
> Generating structured outputs in the form of (target, aspect, opinion, sentiment) tuples from conversational utterances.

**[Exploring the Impact of Personality Traits onLLMBias and Toxicity](https://aclanthology.org/2025.emnlp-main.207.pdf) (as "Single-element extraction")**
> The task of extracting individual sentiment elements, such as the target, aspect, or opinion, as separate items from text.

**[Pragmatic Inference Chain (PIC) ImprovingLLMs’ Reasoning of Authentic Implicit Toxic Language](https://aclanthology.org/2025.emnlp-main.297.pdf) (as "Medical relation extraction")**
> Identifying a relation expressed between medical entities in text.

**[GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.288.pdf) (as "Nested entity extraction")**
> The task of identifying and classifying named entities that may be embedded within other entities.

**[Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.306.pdf) (as "Emotion-cause extraction")**
> Identifying the dialogue sentences that express the emotion and the sentences that express the cause.

**[Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.306.pdf) (as "Emotion-cause annotation")**
> The process of identifying and labeling utterances in a dialogue that express an emotion and its underlying cause, based on predefined seeds and contextual alignment.

**[DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf) (as "Grounded multimodal named entity recognition")**
> The task of identifying named entities in text and linking them to their corresponding visual regions within an associated image.

**[DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf) (as "Entity extraction and grounding")**
> A composite task evaluated in the paper that involves both identifying entity spans in text and linking them to their corresponding visual regions.

**[Large Language Models Discriminate Against Speakers ofGerman Dialects](https://aclanthology.org/2025.emnlp-main.416.pdf) (as "Attentional focus extraction")**
> The process of identifying and listing key analytical aspects or dimensions emphasized in an argumentative unit, such as social groups or conceptual perspectives.

**[Noise, Adaptation, and Strategy: AssessingLLMFidelity in Decision-Making](https://aclanthology.org/2025.emnlp-main.392.pdf) (as "Clinical finding extraction")**
> Identifying and organizing relevant clinical observations (e.g., abnormalities, normal findings) under appropriate organ system categories in the Findings section.

**[Large Language Models Discriminate Against Speakers ofGerman Dialects](https://aclanthology.org/2025.emnlp-main.416.pdf) (as "Factual assertion extraction")**
> The task of identifying and extracting verifiable statements of fact from a source text.

**[Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.667.pdf) (as "Candidate extraction")**
> The behavior of identifying and extracting potential recommendation items from retrieved text fragments based on a structured template.

**[Following the Autoregressive Nature ofLLMEmbeddings via Compression and Alignment](https://aclanthology.org/2025.emnlp-main.640.pdf) (as "Edge extraction")**
> Detecting directed connections between diagram elements by analyzing visual cues such as arrows and lines, using vision-capable LLMs to infer logical flows.

**[Following the Autoregressive Nature ofLLMEmbeddings via Compression and Alignment](https://aclanthology.org/2025.emnlp-main.640.pdf) (as "Node extraction")**
> Identifying and grouping text elements in an SVG diagram into coherent nodes, using spatial and semantic criteria, potentially refined with multimodal LLMs.

**[Gamma-Guard: Lightweight Residual Adapters for Robust Guardrails in Large Language Models](https://aclanthology.org/2025.emnlp-main.615.pdf) (as "Property extraction")**
> Identifying key measurable metrics and their associated subjects from a query to support answering, such as 'revenue' and '<Company A>’s 2018 annual report'.

**[RareSyn: Health Record Synthesis for Rare Disease Diagnosis](https://aclanthology.org/2025.emnlp-main.621.pdf) (as "Sticker extraction")**
> Producing a structured summary of key conditions, strategies, and limitations from a prior reasoning trace to serve as a compact guide for future reasoning.

**[32.3%](https://aclanthology.org/2025.emnlp-main.809.pdf) (as "Constraint type extraction")**
> The observable process of identifying and classifying the specific types of constraints (e.g., AllDifferent, Cumulative) present in a natural language problem description.

**[LimRank: Less is More for Reasoning-Intensive Information Reranking](https://aclanthology.org/2025.emnlp-main.1042.pdf) (as "Constraint extraction")**
> Identifying the relevant rules, schedules, concepts, or other instance-specific requirements from a problem statement.

**[Mind the Gap: HowBabyLMs Learn Filler-Gap Dependencies](https://aclanthology.org/2025.emnlp-main.762.pdf) (as "Answer extraction")**
> Replacing the propagated relation token with the correct factual answer token in the final prediction sequence.

**[Web Intellectual Property at Risk: Preventing Unauthorized Real-Time Retrieval by Large Language Models](https://aclanthology.org/2025.emnlp-main.871.pdf) (as "Argument extraction")**
> The task of identifying text spans that serve as arguments for a scientific event and classifying them into specific semantic roles like Context, Method, or Result.

**[Governance in Motion: Co-evolution of Constitutions andAImodels for Scalable Safety](https://aclanthology.org/2025.emnlp-main.870.pdf) (as "Content extraction")**
> Parsing and extracting textual information from retrieved webpages, including visible elements and hidden source-code components.

**[MEPT: Mixture of Expert Prompt Tuning as a Manifold Mapper](https://aclanthology.org/2025.emnlp-main.824.pdf) (as "Subgraph extraction")**
> Identifying and retrieving a set of relevant knowledge graph triples that are semantically aligned with the input query, based on textual triplet representations.

**[RoDEval: A Robust Word Sense Disambiguation Evaluation Framework for Large Language Models](https://aclanthology.org/2025.emnlp-main.865.pdf) (as "Topic extraction")**
> The process of identifying and consolidating the main themes or subjects present in a user's historical posts.

**[Multi-Document Event Extraction Using Large and Small Language Models](https://aclanthology.org/2025.emnlp-main.973.pdf) (as "Graph structure extraction")**
> The task of identifying and parsing graph components like nodes, edges, and weights from unstructured or semi-structured text.

**[Mapping Toxic Comments Across Demographics: A Dataset fromGerman Public Broadcasting](https://aclanthology.org/2025.emnlp-main.949.pdf) (as "Intent extraction")**
> Generating a free-form natural language description of the inferred user goal from a sequence of UI interactions, including screenshots and action logs.

**[Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups](https://aclanthology.org/2025.emnlp-main.943.pdf) (as "Multimodal relation extraction")**
> Identifying semantic relations between entities from both text and image inputs, producing relational triples (subject, relation, object) based on joint reasoning.

**[COM-BOM:Bayesian Exemplar Search for Efficiently Exploring the Accuracy-CalibrationPareto Frontier](https://aclanthology.org/2025.emnlp-main.1028.pdf) (as "Evidence extraction")**
> The task of extracting the specific text span corresponding to the evidence supporting a corporate promise from a document.

**[COM-BOM:Bayesian Exemplar Search for Efficiently Exploring the Accuracy-CalibrationPareto Frontier](https://aclanthology.org/2025.emnlp-main.1028.pdf) (as "Promise extraction")**
> The task of extracting the specific text span corresponding to a corporate promise from a document.

**[DiCoRe: Enhancing Zero-shot Event Detection via Divergent-ConvergentLLMReasoning](https://aclanthology.org/2025.emnlp-main.1039.pdf) (as "Trigger extraction")**
> The task of identifying the specific word or phrase in a sentence that most distinctly indicates the occurrence of an event.

**[Can Large Language Models Translate Unseen Languages in Underrepresented Scripts?](https://aclanthology.org/2025.emnlp-main.1180.pdf) (as "Reference extraction")**
> Identifying and isolating mentions of people, texts, events, or ideas within philosophical writings, including both explicit and implicit references.

**[Drivel-ology: ChallengingLLMs with Interpreting Nonsense with Depth](https://aclanthology.org/2025.emnlp-main.1178.pdf) (as "Structured opinion extraction")**
> The task of identifying and extracting a structured set of opinion tuples, such as (entity, feature, opinion), from a given text.

**[HyperKGR: Knowledge Graph Reasoning in Hyperbolic Space with Graph Neural Network Encoding Symbolic Path](https://aclanthology.org/2025.emnlp-main.1280.pdf) (as "Inorganic synthesis recipe extraction")**
> The task of extracting and summarizing step-by-step procedures for synthesizing inorganic materials from scientific literature.

**[Composable Cross-prompt Essay Scoring by Merging Models](https://aclanthology.org/2025.emnlp-main.1241.pdf) (as "Key-fact extraction")**
> Identifying and structuring central themes, supporting ideas, and fine-grained details from text segments into a hierarchical representation.

**[[CLS]](https://aclanthology.org/2025.emnlp-main.1313.pdf) (as "Causal tree extraction")**
> The task of generating a structured, multi-layered causal tree from an unstructured medical case report, where nodes are medical entities and edges represent causal or evidential relationships.

**[CompoundAISystems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1464.pdf) (as "Cause-effect span extraction")**
> The task of identifying and labeling the specific text segments (spans) that correspond to the cause and the effect in a causal relationship.

**[Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking](https://aclanthology.org/2025.emnlp-main.1494.pdf) (as "Highlight explanation extraction")**
> Identifying input tokens, token pairs, or spans that are most important for a model's prediction, based on attention weights or other attribution methods.

**[2025.emnlp-main.1557.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1557.checklist.pdf) (as "Frame-semantic argument extraction")**
> The observable task of identifying and labeling the semantic arguments (e.g., who did what to whom) associated with a predicate in a sentence based on a frame-semantic schema.

**[Plutus: Benchmarking Large Language Models in Low-ResourceGreek Finance](https://aclanthology.org/2025.emnlp-main.1536.pdf) (as "Knowledge slice extraction")**
> Identifying and extracting text segments from research papers that are highly relevant to a given taxonomy topic.

**[UNCLE: Benchmarking Uncertainty Expressions in Long-Form Generation](https://aclanthology.org/2025.emnlp-main.1544.pdf) (as "Numeric data extraction")**
> The observable task of identifying and extracting specific numerical values, such as event counts or standard deviations, from unstructured text and presenting them in a structured format.

**[Can Large Language Models Outperform Non-Experts in Poetry Evaluation? A Comparative Study Using the Consensual Assessment Technique](https://aclanthology.org/2025.emnlp-main.1626.pdf) (as "Nested field extraction")**
> The specific task of extracting information from hierarchical or nested structures within a document, such as job roles within a work experience section.

**[Towards Language-AgnosticSTIPA: Universal Phonetic Transcription to Support Language Documentation at Scale](https://aclanthology.org/2025.emnlp-main.1601.pdf) (as "Temporal relation extraction")**
> The task of identifying and classifying the temporal relationship (e.g., before, after, includes) between a given pair of event mentions in a text.

**[so much depends / upon / a whitespace: Why Whitespace Matters for Poets andLLMs](https://aclanthology.org/2025.emnlp-main.1784.pdf) (as "Verbatim quote generation")**
> The model produces exact or near-exact sequences of text matching copyrighted source material, particularly long spans exceeding a defined threshold.

**[Not Your Typical Government Tipline:LLM-Assisted Routing of Environmental Protection Agency Citizen Tips](https://aclanthology.org/2025.emnlp-main.1789.pdf) (as "Training data extraction")**
> The model reveals memorized training examples in response to adversarial prompts.

**[From Input Perception to Predictive Insight: Modeling Model Blind Spots Before They Become Errors](https://aclanthology.org/2025.emnlp-main.1741.pdf) (as "Joint entity and relation extraction")**
> The observable task of simultaneously identifying named entity spans and the semantic relations that exist between them in a single step.

**[Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Cross-Lingual Transfer in Sense-Aware Tasks](https://aclanthology.org/2025.emnlp-main.1774.pdf) (as "Parallel term extraction")**
> The task of identifying and extracting the translation of a specific source term from a parallel text, which consists of a source sentence and its corresponding translation.

**[Breaking Agents: Compromising AutonomousLLMAgents Through Malfunction Amplification](https://aclanthology.org/2025.emnlp-main.1772.pdf) (as "Spatial primitive extraction")**
> Identifying and outputting directional, topological, and distal spatial relations along with Frame of Reference from a spatial expression to support downstream reasoning tasks.

**[M-ABSA: A Multilingual Dataset for Aspect-Based Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.129.pdf) (as "Nested entity recognition")**
> Identifying and extracting disease-related entities from clinical text, including cases where entities are embedded within other entities.

**[DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf) (as "Multimodal named entity recognition")**
> A subtask of GMNER that focuses specifically on identifying the textual spans and types of named entities using both text and image context.

**[Model Consistency as a Cheap yet Predictive Proxy forLLMElo Scores](https://aclanthology.org/2025.emnlp-main.1535.pdf) (as "Numeric named entity recognition")**
> The task of identifying and classifying numerical expressions in text into predefined categories like monetary, percentage, temporal, and quantity.

**[Model Consistency as a Cheap yet Predictive Proxy forLLMElo Scores](https://aclanthology.org/2025.emnlp-main.1535.pdf) (as "Textual named entity recognition")**
> Detecting and categorizing named entities such as persons, locations, and organizations in Greek financial texts, particularly in complex linguistic expressions.

**[Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf) (as "Event Argument Extraction")**
> The task of identifying event arguments and their specific roles in text, given the presence of an event trigger.

**[LoGU: Long-form Generation with Uncertainty Expressions](https://aclanthology.org/2025.acl-long.929.pdf) (as "Knowledge triple extraction")**
> Decomposing document content into structured ⟨head entity, relation, tail entity⟩ triples using an LLM with in-context learning.

**[UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf) (as "Entity recognition")**
> Identifying relevant urban entities in text before relation extraction.

**[LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Legal named-entity recognition")**
> Extracting all named entities from a legal text and determining their specific entity types.

**[UnifyingAITutor Evaluation: An Evaluation Taxonomy for Pedagogical Ability Assessment ofLLM-PoweredAITutors](https://aclanthology.org/2025.naacl-long.58.pdf) (as "Parametric knowledge extraction")**
> The ability of a language model to retrieve factual knowledge stored in its parameters, learned during training on documents, in response to diverse queries.

**[AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.334.pdf) (as "Information retrieval")**
> Locating and extracting a specific piece of information (needle) from a large body of text (haystack), particularly in long and multilingual contexts.

**[Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf) (as "Information Retrieval")**
> A two-stage evaluation method that assesses a model's ability to first retrieve relevant tables from a timeline and then generate answers based on them, isolating the retrieval component of temporal reasoning.

**[Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf) (as "Information Extraction")**
> A two-stage evaluation method that tests a model's ability to directly extract relevant attributes from tables without full table retrieval, focusing on fine-grained evidence extraction.

**[Towards a Perspectivist Turn in Argument Quality Assessment](https://aclanthology.org/2025.naacl-long.383.pdf) (as "Feature extraction")**
> The model's ability to identify and utilize relevant patterns from time-series data, such as pictorial, time-aware, cross-dimension, or frequency-domain features, which are critical for accurate reasoning.

**[Regularized Best-of-N Sampling with MinimumBayes Risk Objective for Language Model Alignment](https://aclanthology.org/2025.naacl-long.473.pdf) (as "Data extraction")**
> The latent capability to accurately perceive and retrieve numerical, categorical, or textual information from visual representations like legends and color mappings.

**[Bayelemabaga: Creating Resources forBambaraNLP](https://aclanthology.org/2025.naacl-long.603.pdf) (as "Span extraction capability")**
> The underlying ability of a model to accurately identify and extract text spans corresponding to specific semantic roles, such as aspects and opinions, even when surface forms vary.

## Relationships

### Information extraction →
- **CoNLL-2003** (measurements) — *measured_by*
  > English flat NER datasets (CoNLL’03 (Sang and De Meulder, 2003) and MIT-Movie (Liu et al., 2013)); (Section 4.1)
  - [Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf)
- **TACRED** (measurements) — *measured_by*
  > “We conducted experiments on SemEval and three versions of TACRED: SemEval 2010 Task 8 (SemEval) (Hendrickx et al., 2010), TACRED (Zhang et al., 2017), TACRED-Revisit (Alt et al., 2020), Re-TACRED (Stoica et al., 2021).”
  - [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
- **SLURP** (measurements) — *measured_by*
  > SLURP dataset (Bastianelli et al., 2020) was used which contains 16.5k sentences and 72k audio recordings of single-turn user interactions with a home assistant, annotated with scenarios, actions and entities. (Section 5.1)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **T-REx** (measurements) — *measured_by*
  - [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **Zero-shot relation extraction (zsRE)** (measurements) — *measured_by*
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
- **CrossNER** (measurements) — *measured_by*
  - [Faster Speculative Decoding via Effective Draft Decoder with Pruned Candidate Tree](https://aclanthology.org/2025.acl-long.487.pdf)
- **SemEval 2010 Task 8** (measurements) — *measured_by*
  - [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)
- **zs-RE** (measurements) — *measured_by*
  > “zs-RE (Levy et al., 2017), Relation extraction”
  - [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > To further verify, a human rater compared 20 Mind2Web trajectories with intent predictions from Gemini Flash 8B, choosing between CoT and Decomposed-FT responses (details in Appendix D). (Section 6.1)
  - [[CLS]](https://aclanthology.org/2025.emnlp-main.1313.pdf)
- **MT-Bench** (measurements) — *measured_by*
  > “The second benchmark, MT-Bench (Zheng et al., 2024), consists of 80 multi-turn dialogues spanning various domains, including writing, roleplay, reasoning, math, coding, extraction, STEM, and humanities.”
  - [s3: You Don’t Need That Much Data to Train a Search Agent viaRL](https://aclanthology.org/2025.emnlp-main.1096.pdf)
- **Reward function generation** (behaviors tasks) — *causes*
  - [A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/file/074f42212be2c8ee651db00f17965ec4-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **SWDE** (measurements) — *measured_by*
  > To further evaluate Longhorn's ability to recall in long real-world sequences, following the experiment setup in Arora et al. (2024c), we consider the following six recall-intensive tasks: information extraction tasks like FDA and SWDE (Arora et al., 2024a; 2023b; Wu et al., 2021; Deng et al., 2022), and question-answering benchmarks like Squad (Rajpurkar et al., 2018), NaturalQuestion (NQ) (Kwiatkowski et al., 2019), TriviaQA (Joshi et al., 2017), and DROP (Dua et al., 2019).
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
- **LongMemEval** (measurements) — *measured_by*
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Consistency** (constructs) — *causes*
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Activation patching** (measurements) — *measured_by*
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **MMAU** (measurements) — *measured_by*
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **FewRel** (measurements) — *measured_by*
  - [Soft Prompting for Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.205.pdf)
- **WikiAnn** (measurements) — *measured_by*
  - [LLMs as Meta-Reviewers’ Assistants: A Case Study](https://aclanthology.org/2025.naacl-long.396.pdf)
- **OntoNotes** (measurements) — *measured_by*
  > To demonstrate the effectiveness of our method, we evaluate it on five NER datasets... These datasets include... OntoNotes (Weischedel et al., 2013) for web text from various sources.
  - [Seeing the Same Story Differently:Framing‐Divergent Event Coreference for Computational Framing Analysis](https://aclanthology.org/2025.emnlp-main.1441.pdf)
- **UNER** (measurements) — *measured_by*
  - [AXIS: Efficient Human-Agent-Computer Interaction withAPI-FirstLLM-Based Agents](https://aclanthology.org/2025.acl-long.382.pdf)
- **Twitter-GMNER** (measurements) — *measured_by*
  > In our work, we conduct experiments on two datasets: Twitter-GMNER and Twitter-FMNERG. (Section 4.1)
  - [DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf)
- **FUNSD** (measurements) — *measured_by*
  - [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.844.pdf)
- **SROIE** (measurements) — *measured_by*
  - [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.844.pdf)
- **Twitter-FMNERG** (measurements) — *measured_by*
  > In our work, we conduct experiments on two datasets: Twitter-GMNER and Twitter-FMNERG. (Section 4.1)
  - [DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf)
- **REBEL** (measurements) — *measured_by*
  > On relation extraction (RE), our pipeline achieves 65.8% macro-F1 on REBEL, an 8-point gain over the prior state of the art... (Abstract)
  - [Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf)
- **CoQA** (measurements) — *measured_by*
  > “We use all 500 examples (each with 10 to 25 questions) from the validation set to demonstrate how writing style affects fact extraction.”
  - [EnhancingChinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1155.pdf)

### → Information extraction
- **Logical reasoning** (constructs) — *causes*
  - [A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/file/074f42212be2c8ee651db00f17965ec4-Paper-Conference.pdf)
- **Instruction following** (constructs) — *causes*
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Persuasiveness** (constructs) — *causes*
  - [Palm: A Culturally Inclusive and Linguistically Diverse Dataset forArabicLLMs](https://aclanthology.org/2025.acl-long.1580.pdf)
- **Semantic understanding** (constructs) — *causes*
  > The integration of sentence-level semantic RAG enhances the LLM’s ability to accurately extract relations by providing rich and relevant semantic information, which empowers the semantic understanding of LLMs and ultimately improves the performance of document-level RE. (Section 4.3. Sentence-Level Semantic RAG Enhancement)
  - [DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf)
- **Coreference resolution** (behaviors tasks) — *causes*
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf)
- **Text simplification** (behaviors tasks) — *causes*
  > Ablation studies demonstrate that integrating coreference and decomposition increases recall on rare relations by over 20%. (Abstract)
  - [Complex Numerical Reasoning with Numerical Semantic Pre-training Framework](https://aclanthology.org/2025.emnlp-main.783.pdf)

### Associated with
- **Information retrieval** (behaviors tasks)
  > Information Retrieval. Effective search functionality is essential in SNS. Models should interpret query intent and retrieve relevant information from large datasets, delivering the most accurate results. Tasks: (3) Note-NER. Extracts named entities from note content.
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Relational reasoning** (constructs)
  > EntiGraph consists of two steps/prompts: extracting entities from the document and analyzing relations among an arbitrary subset of the entities (Figure 1). (Section 2.2)
  - [Synthetic continued pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **Long-context processing** (constructs)
  - [Are We Done withMMLU?](https://aclanthology.org/2025.naacl-long.263.pdf)
- **Knowledge awareness** (constructs)
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **Understanding** (constructs)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense knowledge** (constructs)
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Long-term memory** (constructs)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Ranking** (behaviors tasks)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Few-shot learning** (measurements)
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Continual learning** (constructs)
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Natural language inference** (behaviors tasks)
  - [Incremental Sentence Processing Mechanisms in Autoregressive Transformer Language Models](https://aclanthology.org/2025.naacl-long.165.pdf)
- **Temporal video grounding** (behaviors tasks)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Spatial reasoning** (constructs)
  - [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.844.pdf)
- **Evaluation** (behaviors tasks)
  - [LimRank: Less is More for Reasoning-Intensive Information Reranking](https://aclanthology.org/2025.emnlp-main.1042.pdf)
- **Table reasoning** (constructs)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf)

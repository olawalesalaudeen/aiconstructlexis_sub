# Text classification
**Type:** Behavior  
**Referenced in:** 140 papers  
**Also known as:** Topic classification, Facial expression recognition, Masked multi-modality modeling, Toxicity classification, News headline classification, Hawkish-dovish classification, Argument unit classification, Deal completeness classification, ESG issue identification, Triplet classification, Single-sentence classification, Cross-lingual sentence classification, Textual classification, Stance classification, Data practice identification, Headline classification, Persuasion strategy classification, Note classification, Topic assignment, Resume classification, Occupation prediction, Question classification, Evergreen question classification, Long document classification, Question type classification, Section classification, Sequential sentence classification, Problem classification, Paper classification, Multi-label classification, Multilabel classification  

## State of the Field

Across the surveyed literature, text classification is overwhelmingly defined as the task of assigning a discrete, predefined label to an input text sequence. This general framing encompasses a wide variety of specific tasks, including topic classification, sentiment analysis, stance detection, and question classification. A smaller body of work extends this to more specialized domains, such as classifying financial texts (e.g., 'hawkish-dovish classification'), identifying data practices in privacy policies, or predicting occupations from biographies. The field operationalizes and measures this behavior using a diverse set of benchmark datasets, with the most frequently cited instruments being AG News, TREC, SST-2, IMDb, DBPedia, and the GLUE benchmark suite. Other datasets such as Subj, Financial Phrasebank, and SIB-200 are also used, though less commonly in this set of papers. Text classification serves as a common downstream task for evaluating models under various learning paradigms, including in-context learning, zero-shot prompting, and continual learning. Beyond being an evaluation task in itself, it is also used to measure other constructs like model sensitivity, faithfulness, and social bias, with specific tasks like 'Resume classification' being employed to probe for allocational harms. The task is also studied in relation to synthetic data generation, which one paper reports can improve classification performance.

## Sources

**[A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)**
> Assigning a discrete label to an input text sequence.

**[Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf) (as "Topic classification")**
> The task of identifying the main subject or topic of a document from a predefined set of topics.

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Facial expression recognition")**
> The task of classifying a human face in an image into one of several basic emotional expressions.

**[OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Stance detection")**
> The task of identifying the viewpoint or stance of an author within a text, such as 'affirmative' or 'negative'.

**[Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf) (as "Masked multi-modality modeling")**
> A pre-training task involving data from multiple modalities (e.g., images and text) where parts of the input are masked and the model must predict the masked content.

**[Soft-Label Integration for Robust Toxicity Classification](https://proceedings.neurips.cc/paper_files/paper/2024/file/ac4c13a5c6ec1bba68c9ce1d908321d2-Paper-Conference.pdf) (as "Toxicity classification")**
> Assigning a text instance to toxic or non-toxic categories, or to a finer-grained toxicity-related class set.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "News headline classification")**
> Classifying financial headlines according to whether they contain specific market-related information.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Hawkish-dovish classification")**
> Classifying monetary-policy text by whether it signals tightening, easing, or neutrality.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Argument unit classification")**
> The task of categorizing sentences in financial texts, such as earnings calls, into argumentative functions like 'claim' or 'premise'.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Deal completeness classification")**
> Classifying merger-and-acquisition mentions as completed deals or rumors.

**[FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "ESG issue identification")**
> The task of detecting and classifying Environmental, Social, and Governance (ESG) related concerns within financial documents.

**[MKGL: Mastery of a Three-Word Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe03053bd2cf5b5c56de1e463bc53e1a-Paper-Conference.pdf) (as "Triplet classification")**
> Judging whether a knowledge graph triplet is valid or correct.

**[Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf) (as "Single-sentence classification")**
> The task of classifying a single sentence into a predefined category, such as determining its grammatical acceptability or sentiment.

**[Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf) (as "Textual classification")**
> The task of assigning a label to a text input, especially in scenarios where visual data is converted into descriptive text for evaluation.

**[MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf) (as "Cross-lingual sentence classification")**
> Assigning a natural language inference label to sentences across multiple languages.

**[The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc3ce215c378815ce0be41cb0f65d0b5-Paper-Conference.pdf) (as "Stance classification")**
> Assigning a comment to a stance category such as favor or against with respect to a posed question.

**[Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf) (as "Data practice identification")**
> The observable task of classifying segments of a privacy policy into predefined categories related to data collection, use, and sharing.

**[Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf) (as "Persuasion strategy classification")**
> The observable task of identifying the persuasion techniques used in media content such as advertisements.

**[Teaching LLMs How to Learn with Contextual Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb0494e5ce9351cb120c3a35328dffef-Paper-Conference.pdf) (as "Headline classification")**
> The task of assigning a news article to one of several predefined categories based on the content of its headline.

**[Second-Order Fine-Tuning without Pain for LLMs: A Hessian Informed Zeroth-Order Optimizer](https://proceedings.iclr.cc/paper_files/paper/2025/file/6bf82cc56a5fa0287c438baa8be65a70-Paper-Conference.pdf) (as "Sentence classification")**
> The task of assigning a predefined category or label to a given sentence, such as for sentiment or topic analysis.

**[ZETA: Leveraging $Z$-order Curves for Efficient Top-$k$ Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/b508c1737d9242e40552699a6e98c87b-Paper-Conference.pdf) (as "Sequence classification")**
> The observable task of assigning a categorical label to an entire input sequence.

**[Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf) (as "Pair classification")**
> The task of classifying a pair of texts, for example, determining if they are paraphrases or have a specific relationship.

**[SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf) (as "Note classification")**
> Categorizing social media notes into predefined topics or taxonomies based on content, in single- or multiple-choice format.

**[Synthesizing Privacy-Preserving Text Data via Finetuning *without* Finetuning Billion-Scale LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25g/tan25g.pdf) (as "Topic assignment")**
> Mapping a given document to a predefined topic cluster based on its content, using document embeddings and clustering techniques.

**[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf) (as "Resume classification")**
> Determining whether a resume is appropriate for a given job category, used to assess allocational bias in hiring-related decisions.

**[Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf) (as "Occupation prediction")**
> Predicting a person's job based on biographical information, used to assess whether models rely on gender or other stereotypes.

**[A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.9.pdf) (as "Question classification")**
> The task of classifying a question into a category based on the type of answer it expects (e.g., person, location, numeric).

**[Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks onLLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.434.pdf) (as "Evergreen question classification")**
> The observable task of classifying a given question as either 'evergreen' (having a stable answer over time) or 'mutable' (having an answer that changes).

**[CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.474.pdf) (as "Long document classification")**
> Assigning labels to lengthy documents based on their content.

**[VELA: AnLLM-Hybrid-as-a-Judge Approach for Evaluating Long Image Captions](https://aclanthology.org/2025.emnlp-main.439.pdf) (as "Question type classification")**
> Categorizing questions into types such as count, comparative, or multihop based on their structure and reasoning requirements.

**[Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.697.pdf) (as "Sequential sentence classification")**
> The task of assigning a label to each sentence in a text that indicates its role or category, such as a section header.

**[Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.697.pdf) (as "Section classification")**
> The process of assigning section labels (e.g., Background, Results) to sentences in a plain language summary based on content and context.

**[Multi-Document Event Extraction Using Large and Small Language Models](https://aclanthology.org/2025.emnlp-main.973.pdf) (as "Problem classification")**
> Determining the type of graph problem (e.g., TSP, Vertex Cover) from natural language descriptions and extracting constraints and optimization objectives.

**[GRASP: Replace Redundant Layers with Adaptive Singular Parameters for Efficient Model Compression](https://aclanthology.org/2025.emnlp-main.1339.pdf) (as "Paper classification")**
> The task of assigning a predefined category or label to a scientific paper based on its content.

**[MixLoRA-DSI: Dynamically Expandable Mixture-of-LoRAExperts for Rehearsal-Free Generative Retrieval over Dynamic Corpora](https://aclanthology.org/2025.emnlp-main.21.pdf) (as "Multi-label classification")**
> The task of assigning one or more labels to an input, such as a sentence, from a predefined set of categories.

**[No Need for Explanations:LLMs can implicitly learn from mistakes in-context](https://aclanthology.org/2025.emnlp-main.1687.pdf) (as "Multilabel classification")**
> The observable task of assigning zero, one, or multiple labels from a predefined set to a single text example, reflecting the co-occurrence of moral dimensions.

## Relationships

### Text classification →
- **AG News** (measurements) — *measured_by*
  > performing classification on two common datasets...: SST-2, AG-News and one modern dataset: StrategyQA
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **TREC** (measurements) — *measured_by*
  > We use eight text classification datasets for ID data: SST-2 (SST; Socher et al., 2013), Subjectivity (SUBJ; Pang & Lee, 2004), AG-News (AGN; Zhang et al., 2015), and TREC (TREC; Li & Roth, 2002), BigPatent (BP; Sharma et al., 2019), AmazonReviews (AR; McAuley et al., 2015), MovieGenre (MG; Maas et al., 2011), 20NewsGroups (NG; Lang, 1995). (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  > We use eight text classification datasets for ID data: SST-2 (SST; Socher et al., 2013), Subjectivity (SUBJ; Pang & Lee, 2004), AG-News (AGN; Zhang et al., 2015), and TREC (TREC; Li & Roth, 2002), BigPatent (BP; Sharma et al., 2019), AmazonReviews (AR; McAuley et al., 2015), MovieGenre (MG; Maas et al., 2011), 20NewsGroups (NG; Lang, 1995). (Section 4.1)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **IMDb** (measurements) — *measured_by*
  > Table 1 gives an overview of our experimental setup, including specifics for the task, datasets, encoders, LLMs, and task-specific prompts we use.
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **DBPedia** (measurements) — *measured_by*
  > We study text classification on three datasets: 4-way news classification AGNews (Zhang et al., 2015), 6-way question classification TREC (Voorhees and Tice, 2000), and 14-way topic classification DBPedia (Zhang et al., 2015).
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > We evaluate on the GLUE benchmark, where we exclude the RTE dataset due to high standard deviations in the obtained scores. (Section 4.1)
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **GoEmotions** (measurements) — *measured_by*
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **Subj** (measurements) — *measured_by*
  > text classification using TREC, MR, Subj, and AG News datasets (Voorhees & Tice, 2000; Pang & Lee, 2004; 2005; Zhang et al., 2015). (Section 4.1)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **Rotten Tomatoes** (measurements) — *measured_by*
  > Table 1 gives an overview of our experimental setup, including specifics for the task, datasets, encoders, LLMs, and task-specific prompts we use.
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **SIB-200** (measurements) — *measured_by*
  > We also take the Filipino and Cebuano subsets of SIB-200 (Adelani et al., 2024), and the text-only subset of Balita NLP (Buñag and Esquivel, 2023). (Section 3.2)
  - [PSET: a Phonetics-Semantics Evaluation Testbed](https://aclanthology.org/2025.emnlp-main.374.pdf)
- **20 Newsgroups** (measurements) — *measured_by*
  - [Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Amazon Reviews** (measurements) — *measured_by*
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **CoLA** (measurements) — *measured_by*
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **ChemProt** (measurements) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **SciERC** (measurements) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **Super-Natural Instructions** (measurements) — *measured_by*
  > These sequences consist of pure generation tasks, pure classification tasks and mixed sequences containing both generation and classification tasks. (Section 3)
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  > In Table 2, we present the text classification results of different dataset pruning methods on the MMLU benchmark. (Section 4.2.2)
  - [Exploring Learning Complexity for Efficient Downstream Dataset Pruning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7e4aab3786a1f8e39e0f9b8dd9fa105-Paper-Conference.pdf)
- **Financial Phrasebank** (measurements) — *measured_by*
  > We assessed our proposed methods by comparing them with standard loss functions across several text classification benchmarks, including Financial Phrasebank (Financial) (Malo et al., 2014), irony detection (Tweet Irony) (Van Hee et al., 2018), and the MRPC dataset from GLUE (Wang et al., 2018).
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
- **MR** (measurements) — *measured_by*
  > We build ICL-formed test inputs from 6 real-world sentence classification datasets...: ... MR (Pang & Lee, 2005) (Section 2.2)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  > The SciQ dataset (Welbl et al., 2017) is used, which contains 13,679 crowdsourced science exam questions about Physics, Chemistry and Biology, among others. (Section 5.1)
  - [Bayesian WeakS-to-Strong from Text Classification to Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/495e55f361708bedbab5d81f92048dcd-Paper-Conference.pdf)
- **QNLI** (measurements) — *measured_by*
  > 2) QNLI: This is a dataset containing sentence pairs for binary classification (entailment/not entailment). We use accuracy as the metric. (Section 5)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **BANKING77** (measurements) — *measured_by*
  - [SURE: Safety Understanding and Reasoning Enhancement for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.385.pdf)
- **OpenReview** (measurements) — *measured_by*
  > Accuracy (%, ↑) of different algorithms on a variety of tasks and datasets (...OpenReview is text classification accuracy). (Table 1).
  - [Private Federated Learning using Preference-Optimized Synthetic Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25g/hou25g.pdf)
- **Twitter Financial News Sentiment** (measurements) — *measured_by*
  > We evaluate our models on 9 text classification benchmark datasets to ensure a comprehensive assessment across multiple domains, text lengths, and classification types - sentiment analysis, movie reviews, news categorization, and social media analysis. These are: AG News (Zhang et al., 2015), Emotion (Saravia et al., 2018), Stanford Sentiment Treebank (SST2 & SST5) (Socher et al., 2013), Multiclass Sentiment Analysis, Twitter Financial News Sentiment, IMDb (Maas et al., 2011), and Hate Speech Offensive (Davidson et al., 2017).
  - [Reimagining Safety Alignment with An Image](https://aclanthology.org/2025.emnlp-main.486.pdf)

### → Text classification
- **Synthetic data generation** (behaviors tasks) — *causes*
  > synthetic data plays a crucial role in boosting the performance of LLMs across a variety of downstream tasks, including text classification... (Section 2.2)
  - [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e0bfe8bbaa0e70809f0a8ccd9c2ff3e-Paper-Conference.pdf)
- **Consistency** (constructs) — *measured_by*
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Sensitivity** (constructs) — *measured_by*
  > We perform an empirical comparison of these metrics on text classification tasks, using them as guideline for understanding failure modes of the LLM. (Section 1)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [Mutual-Taught](https://aclanthology.org/2025.acl-long.795.pdf)
- **Social bias** (constructs) — *measured_by*
  - [Position: Rethinking LLM Bias Probing Using Lessons from the Social Sciences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/morehouse25a/morehouse25a.pdf)

### Associated with
- **In-context learning** (constructs)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **Multiclass classification** (behaviors tasks)
  - [MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf)
- **Semantic understanding** (constructs)
  - [Empowering Math Problem Generation and Reasoning for Large Language Model via Synthetic Data based Continual Learning Framework](https://aclanthology.org/2025.emnlp-main.1224.pdf)
- **Pseudo-label generation** (behaviors tasks)
  > We utilize LLMs to generate pseudo-labels for unlabeled texts through task-specific prompting designed for classification. (Section 3.1)
  - [MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf)

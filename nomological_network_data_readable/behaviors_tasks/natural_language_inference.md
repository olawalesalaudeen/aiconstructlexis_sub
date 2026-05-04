# Natural language inference
**Type:** Behavior  
**Referenced in:** 112 papers  
**Also known as:** Test output prediction, Visual entailment, Implicit relation inference, Semantic inference, Speaker meaning inference, Textual entailment prediction, Linguistic inference, Pragmatic inference, Abductive inference, Deductive inference, Inductive inference, Compositional rule inference, Reverse event inference  

## State of the Field

Across the provided literature, Natural Language Inference (NLI) is overwhelmingly defined as the task of determining the logical relationship between a 'premise' sentence and a 'hypothesis' sentence. This relationship is most frequently classified into three categories: entailment (the hypothesis is true given the premise), contradiction (the hypothesis is false), and neutral (the relationship is undetermined). The field operationalizes and measures this behavior using a wide array of datasets, with MNLI, XNLI, RTE, QNLI, and SNLI being the most commonly cited instruments. Other datasets such as HellaSwag are also used, with some work framing the task as predicting the most logical continuation of an event. A closely related framing, 'textual entailment,' is also present, described as deciding whether a hypothesis is 'supported by' a premise, with one source likening it to a 'soft version of theorem proving'. A smaller body of work extends the concept to other modalities and reasoning types, with definitions for 'visual entailment' (using an image as the premise), 'pragmatic inference' (inferring speaker intent), and specific logical forms like deductive and inductive inference. NLI is frequently positioned as a core task for evaluating broader capabilities, with one paper stating it is a 'popular way of evaluating natural language understanding'. While the dominant usage centers on a three-way classification of sentence pairs, the term also encompasses a wider range of inferential behaviors.

## Sources

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)**
> The task of determining whether a 'hypothesis' sentence is true (entailment), false (contradiction), or undetermined (neutral) given a 'premise' sentence.

**[Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf) (as "Textual entailment")**
> Deciding whether a hypothesis is supported by a premise in a sentence-pair classification format.

**[LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (as "Test output prediction")**
> The observable task of generating the expected output for a given test case input, based solely on a natural language problem statement.

**[Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf) (as "Visual entailment")**
> The task of determining whether a textual hypothesis is true, false, or neutral based on the content of a given image.

**[Self-Adjust Softmax](https://aclanthology.org/2025.emnlp-main.398.pdf) (as "Implicit relation inference")**
> Inferring relationships between entities that are not explicitly stated in the text but can be deduced from context, such as deducing (cat, near, window) from 'The cat is on the mat' and 'The mat is under the window'.

**[DiplomacyAgent: DoLLMs Balance Interests and Ethical Principles in International Events?](https://aclanthology.org/2025.emnlp-main.694.pdf) (as "Semantic inference")**
> The task of determining the logical relationship between two sentences, such as entailment or contradiction.

**[Sketch-of-Thought: EfficientLLMReasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1237.pdf) (as "Speaker meaning inference")**
> Inferring intended meaning, implications, or pragmatic intent behind utterances, beyond literal content.

**[Emergent morpho-phonological representations in self-supervised speech models](https://aclanthology.org/2025.emnlp-main.1426.pdf) (as "Textual entailment prediction")**
> The task of determining whether a 'hypothesis' sentence can be logically inferred from a 'premise' sentence.

**[DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models’ Understanding onIndian Culture](https://aclanthology.org/2025.emnlp-main.69.pdf) (as "Linguistic inference")**
> The capacity to draw correct conclusions about missing linguistic forms or glosses from contextual and grammatical evidence.

**[Merger-as-a-Stealer: Stealing TargetedPIIfrom AlignedLLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.296.pdf) (as "Pragmatic inference")**
> The latent ability to derive meaning from context, speaker intention, and social conventions, going beyond literal interpretation to understand implicatures in language.

**[What are Foundation Models Cooking in the Post-Soviet World?](https://aclanthology.org/2025.emnlp-main.1045.pdf) (as "Abductive inference")**
> The ability to form a plausible explanatory hypothesis from observations that require explanation.

**[What are Foundation Models Cooking in the Post-Soviet World?](https://aclanthology.org/2025.emnlp-main.1045.pdf) (as "Deductive inference")**
> The ability to apply a rule or hypothesis to premises so that conclusions follow with logical necessity.

**[What are Foundation Models Cooking in the Post-Soviet World?](https://aclanthology.org/2025.emnlp-main.1045.pdf) (as "Inductive inference")**
> A form of logical reasoning where general rules or conclusions are derived from specific instances or observations, often associated with fast, intuitive System 1 thinking.

**[ECODecoding: Entropy-Based Control for Controllability and Fluency in Controllable Dialogue Generation](https://aclanthology.org/2025.emnlp-main.1438.pdf) (as "Compositional rule inference")**
> The ability to infer underlying compositional rules from implicit patterns presented in limited data, as humans do when learning language.

**[Charting the Landscape ofAfricanNLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1415.pdf) (as "Reverse event inference")**
> The ability to determine the correct sequence of events or actions by reconstructing the event flow from partial information.

## Relationships

### Natural language inference →
- **MNLI** (measurements) — *measured_by*
  > natural language inference and entailment: ANLI-R{1,2,3} (Nie et al., 2020), CB (De Marneffe et al., 2019), RTE, QNLI (QA/NLI), MNLI (Williams et al., 2018). (Section 5.1)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
- **XNLI** (measurements) — *measured_by*
  > For NLI and reasoning, we use XNLI (Conneau et al., 2018) and XCOPA (Ponti et al., 2020) with zero-shot prompting. (Section 5.4)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **RTE** (measurements) — *measured_by*
  > We also evaluate KnOTS in the NLI setting, by merging six PEFT llama3-8B (AI, 2024) models finetuned on SNLI (Bowman et al., 2015), MNLI (Williams et al., 2018), SICK (Marelli et al., 2014), QNLI, RTE (Wang et al., 2019), and SCITAIL (Khot et al., 2018). (§ 5.2)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **QNLI** (measurements) — *measured_by*
  > natural language inference and entailment: ANLI-R{1,2,3} (Nie et al., 2020), CB (De Marneffe et al., 2019), RTE, QNLI (QA/NLI), MNLI (Williams et al., 2018). (Section 5.1)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
- **SNLI** (measurements) — *measured_by*
  > We also evaluate KnOTS in the NLI setting, by merging six PEFT llama3-8B (AI, 2024) models finetuned on SNLI (Bowman et al., 2015), MNLI (Williams et al., 2018), SICK (Marelli et al., 2014), QNLI, RTE (Wang et al., 2019), and SCITAIL (Khot et al., 2018). (§ 5.2)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > We consider nine varied downstream tasks: ... (e) natural language inference (HellaSwag (Zellers et al., 2019))
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **ANLI** (measurements) — *measured_by*
  - [EncryptedLLM: Privacy-Preserving Large Language Model Inference via GPU-Accelerated Fully Homomorphic Encryption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/de-castro25a/de-castro25a.pdf)
- **GLUE-X** (measurements) — *measured_by*
  > In particular, we consider 7 classical NLU tasks: Sentiment Analysis (SA), Natural Language Inference (NLI), Paraphrasing, Question-Answering NLI (QNLI), Textual Entailment, Textual Similarity, and Linguistic Acceptability (Grammar). (Section 3.1)
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **MultiNLI** (measurements) — *measured_by*
  > NLI accuracies on MultiNLI test splits and two Adversarial NLI evaluation datasets for Sheared Llama-1.3B (LM) finetuned (FT) on MultiNLI.
  - [Follow the Beaten Path: The Role of Route Patterns on Vision-Language Navigation Agents Generalization Abilities](https://aclanthology.org/2025.naacl-long.407.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  > All the tasks except for MT are classification tasks, where we use the lm-evaluation-harness (Gao et al., 2024) evaluation tool and report accuracy. (Section 5.4)
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **WNLI** (measurements) — *measured_by*
  > for inference tasks, the RTE and WNLI (both from GLUE) datasets (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > Natural Language Inference (NLI) using PIQA (Bisk et al., 2020) and WinoGrande (Sakaguchi et al., 2020) (Section 4).
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [It Helps to Take a Second Opinion: Teaching Smaller LLMs To Deliberate Mutually via Selective Rationale Optimisation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bc12914d66b41b6bfc2d3a5decdb498b-Paper-Conference.pdf)
- **LogicNLI** (measurements) — *measured_by*
  - [Continual Learning in Multilingual Sign Language Translation](https://aclanthology.org/2025.naacl-long.547.pdf)
- **HANS** (measurements) — *measured_by*
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **e-SNLI** (measurements) — *measured_by*
  > The task of e-SNLI is to determine the logical relationship (contradiction, neutral or entailment) between the premise and hypothesis. (Section 4.1)
  - [When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity](https://aclanthology.org/2025.emnlp-main.427.pdf)
- **PubMedQA** (measurements) — *measured_by*
  > For yes/no QA, we select PubMedQA (Jin et al., 2019), an English natural language inference task related to medical research papers. (Section 4.2)
  - [OmniEval: An Omnidirectional and AutomaticRAGEvaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.293.pdf)

### → Natural language inference
- **Natural language understanding** (constructs) — *measured_by*
  > In the recent past, a popular way of evaluating natural language understanding (NLU), was to consider a model’s ability to perform natural language inference (NLI) tasks. (Abstract)
  - [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.466.pdf)

### Associated with
- **Logical reasoning** (constructs)
  > “what is required is not the capability of logical reasoning ... However, understanding implicit toxic language needs inferences that draw on nonlogical, subjective social experiences, conventional knowledge, and contextual awareness. ... Such reasoning from context, intention, and signs is named ‘pragmatic inference’”
  - [Merger-as-a-Stealer: Stealing TargetedPIIfrom AlignedLLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.296.pdf)
- **MNLI** (measurements)
  > Paraphrasing datasets like PAWS (Zhang et al., 2019) are common pretraining datasets, and standard NLI datasets like MNLI (Williams et al., 2018) contain many similar samples due to their construction through edits, so NLI predictions are expected to be more reliable on these pairs. (Section 4.3)
  - [Auto-GDA: Automatic Domain Adaptation for Efficient Grounding Verification in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eb6233e02f7d9efbb84acd839a996fb-Paper-Conference.pdf)
- **Knowledge** (constructs)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Textual reasoning** (behaviors tasks)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks)
  - [Incremental Sentence Processing Mechanisms in Autoregressive Transformer Language Models](https://aclanthology.org/2025.naacl-long.165.pdf)
- **Consistency** (constructs)
  - [Query-focused Referentiability Learning for Zero-shot Retrieval](https://aclanthology.org/2025.naacl-long.277.pdf)

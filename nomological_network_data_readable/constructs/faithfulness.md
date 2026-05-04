# Faithfulness
**Type:** Construct  
**Referenced in:** 1024 papers  
**Also known as:** Believability, Factual consistency, Honesty, Utility, Sensitivity to contextual knowledge, Knowledge sensitivity, Legal accuracy, Legal fidelity, Legal relevance judgment, Legal language understanding, Contextual adherence, Context fidelity, Faithful reasoning, Translation adequacy, Reasoning fidelity, Faithful calibration, Source fidelity, Entity-relation consistency, Factuality hallucination, Factual reliability, Information accuracy, Factual correctness, Chemical understanding, Clinical factual accuracy, Overall satisfaction, Meaning accuracy, Correctness, Response accuracy, Knowledge accuracy, Medical factuality, Detoxification accuracy, Factual completeness, Omission-aware reasoning, Logical correctness, Functional correctness, Code correctness, Response correctness, Linguistic correctness, Utterance fluency, Syntactic correctness, Chart correctness, Normative correctness, Calibration, Verbalized calibration, Trust calibration, Emotional calibration, Linguistic calibration, Probability calibration, Clinical reliability, Source reliability, Code reliability, Answer reliability, Disambiguation reliability, Editing reliability, Predictive accuracy, Contextual faithfulness, Context-faithfulness, Task correctness, Prediction correctness, Plot quality, Proof correctness, Syntax correctness, Formal correctness, Formulation correctness, Synthetic data quality, Token quality, Mathematical rigor, Miscalibration, QA-calibration, Belief calibration, Internal consistency, Logical rigor, Semantic coherence, Argument coherence, Behavioral accuracy, Behavioral coherence, Description correctness, Emotional coherence, Factual inconsistency, Factual reasoning, Logical coherence, Plot coherence, Proof accuracy, Robustness to prompt variations, Self-consistency, Story coherence, Style coherence, Terminology accuracy, Text coherence, Topic coherence, Understandability, Safety inconsistency, Annotation reliability, Cognitive fidelity, Grounding ability, Grounding capability, Groundedness, Visual localization, Attribution groundedness, Grounded understanding, Argument groundedness, Evidence attribution, Context utilisation, Region understanding, Framing divergence, Scoring reliability, Trustfulness, Trust, Credibility, Clinical trustworthiness, Image fidelity, Downstream Performance, Downstream performance, General abilities, General ability, General capability, General performance, Generic performance, Model Capability, Model capability, Model performance, General purpose performance, General-purpose ability, General-purpose capabilities, Model utility, Model Utility, Model competence, Effectiveness, General task performance, Task performance, Downstream benchmark performance, Foundational capabilities, LLM capability, Benign capabilities, Generalist abilities, General problem-solving, Capability, General model utility, Skill, Cross capabilities, Worst-case performance, Ability, AI R&D capability, ML R&D capability, Research engineering skill, Latent abilities, Latent capability, Action-level ability, Decision-level ability, General language model capability, General model capability, Capabilities set, Benchmark utility, Value, Capabilities, All-round capability, Model reliability, Benign utility, Factual attribution, Factual and Logical Correctness, Coherent factuality, Independent factuality, Long-context factuality, Response truthfulness, Distributional faithfulness, Skill-specific truthfulness, Situated faithfulness, Word-deed consistency, Causal faithfulness, Distributional fidelity, Evaluation fidelity, Circuit faithfulness, Explanation faithfulness, Downstream task performance, Model usefulness, Fact-checking capability, Sincerity, Fact discernment, Factuality preservation, General utility, Prediction reliability, Reasoning reliability, Reward model reliability, Tool reliability, Verifier reliability, Trust and safety, Agreeableness, Openness to Experience, Honesty-Humility, Extraversion, Emotional Stability  

## State of the Field

Faithfulness is a broad construct with numerous, often overlapping definitions, appearing under names such as 'Truthfulness,' 'Factual Consistency,' 'Honesty,' and 'Reliability.' The prevailing usage concerns the alignment of a model's output with verifiable information, which is framed in two primary ways: correspondence to real-world facts, or consistency with a specific provided context. For instance, some papers define it as the "latent tendency... to produce responses that are factually accurate" ("Towards Understanding Sycophancy in Language Models"), while others focus on whether generated text is "factually supported by and does not contradict a given source document" ("On-Policy Distillation of Language Models"). A distinct line of work treats faithfulness as an internal property, referring to the alignment between a model's reasoning process and its final output, or the logical coherence of its generated explanations. Less common definitions extend the concept to include the functional correctness of code, the believability of agent behavior, and the calibration of a model's expressed confidence with its actual accuracy. Across these varied framings, faithfulness is most frequently operationalized through performance on benchmarks like TruthfulQA, MMLU, and GSM8k, as well as through human evaluation and LLM-as-a-judge setups. The construct is commonly studied in opposition to 'Hallucination,' which is treated as a failure of faithfulness, and is also discussed alongside 'Safety' and 'Helpfulness'.

## Sources

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf) (as "Truthfulness")**
> The latent tendency of a language model to produce responses that are factually accurate and aligned with reality, regardless of user beliefs or preferences.

**[Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)**
> The degree to which a model's internal reasoning and stated intentions align with its actual behavior, including both internal consistency (own acceptable offers) and external consistency (predictions of opponent's acceptable offers).

**[Guess & Sketch: Language Model Guided Transpilation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e4996c14d3674b5ca5c318829290783-Paper-Conference.pdf) (as "Semantic correctness")**
> The degree to which a generated program preserves the operational meaning and behavior of the source program.

**[On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf) (as "Factual consistency")**
> The degree to which generated text, such as a summary, is factually supported by and does not contradict a given source document.

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf) (as "Honesty")**
> A desirable model trait encompassing truthfulness and the ability to acknowledge when it lacks information, for instance by abstaining from answering or avoiding hallucinations.

**[Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf) (as "Usefulness")**
> The degree to which a model's output effectively meets a user's requirements and performs well on general language processing tasks, often considered in a trade-off with safety.

**[SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3075b88e583a0e98d8b24338a613060-Paper-Conference.pdf) (as "Believability")**
> The extent to which an agent's behavior is perceived as natural, realistic, and consistent with its assigned character profile.

**[Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf) (as "Utility")**
> The model's ability to maintain its performance on general downstream tasks after a targeted intervention like detoxification.

**[Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf) (as "Fidelity")**
> The latent tendency for generated images to appear visually realistic and well-formed.

**[SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.576.pdf) (as "Semantic fidelity")**
> The degree to which a substitution preserves the intended meaning of the original sentence.

**[PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.33.pdf) (as "Factuality")**
> The degree to which model outputs are grounded in correct external information rather than unsupported generation.

**[EMNLP: Educator-role Moral and Normative Large Language Models Profiling](https://aclanthology.org/2025.emnlp-main.43.pdf) (as "Factual accuracy")**
> The degree to which generated summaries correctly reflect the source content without hallucinated or incorrect statements.

**[MultiAgentESC: ALLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.233.pdf) (as "Sensitivity to contextual knowledge")**
> The degree to which a language model adjusts its output to align with information provided in the context, especially when that information conflicts with its internal knowledge.

**[2025.emnlp-main.233.checklist](https://aclanthology.org/attachments/2025.emnlp-main.233.checklist.pdf) (as "Knowledge sensitivity")**
> The degree to which a large language model's behavior is influenced by provided contextual information, which can be controlled or steered.

**[Quantifying Language Disparities in Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.200.pdf) (as "Legal fidelity")**
> The degree to which a model's generated answer aligns with the correct legal interpretation of relevant statutory provisions and does not contradict or omit key legal elements.

**[Quantifying Language Disparities in Multilingual Large Language Models](https://aclanthology.org/2025.emnlp-main.200.pdf) (as "Legal accuracy")**
> The correctness of a model's generated answer according to legal statutes and expert judgment.

**[Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.738.pdf) (as "Legal language understanding")**
> The latent ability to interpret legal texts well enough to judge relevance among statutes and precedents in legal retrieval.

**[Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.738.pdf) (as "Legal relevance judgment")**
> The latent ability of a model to determine whether a legal statute or precedent is relevant to a given case based on factual and legal alignment, beyond mere lexical or semantic similarity.

**[DCP: Dual-Cue Pruning for Efficient Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1075.pdf) (as "Context fidelity")**
> The degree to which a model's answers remain grounded in and consistent with the provided input context rather than contradicting or fabricating information.

**[Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1076.pdf) (as "Contextual adherence")**
> The degree to which the model's generated speech conforms to its conditioning inputs, such as the provided text and speaker identity.

**[Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1302.pdf) (as "Faithful reasoning")**
> The latent tendency of a model to abstain from answering when faced with missing or contradictory input information, reflecting clinical safety awareness.

**[Context andPOSin Action: A Comparative Study ofChinese Homonym Disambiguation in Human and Language Models](https://aclanthology.org/2025.emnlp-main.1405.pdf) (as "Meaning preservation")**
> The latent ability of a model to modify text while retaining the original semantic content, ensuring that the adversarial example conveys the same underlying message.

**[Attacking Misinformation Detection Using Adversarial Examples Generated by Language Models](https://aclanthology.org/2025.emnlp-main.1406.pdf) (as "Translation adequacy")**
> The degree to which a model's translation preserves the meaning of the source text, as judged by human evaluators.

**[Frame First, Then Extract: A Frame-Semantic Reasoning Pipeline for Zero-Shot Relation Triplet Extraction](https://aclanthology.org/2025.emnlp-main.1392.pdf) (as "Reasoning fidelity")**
> The degree to which a model's generated explanation for a safety decision is coherent, logically sound, and faithfully reflects the content of the input prompt.

**[Multilingual Pretraining for Pixel Language Models](https://aclanthology.org/2025.emnlp-main.1505.pdf) (as "Faithful calibration")**
> The degree to which a model's linguistically expressed uncertainty aligns with its intrinsic uncertainty, reflecting a trustworthy and accurate communication of confidence.

**[VISaGE: Understanding Visual Generics and Exceptions](https://aclanthology.org/2025.emnlp-main.1656.pdf) (as "Source fidelity")**
> The degree to which a model's outputs accurately reflect and are grounded in the provided source documents, without introducing unsupported information.

**[MemeArena: Automating Context-Aware Unbiased Evaluation of Harmfulness Understanding for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.891.pdf) (as "Accuracy")**
> The correctness of generated audit procedures as measured by the ability to recover masked technical terms using reference-based evaluation with ROUGE-F1.

**[T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.186.pdf) (as "Factuality hallucination")**
> The latent tendency of a language model to generate semantically plausible but factually ungrounded relationships between entities, reflecting a failure to align with real-world knowledge.

**[T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.186.pdf) (as "Entity-relation consistency")**
> The degree to which the relationships between entities in a text align with verified real-world knowledge, serving as a discriminative trait between human-written and machine-generated content.

**[Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf) (as "Factual reliability")**
> The degree to which the outputs and reasoning steps of an LLM-based system are factually correct and free from hallucination.

**[Good Intentions BeyondACL: Who DoesNLPfor Social Good, and Where?](https://aclanthology.org/2025.emnlp-main.260.pdf) (as "Information accuracy")**
> The degree to which a long-form response supports correct answers to specific proxy questions about the target content.

**[Process-Supervised Reinforcement Learning for Code Generation](https://aclanthology.org/2025.emnlp-main.720.pdf) (as "Factual correctness")**
> The degree to which a model's generated text faithfully represents the semantic information and facts contained within the source knowledge graph.

**[Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf) (as "Chemical understanding")**
> The depth of a model's grasp of chemical concepts, structures, and nomenclature as reflected in its handling of molecular text.

**[Puzzled by Puzzles: When Vision-Language Models Can’t Take a Hint](https://aclanthology.org/2025.emnlp-main.1102.pdf) (as "Clinical factual accuracy")**
> The degree to which a report correctly states findings, locations, severity, and comparison information without clinically meaningful mistakes.

**[GRADA: Graph-based Reranking against Adversarial Documents Attack](https://aclanthology.org/2025.emnlp-main.1133.pdf) (as "Overall satisfaction")**
> A human-perceived, holistic judgment of the quality and appropriateness of the generated audio for a given video.

**[Does Context Matter? A Prosodic Comparison ofEnglish andSpanish in Monolingual and Multilingual Discourse Settings](https://aclanthology.org/2025.emnlp-main.1190.pdf) (as "Correctness")**
> The latent trait reflecting whether the model's final answer is factually or logically accurate and adheres to formatting constraints.

**[Does Context Matter? A Prosodic Comparison ofEnglish andSpanish in Monolingual and Multilingual Discourse Settings](https://aclanthology.org/2025.emnlp-main.1190.pdf) (as "Meaning accuracy")**
> The degree to which the model preserves the intended meaning and logical consistency with the expected output, ensuring fidelity to the task goal.

**[In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1209.pdf) (as "Response accuracy")**
> The ability of the model to correctly understand and address user questions or conversational prompts based on the provided context.

**[Zero-shot Multimodal Document Retrieval via Cross-modal Question Generation](https://aclanthology.org/2025.emnlp-main.1325.pdf) (as "Knowledge accuracy")**
> The model's ability to retrieve and apply factual knowledge accurately, especially in domains requiring broad general or domain-specific information.

**[Sentence Smith: Controllable Edits for Evaluating Text Embeddings](https://aclanthology.org/2025.emnlp-main.1344.pdf) (as "Medical factuality")**
> The extent to which a model's outputs align with established medical knowledge and avoid factual errors in clinical content.

**[Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models](https://aclanthology.org/2025.emnlp-main.1808.pdf) (as "Detoxification accuracy")**
> The underlying capacity of a model to effectively identify and remove toxic content across different forms and contexts without over- or under-correcting.

**[PersonalizedLLMDecoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1724.pdf) (as "Omission-aware reasoning")**
> The latent ability of a model to detect when a factually correct claim is misleading due to the strategic omission of critical context that alters its implied meaning.

**[PersonalizedLLMDecoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1724.pdf) (as "Factual completeness")**
> The degree to which a claim and its supporting evidence contain all critical context necessary for a non-misleading interpretation.

**[VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](https://aclanthology.org/2025.emnlp-main.138.pdf) (as "Logical correctness")**
> The degree to which candidate actions, steps, or solutions are logically feasible and appropriate within a reasoning or agentic process.

**[ReMedy: Learning Machine Translation Evaluation from Human Preferences with Reward Modeling](https://aclanthology.org/2025.emnlp-main.218.pdf) (as "Functional correctness")**
> The degree to which a generated smart contract behaves as intended according to its specification and passes all relevant test cases.

**[Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.286.pdf) (as "Code correctness")**
> The latent property of a model to generate functionally accurate code that passes defined test cases without logical or syntactic errors.

**[Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.983.pdf) (as "Response correctness")**
> The latent ability of the model to generate responses that accurately match reference answers, indicating its capacity to produce factually correct outputs.

**[In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1209.pdf) (as "Utterance fluency")**
> The model's capacity to produce grammatically correct, coherent, and naturally flowing responses in conversational contexts.

**[REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf) (as "Linguistic correctness")**
> The latent proficiency of a model in producing grammatically correct, stylistically appropriate, and normatively fluent text in the target language.

**[HESEIA: A community-based dataset for evaluating social biases in large language models, co-designed in real school settings inLatinAmerica](https://aclanthology.org/2025.emnlp-main.1276.pdf) (as "Syntactic correctness")**
> The ability to generate code that is free of syntax errors and adheres to the rules of the target programming languages like HTML, CSS, and JavaScript.

**[SEMMA: A Semantic Aware Knowledge Graph Foundation Model](https://aclanthology.org/2025.emnlp-main.1622.pdf) (as "Chart correctness")**
> The extent to which a generated chart accurately reflects the query intent and the underlying data.

**[Africa Health Check: Probing Cultural Bias in MedicalLLMs](https://aclanthology.org/2025.emnlp-main.1640.pdf) (as "Normative correctness")**
> The extent to which a model adheres to an idealized standard of gender fairness, such as equal representation of masculine and feminine forms in translations.

**[MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities ofLLMTutors](https://aclanthology.org/2025.emnlp-main.12.pdf) (as "Calibration")**
> The degree to which the model's expressed confidence in its predictions matches its actual accuracy, particularly in detecting misaligned actions.

**[SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.35.pdf) (as "Confidence calibration")**
> The degree to which a model's expressed confidence in its predictions aligns with its actual accuracy.

**[2025.emnlp-main.74.checklist](https://aclanthology.org/attachments/2025.emnlp-main.74.checklist.pdf) (as "Verbalized calibration")**
> The degree to which a model's confidence, when expressed in natural language, aligns with its actual accuracy or correctness on a given task.

**[Few-Shot Learning Translation from New Languages](https://aclanthology.org/2025.emnlp-main.164.pdf) (as "Trust calibration")**
> The alignment between user expectations and actual system capabilities, such that trust in the AI artifact is neither under- nor over-estimated based on its performance and anthropomorphic cues.

**[UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1573.pdf) (as "Emotional calibration")**
> The degree to which responses are appropriately tuned to the emotional complexity and context of a user's situation rather than being generic or overly affirmative.

**[VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://aclanthology.org/2025.emnlp-main.1543.pdf) (as "Linguistic calibration")**
> The ability of a model to express graded levels of confidence in its statements, often through numerical scores embedded in natural language.

**[CourtReasoner: CanLLMAgents Reason Like Judges?](https://aclanthology.org/2025.emnlp-main.1788.pdf) (as "Probability calibration")**
> The degree to which the model's confidence scores align with actual classification accuracy, enabling reliable threshold-based decision-making in operational settings.

**[Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf) (as "Reliability")**
> The degree to which the model produces stable, trustworthy reasoning and answers without content hallucination.

**[D-CoDe: Scaling Image-PretrainedVLMs to Video via Dynamic Compression and Question Decomposition](https://aclanthology.org/2025.emnlp-main.598.pdf) (as "Clinical reliability")**
> The extent to which a generated medical report is trustworthy and valid for use in real-world clinical decision-making.

**[BTC-SAM: LeveragingLLMs for Generation of Bias Test Cases for Sentiment Analysis Models](https://aclanthology.org/2025.emnlp-main.764.pdf) (as "Source reliability")**
> The latent capacity to evaluate the trustworthiness and credibility of information sources cited in a claim or argument.

**[DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset forLLM-based Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.836.pdf) (as "Code reliability")**
> The latent property of a model to consistently generate code that is syntactically correct and executable without errors.

**[Generator-Assistant Stepwise Rollback Framework for Large Language Model Agent](https://aclanthology.org/2025.emnlp-main.893.pdf) (as "Answer reliability")**
> The degree to which the model's generated answers are accurate, complete, and trustworthy, often enhanced through verification processes.

**[Are Large Language Models Chronically Online Surfers? A Dataset forChineseInternet Meme Explanation](https://aclanthology.org/2025.emnlp-main.864.pdf) (as "Disambiguation reliability")**
> The alignment between a model’s self-assessed confidence in its disambiguation ability and its actual accuracy, reflecting cognitive awareness and trustworthiness of outputs.

**[CrystalICL: Enabling In-Context Learning for Crystal Generation](https://aclanthology.org/2025.emnlp-main.930.pdf) (as "Editing reliability")**
> The degree to which a concept editing method consistently and effectively controls a target concept in a model's outputs across different inputs.

**[Enhancing Speech Large Language Models with Prompt-Aware Mixture of Audio Encoders](https://aclanthology.org/2025.emnlp-main.975.pdf) (as "Predictive accuracy")**
> The latent capacity of the model to correctly forecast a student's future performance on educational tasks based on historical interaction data and evolving knowledge states.

**[Self-calibration for Language Model Quantization and Pruning](https://aclanthology.org/2025.naacl-long.510.pdf) (as "Reasoning faithfulness")**
> The degree to which a model's generated reasoning path accurately reflects the actual process leading to its answer, avoiding hallucinated or misleading justifications.

**[Length Controlled Generation for Black-boxLLMs](https://aclanthology.org/2025.acl-long.826.pdf) (as "Contextual faithfulness")**
> The latent ability of a model to generate responses that are fully supported by and consistent with the provided contextual information, avoiding hallucinations or unsupported claims.

**[LongSafety: Evaluating Long-Context Safety of Large Language Models](https://aclanthology.org/2025.acl-long.1531.pdf) (as "Context-faithfulness")**
> The latent ability of a model to generate responses that accurately reflect the provided contextual information, especially when it conflicts with the model's parametric knowledge.

**[Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf) (as "Task correctness")**
> The extent to which the model's predicted answer is right for the question after generating a rationale.

**[Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf) (as "Prediction correctness")**
> The latent ability of a model to produce accurate predictions, typically measured by task-specific accuracy metrics.

**[Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf) (as "Data quality")**
> The degree to which a synthetic or real example is relevant, unambiguous, and representative of the target real-world distribution.

**[Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf) (as "Plot quality")**
> The degree to which a story has a recognizable and coherent structure with events that move the narrative forward without logical or conceptual inconsistencies.

**[ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf) (as "Proof correctness")**
> The property that a generated proof is valid and accepted by the proof assistant as establishing the theorem statement.

**[DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf) (as "Syntax correctness")**
> The model's capability to generate Verilog code that adheres to the language's grammatical and structural rules, allowing it to be successfully compiled.

**[Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf) (as "Formulation correctness")**
> The degree to which a generated mathematical optimization model accurately and faithfully represents the requirements and constraints of a real-world problem described in natural language.

**[WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf) (as "Synthetic data quality")**
> The latent property of synthetic model outputs that determines their effectiveness in improving downstream model performance during post-training, influenced by factors such as comprehensiveness, clarity, and stylistic coherence rather than raw model capability.

**[Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gulati25a/gulati25a.pdf) (as "Mathematical rigor")**
> The quality of a model's generated solution in terms of being logically airtight, providing justification for claims, and adhering to formal proof standards.

**[Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pang25a/pang25a.pdf) (as "Token quality")**
> The degree to which an individual token carries useful task-specific information for supervised fine-tuning rather than being redundant, uninformative, or harmful.

**[Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/petruzzellis25a/petruzzellis25a.pdf) (as "Formal correctness")**
> The extent to which a generated plan satisfies the formal preconditions and postconditions required for execution.

**[Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf) (as "Uncertainty estimation")**
> The latent capacity of a model to estimate the reliability of its own predictions, typically measured via entropy or confidence scores, used here to guide dynamic fusion decisions.

**[LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf) (as "Confidence estimation")**
> Deriving a numerical measure of a model's certainty in its generated output, either at the token, sequence, or claim level.

**[Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf) (as "Miscalibration")**
> The degree to which a model's output probabilities are poorly aligned with the true likelihood of correctness, leading to unreliable confidence scores.

**[QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf) (as "QA-calibration")**
> A latent property where a model's confidence scores match its actual accuracy conditional on specific groups of question-and-answer pairs, ensuring reliability across different topics or user contexts.

**[ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.158.pdf) (as "Belief calibration")**
> The extent to which the model's expressed confidence in a statement matches the statement's actual truthfulness.

**[BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf) (as "Consistency")**
> The similarity between the data distributions of the finetuning tasks and the target task, reflecting how closely the auxiliary tasks align with the objective of the target task in the latent space.

**[Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf) (as "Internal consistency")**
> The degree of agreement between latent predictions decoded from intermediate layers and the final prediction, reflecting the stability of the model's internal reasoning process.

**[Human Simulacra: Benchmarking the Personification of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1de176cfe0d9a288bc97faa574d7197c-Paper-Conference.pdf) (as "Personality")**
> A character's characteristic patterns of thought, feeling, and behavior that can be modeled as a multidimensional latent profile.

**[VibeCheck: Discover and Quantify Qualitative Differences in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/acbfe708197ff78ad04cc1beb1710979-Paper-Conference.pdf) (as "Logical rigor")**
> A tendency for outputs to present well-supported reasoning with clear justification and coherent logic.

**[SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf) (as "Semantic equivalence")**
> The latent notion that two texts express the same meaning, used to treat paraphrased answers as the same event.

**[ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf) (as "Semantic coherence")**
> The ability to maintain logical consistency and meaningful connections within the generated output, especially when processing information from disparate parts of a long context.

**[A Unified Supervised and Unsupervised Dialogue Topic Segmentation Framework Based on Utterance Pair Modeling](https://aclanthology.org/2025.naacl-long.253.pdf) (as "Coherence")**
> The logical consistency of the tutor's response with the prior dialogue and the student's current level of understanding, ensuring continuity in the educational interaction.

**[Embedding derived animacy rankings offer insights into the sources of grammatical animacy](https://aclanthology.org/2025.naacl-long.63.pdf) (as "Story coherence")**
> The overall quality of a long-form story in which plot development, context, and expression remain consistent and readable.

**[Embedding derived animacy rankings offer insights into the sources of grammatical animacy](https://aclanthology.org/2025.naacl-long.63.pdf) (as "Plot coherence")**
> The degree to which the sequence of events in a story follows a logical and causally sound progression, resulting in a fluent and understandable plot.

**[COVE:COntext andVEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.103.pdf) (as "Factual inconsistency")**
> The phenomenon where a model-generated summary contains information that contradicts or is unsupported by the source document or established world knowledge.

**[Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.124.pdf) (as "Proof accuracy")**
> The degree to which a model's generated reasoning steps are both logically correct and relevant to the final conclusion, reflecting faithful internal reasoning.

**[IrokoBench: A New Benchmark forAfrican Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.140.pdf) (as "Terminology accuracy")**
> The latent ability of a model to correctly translate domain-specific financial terms, reflecting its grasp of specialized vocabulary and conceptual consistency across languages.

**[DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf) (as "Factual reasoning")**
> The ability to produce responses grounded in factual knowledge and to avoid generating false claims, especially in the presence of misleading or humorous prompts.

**[Analyzing (In)Abilities ofSAEs via Formal Languages](https://aclanthology.org/2025.naacl-long.250.pdf) (as "Logical coherence")**
> The quality of a dialogue where arguments and responses are logically consistent and make sense within the given context.

**[Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.252.pdf) (as "Topic coherence")**
> The latent degree to which utterances within a dialogue segment belong to the same topic, inferred from their semantic and structural relationships.

**[Token-based Decision Criteria Are Suboptimal in In-context Learning](https://aclanthology.org/2025.naacl-long.279.pdf) (as "Argument coherence")**
> The degree to which a counterspeech response presents specific, logically consistent, and evidence-based arguments that refute the hateful content.

**[Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf) (as "Self-consistency")**
> The ability of a language model to maintain coherent and non-contradictory responses when presented with paraphrased or semantically equivalent prompts.

**[Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf) (as "Robustness to prompt variations")**
> The stability of model responses when the same question is reworded or paraphrased.

**[EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.316.pdf) (as "Emotional coherence")**
> The consistency of emotional expression over the course of a dialogue so that responses remain aligned with the character's emotional pattern.

**[Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf) (as "Behavioral accuracy")**
> The consistency of a character's actions and linguistic patterns with their defined personality and traits.

**[Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf) (as "Behavioral coherence")**
> The logical consistency of a character's actions in relation to their previous behaviors and the current context of the story.

**[MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.499.pdf) (as "Style coherence")**
> The degree to which a response matches the intended character style, tone, and child-directed wording specified by the prompt.

**[Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.504.pdf) (as "Description correctness")**
> The degree to which a model's textual description of an image accurately reflects the visual content, including entities, attributes, and relationships.

**[AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.509.pdf) (as "Text coherence")**
> The degree to which generated calibration text is fluent, semantically plausible, and structurally consistent, as an indicator of quality in synthetic data.

**[KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf) (as "Understandability")**
> The quality of a generated text being clear and easy to comprehend by a human reader.

**[RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://aclanthology.org/2025.emnlp-main.253.pdf) (as "Safety inconsistency")**
> A latent discrepancy in Large Language Models where the ability to identify harmful requests as a discriminator is significantly better than the ability to defend against them as a generator.

**[R-CHAR: A Metacognition-Driven Framework for Role-Playing in Large Language Models](https://aclanthology.org/2025.emnlp-main.1373.pdf) (as "Annotation reliability")**
> The consistency and accuracy of similarity annotations and condition statements across repeated or human-verified judgments.

**[Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1372.pdf) (as "Cognitive fidelity")**
> The extent to which a model authentically simulates a character’s perspective, psychological state, and decision-making processes rather than merely mimicking surface traits.

**[IG-Pruning: Input-Guided Block Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.538.pdf) (as "Evaluation reliability")**
> The stability and dependability of evaluation outcomes, particularly in the presence of ambiguous or subjective criteria.

**[Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf) (as "Grounding")**
> The model's ability to connect high-level concepts and reasoning processes to fine-grained, low-level visual details in a video, such as object identities, motion, and interactions.

**[VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/804e757b7d7043c26701c3a313032101-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Grounding ability")**
> The capacity to produce precise spatial outputs for GUI elements, such as coordinates or bounding boxes, from screenshots.

**[Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf) (as "Grounding capability")**
> The latent ability to accurately associate textual references with specific visual locations or bounding boxes in a UI.

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf) (as "Groundedness")**
> The extent to which an LLM's response is derived solely from the information within provided documents rather than its internal parametric knowledge.

**[MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf) (as "Visual localization")**
> The latent ability to identify where in an image the relevant subject or evidence for a question is located.

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf) (as "Attribution groundedness")**
> The quality of an LLM's generated citations in a RAG context, specifically whether the citations are relevant and sufficiently support the claims they are attached to.

**[CogCoM: A Visual Language Model with Chain-of-Manipulations Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1dcee1cd6890ab7fcdf173ec10526da9-Paper-Conference.pdf) (as "Grounded understanding")**
> The ability to connect language expressions to specific image regions or objects with precise spatial localization.

**[RAGLLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.282.pdf) (as "Evidence attribution")**
> The latent ability of a model to correctly and faithfully link statements in its explanations to the supporting source evidence, ensuring that citations reflect actual content and context from the provided passages.

**[Waste Not, Want Not; RecycledGumbel Noise Improves Consistency in Natural Language Generation](https://aclanthology.org/2025.naacl-long.293.pdf) (as "Argument groundedness")**
> The extent to which a generated argument is factually supported by and consistent with the retrieved evidence, minimizing hallucination or contradiction.

**[Adversarial Alignment with Anchor Dragging Drift (A3D2): Multimodal Domain Adaptation with Partially Shifted Modalities](https://aclanthology.org/2025.acl-long.968.pdf) (as "Context utilisation")**
> The latent ability of a language model to effectively leverage retrieved external information when generating responses, reflecting how well it integrates evidence into its predictions.

**[CPCF: A Cross-Prompt Contrastive Framework for Referring Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25h/zhu25h.pdf) (as "Region understanding")**
> The latent ability of a referring MLLM to accurately interpret and generate responses based on a specific visual region indicated by a prompt, distinguishing it from surrounding or similar regions.

**[learnable soft visual prompt](https://aclanthology.org/2025.emnlp-main.996.pdf) (as "Framing divergence")**
> The latent tendency of an LLM to generate conflicting narrative interpretations of the same event when conditioned on different personas, reflecting epistemic contradictions shaped by perspective.

**[Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf) (as "Trustworthiness")**
> The quality of a model being reliable and consistent in its understanding and generation, as evidenced by properties like self-consistency.

**[Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf) (as "Scoring reliability")**
> The degree to which a reward model consistently and accurately assigns scores that reflect true human preferences, enhanced by access to external verification tools.

**[Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf) (as "Trustfulness")**
> The reliability and credibility of the model's output results, often compromised by the generation of false or unsupported content.

**[Do as We Do, Not as You Think: the Conformity of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1da9ca7e9cef4b1af63913f05d1630a4-Paper-Conference.pdf) (as "Trust")**
> A latent positive disposition developed by an agent towards its peers based on their historical accuracy, which can increase its propensity to conform to their subsequent judgments.

**[CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/70fa5df8e3300dc30bf19bee44a56155-Paper-Conference.pdf) (as "Credibility")**
> The degree to which a model's answers are based on a genuine understanding of relevant evidence within the video content, rather than relying on shortcuts or biases.

**[Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.548.pdf) (as "Clinical trustworthiness")**
> The degree to which model outputs are reliable and safe for clinical use, especially when intermediate reasoning errors could lead to misjudgments.

**[Localize, Understand, Collaborate: Semantic-Aware Dragging via Intention Reasoner](https://proceedings.neurips.cc/paper_files/paper/2024/file/3dd7c683eddc14f8cabcd6ce8d48cd41-Paper-Conference.pdf) (as "Image fidelity")**
> The degree to which a generated image is realistic, high-quality, and free from artifacts or unintended distortions.

**[Private Attribute Inference from Images with Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb97e9a7c811904c9b01f51fde66edcf-Paper-Conference.pdf) (as "General capabilities")**
> A model's overall proficiency and performance across a wide range of tasks, which is shown to correlate with its performance on specific, potentially harmful tasks like private attribute inference.

**[Everything is Editable: Extend Knowledge Editing to Unstructured Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/02763667a5761ff92bb15d8751bcd223-Paper-Conference.pdf) (as "General ability")**
> The model's broader performance on unrelated tasks or knowledge after editing, reflecting whether edits degrade overall capability.

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf) (as "General capability")**
> The model's overall performance on a wide range of standard, non-adversarial tasks, such as question answering and instruction following.

**[Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf) (as "Generic performance")**
> The overall downstream effectiveness of a pre-trained LLM across diverse evaluation tasks rather than a single target domain.

**[Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf) (as "General abilities")**
> The broad set of capabilities of a large language model, such as reasoning and summarization, that are not directly targeted by a specific model edit but can be negatively affected by it.

**[Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf) (as "General performance")**
> The overall capability of a model across a wide range of tasks and domains, as opposed to performance on a specific, narrow task.

**[Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf) (as "General-purpose capabilities")**
> Broad task competence of an LLM across heterogeneous chat and reasoning tasks rather than a single narrow domain.

**[Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf) (as "Downstream Performance")**
> The latent capability of the model to successfully complete tasks, inferred from accuracy or scores on benchmarks.

**[RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf) (as "Downstream performance")**
> The overall capability of a pre-trained model to perform effectively on a wide range of evaluation tasks it was not explicitly trained on.

**[LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf) (as "Model utility")**
> The overall performance and general knowledge of a model on tasks and data that are unaffected by the unlearning process.

**[Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf) (as "Model Capability")**
> The general ability of the model to perform desired tasks, such as language modeling or question answering, without degradation.

**[Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf) (as "Model capability")**
> The overall level of a model's general cognitive abilities, such as reasoning and knowledge, which often correlates with its scale and performance on standard benchmarks.

**[Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf) (as "General-purpose ability")**
> A model's broad capability across a wide range of tasks and domains, as opposed to specialized performance on a narrow domain.

**[Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf) (as "Model Utility")**
> The latent general capability of a model to perform diverse tasks effectively without degradation from interventions.

**[Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf) (as "Model performance")**
> The overall effectiveness of a model on a given set of tasks, which is a key determinant for successful ensembling.

**[Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf) (as "General purpose performance")**
> The overall capability of a model across a wide range of domains and tasks, as opposed to specialized performance in a narrow domain.

**[Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf) (as "Task performance")**
> The overall quality of an ensemble's outputs on a downstream benchmark or task, as reflected by how well it solves the target evaluation problems.

**[Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf) (as "General task performance")**
> The overall capability of the model to perform standard NLP tasks without regression when optimized for specific constraints like long context.

**[TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf) (as "Effectiveness")**
> The overall quality or performance of the model in achieving its objectives, as measured by accuracy on evaluation benchmarks, distinct from its computational cost.

**[Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf) (as "Model competence")**
> The overall capability and effectiveness of a language model that results from its pretraining regimen, which is crucially impacted by data mixture proportions.

**[Improving Pretraining Data Using Perplexity Correlations](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c625366ae28066fcb1827b44517d674-Paper-Conference.pdf) (as "Downstream benchmark performance")**
> The latent capability of a language model that enables it to score highly on a diverse set of evaluation benchmarks.

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "LLM capability")**
> The overall latent ability level of a language model across evaluation tasks, inferred from how well it performs and is ranked relative to other models.

**[StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf) (as "Foundational capabilities")**
> The general, pre-existing knowledge and skills of a large language model, which are evaluated to ensure they are not degraded by specialized fine-tuning.

**[HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf) (as "General problem-solving")**
> A broad capability to handle a variety of tasks and input formats, acquired through training on a diverse multi-task dataset.

**[Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf) (as "Generalist abilities")**
> The model's capacity to perform well across a wide and diverse range of tasks and domains without task-specific fine-tuning.

**[Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf) (as "Benign capabilities")**
> The extent to which a safeguarded model retains general-purpose performance on non-target tasks after safety training and tampering.

**[Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf) (as "Capability")**
> A general, transferable ability of a model, reflected as a commonality across a dataset, that can be localized to a specific set of neurons and enhances performance on related tasks.

**[Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf) (as "General model utility")**
> The model's broad task performance across general-purpose evaluations, used here as an overall indicator of whether interventions preserve usefulness.

**[Unearthing Skill-level Insights for Understanding Trade-offs of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5526c73e3ff4f2a34009e13d15f52fcb-Paper-Conference.pdf) (as "Skill")**
> A latent underlying competency that a model must apply to solve an evaluation instance, often spanning multiple benchmarks and surfacing only through solution steps.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Cross capabilities")**
> The ability to integrate multiple distinct capabilities across different types of expertise to address complex, real-world tasks.

**[Estimating the Probabilities of Rare Outputs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdaac2a02c4fdcae77ba083b110efcc3-Paper-Conference.pdf) (as "Worst-case performance")**
> The extent to which a model avoids highly undesirable outputs on rare or adversarially shifted inputs rather than only performing well on average.

**[A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf) (as "Decision-level ability")**
> The latent cognitive capacity for problem-solving, diagnosis, and planning required to determine a course of action for a given skill.

**[A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf) (as "Action-level ability")**
> The latent capacity for executing a pre-determined solution, such as implementing a fix or carrying out a planned procedure for a given skill.

**[Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf) (as "General language model capability")**
> The overall proficiency of a model across a wide range of standard language understanding and generation benchmarks.

**[Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf) (as "General model capability")**
> The overall performance and competence of a model across a wide range of standard tasks, distinct from its specialized safety behaviors.

**[MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf) (as "Competence")**
> The underlying ability of an agent to successfully achieve a given goal, often operationalized as the probability of success.

**[The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf) (as "Latent capability")**
> A capability that a model possesses but exhibits with low probability by default, which can be revealed through specific elicitation techniques.

**[MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf) (as "Latent abilities")**
> The underlying, unobservable capabilities of a model, such as problem-solving or linguistic skills, which are estimated using statistical methods rather than being directly measured.

**[PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://raw.githubusercontent.com/mlresearch/v267/main/assets/starace25a/starace25a.pdf) (as "ML R&D capability")**
> The latent ability of an AI agent to perform tasks associated with machine learning research and development, such as understanding, implementing, and experimentally validating novel concepts from academic papers.

**[Reliable and Efficient Amortized Model-based Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25c/truong25c.pdf) (as "Ability")**
> The unobservable, unidimensional latent trait of a language model that determines its probability of correctly answering a question, independent of the question's difficulty.

**[RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf) (as "AI R&D capability")**
> The latent ability of an AI agent to autonomously perform the complex, open-ended tasks involved in advancing artificial intelligence research and development.

**[RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf) (as "Research engineering skill")**
> The underlying competence to make progress on open-ended machine learning research engineering problems through experimentation, implementation, and compute-efficient problem solving.

**[Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf) (as "Capabilities set")**
> The latent trait representing the scope of tasks an LLM can reliably perform, which determines its suitability for specific agent roles within a system.

**[STAMP Your Content: Proving Dataset Membership via Watermarked Rephrasings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rastogi25a/rastogi25a.pdf) (as "Benchmark utility")**
> The extent to which a watermarked or modified benchmark continues to function as a reliable and valid measure of model performance, preserving both absolute scores and relative model rankings.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Value")**
> The usefulness or functional benefit of a creative artifact to the user, assessed based on task-specific criteria such as persuasiveness, clarity, or appropriateness.

**[A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Capabilities")**
> The general ability of a model to perform tasks correctly and generate high-quality, useful, and coherent information.

**[MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf) (as "All-round capability")**
> Broad general task competence across diverse benchmark types, including knowledge and reasoning tasks.

**[CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf) (as "Model reliability")**
> The overall dependability and consistency of a model's performance and outputs across different situations.

**[Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf) (as "Benign utility")**
> The model's ability to maintain its performance and helpfulness on legitimate, non-malicious tasks and prompts.

**[Scalable Influence and Fact Tracing for Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/65798a76cc176c29b6bfefe84b0a03ff-Paper-Conference.pdf) (as "Factual attribution")**
> The degree to which a model's factual prediction can be traced back to training examples that logically entail or explicitly state the fact.

**[Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf) (as "Coherent factuality")**
> A property of a sequence of generated claims where each claim is not only factually correct but also logically deducible from the preceding claims, the initial prompt, and a body of ground truth knowledge.

**[Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf) (as "Independent factuality")**
> A property of a generated output where correctness is determined by evaluating each constituent claim in isolation against a ground truth, without considering the logical dependencies between claims.

**[Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf) (as "Long-context factuality")**
> The degree to which a model's outputs are faithful to the information presented in a long input context, as opposed to generating fabricated content.

**[JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf) (as "Factual and Logical Correctness")**
> The latent ability to distinguish objectively true statements from false or logically flawed ones, independent of stylistic preferences.

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf) (as "Response truthfulness")**
> A quality of an LLM's generated claims in a RAG context, specifically focusing on the correctness of the claims themselves.

**[LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations](https://proceedings.iclr.cc/paper_files/paper/2025/file/a712d461e57201efe35d429a6f1731c1-Paper-Conference.pdf) (as "Skill-specific truthfulness")**
> The property that a model's internal encoding of truthfulness is not universal, but rather multifaceted and dependent on the specific cognitive skill required by a task, such as factual retrieval or common-sense reasoning.

**[Model Equality Testing: Which Model is this API Serving?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d73234a13815fc1f9779dd17d89be9b4-Paper-Conference.pdf) (as "Distributional faithfulness")**
> The degree to which an API's output distribution matches the reference model's distribution without undisclosed modifications.

**[To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf) (as "Situated faithfulness")**
> The ability of a model to provide a correct answer by dynamically calibrating its trust between its internal knowledge and an external context, regardless of whether the context is correct or incorrect.

**[Large Language Models Often Say One Thing and Do Another](https://proceedings.iclr.cc/paper_files/paper/2025/file/3be14af22f0b311325664277f48111f4-Paper-Conference.pdf) (as "Word-deed consistency")**
> The degree to which a model's actions in specific, grounded scenarios align with its stated opinions, values, or theoretical beliefs.

**[Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf) (as "Causal faithfulness")**
> The extent to which a feature's interpretation matches its causal role in the model's computation.

**[A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf) (as "Distributional fidelity")**
> The capacity of a generative model to preserve the statistical properties of the true data distribution across successive generations of data synthesis.

**[GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5ce40ee957e4f76ef53c09d0bae20f4-Paper-Conference.pdf) (as "Evaluation fidelity")**
> The degree to which an LLM's evaluation of content, such as a research idea, aligns with high-quality, human-level judgment.

**[Evaluating Neuron Explanations: A Unified Framework with Sanity Checks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oikarinen25a/oikarinen25a.pdf) (as "Explanation faithfulness")**
> The degree to which a textual explanation accurately and reliably describes the behavior of a specific neural network unit, such as a neuron.

**[Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ak/wang25ak.pdf) (as "Circuit faithfulness")**
> The degree to which a discovered subcircuit replicates the behavior of the full model, reflecting how reliably the circuit captures the model's functional mechanisms.

**[BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.444.pdf) (as "Model usefulness")**
> The latent capacity of a model to maintain general language understanding and generation quality during and after unlearning procedures.

**[AutoEval-ToD: Automated Evaluation of Task-oriented Dialog Systems](https://aclanthology.org/2025.naacl-long.509.pdf) (as "Downstream task performance")**
> The ability of a language model to maintain its effectiveness on a range of evaluation tasks after undergoing compression techniques like quantization or pruning.

**[ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.17.pdf) (as "Fact-checking capability")**
> The overall capacity of an LLM to correctly verify claims and produce sound justifications across diverse and complex real-world scenarios.

**[Capture the Key in Reasoning to EnhanceCoTDistillation Generalization](https://aclanthology.org/2025.acl-long.22.pdf) (as "Sincerity")**
> The latent tendency of a model to provide truthful and evidence-backed responses without deception during cooperation with humans.

**[400B](https://aclanthology.org/2025.acl-long.250.pdf) (as "Fact discernment")**
> The ability to accurately distinguish between correct factual information and incorrect or counterfactual statements, especially when both are present in the context.

**[Data Quality Issues in Multilingual Speech Datasets: The Need for Sociolinguistic Awareness and Proactive Language Planning](https://aclanthology.org/2025.acl-long.371.pdf) (as "Factuality preservation")**
> The degree to which generated text remains faithful to the factual information contained in the original source text across iterations.

**[Knowledge Graph Retrieval-Augmented Generation forLLM-based Recommendation](https://aclanthology.org/2025.acl-long.1318.pdf) (as "General utility")**
> The model's ability to maintain high performance on general tasks and benchmarks regardless of the presence or activation of the SUDO key.

**[A Hitchhiker’s Guide to Scaling Law Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/choshen25a/choshen25a.pdf) (as "Prediction reliability")**
> The degree to which estimated scaling laws consistently and accurately forecast the performance of target models, accounting for variability across seeds and training dynamics.

**[Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf) (as "Tool reliability")**
> The ability of a large language model to accurately and effectively interact with external tools throughout a task, maximizing successful outcomes while minimizing errors and hallucinations.

**[Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf) (as "Reward model reliability")**
> The degree to which a reward model's assigned rewards align with the actual performance of model responses, varying across reward ranges.

**[BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf) (as "Reasoning reliability")**
> The consistency and trustworthiness of a model's reasoning outputs, such that generated rationales are valid and lead to correct conclusions across diverse problems.

**[From Passive to Active Reasoning: Can Large Language Models Ask the Right Questions under Incomplete Information?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25e/zhou25e.pdf) (as "Verifier reliability")**
> The consistency and accuracy with which a model component evaluates and selects promising reasoning paths during search-based active reasoning, affecting the overall effectiveness of strategies like tree-of-thought.

**[Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf) (as "Trust and safety")**
> The latent property of a system that ensures user protection from harm, including misinformation, abuse, and unsafe content, while fostering user confidence in the technology.

**[Multimedia Event Extraction withLLMKnowledge Editing](https://aclanthology.org/2025.emnlp-main.206.pdf) (as "Agreeableness")**
> The latent tendency of an LLM to generate responses that are cooperative, empathetic, and non-confrontational, reducing biased and toxic outputs.

**[Multimedia Event Extraction withLLMKnowledge Editing](https://aclanthology.org/2025.emnlp-main.206.pdf) (as "Openness to Experience")**
> The latent tendency of an LLM to generate novel, imaginative, and cognitively flexible responses, associated with reduced toxicity in text generation.

**[Multimedia Event Extraction withLLMKnowledge Editing](https://aclanthology.org/2025.emnlp-main.206.pdf) (as "Honesty-Humility")**
> The latent tendency of an LLM to avoid flattery, deception, and self-serving responses, promoting truthful and ethically grounded outputs.

**[Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.277.pdf) (as "Extraversion")**
> A personality trait characterized by sociability, assertiveness, and a tendency to be outgoing and energetic.

**[Bias Mitigation or Cultural Commonsense? EvaluatingLLMs with aJapanese Dataset](https://aclanthology.org/2025.emnlp-main.875.pdf) (as "Emotional Stability")**
> The latent disposition of an LLM to generate responses perceived as calm, resilient to emotional influence, and low in emotional variability.

## Relationships

### Faithfulness →
- **MMLU** (measurements) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Expected calibration error** (measurements) — *measured_by*
  - [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.503.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC** (measurements) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons](https://proceedings.neurips.cc/paper_files/paper/2024/file/08a9e28c96d016dd63903ab51cd085b0-Paper-Conference.pdf)
- **FactScore** (measurements) — *measured_by*
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **RTE** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **WikiText** (measurements) — *measured_by*
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
- **TOFU** (measurements) — *measured_by*
  - [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b69bc53449ba46bb981951078929a5e-Paper-Conference.pdf)
- **Arena-Hard** (measurements) — *measured_by*
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **Trustworthiness** (constructs) — *causes*
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **GLUE** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **WikiText-2** (measurements) — *measured_by*
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **FLASK** (measurements) — *measured_by*
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)
- **HelpSteer** (measurements) — *measured_by*
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **LongBench** (measurements) — *measured_by*
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf)
- **Reliability diagrams** (measurements) — *measured_by*
  - [Calibrating Expressions of Certainty](https://proceedings.iclr.cc/paper_files/paper/2025/file/66b35d2e8d524706f39cc21f5337b002-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **SIQA** (measurements) — *measured_by*
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **DS-1000** (measurements) — *measured_by*
  - [Removal of Hallucination on Hallucination: Debate-AugmentedRAG](https://aclanthology.org/2025.acl-long.771.pdf)
- **CC-SHAP** (measurements) — *measured_by*
  - [Bit-Flip Error Resilience inLLMs: A Comprehensive Analysis and Defense Framework](https://aclanthology.org/2025.emnlp-main.529.pdf)
- **MiniCheck** (measurements) — *measured_by*
  - [SLM-Mod: Small Language Models SurpassLLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.442.pdf)
- **LibriSpeech** (measurements) — *measured_by*
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **APPS** (measurements) — *measured_by*
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
- **CodeContests** (measurements) — *measured_by*
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
- **BLiMP** (measurements) — *measured_by*
  - [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **NQ-Swap** (measurements) — *measured_by*
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **Reward model** (measurements) — *measured_by*
  - [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **WebQuestions** (measurements) — *measured_by*
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **MathQA** (measurements) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **Reasoning** (constructs) — *causes*
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
- **UltraFeedback** (measurements) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **OpenLLM Leaderboard** (measurements) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RAGAS** (measurements) — *measured_by*
  - [Speech Discrete Tokens or Continuous Features? A Comparative Analysis for Spoken Language Understanding inSpeechLLMs](https://aclanthology.org/2025.emnlp-main.1267.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
- **XSum** (measurements) — *measured_by*
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **EAP-IG** (measurements) — *measured_by*
  - [Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ak/wang25ak.pdf)
- **SocialIQA** (measurements) — *measured_by*
  - [RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf)
- **COPA** (measurements) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **MultiRC** (measurements) — *measured_by*
  - [Predictive Data Selection: The Data That Predicts Is the Data That Teaches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shum25a/shum25a.pdf)
- **BM25** (measurements) — *measured_by*
  - [Scalable Influence and Fact Tracing for Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/65798a76cc176c29b6bfefe84b0a03ff-Paper-Conference.pdf)
- **Creak** (measurements) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **CommonsenseQA 2.0** (measurements) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **CEval** (measurements) — *measured_by*
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **BigBench** (measurements) — *measured_by*
  - [QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurements) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **JudgeBench** (measurements) — *measured_by*
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **SST** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **MRPC** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **CoLA** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **NLI** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **IFEval** (measurements) — *measured_by*
  - [Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation andGaussian-Decayed Contrastive Learning](https://aclanthology.org/2025.acl-long.245.pdf)
- **VicunaEval** (measurements) — *measured_by*
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **AG News** (measurements) — *measured_by*
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Spider** (measurements) — *measured_by*
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)
- **HumanEval-X** (measurements) — *measured_by*
  - [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf)
- **Generalization** (constructs) — *causes*
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Elo rating system** (measurements) — *measured_by*
  - [UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eafca59fcbabb555fdb5373e2f34385e-Paper-Conference.pdf)
- **Bradley-Terry model** (measurements) — *measured_by*
  - [UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eafca59fcbabb555fdb5373e2f34385e-Paper-Conference.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf)
- **Privacy** (constructs) — *causes*
  - [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf)
- **BBQ** (measurements) — *measured_by*
  - [Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf)
- **MedQA** (measurements) — *measured_by*
  - [Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf)
- **LIMA** (measurements) — *measured_by*
  - [Data Selection via Optimal Control for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
- **FaithEval** (measurements) — *measured_by*
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **FreshQA** (measurements) — *measured_by*
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **NaturalQA** (measurements) — *measured_by*
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **PopQA** (measurements) — *measured_by*
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **SAMSum** (measurements) — *measured_by*
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **LMSYS Chatbot Arena** (measurements) — *measured_by*
  - [Re-evaluating Open-ended Evaluation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/57a009897ab00e2d811a4581ad1f7239-Paper-Conference.pdf)
- **MQUAKE** (measurements) — *measured_by*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **AlignScore** (measurements) — *measured_by*
  - [SafeKey: Amplifying Aha-Moment Insights for Safety Reasoning](https://aclanthology.org/2025.emnlp-main.1292.pdf)
- **CMMLU** (measurements) — *measured_by*
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Winograd** (measurements) — *measured_by*
  - [Evaluating Morphological Compositional Generalization in Large Language Models](https://aclanthology.org/2025.naacl-long.60.pdf)
- **HaluEval** (measurements) — *measured_by*
  - [DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf)
- **TofuEval** (measurements) — *measured_by*
  - [Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.498.pdf)
- **Comprehensiveness** (constructs) — *measured_by*
  - [The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1769.pdf)
- **Knowledge forgetting** (constructs) — *correlates*
  - [SLM-Mod: Small Language Models SurpassLLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.442.pdf)
- **LongEval** (measurements) — *measured_by*
  - [COVE:COntext andVEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.103.pdf)
- **HumanEvalPlus** (measurements) — *measured_by*
  - [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf)
- **AlpacaEval 2** (measurements) — *measured_by*
  - [Data Whisperer: Efficient Data Selection for Task-SpecificLLMFine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1136.pdf)
- **MedMCQA** (measurements) — *measured_by*
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **LiveCodeBench** (measurements) — *measured_by*
  - [Removal of Hallucination on Hallucination: Debate-AugmentedRAG](https://aclanthology.org/2025.acl-long.771.pdf)
- **TRUE** (measurements) — *measured_by*
  - [POINTS-Reader: Distillation-Free Adaptation of Vision-Language Models for Document Conversion](https://aclanthology.org/2025.emnlp-main.83.pdf)
- **MM-Hal-Bench** (measurements) — *measured_by*
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **NL4OPT** (measurements) — *measured_by*
  - [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf)
- **IndustryOR** (measurements) — *measured_by*
  - [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf)
- **ComplexOR** (measurements) — *measured_by*
  - [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf)
- **EvoEval** (measurements) — *measured_by*
  - [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **PPI++** (measurements) — *measured_by*
  - [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf)
- **BIG-Bench** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **CUAD** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **FrontierMath** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **AIME** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **SWE-Bench Verified** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **LiveBench** (measurements) — *measured_by*
  - [Position: Don’t Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bowyer25a/bowyer25a.pdf)
- **GSM** (measurements) — *measured_by*
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **MELD** (measurements) — *measured_by*
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **Logit lens** (measurements) — *measured_by*
  - [WISE: Weak-Supervision-Guided Step-by-Step Explanations for MultimodalLLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.742.pdf)
- **VisEval** (measurements) — *measured_by*
  - [DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset forLLM-based Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.836.pdf)
- **Personality mirroring** (behaviors tasks) — *correlates*
  - [Bias Mitigation or Cultural Commonsense? EvaluatingLLMs with aJapanese Dataset](https://aclanthology.org/2025.emnlp-main.875.pdf)
- **MOLERR2FIX** (measurements) — *measured_by*
  - [Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf)
- **RoBERTa-MNLI** (measurements) — *measured_by*
  - [learnable soft visual prompt](https://aclanthology.org/2025.emnlp-main.996.pdf)
- **MMMU-Pro** (measurements) — *measured_by*
  - [Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf)
- **MathVista** (measurements) — *measured_by*
  - [Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf)
- **MathVision** (measurements) — *measured_by*
  - [Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf)
- **Originality** (constructs) — *correlates*
  - [On the Same Wavelength? Evaluating Pragmatic Reasoning in Language Models across Broad Concepts](https://aclanthology.org/2025.emnlp-main.1009.pdf)
- **PLLuM-Align** (measurements) — *measured_by*
  - [REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Faithfulness
- **Catastrophic forgetting** (behaviors tasks) — *causes*
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Overconfidence** (constructs) — *causes*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *causes*
  - [Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [Structure-Guided Large Language Models for Text-to-SQL Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25k/zhang25k.pdf)
- **Contextual understanding** (constructs) — *causes*
  - [ReMedy: Learning Machine Translation Evaluation from Human Preferences with Reward Modeling](https://aclanthology.org/2025.emnlp-main.218.pdf)
- **Factuality** (constructs) — *causes*
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Generation diversity** (constructs) — *causes*
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **Uncertainty quantification** (constructs) — *causes*
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *measured_by*
  - [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Prior knowledge** (constructs) — *causes*
  - [P](https://aclanthology.org/2025.acl-long.722.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Factuality** (constructs)
  - [Large language model validity via enhanced conformal prediction methods](https://proceedings.neurips.cc/paper_files/paper/2024/file/d02ff1aeaa5c268dc34790dd1ad21526-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf)
- **Self-reflection** (behaviors tasks)
  - [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Truthfulness** (constructs)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
- **Constraint satisfaction** (constructs)
  - [KITAB: Evaluating LLMs on Constraint Satisfaction for Information Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/82846e19e6d42ebfd4ace4361def29ae-Paper-Conference.pdf)
- **Overconfidence** (constructs)
  - [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25b/xiao25b.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Uncertainty** (constructs)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Generation diversity** (constructs)
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Self-consistency** (measurements)
  - [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf)
- **Ambiguity** (constructs)
  - [Automatically Discovering How Misogyny is Framed on Social Media](https://aclanthology.org/2025.naacl-long.609.pdf)
- **In-context learning** (constructs)
  - [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **Coherence** (constructs)
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
- **Object hallucination** (behaviors tasks)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Sensitivity** (constructs)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
- **Helpfulness** (constructs)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness inLLMAgents](https://aclanthology.org/2025.naacl-long.596.pdf)
- **Information extraction** (behaviors tasks)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks)
  - [When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity](https://aclanthology.org/2025.emnlp-main.427.pdf)
- **Code efficiency** (constructs)
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Safety alignment** (constructs)
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
- **Knowledge** (constructs)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
- **Conversational ability** (constructs)
  - [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Plausibility** (constructs)
  - [SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **Programming** (behaviors tasks)
  - [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf)
- **Sycophancy** (constructs)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Objectivity** (constructs)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Context utilization** (constructs)
  - [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Conformal Prediction** (measurements)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Forget quality** (constructs)
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
- **Decision-making under uncertainty** (constructs)
  - [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf)
- **Future prediction** (behaviors tasks)
  - [DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf)
- **Language model pre-training** (behaviors tasks)
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **Compositionality** (constructs)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **Data-to-text generation** (behaviors tasks)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Causal reasoning** (constructs)
  - [Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf)
- **Parametric knowledge** (constructs)
  - [Probing for Arithmetic Errors in Language Models](https://aclanthology.org/2025.emnlp-main.412.pdf)
- **Reading comprehension** (constructs)
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **World knowledge** (constructs)
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [Removal of Hallucination on Hallucination: Debate-AugmentedRAG](https://aclanthology.org/2025.acl-long.771.pdf)
- **Min-K% method** (measurements)
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
- **Long-context reasoning** (constructs)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [SLM-Mod: Small Language Models SurpassLLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.442.pdf)
- **Privacy** (constructs)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Fact checking** (behaviors tasks)
  - [CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf)
- **Stealthiness** (constructs)
  - [Black-Box Adversarial Attacks on LLM-Based Code Completion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jenko25a/jenko25a.pdf)
- **Distribution alignment** (constructs)
  - [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.126.pdf)
- **WikiText** (measurements)
  - [Eliciting Implicit Acoustic Styles from Open-domain Instructions to Facilitate Fine-grained Controllable Generation of Speech](https://aclanthology.org/2025.emnlp-main.183.pdf)
- **LLM-as-a-judge** (measurements)
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Free-text explanation generation** (behaviors tasks)
  - [2025.emnlp-main.797.checklist](https://aclanthology.org/attachments/2025.emnlp-main.797.checklist.pdf)
- **Repetitive generation** (behaviors tasks)
  - [Current Semantic-change Quantification Methods Struggle with Discovery in the Wild](https://aclanthology.org/2025.emnlp-main.1792.pdf)

# Consistency
**Type:** Construct  
**Referenced in:** 803 papers  
**Also known as:** Internal consistency, Logical rigor, Semantic coherence, Argument coherence, Behavioral accuracy, Behavioral coherence, Correctness, Description correctness, Emotional coherence, Factual correctness, Factual inconsistency, Factual reasoning, Information accuracy, Knowledge accuracy, Logical coherence, Logical correctness, Plot coherence, Proof accuracy, Robustness to prompt variations, Self-consistency, Story coherence, Style coherence, Terminology accuracy, Text coherence, Topic coherence, Understandability, Safety inconsistency, Annotation reliability, Cognitive fidelity, Logical robustness, Self-Consistency, Solution consistency, Visual-semantic consistency, Reasoning consistency, Answer consistency, Cross-lingual consistency, Persona consistency, Output consistency, Temporal referential consistency, Role consistency, Character consistency, Global consistency, Evaluation consistency, Structural consistency, Task correctness, Prediction correctness, Plot quality, Proof correctness, Functional correctness, Response correctness, Syntactic correctness, Syntax correctness, Formal correctness, Formulation correctness, Synthetic data quality, Token quality, Mathematical rigor, Hallucination, Knowledge hallucination, Molecular hallucination, Object hallucination, Truth alignment, Factual precision, Factual recall, Factual consistency, Prompt faithfulness, Unfaithfulness, Believability, Honesty, Utility, Sensitivity to contextual knowledge, Knowledge sensitivity, Legal accuracy, Legal fidelity, Legal relevance judgment, Legal language understanding, Contextual adherence, Context fidelity, Faithful reasoning, Translation adequacy, Reasoning fidelity, Faithful calibration, Source fidelity, Entity-relation consistency, Factuality hallucination, Factual reliability, Chemical understanding, Clinical factual accuracy, Overall satisfaction, Meaning accuracy, Response accuracy, Medical factuality, Detoxification accuracy, Factual completeness, Omission-aware reasoning, Code correctness, Linguistic correctness, Utterance fluency, Chart correctness, Normative correctness, Calibration, Verbalized calibration, Trust calibration, Emotional calibration, Linguistic calibration, Probability calibration, Clinical reliability, Source reliability, Code reliability, Answer reliability, Disambiguation reliability, Editing reliability, Predictive accuracy, Factual attribution, Factual and Logical Correctness, Coherent factuality, Independent factuality, Long-context factuality, Context-faithfulness, Contextual faithfulness, Response truthfulness, Distributional faithfulness, Skill-specific truthfulness, Situated faithfulness, Word-deed consistency, Causal faithfulness, Distributional fidelity, Evaluation fidelity, Circuit faithfulness, Explanation faithfulness, Evaluation Reliability, Fact-checking capability, Sincerity, Fact discernment, Factuality preservation, Contextual coherence, Linguistic coherence, Local coherence, Response coherence, Spatiotemporal coherence, Audio-visual content consistency, Compositional consistency, Performance consistency, Expert activation consistency, Prediction consistency, Repository-level consistency, Sequential consistency, Statistical consistency, Storyline consistency, Stylistic consistency, Type consistency, Win rate-consistency, Conceptual incoherence, Process consistency, Agreeableness, Openness to Experience, Honesty-Humility, Extraversion, Emotional Stability, Speech-suitability  

## State of the Field

Across the surveyed literature, "Consistency" is a multifaceted construct used to describe several distinct desirable properties of language models, rather than a single, unified concept. The most prevalent usage frames consistency in terms of factuality, correctness, and faithfulness, where a model's output must align with verifiable facts and be grounded in provided source material. This framing is frequently operationalized as the inverse of `Hallucination`, an observable failure mode defined as generating factually incorrect or unsupported information; as one paper notes, "factual inconsistency" is one type of hallucination. A second major line of work defines consistency as internal coherence, encompassing logical, semantic, and narrative continuity, ensuring that generated text is free from self-contradiction and maintains a logical flow. A third common framing treats consistency as stability or robustness, where a model produces similar outputs for semantically equivalent inputs, often discussed under the term "self-consistency." Less frequent definitions describe consistency in terms of maintaining a stable persona, aligning data distributions during finetuning, or ensuring coherence across different languages and modalities. The construct is operationalized and measured through various means, including performance on benchmarks like `SNLI` and the `Alpaca instruction dataset`, evaluation frameworks such as `FLASK`, and the use of an `LLM-as-a-judge`.

## Sources

**[BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf)**
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

**[Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.183.pdf) (as "Factuality")**
> The degree to which a generated SQL query correctly and accurately represents the user's intended question.

**[ALiiCE: Evaluating Positional Fine-grained Citation Generation](https://aclanthology.org/2025.naacl-long.24.pdf) (as "Correctness")**
> The degree to which a generated response answers the query accurately.

**[Amphista: Bi-directional Multi-head Decoding for AcceleratingLLMInference](https://aclanthology.org/2025.naacl-long.451.pdf) (as "Factual correctness")**
> The degree to which a generated radiology report accurately and completely reflects the clinical observations present in the source medical image.

**[ALERT: AnLLM-powered Benchmark for Automatic Evaluation of Recommendation Explanations](https://aclanthology.org/2025.naacl-long.138.pdf) (as "Factual accuracy")**
> The latent ability of the model to generate responses that correctly reflect all plausible interpretations and ground-truth answers for ambiguous questions.

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

**[Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.290.pdf) (as "Accuracy")**
> The degree to which the model's generated responses are factually correct and align with established legal knowledge.

**[Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf) (as "Self-consistency")**
> The ability of a language model to maintain coherent and non-contradictory responses when presented with paraphrased or semantically equivalent prompts.

**[Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf) (as "Robustness to prompt variations")**
> The stability of model responses when the same question is reworded or paraphrased.

**[EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms](https://aclanthology.org/2025.naacl-long.316.pdf) (as "Emotional coherence")**
> The consistency of emotional expression over the course of a dialogue so that responses remain aligned with the character's emotional pattern.

**[Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf) (as "Knowledge accuracy")**
> The correctness of factual information provided by the character, ensuring it aligns with their established background and knowledge base.

**[Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf) (as "Behavioral accuracy")**
> The consistency of a character's actions and linguistic patterns with their defined personality and traits.

**[Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf) (as "Behavioral coherence")**
> The logical consistency of a character's actions in relation to their previous behaviors and the current context of the story.

**[CROPE: Evaluating In-Context Adaptation of Vision and Language Models to Culture-Specific Concepts](https://aclanthology.org/2025.naacl-long.403.pdf) (as "Information accuracy")**
> The degree to which a system's responses are factually correct and consistent with dialogue state labels and external knowledge.

**[MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.499.pdf) (as "Style coherence")**
> The degree to which a response matches the intended character style, tone, and child-directed wording specified by the prompt.

**[Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.504.pdf) (as "Description correctness")**
> The degree to which a model's textual description of an image accurately reflects the visual content, including entities, attributes, and relationships.

**[Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.504.pdf) (as "Logical correctness")**
> The degree to which a reasoning step is logically deduced from the facts and previous steps without contradiction.

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

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf) (as "Logical robustness")**
> The degree to which a response remains logically consistent and generally applicable throughout its reasoning process without contradictions.

**[BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf) (as "Logical consistency")**
> The absence of internal contradictions or discrepancies within the plot, character development, or themes of a generated summary.

**[Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf) (as "Self-Consistency")**
> The property of the model's internal beliefs not contradicting each other across different prompts or logical relations.

**[Step-by-Step Reasoning for Math Problems  via Twisted Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4d92f656cc99f60fe1bfc98386aee34-Paper-Conference.pdf) (as "Solution consistency")**
> The degree to which the model maintains logical coherence and correctness throughout the entire reasoning process.

**[FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf) (as "Visual-semantic consistency")**
> The degree to which the model's visual representations maintain a coherent and meaningful alignment with their corresponding semantic (textual) representations across different levels of granularity.

**[Empowering Visible-Infrared Person Re-Identification with Large Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d4ee9e805cc90f636c66778225181036-Paper-Conference.pdf) (as "Semantic consistency")**
> The extent to which representations preserve the same underlying meaning across text, fusion, and visible modalities.

**[SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf) (as "Temporal consistency")**
> The ability to maintain coherence and logical flow of events and objects across frames in a generated video.

**[Learning to Substitute Words with Model-based Score Ranking](https://aclanthology.org/2025.naacl-long.577.pdf) (as "Reasoning consistency")**
> The degree to which a model produces coherent and uniform reasoning patterns across diverse problems, reducing cognitive load through structural harmony.

**[SLIM: LetLLMLearn More and Forget Less with SoftLoRAand Identity Mixture](https://aclanthology.org/2025.naacl-long.247.pdf) (as "Answer consistency")**
> The extent to which multiple sampled reasoning paths yield the same final answer, serving as an indicator of confidence in the output.

**[Crowd Comparative Reasoning: Unlocking Comprehensive Evaluations forLLM-as-a-Judge](https://aclanthology.org/2025.acl-long.253.pdf) (as "Cross-lingual consistency")**
> The degree to which a multilingual model produces semantically equivalent and correct outputs for the same factual query when presented in different languages.

**[Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.277.pdf) (as "Persona consistency")**
> The degree to which persona traits remain stable after being used to generate a dialogue.

**[EcoTune: Token-Efficient Multi-Fidelity Hyperparameter Optimization for Large Language Model Inference](https://aclanthology.org/2025.emnlp-main.395.pdf) (as "Output consistency")**
> The degree to which a model produces the same output when presented with identical prompts multiple times.

**[Evaluating the Effectiveness and Scalability ofLLM-Based Data Augmentation for Retrieval](https://aclanthology.org/2025.emnlp-main.889.pdf) (as "Temporal referential consistency")**
> The latent ability of a model to produce identical correct answers to semantically equivalent temporal queries that differ only in whether they use absolute time references (e.g., 'January 1949') or event-based chronological references (e.g., 'before Concordia Seminary').

**[Improving Task Diversity in Label Efficient Supervised Finetuning ofLLMs](https://aclanthology.org/2025.emnlp-main.1094.pdf) (as "Role consistency")**
> The ability to maintain a consistent persona or role throughout a simulated dialogue interaction.

**[In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1209.pdf) (as "Character consistency")**
> The latent trait reflecting the model's ability to maintain a stable persona and behavioral patterns across interactions, consistent with the character's identity and background.

**[EnhancingLLM-Based Social Bot via an Adversarial Learning Framework](https://aclanthology.org/2025.emnlp-main.1186.pdf) (as "Global consistency")**
> The degree to which alignment decisions across multiple entity pairs maintain one-to-one correspondence and avoid conflicting matches, ensuring coherent integration across the entire dataset.

**[IG-Pruning: Input-Guided Block Pruning for Large Language Models](https://aclanthology.org/2025.emnlp-main.538.pdf) (as "Evaluation consistency")**
> The degree to which an LLM evaluator produces stable judgments across repeated assessments of the same response pair or score.

**[COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.136.pdf) (as "Structural consistency")**
> The degree to which the generated survey follows a coherent and logically organized structure with appropriate section divisions and thematic development, matching human-authored conventions.

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

**[CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf) (as "Functional correctness")**
> The latent tendency for generated code to satisfy the intended specification and pass functional verification.

**[Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b1cfc8ede53f452cabf8b9cf4eef76-Paper-Conference.pdf) (as "Response correctness")**
> The latent property of a model's generated response being factually or logically correct for a given input, which can be inferred from internal model states.

**[Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43f900f571de6c96a70d5724a0fb565-Paper-Conference.pdf) (as "Syntactic correctness")**
> The degree to which generated code conforms to programming-language syntax and avoids linter-detected errors.

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

**[An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf) (as "Hallucination")**
> An observable failure mode where the model generates information that is factually incorrect or not supported by the provided context.

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

**[Guess & Sketch: Language Model Guided Transpilation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e4996c14d3674b5ca5c318829290783-Paper-Conference.pdf) (as "Semantic correctness")**
> The degree to which a generated program preserves the operational meaning and behavior of the source program.

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

**[T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.186.pdf) (as "Factuality hallucination")**
> The latent tendency of a language model to generate semantically plausible but factually ungrounded relationships between entities, reflecting a failure to align with real-world knowledge.

**[T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.186.pdf) (as "Entity-relation consistency")**
> The degree to which the relationships between entities in a text align with verified real-world knowledge, serving as a discriminative trait between human-written and machine-generated content.

**[Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf) (as "Factual reliability")**
> The degree to which the outputs and reasoning steps of an LLM-based system are factually correct and free from hallucination.

**[Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf) (as "Chemical understanding")**
> The depth of a model's grasp of chemical concepts, structures, and nomenclature as reflected in its handling of molecular text.

**[Puzzled by Puzzles: When Vision-Language Models Can’t Take a Hint](https://aclanthology.org/2025.emnlp-main.1102.pdf) (as "Clinical factual accuracy")**
> The degree to which a report correctly states findings, locations, severity, and comparison information without clinically meaningful mistakes.

**[GRADA: Graph-based Reranking against Adversarial Documents Attack](https://aclanthology.org/2025.emnlp-main.1133.pdf) (as "Overall satisfaction")**
> A human-perceived, holistic judgment of the quality and appropriateness of the generated audio for a given video.

**[Does Context Matter? A Prosodic Comparison ofEnglish andSpanish in Monolingual and Multilingual Discourse Settings](https://aclanthology.org/2025.emnlp-main.1190.pdf) (as "Meaning accuracy")**
> The degree to which the model preserves the intended meaning and logical consistency with the expected output, ensuring fidelity to the task goal.

**[In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1209.pdf) (as "Response accuracy")**
> The ability of the model to correctly understand and address user questions or conversational prompts based on the provided context.

**[Sentence Smith: Controllable Edits for Evaluating Text Embeddings](https://aclanthology.org/2025.emnlp-main.1344.pdf) (as "Medical factuality")**
> The extent to which a model's outputs align with established medical knowledge and avoid factual errors in clinical content.

**[Unconditional Truthfulness: Learning Unconditional Uncertainty of Large Language Models](https://aclanthology.org/2025.emnlp-main.1808.pdf) (as "Detoxification accuracy")**
> The underlying capacity of a model to effectively identify and remove toxic content across different forms and contexts without over- or under-correcting.

**[PersonalizedLLMDecoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1724.pdf) (as "Omission-aware reasoning")**
> The latent ability of a model to detect when a factually correct claim is misleading due to the strategic omission of critical context that alters its implied meaning.

**[PersonalizedLLMDecoding via Contrasting Personal Preference](https://aclanthology.org/2025.emnlp-main.1724.pdf) (as "Factual completeness")**
> The degree to which a claim and its supporting evidence contain all critical context necessary for a non-misleading interpretation.

**[Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.286.pdf) (as "Code correctness")**
> The latent property of a model to generate functionally accurate code that passes defined test cases without logical or syntactic errors.

**[In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1209.pdf) (as "Utterance fluency")**
> The model's capacity to produce grammatically correct, coherent, and naturally flowing responses in conversational contexts.

**[REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf) (as "Linguistic correctness")**
> The latent proficiency of a model in producing grammatically correct, stylistically appropriate, and normatively fluent text in the target language.

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

**[Scalable Influence and Fact Tracing for Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/65798a76cc176c29b6bfefe84b0a03ff-Paper-Conference.pdf) (as "Factual attribution")**
> The degree to which a model's factual prediction can be traced back to training examples that logically entail or explicitly state the fact.

**[Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf) (as "Context-faithfulness")**
> The ability of a large language model to adhere to and effectively integrate information provided in the input context, even when it conflicts with the model's parametric knowledge.

**[Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf) (as "Coherent factuality")**
> A property of a sequence of generated claims where each claim is not only factually correct but also logically deducible from the preceding claims, the initial prompt, and a body of ground truth knowledge.

**[Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf) (as "Independent factuality")**
> A property of a generated output where correctness is determined by evaluating each constituent claim in isolation against a ground truth, without considering the logical dependencies between claims.

**[Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf) (as "Long-context factuality")**
> The degree to which a model's outputs are faithful to the information presented in a long input context, as opposed to generating fabricated content.

**[JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf) (as "Factual and Logical Correctness")**
> The latent ability to distinguish objectively true statements from false or logically flawed ones, independent of stylistic preferences.

**[FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf) (as "Contextual faithfulness")**
> The degree to which a model's responses remain aligned with the provided context rather than drifting to unsupported or external information.

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

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf) (as "Evaluation Reliability")**
> The degree to which an LLM evaluator produces consistent and unbiased scores unaffected by external manipulation or data contamination.

**[ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.17.pdf) (as "Fact-checking capability")**
> The overall capacity of an LLM to correctly verify claims and produce sound justifications across diverse and complex real-world scenarios.

**[Capture the Key in Reasoning to EnhanceCoTDistillation Generalization](https://aclanthology.org/2025.acl-long.22.pdf) (as "Sincerity")**
> The latent tendency of a model to provide truthful and evidence-backed responses without deception during cooperation with humans.

**[400B](https://aclanthology.org/2025.acl-long.250.pdf) (as "Fact discernment")**
> The ability to accurately distinguish between correct factual information and incorrect or counterfactual statements, especially when both are present in the context.

**[Data Quality Issues in Multilingual Speech Datasets: The Need for Sociolinguistic Awareness and Proactive Language Planning](https://aclanthology.org/2025.acl-long.371.pdf) (as "Factuality preservation")**
> The degree to which generated text remains faithful to the factual information contained in the original source text across iterations.

**[AGAV-Rater: Adapting Large Multimodal Model for AI-Generated Audio-Visual Quality Assessment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25f/cao25f.pdf) (as "Audio-visual content consistency")**
> The latent ability of a model to perceive whether the audio aligns semantically and contextually with the visual content in a video, reflecting coherence between modalities.

**[TypyBench: Evaluating LLM Type Inference for Untyped Python Repositories](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25l/dong25l.pdf) (as "Type consistency")**
> The degree to which the type annotations generated by a model are coherent and free of contradictions when analyzed across an entire codebase.

**[TypyBench: Evaluating LLM Type Inference for Untyped Python Repositories](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25l/dong25l.pdf) (as "Repository-level consistency")**
> The degree to which inferred type annotations form a globally coherent system across an entire codebase, ensuring compatibility across function calls and module boundaries.

**[Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf) (as "Local coherence")**
> The ability of a model to generate text that is logical and consistent within a small, local window of tokens.

**[Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf) (as "Contextual coherence")**
> The latent ability of an LLM to maintain semantic and structural consistency across long sequences of generated text by preserving relevant long-range dependencies.

**[Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf) (as "Prediction consistency")**
> The degree to which a model's prediction for a given input remains stable across multiple fine-tuned variants of the same pre-trained model under minor training variations.

**[Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf) (as "Statistical consistency")**
> The property that the learned model converges to the true optimal model reflecting actual human preferences as the amount of data increases, regardless of the underlying preference structure.

**[CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25e/jiang25e.pdf) (as "Sequential consistency")**
> The property of certain attention heads exhibiting stable, predictable attention patterns that focus on a consistent set of critical tokens across both pre-filling and decoding stages of generation.

**[Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf) (as "Compositional consistency")**
> The degree to which answers to complex questions are logically consistent with answers to their constituent sub-questions within a hierarchical reasoning structure.

**[Potemkin Understanding in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mancoridis25a/mancoridis25a.pdf) (as "Conceptual incoherence")**
> A state where a model holds conflicting or inconsistent internal representations of the same concept, leading it to contradict its own generations or classifications.

**[Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf) (as "Linguistic coherence")**
> The quality of generated text being fluent, plausible, and syntactically correct, for which LLMs are primarily optimized via next-token prediction.

**[NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf) (as "Response coherence")**
> The quality of a model's generated responses being logically connected and relevant to the ongoing conversation.

**[CoSER: Coordinating LLM-Based Persona Simulation of Established Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dk/wang25dk.pdf) (as "Storyline consistency")**
> The degree to which the simulated conversation maintains alignment with the original dialogue in terms of character reactions, emotions, attitudes, and behavioral trajectories.

**[VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25h/wei25h.pdf) (as "Spatiotemporal coherence")**
> The ability of a model to preserve and accurately represent the joint spatial and temporal structure of video data through its positional encoding scheme.

**[Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf) (as "Performance consistency")**
> The degree to which an LLM agent maintains reliable success across multiple attempts at complex, multi-step tasks, minimizing variance between average-case and best-case outcomes.

**[Preference learning made easy: Everything should be understood through win rate](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bm/zhang25bm.pdf) (as "Win rate-consistency")**
> The property that the optimal solution of an objective function achieves the maximum possible win rate over a competitor, ensuring that the objective does not fundamentally limit the model's alignment potential.

**[Function-to-Style Guidance of LLMs for Code Translation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cb/zhang25cb.pdf) (as "Stylistic consistency")**
> The latent ability of an LLM to preserve the source code's stylistic features—such as variable naming, code structure, and API usage—in the translated output, enhancing readability and maintainability.

**[Oracle-MoE: Locality-preserving Routing in the Oracle Space for Memory-constrained Large Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25b/zhou25b.pdf) (as "Expert activation consistency")**
> The degree to which a Mixture-of-Experts model activates the same experts for consecutive, semantically related tokens, reducing the need for frequent changes.

**[Position: Theory of Mind Benchmarks are Broken for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/riemer25a/riemer25a.pdf) (as "Process consistency")**
> The degree to which an agent's internal reasoning process remains coherent and aligned across different questions or steps in a task, particularly in how predictions inform actions.

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

**[SHARP: Steering Hallucination inLVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.726.pdf) (as "Speech-suitability")**
> The degree to which a model's output is appropriate for spoken delivery, encompassing naturalness, conciseness, and ease of comprehension when heard rather than read.

## Relationships

### Consistency →
- **Human evaluation** (measurements) — *measured_by*
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d9a0718883f4a2eecee3c69c7213b05-Paper-Conference.pdf)
- **FLASK** (measurements) — *measured_by*
  - [Bridging the Visual Gap: Fine-Tuning Multimodal Models with Knowledge-Adapted Captions](https://aclanthology.org/2025.naacl-long.528.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
- **CounterFact** (measurements) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **TREC** (measurements) — *measured_by*
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **LiveBench** (measurements) — *measured_by*
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
- **Stability** (constructs) — *measured_by*
  - [Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hamman25a/hamman25a.pdf)
- **NOVA-63** (measurements) — *measured_by*
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.364.pdf)
- **Xsafety** (measurements) — *measured_by*
  - [Frame First, Then Extract: A Frame-Semantic Reasoning Pipeline for Zero-Shot Relation Triplet Extraction](https://aclanthology.org/2025.emnlp-main.1392.pdf)

### → Consistency
- **Logical reasoning** (constructs) — *causes*
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks) — *causes*
  - [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1389.pdf)
- **Editing locality** (constructs) — *causes*
  - [Oracle-MoE: Locality-preserving Routing in the Oracle Space for Memory-constrained Large Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25b/zhou25b.pdf)
- **Situational awareness** (constructs) — *causes*
  - [Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1389.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf)
- **In-context learning** (constructs)
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks)
  - [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf)
- **Uncertainty** (constructs)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  > Although prior medical multimodal foundation models have demonstrated promising capabilities on report generation given the radiology image, they still suffer from serious hallucinations by generating factually inaccurate reports
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Hallucination detection** (behaviors tasks)
  - [Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf)
- **Conversational ability** (constructs)
  - [NTPP: Generative Speech Language Modeling for Dual-Channel Spoken Dialogue via Next-Token-Pair Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25by/wang25by.pdf)
- **Robustness** (constructs)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Natural language inference** (behaviors tasks)
  - [Query-focused Referentiability Learning for Zero-shot Retrieval](https://aclanthology.org/2025.naacl-long.277.pdf)
- **Adaptability** (constructs)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf)
- **Semantic uncertainty** (constructs)
  - [Rethinking Word Similarity: Semantic Similarity through Classification Confusion](https://aclanthology.org/2025.naacl-long.300.pdf)
- **Semantic textual similarity** (behaviors tasks)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Relevance** (constructs)
  - [Delving into Multilingual Ethical Bias: TheMSQADwith Statistical Hypothesis Tests for Large Language Models](https://aclanthology.org/2025.acl-long.16.pdf)
- **Agency** (constructs)
  - [Guided Search Strategies in Non-Serializable Environments with Applications to Software Engineering Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zainullina25a/zainullina25a.pdf)
- **External validity** (constructs)
  - [Compositional Causal Reasoning Evaluation in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/maasch25a/maasch25a.pdf)
- **Knowledge retention** (constructs)
  - [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf)
- **Human preference alignment** (constructs)
  - [Direct Density Ratio Optimization: A Statistically Consistent Approach to Aligning Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/higuchi25a/higuchi25a.pdf)
- **Value-reasoning reliability** (constructs)
  - [EcoTune: Token-Efficient Multi-Fidelity Hyperparameter Optimization for Large Language Model Inference](https://aclanthology.org/2025.emnlp-main.395.pdf)
- **Free-text explanation generation** (behaviors tasks)
  - [2025.emnlp-main.797.checklist](https://aclanthology.org/attachments/2025.emnlp-main.797.checklist.pdf)

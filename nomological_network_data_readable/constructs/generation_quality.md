# Generation quality
**Type:** Construct  
**Referenced in:** 126 papers  
**Also known as:** Content quality, Text Quality, Summary quality, Summarization quality, Language quality, Language generation, Generative quality, Generator quality, Predictive quality, Generative performance, Output effectiveness, Generative model quality, Human readability, Conversation quality, Visual quality, Composition, Generation capacity, Overall quality, Generative capabilities, Professional response quality, Synthetic data quality, Language modeling quality, Search quality, Hypothesis quality, Image quality, Emotional support quality, Reconstruction quality, Annotation quality, Dialogue quality, Label quality, Storyline quality, Detoxification quality, Information quality, Rationale quality  

## State of the Field

Across the provided literature, "Generation quality" is a broad construct referring to the overall goodness of a model's generated output, frequently encompassing aspects like coherence, fluency, accuracy, and relevance. While some papers define it generally as "overall quality" or "output quality," many use more specific variants tailored to the task, such as "Summary quality," "Translation quality," "Dialogue quality," or even "Visual quality" for non-textual outputs. The most prevalent method for operationalizing this construct is through human evaluation, where evaluators rate outputs on Likert scales for criteria such as naturalness, coherence, and overall quality. In addition to human judgment, the construct is also measured using automated metrics on standard benchmarks; for instance, perplexity on datasets like WikiText-2 is a common proxy for language modeling quality. In many studies, preserving or improving generation quality is a central goal, often framed as a trade-off against other objectives like inference speed, as one paper aims to "accelerate LLM inference without compromising generation quality." The construct is multifaceted, with definitions highlighting various dimensions including linguistic correctness, the preservation of salient information in summarization, and the credibility of sources for "Citation quality." The concept is also studied in relation to other phenomena, such as Safety in conversational contexts and the avoidance of Model collapse when using synthetic data.

## Sources

**[Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)**
> The overall quality of a model's generated text, often encompassing aspects like coherence, diversity, and fluency, independent of its alignment to specific objectives.

**[AutoSurvey: Large Language Models Can Automatically Write Surveys](https://proceedings.neurips.cc/paper_files/paper/2024/file/d07a9fc7da2e2ec0574c38d5f504d105-Paper-Conference.pdf) (as "Content quality")**
> The overall quality of a generated survey in terms of how comprehensively, coherently, and topically it is written.

**[Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf) (as "Quality")**
> The overall goodness of a generated response, assessed through criteria like relevance, accuracy, and insightfulness.

**[Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf) (as "Text Quality")**
> The degree to which generated text is coherent, grammatical, and practically useful.

**[Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf) (as "Summary quality")**
> The degree to which a generated summary is good overall as a summary, including its informativeness and quality.

**[RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Summarization quality")**
> The degree to which an agent can compress retrieved content into summaries that preserve salient, valid, and information-dense entities.

**[Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf) (as "Response quality")**
> The overall quality of a model's generated response, encompassing aspects like linguistic correctness, usefulness, and relevance.

**[Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf) (as "Language quality")**
> The linguistic correctness and fluency of a model's generated text, assessed by the absence of flaws like repetition or inconsistency.

**[PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf) (as "Generative quality")**
> The overall quality and accuracy of the model's generated output, particularly when comparing a compressed version to its non-quantized original.

**[Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf) (as "Language generation")**
> The latent ability to produce fluent task-relevant text outputs in open-ended settings.

**[STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf) (as "Predictive quality")**
> The latent tendency of a language model to produce better next-token predictions and downstream task performance across evaluation settings.

**[Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf) (as "Generator quality")**
> The latent ability of a model to produce high-quality synthesized outputs that can be useful if properly selected.

**[TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf) (as "Generative performance")**
> The overall quality and accuracy of the text generated by the model across various tasks, which sparse attention methods aim to preserve.

**[Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf) (as "Output effectiveness")**
> The general quality of a model's generated sequences, considered as a property distinct from the efficiency of the generation process.

**[LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/59f278de1619bdb6b53fd04e8e0976e0-Paper-Conference.pdf) (as "Output quality")**
> A general latent trait representing the overall quality of a model's generated text, assessed across dimensions like relevance, accuracy, and coherence.

**[Maximizing the Potential of Synthetic Data: Insights from Random Matrix Theory](https://proceedings.iclr.cc/paper_files/paper/2025/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf) (as "Generative model quality")**
> The degree to which a generative model can produce high-fidelity synthetic data that accurately reflects the statistics of real data, influencing the performance of models trained on that data.

**[In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf) (as "Linguistic quality")**
> The degree to which a model's generated text is natural, fluent, and coherent after an editing operation.

**[Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf) (as "Human readability")**
> The extent to which generated adversarial prompts remain understandable and natural enough to avoid detection by readability-based filters.

**[Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf) (as "Text quality")**
> The overall quality of generated text, encompassing aspects like coherence, fluency, and correctness.

**[Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf) (as "Conversation quality")**
> The overall value of a multi-turn conversation, which is inferred from cumulative rewards based on metrics such as user engagement and safety.

**[MetaDesigner: Advancing Artistic Typography through AI-Driven, User-Centric, and Multilingual WordArt Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/a10c3d85879c29331ba4d73ede56c7d3-Paper-Conference.pdf) (as "Visual quality")**
> The overall aesthetic appeal, fidelity, and clarity of the generated image.

**[Personality Vector: Modulating Personality of Large Language Models by Model Merging](https://aclanthology.org/2025.emnlp-main.1254.pdf) (as "Composition")**
> The latent ability to generate coherent and structured text that meets specified stylistic, length, and organizational requirements.

**[Definition Generation for Word Meaning Modeling: Monolingual, Multilingual, and Cross-Lingual Perspectives](https://aclanthology.org/2025.emnlp-main.1322.pdf) (as "Generation capacity")**
> The model's ability to effectively generate complex and high-fidelity outputs, particularly when dealing with a large number of predictive targets like deep RVQ layers.

**[VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](https://aclanthology.org/2025.emnlp-main.138.pdf) (as "Overall quality")**
> A holistic judgment of a candidate output that summarizes multiple aspects into a single general assessment.

**[Molecular String Representation Preferences in PretrainedLLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.57.pdf) (as "Generative capability")**
> The extent to which a language model can produce fluent and effective next-token predictions and text generation under sparsification.

**[Selective Preference Optimization via Token-Level Reward Function Estimation](https://aclanthology.org/2025.emnlp-main.360.pdf) (as "Generative capabilities")**
> The underlying ability of a large language model to produce diverse, coherent, and high-quality text for a wide range of tasks.

**[COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.136.pdf) (as "Citation quality")**
> The degree to which a model selects and references academically impactful, relevant, and credible sources in a survey, reflecting scholarly standards.

**[2025.emnlp-main.172.checklist](https://aclanthology.org/attachments/2025.emnlp-main.172.checklist.pdf) (as "Professional response quality")**
> The latent trait reflecting the degree to which a model's responses align with professional standards in role-playing contexts, including appropriateness, coherence, and domain-specific accuracy.

**[Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.214.pdf) (as "Aesthetic quality")**
> The overall visual appeal of a generated banner, encompassing factors like color harmony, layout balance, and typography.

**[DecoupleSearch: Decouple Planning and Search via Hierarchical Reward Modeling](https://aclanthology.org/2025.emnlp-main.223.pdf) (as "Synthetic data quality")**
> The latent property of synthetic data that determines its effectiveness in fine-tuning LLMs for domain-specific tasks, reflecting both coherence and task relevance.

**[QuZO: Quantized Zeroth-Order Fine-Tuning for Large Language Models](https://aclanthology.org/2025.emnlp-main.272.pdf) (as "Language modeling quality")**
> The model's underlying ability to understand and generate coherent and probable sequences of text, typically measured by its prediction loss.

**[ToDi: Token-wise Distillation via Fine-Grained Divergence Control](https://aclanthology.org/2025.emnlp-main.410.pdf) (as "Search quality")**
> The effectiveness of a search algorithm in identifying correct and optimal solutions, determined by the alignment of explored paths with valid reasoning and the avoidance of erroneous trajectories.

**[CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf) (as "Hypothesis quality")**
> The latent trait reflecting how effectively a generated hypothesis captures meaningful patterns, supports downstream classification, and provides helpful or novel insights.

**[Dynamic Energy-Based Contrastive Learning with Multi-Stage Knowledge Verification for Event Causality Identification](https://aclanthology.org/2025.emnlp-main.617.pdf) (as "Image quality")**
> A general assessment of the generated image's technical and visual excellence, including aspects like realism and lack of artifacts.

**[VisEscape: A Benchmark for Evaluating Exploration-driven Decision-making in Virtual Escape Rooms](https://aclanthology.org/2025.emnlp-main.811.pdf) (as "Emotional support quality")**
> The overall effectiveness of a conversational agent in providing supportive, counseling-oriented dialogue to a help seeker.

**[CanLLMs be Literary Companions?: AnalysingLLMs onBengali Figures of Speech Identification](https://aclanthology.org/2025.emnlp-main.942.pdf) (as "Reconstruction quality")**
> The fidelity with which a sparse autoencoder can reconstruct a model's original dense activations from its learned sparse features.

**[DiCoRe: Enhancing Zero-shot Event Detection via Divergent-ConvergentLLMReasoning](https://aclanthology.org/2025.emnlp-main.1039.pdf) (as "Annotation quality")**
> The accuracy and completeness of event trigger and event type labels in synthetic data, minimizing both incorrect and missing annotations.

**[Dynamic Jointly Batch Selection for Data Efficient Machine Translation Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1353.pdf) (as "Dialogue quality")**
> The quality of the model’s consultation dialogue, including how well it communicates and conducts the interaction during a medical consultation.

**[iVISPAR— An Interactive Visual-Spatial Reasoning Benchmark forVLMs](https://aclanthology.org/2025.emnlp-main.1360.pdf) (as "Label quality")**
> The degree to which dataset labels reflect the intended ground truth rather than annotation mistakes or inconsistencies.

**[Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1389.pdf) (as "Storyline quality")**
> The overall coherence and fluency of the generated narrative, including logical flow and narrative development.

**[Measuring scalar constructs in social science withLLMs](https://aclanthology.org/2025.emnlp-main.1636.pdf) (as "Detoxification quality")**
> The latent ability of a model to remove toxic content from text while transforming it into a non-toxic form.

**[so much depends / upon / a whitespace: Why Whitespace Matters for Poets andLLMs](https://aclanthology.org/2025.emnlp-main.1784.pdf) (as "Information quality")**
> The degree to which a model's output is relevant, faithful to source information, and free from fabrications.

**[Computational Analysis of Conversation Dynamics through Participant Responsivity](https://aclanthology.org/2025.emnlp-main.1799.pdf) (as "Model quality")**
> The overall performance and effectiveness of a language model, inferred from its accuracy on various downstream tasks and its ability to maintain the output distribution of the original, unquantized model.

**[Measuring Risk of Bias in Biomedical Reports: TheRoBBRBenchmark](https://aclanthology.org/2025.emnlp-main.161.pdf) (as "Translation quality")**
> The latent trait reflecting the accuracy, fluency, and adequacy of a model's translated output relative to a reference, encompassing both linguistic fidelity and contextual appropriateness.

**[Let’s Reason Formally: Natural-Formal Hybrid Reasoning EnhancesLLM’s Math Capability](https://aclanthology.org/2025.emnlp-main.851.pdf) (as "Rationale quality")**
> The degree to which a model's generated explanation for an answer is plausible, logical, and appropriate for the given problem.

**[OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models](https://aclanthology.org/2025.emnlp-main.184.pdf) (as "Reasoning quality")**
> The degree to which a model produces correct solutions on reasoning tasks, especially when balancing correctness against efficiency.

## Relationships

### Generation quality →
- **Human evaluation** (measurements) — *measured_by*
  > “we conduct comprehensive expert evaluations of the translation quality.”
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **WikiText-2** (measurements) — *measured_by*
  > “To evaluate the generative capability of the sparsified models, we conducted comprehensive perplexity experiments across different sparsity levels” and “we use the model’s perplexity on the WikiText2 (Merity et al., 2016) as the evaluation metric.”
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **WritingPrompts** (measurements) — *measured_by*
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **AG News** (measurements) — *measured_by*
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf)
- **UCF-101** (measurements) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MSRVTT** (measurements) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VBench** (measurements) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reddit TL;DR dataset** (measurements) — *measured_by*
  - [InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf)
- **UTMOS** (measurements) — *measured_by*
  - [GenSE: Generative Speech Enhancement via Language Models using Hierarchical Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/acde98fb254b8021d194ccdb80a1241e-Paper-Conference.pdf)
- **PopQA** (measurements) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **QMSum** (measurements) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **3MDBench** (measurements) — *measured_by*
  > "3MDBench simulates patient variability through temperament-based Patient Agent and evaluates diagnostic accuracy and dialogue quality via Assessor Agent."
  - [Dynamic Jointly Batch Selection for Data Efficient Machine Translation Fine-Tuning](https://aclanthology.org/2025.emnlp-main.1353.pdf)
- **VisEval** (measurements) — *measured_by*
  > To evaluate the visual quality of the generated charts, we conducted an analysis using the VLM Score metric on the VisEval benchmark with k = 15. (Section 4.6)
  - [DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset forLLM-based Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.836.pdf)

### → Generation quality
- **Reward hacking** (behaviors tasks) — *causes*
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
- **Context utilization** (constructs) — *causes*
  - [Radar: Fast Long-Context Decoding for Any Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/3c44405d619a6920384a45bce876b41e-Paper-Conference.pdf)

### Associated with
- **Reward overoptimization** (constructs)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
- **Safety** (constructs)
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
- **Model collapse** (constructs)
  > “a better generator always improves performance”
  - [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
- **Output diversity** (constructs)
  - [ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)

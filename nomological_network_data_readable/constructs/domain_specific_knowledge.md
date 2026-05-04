# Domain-specific knowledge
**Type:** Construct  
**Referenced in:** 41 papers  
**Also known as:** Base knowledge of ML algorithms, CAD design knowledge, CAD knowledge, Chemical knowledge, Scientific knowledge, Clinical knowledge, Medical knowledge, In-domain knowledge, Domain-specific expertise, Domain expertise, Localized domain knowledge, ESG knowledge, Sustainability knowledge, Legal knowledge, Comprehensive knowledge, Authority, Expertise, Depth of knowledge, Subject expertise, Professional expertise  

## State of the Field

Across the surveyed literature, domain-specific knowledge is predominantly framed as a model's latent, specialized understanding of a narrow field, such as medicine, law, science, or Computer-Aided Design (CAD). Definitions vary on its origin, with some describing it as a foundational quality acquired during pre-training, while others state it is gained through fine-tuning on specialized data. A smaller set of papers treats it as an observable quality of a model's output, using terms like "Authority" or "Depth of knowledge." The field operationalizes this construct by evaluating model performance on a wide array of benchmarks, including MMLU for "comprehensive knowledge," MedQA for knowledge assessment "without human input," SciQ for "scientific knowledge," and MathTutorBench for "subject-matter expertise." This construct is studied alongside behaviors like scientific problem solving and question answering, and some work contrasts it with reasoning, noting that certain benchmarks "solely evaluate basic visual perception and medical knowledge." At least one paper suggests that insufficient legal knowledge can lead to unreliable reasoning. Several papers discuss methods to enhance this capability, such as through fine-tuning or Retrieval-Augmented Generation (RAG), to improve performance on specialized tasks. One study also observes that "subject expertise, indicated by solving ability, does not immediately translate to good teaching."

## Sources

**[S3- Semantic Signal Separation](https://aclanthology.org/2025.acl-long.33.pdf)**
> The model's specialized understanding and factual recall within a narrow field, such as medicine, law, or finance, acquired through fine-tuning.

**[How does Misinformation Affect Large Language Model Behaviors and Preferences?](https://aclanthology.org/2025.acl-long.675.pdf) (as "Domain knowledge")**
> The underlying understanding of scientific concepts and terminology necessary to generate and evaluate accurate, relevant responses in multidisciplinary scienceQ&A.

**[Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf) (as "Scientific knowledge")**
> The latent breadth of factual knowledge about scientific topics that supports answering science-oriented questions.

**[LLM-Augmented Chemical Synthesis and Design Decision Programs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ag/wang25ag.pdf) (as "Chemical knowledge")**
> The implicit understanding of chemical principles, structures, and reactions encoded within the language model.

**[Text-to-CAD Generation Through Infusing Visual Feedback in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eg/wang25eg.pdf) (as "CAD design knowledge")**
> The model's internalized, foundational knowledge about the principles, components, and common structures of Computer-Aided Design.

**[CAD-Editor: A Locate-then-Infill Framework with Automated Training Data Synthesis for Text-Based CAD Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25g/yuan25g.pdf) (as "CAD knowledge")**
> The model's internalized knowledge of Computer-Aided Design principles, including Sketch-and-Extrude (SE) operations and geometric concepts.

**[Adaptive Self-improvement LLM Agentic System for ML Library Development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25at/zhang25at.pdf) (as "Base knowledge of ML algorithms")**
> The pre-existing, latent understanding of machine learning algorithms that a model possesses from its training.

**[MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zuo25a/zuo25a.pdf) (as "Medical knowledge")**
> The body of factual information, principles, and concepts related to medicine that a model possesses and can apply.

**[Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf) (as "Clinical knowledge")**
> The latent body of medically relevant knowledge about diseases, symptoms, procedures, medications, and related concepts used in practice.

**[DA-Pred: Performance Prediction for Text Summarization under Domain-Shift and Instruct-Tuning](https://aclanthology.org/2025.emnlp-main.388.pdf) (as "In-domain knowledge")**
> The specialized knowledge a model acquires by being fine-tuned on a specific, narrow dataset, allowing it to capture domain-specific conventions and patterns.

**[BenchmarkingLLMs for Translating ClassicalChinese Poetry: Evaluating Adequacy, Fluency, and Elegance](https://aclanthology.org/2025.emnlp-main.1679.pdf) (as "Domain-specific expertise")**
> The model's proficiency and specialized knowledge within particular professional or academic fields.

**[CARFT: BoostingLLMReasoning via Contrastive Learning with Annotated Chain-of-Thought-based Reinforced Fine-Tuning](https://aclanthology.org/2025.emnlp-main.303.pdf) (as "Domain expertise")**
> The latent ability of a model to demonstrate knowledge and reasoning aligned with professional standards in specific vertical domains such as engineering, finance, or safety regulation, as validated by official qualification criteria.

**[CARFT: BoostingLLMReasoning via Contrastive Learning with Annotated Chain-of-Thought-based Reinforced Fine-Tuning](https://aclanthology.org/2025.emnlp-main.303.pdf) (as "Localized domain knowledge")**
> The latent ability of a model to understand and apply domain-specific knowledge that is grounded in the Chinese sociopolitical, regulatory, and professional context, enabling accurate performance on localized qualification tasks.

**[2025.emnlp-main.739.checklist](https://aclanthology.org/attachments/2025.emnlp-main.739.checklist.pdf) (as "ESG knowledge")**
> The latent understanding of environmental, social, and governance principles and practices, particularly as applied in corporate and sustainability contexts.

**[2025.emnlp-main.739.checklist](https://aclanthology.org/attachments/2025.emnlp-main.739.checklist.pdf) (as "Sustainability knowledge")**
> The underlying comprehension of sustainability concepts, including environmental stewardship, social responsibility, and long-term ecological and economic balance.

**[Language Models as Continuous Self-Evolving Data Engineers](https://aclanthology.org/2025.emnlp-main.915.pdf) (as "Legal knowledge")**
> The extent to which the model has encoded and can accurately retrieve legal principles, statutes, and case law.

**[Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1348.pdf) (as "Comprehensive knowledge")**
> The breadth and depth of a model's general knowledge across a wide range of academic and professional subjects.

**[FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.736.pdf) (as "Authority")**
> The quality of a response conveying a sense of expertise and credibility on the subject matter.

**[FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.736.pdf) (as "Depth of knowledge")**
> The degree to which a response demonstrates substantive expertise or detailed subject-matter knowledge.

**[FIRE: Flexible Integration of Data Quality Ratings for Effective Pretraining](https://aclanthology.org/2025.emnlp-main.736.pdf) (as "Expertise")**
> The quality of a response demonstrating specialized knowledge or skill in a particular field.

**[Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.11.pdf) (as "Subject expertise")**
> The model's underlying knowledge and mastery of the subject matter being taught, in this case, mathematics.

**[Probing Narrative Morals: A New Character-FocusedMFTFramework for Use with Large Language Models](https://aclanthology.org/2025.emnlp-main.1450.pdf) (as "Professional expertise")**
> The latent ability to demonstrate domain-specific knowledge and reasoning in specialized fields such as medicine or law.

## Relationships

### Domain-specific knowledge →
- **MMLU** (measurements) — *measured_by*
  > MMLU (Hendrycks et al., 2021) and GAOKAO (Zhong et al., 2023) for comprehensive knowledge evaluation. (Section 3.2)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MedQA** (measurements) — *measured_by*
  > “we define five fundamental LLM capabilities, namely Mathematical Reasoning, Reading Comprehension, Commonsense Reasoning, Scientific Reasoning, and Professional Expertise”
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **PubHealth** (measurements) — *measured_by*
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **SciFact** (measurements) — *measured_by*
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **MedMCQA** (measurements) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMAU** (measurements) — *measured_by*
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  - [SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cb240de90aa20207db944c6c88a7cc0-Paper-Conference.pdf)
- **ScienceQA** (measurements) — *measured_by*
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  > We include a set of tasks to evaluate the model’s core capabilities of natural language understanding, scientific knowledge, and reasoning. We report the zero-shot performance on ARC-challenge (Clark et al., 2018), ARC-easy (Clark et al., 2018), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), PiQA (Bisk et al., 2020), LAMBADA-OpenAI (Paperno et al., 2016), and SciQ (Welbl et al., 2017).
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **MathTutorBench** (measurements) — *measured_by*
  > Therefore, MATHTUTORBENCH is divided into three categories: math expertise which evaluates the subject-matter expertise of the tutor... (Section 1)
  - [Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.11.pdf)

### Associated with
- **Scientific problem solving** (behaviors tasks)
  - [SciCode: A Research Coding Benchmark Curated by Scientists](https://proceedings.neurips.cc/paper_files/paper/2024/file/36850592258c8c41cecdaa3dea5ff7de-Paper-Datasets_and_Benchmarks_Track.pdf)

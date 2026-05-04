# Language understanding
**Type:** Behavior  
**Referenced in:** 32 papers  
**Also known as:** Text comprehension, Script handling, Multilingual understanding, Multi-party dialogue understanding  

## State of the Field

Across the surveyed literature, Language understanding is a broad behavior most frequently operationalized by model performance on a wide array of benchmarks. The most prevalent measurement instrument is MMLU, which is described as assessing a model's "multitask accuracy" across diverse domains and is "widely used to evaluate the language understanding of real-world large language models." Other commonly used benchmarks for its evaluation include HellaSwag, OpenBookQA, BoolQ, and GLUE. While the dominant usage is general, with one paper defining it as performing tasks like those in SuperGLUE, some papers offer more specific definitions. These include framing it as "text comprehension" (integrating information from text), "multilingual understanding," "multi-party dialogue understanding," or "script handling." The latter is concerned with correctly processing diverse writing systems, where one study notes that "models frequently fail to handle special glyphs or non-standard writing directions" in low-resource scripts. The behavior is also studied alongside commonsense knowledge, tabular reasoning, and textual reasoning. Finally, some work suggests that language understanding is influenced by methods like masked language modeling and question-answer pair generation.

## Sources

**[From Personas to Talks: Revisiting the Impact of Personas onLLM-Synthesized Emotional Support Conversations](https://aclanthology.org/2025.emnlp-main.278.pdf) (as "Text comprehension")**
> Answering questions or producing outputs that require understanding and integrating information from text.

**[TCP: a Benchmark for Temporal Constraint-Based Planning](https://aclanthology.org/2025.emnlp-main.1143.pdf)**
> Performing a range of language understanding tasks such as those included in SuperGLUE.

**[CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning inSLMs](https://aclanthology.org/2025.emnlp-main.705.pdf) (as "Script handling")**
> Correctly processing text in diverse writing systems, including right-to-left scripts and non-standard glyphs, particularly in low-resource languages.

**[Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.932.pdf) (as "Multilingual understanding")**
> Handling and understanding inputs across multiple languages.

**[Logit Space Constrained Fine-Tuning for Mitigating Hallucinations inLLM-Based Recommender Systems](https://aclanthology.org/2025.emnlp-main.1492.pdf) (as "Multi-party dialogue understanding")**
> Tracking and interpreting conversations involving more than two participants, including attributing utterances to correct speakers and maintaining coherent context.

## Relationships

### Language understanding →
- **MMLU** (measurements) — *measured_by*
  > We have selected three datasets that measure common sense reasoning and language understanding to evaluate the possible performance loss after altering the model: ... Massive Multitask Language Understanding (MMLU) (Hendrycks et al., 2021)... (Section 2.5)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  > The four benchmarks are ARC_C, HellaSwag, PIQA and MMLU... Results of the zero-shot performance are displayed in Table 1, which demonstrates that there is no significant loss of the ability of the language understanding of LLMs after the aligning with embodied environments (Section 5.5)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  > We have selected three datasets that measure common sense reasoning and language understanding to evaluate the possible performance loss after altering the model: OpenBookQA (OBQA) (Mihaylov et al., 2018)... (Section 2.5)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  > We evaluated these models on six different benchmarks ... including PIQA (Bisk et al., 2020), hellaswag (Zellers et al., 2019), BoolQ (Clark et al., 2019), ARC (Clark et al., 2018), winogrande (Sakaguchi et al., 2021) and SIQA (Sap et al., 2019). These tasks examine models’ language understanding, logical reasoning, knowledge utilization, and social awareness capabilities.
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  > We first evaluate the language understanding tasks from the GLUE benchmark(Wang et al., 2018) including MNLI, SST2, QNLI and QQP using the RoBERTa model.
  - [Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > The four benchmarks are ARC_C, HellaSwag, PIQA and MMLU... Results of the zero-shot performance are displayed in Table 1, which demonstrates that there is no significant loss of the ability of the language understanding of LLMs after the aligning with embodied environments (Section 5.5)
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **SuperGLUE** (measurements) — *measured_by*
  - [BERTs are Generative In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/04ea184dfb5f1babb78c093e850a83f9-Paper-Conference.pdf)
- **Lambada-OpenAI** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > “Experiments are conducted on five widely used benchmarks: GSM8K (Cobbe et al., 2021), MATH, HumanEval, Trivia Creative Writing, and HotpotQA”
  - [From Personas to Talks: Revisiting the Impact of Personas onLLM-Synthesized Emotional Support Conversations](https://aclanthology.org/2025.emnlp-main.278.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [LACA: Improving Cross-lingual Aspect-Based Sentiment Analysis withLLMData Augmentation](https://aclanthology.org/2025.acl-long.42.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **Winograd** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf)
- **RACE** (measurements) — *measured_by*
  > RACE is a reading comprehension benchmark introduced in Lai et al. (2017) collected from English examinations of middle and high school students. (Section 3)
  - [Wings: Learning Multimodal LLMs without Text-only Forgetting](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852f6d247ba7deb46e4e4be9e702601-Paper-Conference.pdf)
- **XNLI** (measurements) — *measured_by*
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **TACT** (measurements) — *measured_by*
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
- **XQuAD** (measurements) — *measured_by*
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
- **CEval** (measurements) — *measured_by*
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.932.pdf)
- **BBH** (measurements) — *measured_by*
  - [Fractal Patterns May Illuminate the Success of Next-Token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd004fa45fc1fe5c0218b7801d98d036-Paper-Conference.pdf)
- **Belebele** (measurements) — *measured_by*
  > We evaluate understanding capabilities using MMLU (Hendrycks et al., 2021), HellaSwag (Zellers et al., 2019), and Belebele (Bandarkar et al., 2024) benchmarks, each adapted to both EGY and MOR dialects. (Section 4.1)
  - [Layer Swapping for Zero-Shot Cross-Lingual Transfer in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f9a44cb707ede42a659ad85d940dd55-Paper-Conference.pdf)
- **MNLI** (measurements) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **QNLI** (measurements) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **SNLI** (measurements) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **WNLI** (measurements) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **Exploration** (constructs) — *causes*
  - [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
- **Adversarial attacks** (behaviors tasks) — *causes*
  - [One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf)
- **LiveBench** (measurements) — *measured_by*
  - [PicPersona-TOD: A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.404.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [LACA: Improving Cross-lingual Aspect-Based Sentiment Analysis withLLMData Augmentation](https://aclanthology.org/2025.acl-long.42.pdf)
- **CSRT** (measurements) — *measured_by*
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)
- **TweetEval** (measurements) — *measured_by*
  - [Steering off Course: Reliability Challenges in Steering Language Models](https://aclanthology.org/2025.acl-long.975.pdf)

### → Language understanding
- **Masked language modeling** (behaviors tasks) — *causes*
  - [Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf)
- **Question-answer pair generation** (behaviors tasks) — *causes*
  - [Web-Scale Visual Entity Recognition: An LLM-Driven Data Approach](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d158f054ff0cb83397367234899db07-Paper-Conference.pdf)

### Associated with
- **Instruction following** (constructs)
  - [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Beemo: Benchmark of Expert-edited Machine-generated Outputs](https://aclanthology.org/2025.naacl-long.358.pdf)
- **Tabular reasoning** (constructs)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Textual reasoning** (behaviors tasks)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)

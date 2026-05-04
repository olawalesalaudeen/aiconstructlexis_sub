# Coherence
**Type:** Construct  
**Referenced in:** 106 papers  
**Also known as:** Semantic coherence, Coherency, Internal consistency, Contextual consistency, Long-range consistency, Logical coherence, Temporal coherence, Dialogue coherence, Cohesion  

## State of the Field

Across the surveyed literature, coherence is most frequently described as the quality of a model's output being logical, internally consistent, and free from contradictions. This general concept is specified across various contexts, including `semantic coherence` (relevance to preceding text), `dialogue coherence` (consistency across conversational turns), and `temporal coherence` (logical progression in video). While most definitions focus on the properties of the generated text, a distinct framing defines coherence as the alignment between a model's generative and discriminative judgments, where both procedures should "agree about which candidate answers are correct" (The Consensus Game: Language Model Generation via Equilibrium Search). The construct is operationalized through several methods, with some papers relying on `Human evaluation` or using specific benchmarks like `MCBench` to assess it. Other approaches employ automated metrics, such as calculating the "cosine similarity between the sentence embedding of the prefix... and the generated continuation" (Language Model Decoding as Direct Metrics Optimization), using log-perplexity for speech quality, or applying statistical measures like Cronbach's alpha for internal consistency. Several papers distinguish coherence from other qualities; for example, one study notes that compressed models can generate text that is "fluent, consistent, and coherent" yet factually incorrect (Compressing LLMs: The Truth is Rarely Pure and Never Simple). The challenge of maintaining coherence is a recurring theme, particularly in long-form generation where models may exhibit "a loss of coherence and adherence to task instructions" over extended outputs (LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs).

## Sources

**[BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)**
> The degree to which a language model's generative and discriminative judgments align, reflecting a consistent internal assessment of correctness across different query modes.

**[ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf) (as "Semantic coherence")**
> The latent ability of a model to generate text that is contextually consistent and semantically relevant to the preceding input.

**[MMRole: A Comprehensive Framework for Developing and Evaluating Multimodal Role-Playing Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5c7206fd66e8314bb21a04492359353-Paper-Conference.pdf) (as "Coherency")**
> The extent to which an agent's responses maintain a consistent line of dialogue, avoiding contradictions with previous turns or internal inconsistencies.

**[Mixture of Length and Pruning Experts for Knowledge Graphs Reasoning](https://aclanthology.org/2025.emnlp-main.24.pdf) (as "Logical consistency")**
> The tendency for a reasoning chain to remain coherent and free of contradictions across its steps.

**[Preemptive Detection and Correction of Misaligned Actions inLLMAgents](https://aclanthology.org/2025.emnlp-main.13.pdf) (as "Internal consistency")**
> The degree to which a model's responses to items measuring the same underlying construct are correlated and reliable.

**[CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.474.pdf) (as "Contextual consistency")**
> The tendency to keep generated content aligned with earlier context and avoid contradictions or drift as sequence length grows.

**[DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf) (as "Long-range consistency")**
> The ability to maintain and correctly reuse intermediate results and other information across multiple steps of a long computational process.

**[MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Logical coherence")**
> The quality of a model's generated output being logically structured, consistent, and free from contradictions.

**[ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Temporal coherence")**
> The extent to which a generated video maintains smooth, logically continuous progression across frames without flicker or discontinuities.

**[One Token to Seg Them All: Language Instructed Reasoning Segmentation in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf) (as "Temporal consistency")**
> The quality of producing segmentation masks for an object that are stable and coherent across consecutive video frames.

**[Corrupted but Not Broken: Understanding and Mitigating the Negative Impacts of Corrupted Data in Visual Instruction Tuning](https://aclanthology.org/2025.emnlp-main.1318.pdf) (as "Dialogue coherence")**
> The quality of a conversation where responses are logically connected, consistent, and relevant to the preceding context, especially over long interactions.

**[Game Development as Human-LLMInteraction](https://aclanthology.org/2025.acl-long.219.pdf) (as "Cohesion")**
> The latent ability to maintain discourse coherence through appropriate use of anaphoric and cataphoric reference words (e.g., pronouns) that link utterances in dialogue.

## Relationships

### Coherence →
- **Human evaluation** (measurements) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HelpSteer** (measurements) — *measured_by*
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **HelpSteer2** (measurements) — *measured_by*
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Human evaluation** (measurements) — *correlates*
  - [BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [ReSURE: Regularizing Supervision Unreliability for Multi-turn Dialogue Fine-tuning](https://aclanthology.org/2025.emnlp-main.960.pdf)
- **BERTScore** (measurements) — *measured_by*
  - [A Unified Supervised and Unsupervised Dialogue Topic Segmentation Framework Based on Utterance Pair Modeling](https://aclanthology.org/2025.naacl-long.253.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Reflection-Window Decoding: Text Generation with Selective Refinement](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25a/tang25a.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [DoLLMs Adhere to Label Definitions? Examining Their Receptivity to External Label Definitions](https://aclanthology.org/2025.emnlp-main.1649.pdf)
- **MATH** (measurements) — *measured_by*
  - [DoLLMs Adhere to Label Definitions? Examining Their Receptivity to External Label Definitions](https://aclanthology.org/2025.emnlp-main.1649.pdf)
- **MCBench** (measurements) — *measured_by*
  - [DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf)

### → Coherence
- **Memory retention** (constructs) — *causes*
  - [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf)
- **Causal reasoning** (constructs) — *causes*
  - [Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.306.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25ae/zhu25ae.pdf)
- **Generation diversity** (constructs)
  - [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf)
- **Truthfulness** (constructs)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Creativity** (constructs)
  - [Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/afa5f124e36bed5cc2125067005d43f5-Paper-Conference.pdf)
- **Stability** (constructs)
  - [Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.588.pdf)
- **Instruction following** (constructs)
  - [ReSURE: Regularizing Supervision Unreliability for Multi-turn Dialogue Fine-tuning](https://aclanthology.org/2025.emnlp-main.960.pdf)

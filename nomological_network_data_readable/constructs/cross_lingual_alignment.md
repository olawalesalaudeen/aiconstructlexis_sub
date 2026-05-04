# Cross-lingual alignment
**Type:** Construct  
**Referenced in:** 14 papers  
**Also known as:** Multilingual alignment, Multilingual representation alignment, Multilingual semantic alignment, Language-agnostic semantic processing  

## State of the Field

Across the surveyed literature, Cross-lingual alignment is predominantly described as a latent ability of multilingual models to transfer knowledge across languages, particularly in zero-shot settings. This is commonly understood to be achieved by mapping semantically equivalent texts from different languages to similar or "geometrically closer" representations within a shared semantic space. A smaller set of papers frame this as "language-agnostic semantic processing," where the model processes meaning independently of the input language by converging representations. The field operationalizes and measures this construct through performance on multilingual benchmarks, with papers in this set using XNLI, MKQA, and CoVoST 2 for evaluation. This alignment is consistently positioned as the foundation for cross-lingual knowledge transfer and is also studied in the context of information retrieval. Some sources specify that this alignment is "typically achieved by training on parallel data" or by using "structural and lexical cues." While generally presented as a desirable property, one paper suggests a potential trade-off, noting that alignment training can distort "the optimal monolingual structure of semantic spaces of individual languages."

## Sources

**[Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)**
> The latent ability of a multilingual model to transfer knowledge across languages, particularly in zero-shot settings.

**[Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf) (as "Multilingual alignment")**
> The latent ability of a language model to produce similar representations for semantically equivalent texts across different languages, forming the foundation for cross-lingual transfer.

**[LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.328.pdf) (as "Multilingual representation alignment")**
> The process and resulting state of making the hidden-state representations of multilingual concepts more similar or geometrically closer within the model's semantic space.

**[HookMoE: A learnable performance compensation strategy of Mixture-of-Experts forLLMinference acceleration](https://aclanthology.org/2025.emnlp-main.1611.pdf) (as "Multilingual semantic alignment")**
> The latent ability to map concepts and meanings across languages using structural and lexical cues to support cross-lingual inference.

**[Label Set Optimization via Activation Distribution Kurtosis for Zero-Shot Classification with Generative Models](https://aclanthology.org/2025.emnlp-main.1618.pdf) (as "Language-agnostic semantic processing")**
> The latent ability of a multilingual LLM to process meaning independently of input language by converging representations into a shared semantic latent space where reasoning occurs.

## Relationships

### Cross-lingual alignment →
- **XNLI** (measurements) — *measured_by*
  > In this section, we pretrain small multilingual MLMs and evaluate their performance on the XNLI dataset (Conneau et al., 2018). (Section 5)
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **MKQA** (measurements) — *measured_by*
  > Notably, it achieves significant improvements of +3.6% R@20 and +5.7% nDCG@10 over the strongest baseline (M3-Embedding), demonstrating superior cross-lingual alignment capability. (Section 4.4)
  - [CoEvo: Coevolution ofLLMand Retrieval Model for Domain-Specific Information Retrieval](https://aclanthology.org/2025.emnlp-main.758.pdf)
- **CoVoST 2** (measurements) — *measured_by*
  - [Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection](https://aclanthology.org/2025.emnlp-main.1216.pdf)
- **Knowledge transfer** (constructs) — *causes*
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.328.pdf)

### Associated with
- **Information retrieval** (behaviors tasks)
  > Cross-lingual context retrieval (extracting contextual information in one language based on requests in another) is a fundamental aspect of cross-lingual alignment (Abstract).
  - [C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations](https://aclanthology.org/2025.emnlp-main.1161.pdf)

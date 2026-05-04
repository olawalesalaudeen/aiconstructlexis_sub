# WINOGROUND
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** WinoGround, Winoground  

## State of the Field

WINOGROUND is consistently described across the provided literature as a dataset or benchmark for evaluating vision-language models. Its primary purpose, as stated in multiple definitions, is to assess compositional understanding, often referred to as "visio-linguistic compositionality" or "compositional reasoning." The benchmark operationalizes this by requiring models to perform an image-text matching task, using what one paper calls "carefully constructed minimal pairs" of images and captions. Consequently, WINOGROUND is most frequently used to measure constructs like compositional reasoning and compositionality. It is also reported to evaluate more specific capabilities such as "fine-grained alignment," relation understanding, and cross-modal retrieval. While the prevailing usage centers on matching tasks, one study presents a different application, using the dataset's images for human evaluation of token-level predictions to test if a model can "self-correct its own hallucinations."

## Sources

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A dataset for probing visio-linguistic compositionality by requiring models to correctly match images and captions from carefully constructed minimal pairs.

**[TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf) (as "WinoGround")**
> A dataset of images used to evaluate vision-language models, particularly for tasks like image captioning and assessing compositional understanding.

**[Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf) (as "Winoground")**
> A compositional image-text matching benchmark with paired images and captions designed to test fine-grained alignment and reasoning.

## Relationships

### → WINOGROUND
- **Compositional reasoning** (constructs) — *measured_by*
  > "We evaluate the compositional capabilities of CECE in three different tasks. 1) Image-text matching evaluation through binary retrieval tasks... We report results on two benchmarks (Winoground (Thrush et al., 2022), EqBen (Wang et al., 2023b))"
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
- **Compositionality** (constructs) — *measured_by*
  - [EfficientQAT: Efficient Quantization-Aware Training for Large Language Models](https://aclanthology.org/2025.acl-long.499.pdf)
- **Relation understanding** (constructs) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)

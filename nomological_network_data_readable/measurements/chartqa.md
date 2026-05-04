# ChartQA
**Type:** Measurement  
**Referenced in:** 37 papers  

## State of the Field

ChartQA is a benchmark dataset primarily used to evaluate models on chart understanding and visual question answering. The most prevalent application across the surveyed literature is to measure a model's ability for "Chart and diagram understanding," with papers stating it assesses "understanding, reasoning, and data extraction skills" and "visual and logical reasoning over charts." The dataset is described as containing human-crafted questions that require models to perform tasks like "item comparison, counting, and numerical computation" based on chart images. It is also frequently used to evaluate the broader behavior of "Visual question answering," often included in a suite of benchmarks to test general or domain-specific VQA capabilities. A smaller set of papers operationalizes ChartQA to measure more specific constructs, including "Visual reasoning" and "Optical character recognition." A few sources also refer to it more generally as a "single-page document understanding dataset" alongside benchmarks like DocVQA. The dataset is used to demonstrate model advancements, as one study notes its method "solves previously unsolvable problem in ChartQA dataset" (ReFocus: Visual Editing as a Chain of Thought for Structured Image Understanding).

## Sources

**[SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)**
> Chart question answering benchmark referenced as a prior single-page document understanding dataset.

## Relationships

### → ChartQA
- **Chart and diagram understanding** (behaviors tasks) — *measured_by*
  > Previous works focus on chart question answering (Masry et al., 2022; Methani et al., 2020; Xu et al., 2023; Wang et al., 2024b; Li et al., 2024c; Zeng et al., 2024) and chart captioning (Rahman et al., 2023; Kantharaj et al., 2022). (Section 5)
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We collect question-document pairs from a series of VQA datasets, targeting different document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024b), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for various figure types, and SlideVQA (Tanaka et al., 2023) for presentation slides.
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > ChartQA (Masry et al., 2022), OCRVQA (Mishra et al., 2019), TextVQA (Singh et al., 2019) and DocVQA (Mathew et al., 2021) to examine their ability to recognize optical character (Section 5.1)
  - [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Document understanding** (constructs) — *measured_by*
  - [Matryoshka Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/722fcbc1a6667f2075d75ea79a1b3552-Paper-Conference.pdf)
- **Chart question answering** (behaviors tasks) — *measured_by*
  - [ShouldIShare this Translation? Evaluating Quality Feedback for User Reliance on Machine Translation](https://aclanthology.org/2025.emnlp-main.607.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **Fine-grained understanding** (constructs) — *measured_by*
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1166.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)

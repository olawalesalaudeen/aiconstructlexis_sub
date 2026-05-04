# OCRBench
**Type:** Measurement  
**Referenced in:** 23 papers  

## State of the Field

Across the provided literature, OCRBench is consistently characterized as a benchmark for evaluating model capabilities related to visual text. The most prevalent definition describes it as an instrument for assessing "optical character recognition (OCR) and text reading in visual inputs." A few papers offer a slightly broader scope, defining it as a tool for measuring "text understanding" or a model's ability to "reason about text within images." In practice, OCRBench is primarily used to measure the construct of "Optical character recognition," and is frequently grouped with other benchmarks for document and text understanding tasks. One study also uses OCRBench to evaluate "Fine-grained visual understanding," selecting it as an "OCR-extensive" benchmark that requires detailed visual information. While it is also listed as a measurement for "Multimodal perception" and "Fine-grained understanding," the provided data does not detail the specifics of this usage. The instrument is referred to as one of the "widely-adopted VLM benchmarks" used for conducting "extensive experiments."

## Sources

**[Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)**
> A benchmark for optical character recognition and text reading in visual inputs.

## Relationships

### → OCRBench
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Fine-grained understanding** (constructs) — *measured_by*
  - [ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering](https://aclanthology.org/2025.emnlp-main.55.pdf)

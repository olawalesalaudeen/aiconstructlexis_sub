# InfoVQA
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, InfoVQA is consistently characterized as a benchmark dataset for information-based visual question answering on document images. The prevailing usage of the benchmark is to evaluate a model's ability to extract specific information from these images, with papers describing its focus as "information localization and extraction." It is also referred to as a "single-page document understanding dataset." Papers use InfoVQA to measure several capabilities, including natural language understanding, optical character recognition, and fine-grained visual understanding. Reinforcing this, some sources classify it among "OCR-extensive benchmarks" that "require fine-grained visual information." One paper notes that tasks like InfoVQA often necessitate "understanding only small portions of text within an image." In practice, InfoVQA is frequently grouped with other text-rich evaluation datasets such as DocVQA, ChartQA, and TextVQA.

## Sources

**[SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)**
> Information visual question answering benchmark referenced as a prior single-page document understanding dataset.

## Relationships

### → InfoVQA
- **Document understanding** (constructs) — *measured_by*
  - [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)

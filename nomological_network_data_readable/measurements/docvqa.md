# DocVQA
**Type:** Measurement  
**Referenced in:** 46 papers  
**Also known as:** MP-DocVQA  

## State of the Field

DocVQA is a benchmark predominantly used for document visual question answering, where models are evaluated on their capacity to answer questions based on document images. Across the provided literature, it is described as testing a model's ability to extract and reason about information from a document's text and layout. There is some disagreement regarding its scope; while the most common definition states it is used for both single-page and multi-page documents, one paper explicitly claims it "can only assess single-page documents" and contrasts it with multi-page benchmarks. The benchmark is most frequently used to operationalize and measure capabilities related to `Optical character recognition` (OCR) and `Fine-grained visual understanding`, with several sources grouping it with other OCR-extensive tasks. It is also widely employed to assess `Natural language understanding`, particularly "reading comprehension tasks over document images." Other abilities it is reported to measure include `Visual question answering`, `Document question answering`, `Information retrieval`, and `Multimodal perception`.

## Sources

**[SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)**
> Document visual question answering benchmark used for evaluating single-page and multi-page document QA and retrieval.

**[BIPro: Zero-shotChinese Poem Generation via Block Inverse Prompting Constrained Generation Framework](https://aclanthology.org/2025.acl-long.57.pdf) (as "MP-DocVQA")**
> A benchmark for multi-page document question answering, limited to documents under 20 pages.

## Relationships

### → DocVQA
- **Document understanding** (constructs) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > OCR-Related Tasks. DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), TextVQA (Singh et al., 2019), InfoVQA (Mathew et al., 2022), VisualMRC (Tanaka et al., 2021), OCRBench (Liu et al., 2023c).
  - [InternLM-XComposer2-4KHD: A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b06cdddb1cde6624c0be1465c7b800f-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > “We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA 2 (Singh et al., 2019), V∗ (Wu and Xie, 2023), POPE (Li et al., 2023c), DocVQA (Mathew et al., 2021))”
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > DocVQA (Mathew et al., 2021) focuses on reading comprehension tasks over document images. (Section 4.1)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Enhancing Machine Translation with Self-Supervised Preference Data](https://aclanthology.org/2025.acl-long.1166.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/532ce4fcf853023c4cf2ac38cbc5d002-Paper-Conference.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)

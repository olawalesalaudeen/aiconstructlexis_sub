# COCO
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, COCO is consistently defined and used as a benchmark to evaluate image-to-text description generation. Its most prevalent application, supported by extensive evidence, is to measure model performance on the `Image captioning` task. Papers frequently cite its use for the "COCO captioning task" and position it as a standard instrument for this purpose. A more specialized use is also documented, where its validation set is employed to measure `Object hallucination` within visual captions. While its primary role centers on text generation from images, COCO is also reported as a measurement instrument for a wider array of behaviors, including `Semantic segmentation`, `Object detection`, `Pose estimation`, `Image generation`, `Cross-modal retrieval`, and `Multimodal alignment`, although the provided data lacks specific evidence detailing these applications.

## Sources

**[OmniCorpus: A Unified Multimodal Corpus of 10 Billion-Level Images Interleaved with Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/24015a142377bb08f374714648daafb6-Paper-Conference.pdf)**
> The MS COCO image captioning benchmark used to evaluate image-to-text description generation.

## Relationships

### → COCO
- **Image captioning** (behaviors tasks) — *measured_by*
  > We evaluate our models on VQA benchmarks (Goyal et al., 2017; Singh et al., 2019; Gurari et al., 2018; Marino et al., 2019) and image captioning benchmarks (Chen et al., 2015; Young et al., 2014). (Section 5.1)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Semantic segmentation** (behaviors tasks) — *measured_by*
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Object detection** (behaviors tasks) — *measured_by*
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > To evaluate object hallucination in visual caption, we use images from the COCO validation and Nocaps (Agrawal et al., 2019) datasets (Section 5.1).
  - [Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Multimodal alignment** (constructs) — *measured_by*
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **Pose estimation** (behaviors tasks) — *measured_by*
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)

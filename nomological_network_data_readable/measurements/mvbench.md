# MVBench
**Type:** Measurement  
**Referenced in:** 28 papers  

## State of the Field

Across the provided literature, MVBench is consistently used as a benchmark to measure `Video understanding` in multimodal models. The most prevalent definition characterizes it as a tool for assessing `visual temporal reasoning`, specifying that it contains "nine core temporal tasks with 20 subtasks" that are explicitly "designed to be unsolvable using a single frame." This design underscores its focus on temporal comprehension rather than static image analysis. Papers operationalize its use by evaluating models on its various subtasks, with some work focusing specifically on its action-related components like "Action Antonym, Action Count, Action Sequence," while others use it to assess "action recognition, object existence, and episodic reasoning." A smaller number of sources also employ MVBench to measure `Multi-image understanding`, and it is listed as an instrument for evaluating `Action localization` and `Mathematical reasoning`. Beyond model evaluation, it is also used to assess the generalizability of methods across different datasets.

## Sources

**[TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf)**
> A benchmark for visual temporal reasoning that defines nine core temporal tasks with 20 subtasks, designed to be unsolvable using a single frame.

## Relationships

### → MVBench
- **Video understanding** (constructs) — *measured_by*
  > We evaluate LLaVA-Mini on image and video understanding tasks. Experiments are conducted on 11 image benchmarks and 7 video benchmarks... Table 3: Performance on MVBench
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Action localization** (behaviors tasks) — *measured_by*
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  - [HydraRAG: Structured Cross-Source Enhanced Large Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.731.pdf)
- **Multi-image understanding** (constructs) — *measured_by*
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)

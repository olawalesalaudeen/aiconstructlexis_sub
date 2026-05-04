# TempCompass
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

TempCompass is a benchmark predominantly used to assess temporal and video understanding in models. Across the provided sources, it is most frequently described as a tool for "diagnosing multi-facet basic video temporal understanding abilities" and evaluating the "temporal understanding capabilities of video language models." The benchmark is also used more broadly to measure general video understanding and is categorized as a video question answering (VideoQA) benchmark. According to its definition, TempCompass operationalizes these assessments through a diverse set of tasks, including multiple-choice QA, yes/no QA, caption matching, and caption generation. This design is noted as a response to a perceived "lack of tasks diversity" in other instruments. While the data also associates TempCompass with mathematical reasoning, no specific evidence is provided to describe how it measures this construct. The prevailing use of TempCompass is to evaluate models on fine-grained comprehension through these varied formats.

## Sources

**[TOMATO: Assessing Visual Temporal Reasoning Capabilities in Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/16ba99f25a235f1100a4014d71d34ad8-Paper-Conference.pdf)**
> A benchmark for visual temporal reasoning that expands task types to include multiple-choice QA, yes/no QA, caption matching, and caption generation.

## Relationships

### → TempCompass
- **Temporal understanding** (constructs) — *measured_by*
  > MVBench (Li et al., 2023d), TempCompass (Liu et al., 2024c) centers on temporal understanding
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Video understanding** (constructs) — *measured_by*
  > we adopt the fine-grained temporal understanding benchmark, TempCompass (Liu et al., 2024b) (Multiple-Choice subset), diagnosing multi-facet basic video temporal understanding abilities. (Section 4.1)
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks) — *measured_by*
  > Examples of several VideoQA benchmarks. We examine four existing representative benchmarks and ours: VITATECS, MVBench, TempCompass, ReXTime, and TOMATO.
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)

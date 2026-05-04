# LongVideoBench
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** LongVideo-Bench  

## State of the Field

LongVideoBench is predominantly described as a benchmark dataset used to evaluate model performance on tasks involving long videos. Across the surveyed literature, it is most frequently used to measure the construct of `Video understanding`. Papers also use it to assess related capabilities such as `long-context understanding`, `multimodal understanding`, and `long-context processing`. The most common specific task it is said to evaluate is `video question answering`. A smaller set of papers offer more granular descriptions of its purpose, framing it as a benchmark for "referred reasoning in long videos" ("Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation") or for evaluating "temporal reasoning tasks" across diverse domains. The definitions consistently highlight that the dataset contains "very long videos," with one study noting they are "even longer" than those in other benchmarks. The various descriptions are largely complementary, centering on the evaluation of models' abilities to comprehend extended video content.

## Sources

**[Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)**
> A dataset containing very long videos used to evaluate video question answering models.

**[Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf) (as "LongVideo-Bench")**
> A benchmark dataset used to evaluate model performance on long video understanding tasks.

## Relationships

### → LongVideoBench
- **Video understanding** (constructs) — *measured_by*
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **Long-context multimodal understanding** (constructs) — *measured_by*
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > In Table 6, we provide results zero-shot transferring to the computer vision domain, evaluating NAMMs with a Llava Next Video 7B model (Zhang et al., 2024b) on LongVideoBench (Wu et al., 2024) and Multi-Task Long Video Understanding (MLVU) (Zhou et al., 2024). (Section 4.2)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks) — *measured_by*
  > We also evaluate MVU on the LongVideoBench dataset which contains even longer videos (Section 5.1)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)

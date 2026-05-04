# MSRVTT
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** MSR-VTT  

## State of the Field

Across the provided literature, MSRVTT is consistently characterized as a benchmark for evaluating video-language tasks. Its most prevalent application is to measure `Video captioning`, a use cited across multiple papers. It is also frequently used to assess `Video generation`. Other papers in this set employ it to evaluate a range of capabilities, including `Video understanding`, `Cross-modal retrieval`, and `Generation quality`. The definitions are complementary, describing it as an "English video captioning dataset," a benchmark for "short video comprehension," and, more specifically, a "Text-to-video retrieval benchmark dataset containing 10,000 video clips with associated natural language descriptions." In practice, it is often listed alongside other video-based visual-language benchmarks such as MSVD, ActivityNet Captions, and DiDeMo.

## Sources

**[Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf) (as "MSR-VTT")**
> An English video captioning dataset referenced as a prior benchmark for video-language evaluation.

**[World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)**
> A video understanding benchmark used here to assess short video comprehension.

## Relationships

### → MSRVTT
- **Video captioning** (behaviors tasks) — *measured_by*
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **Video generation** (behaviors tasks) — *measured_by*
  - [LLM-grounded Video Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d9f8b5abc8e0926539ecbb492af7b2f1-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Video understanding** (constructs) — *measured_by*
  > We evaluate LWM on standard benchmarks for image and short video understanding, with results presented in Table 5.
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [A Multilingual, Culture-First Approach to Addressing Misgendering inLLMApplications](https://aclanthology.org/2025.emnlp-main.1588.pdf)

# VBench
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, VBench is consistently presented as a benchmark leaderboard used to evaluate and rank text-to-video generation models. It is specifically employed to measure the performance of `Video generation` and `Generation quality`. The evaluation is described as comprehensive, assessing models across multiple "quality and semantic dimensions" as well as "quality and consistency." One paper notes that the leaderboard reports "average scores of 16 metrics" covering these areas. Researchers use VBench to compare models, with topping the leaderboard cited as evidence of superior performance. In addition to its evaluative function, the benchmark also serves as a resource, as one study leverages its "946 GPT-augmented text prompts" to generate videos.

## Sources

**[Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf)**
> A benchmark leaderboard used to evaluate and rank the performance of text-to-video generation models across multiple quality and semantic dimensions.

## Relationships

### → VBench
- **Video generation** (behaviors tasks) — *measured_by*
  > Our proposed “Probe-Analyze-Refine” workflow, validated through practical use cases on multimodal tasks such as image-text pre-training with CLIP, image-to-text generation with LLaVA-like models, and text-to-video generation with DiT-based models, yields transferable and notable performance boosts, such as topping the VBench leaderboard. (Abstract)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [ChronoMagic-Bench: A Benchmark for Metamorphic Evaluation of Text-to-Time-lapse Video Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/25b9960c8a5bd887eb5476c951260403-Paper-Datasets_and_Benchmarks_Track.pdf)

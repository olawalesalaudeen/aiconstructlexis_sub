# Perception Test
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** PerceptionTest  

## State of the Field

Across the surveyed literature, Perception Test is consistently described as a benchmark for evaluating video models, particularly Multimodal Large Language Models (MLLMs). The prevailing usage of the benchmark is to assess `video understanding`, a purpose explicitly stated across multiple papers. More specifically, it is frequently characterized as focusing on both the `perception` and `reasoning` skills of models. A smaller set of papers provide further detail, stating that it evaluates more granular capabilities such as `fine-grained visual understanding`, `logical inference`, `object tracking`, `spatial awareness`, and the understanding of `human actions`. One paper specifies its format as a "video multiple-choice question answering dataset," while another describes it as an "open-set video understanding benchmark." This focus on specific skills is reflected in its use, as one study notes selecting "all questions whose tags are related to action" for their experiments (NexusSum: HierarchicalLLMAgents for Long-Form Narrative Summarization). Finally, it is also referred to as a "challenging perception and reasoning diagnostic for video models" (Unifying Specialized Visual Encoders for Video Language Models).

## Sources

**[LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf) (as "PerceptionTest")**
> A video perception benchmark used to assess visual understanding over video sequences.

**[Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)**
> Perception Test (Patraucean et al., 2024) is a benchmark that focuses on the perception and reasoning skills of MLLMs.

## Relationships

### → Perception Test
- **Video understanding** (constructs) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf)

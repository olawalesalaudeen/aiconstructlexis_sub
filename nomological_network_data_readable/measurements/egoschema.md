# EgoSchema
**Type:** Measurement  
**Referenced in:** 26 papers  
**Also known as:** Egoschema, Ego-Schema  

## State of the Field

Across the provided literature, EgoSchema is consistently characterized as a benchmark dataset used to evaluate video question answering (VQA) and broader video understanding capabilities. The prevailing usage focuses on its application to long-form, egocentric videos, with one source noting its test set contains over 5,000 videos. While most definitions frame it as a VQA benchmark, a smaller set of papers describes it more specifically as a tool for measuring causal and temporal reasoning, natural scenario understanding, or "cognitive complexity and reasoning depth." In practice, researchers operationalize evaluation on EgoSchema by reporting top-1 accuracy on its question-answering tasks. The provided evidence shows it is frequently employed to assess model performance on long-context understanding, often alongside other long-video benchmarks. One paper suggests that its inclusion of longer videos and complex questions makes it "particularly well-suited for evaluating video understanding and reasoning capabilities."

## Sources

**[Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)**
> A benchmark dataset for long-form video question answering, designed to measure causal and temporal reasoning abilities in egocentric videos.

**[TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf) (as "Egoschema")**
> A benchmark for evaluating long video question answering capabilities, particularly focusing on egocentric videos.

**[Divide and Conquer: Exploring Language-centric Tree Reasoning for Video Question-Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25d/liao25d.pdf) (as "Ego-Schema")**
> A Video Question-Answering benchmark focused on long-form, egocentric video understanding.

## Relationships

### → EgoSchema
- **Video understanding** (constructs) — *measured_by*
  > “and (b) multi-choice video question answering benchmarks: NExT-QA (Xiao et al., 2021), IntentQA (Li et al., 2023b), and EgoSchema (Mangalam et al., 2024).”
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate on two video question answering datasets focused on long-form videos: EgoSchema (Mangalam et al., 2023) and NExT-QA (Xiao et al., 2021). (Section 5)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  > Table 3: Performance comparisons on 9 video benchmarks, including ActivityNet-QA (Yu et al., 2019), EgoSchema (Mangalam et al., 2023), EventBench (Du et al., 2024), LongVideoBench (Wu et al., 2024), PerceptionTest (Patraucean et al., 2023), MVBench (Li et al., 2024b), NExT-QA (Xiao et al., 2021), VNBench (Zhao et al., 2024), and VideoMME (Fu et al., 2024a). (Table 3)
  - [MMEgo: Towards Building Egocentric Multimodal LLMs for Video QA](https://proceedings.iclr.cc/paper_files/paper/2025/file/b29a95e7d9f1e1a6dfc567b556733744-Paper-Conference.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)

# Video-MME
**Type:** Measurement  
**Referenced in:** 35 papers  
**Also known as:** VideoMME  

## State of the Field

Video-MME is most commonly characterized in the provided literature as a benchmark for evaluating the video understanding capabilities of large multimodal models. The prevailing operationalization across papers is through multiple-choice video question answering tasks, designed to assess diverse reasoning types. While one definition also mentions captioning and retrieval, the most frequent framing is as a comprehensive video understanding and QA benchmark. A recurring theme is its focus on long-form content, with sources noting it features a "diverse collection of lengthy videos, ranging up to 1 hour in duration" specifically to assess long video understanding. Papers use Video-MME to measure general video understanding and, more specifically, video question answering. One study also leverages its defined question types to conduct comparative analysis on model performance in optical character recognition and counting.

## Sources

**[Video Action Differencing](https://proceedings.iclr.cc/paper_files/paper/2025/file/26f62bf3b74cda621831f550c6ee2dce-Paper-Conference.pdf)**
> A video understanding benchmark used to identify and select top-performing large multimodal models for evaluation.

**[MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25aq/li25aq.pdf) (as "VideoMME")**
> Multimodal evaluation benchmark for video models covering captioning, question answering, and retrieval tasks with subtitles.

## Relationships

### → Video-MME
- **Video understanding** (constructs) — *measured_by*
  > in the video understanding benchmark Video-MME (Fu et al., 2024)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks) — *measured_by*
  > We consider two multiple-choice VideoQA datasets: Video-MME (VMME) (Fu et al., 2024) and NExT-QA (Xiao et al., 2021)), and two open-ended VideoQA datasets (e.g., MUSIC-AVQA (Li et al., 2022a) and MSVD (Chen & Dolan, 2011))
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > Leveraging the question types defined in the Video-MME benchmark, we conduct a comparative analysis among three methods... across six distinct categories of questions. (Section 4.2, RQ5)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Counting** (behaviors tasks) — *measured_by*
  > Leveraging the question types defined in the Video-MME benchmark, we conduct a comparative analysis among three methods... across six distinct categories of questions. (Section 4.2, RQ5)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Spatiotemporal reasoning** (constructs) — *measured_by*
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)

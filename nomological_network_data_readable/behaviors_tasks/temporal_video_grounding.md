# Temporal video grounding
**Type:** Behavior  
**Referenced in:** 11 papers  
**Also known as:** Moment localization, Temporal grounding, Video grounding, Temporal action localization  

## State of the Field

Across the surveyed literature, temporal video grounding is most commonly described as the task of localizing a specific moment or time span in a video that corresponds to a natural language text query. This behavior involves predicting a temporal span or identifying video segments that provide evidence for a question, with one study using it to "assess whether an AI model accurately grounds its answers to the correct video segments" (ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos). While this temporal focus is prevalent, a few alternative framings exist; one paper defines 'video grounding' as localizing a target object within a 3D scene video, and another describes 'temporal action localization' as finding all segments containing a specific action. To measure this behavior, researchers commonly use benchmarks such as QVHighlights and Charades-STA, with evaluation methods mentioned including R@N and IoU=M. The task is frequently studied alongside concepts like 'Faithfulness', 'Fine-grained video understanding', and 'Temporal understanding'. One paper also suggests that performance on this task contributes to broader 'Video understanding'.

## Sources

**[ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Moment localization")**
> Predicting the temporal span in a video that corresponds to the answer event or relevant evidence for a question.

**[Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf) (as "Temporal grounding")**
> Identifying the video segments or timestamps that correspond to the evidence needed for a question.

**[Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf) (as "Video grounding")**
> The task of localizing a target object described by text within a video sequence of a 3D scene.

**[E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Temporal action localization")**
> The task of detecting and localizing all temporal segments in a video that contain a specific, given action.

**[ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/32683193e1d0e7a5795b073acecb3549-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of localizing a specific moment or time span in a video that corresponds to a given natural language text query.

## Relationships

### Temporal video grounding →
- **QVHighlights** (measurements) — *measured_by*
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Charades-STA** (measurements) — *measured_by*
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
- **Video understanding** (constructs) — *causes*
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)

### Associated with
- **Grounding** (constructs)
  - [E.T. Bench: Towards Open-Ended Event-Level Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/38ace89a980ead30c6be2b46afc1a5bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Fine-grained video understanding** (constructs)
  - [SlowFocus: Enhancing Fine-grained Temporal Understanding in Video LLM](https://proceedings.neurips.cc/paper_files/paper/2024/file/94ef721705ea95d6981632be62bb66e2-Paper-Conference.pdf)
- **Temporal reasoning** (constructs)
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Temporal understanding** (constructs)
  - [Conditional [MASK] Discrete Diffusion Language Model](https://aclanthology.org/2025.emnlp-main.451.pdf)
- **Information extraction** (behaviors tasks)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Information retrieval** (behaviors tasks)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)

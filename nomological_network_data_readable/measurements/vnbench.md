# VNBench
**Type:** Measurement  
**Referenced in:** 3 papers  

## State of the Field

VNBench is characterized in the provided literature as a benchmark for evaluating video understanding, with a specific focus on long videos. Across the surveyed work, it is most commonly used to measure the construct of `Video understanding`. One paper further specifies that VNBench is designed to evaluate three aspects of this capability: "temporal perception, chronological ordering, and spatio-temporal coherence," thereby also operationalizing the measurement of `Temporal reasoning` and `Chronological ordering`. The benchmark is composed of tasks including retrieval, ordering, and counting. A recurring theme is its connection to the "Needle-In-the-Haystack-Search" (NIAH) task, which is said to benefit from the "extended temporal context" the benchmark provides. As one study notes, performance improvements are most pronounced on VNBench, suggesting the NIAH task is particularly sensitive to this extended context.

## Sources

**[Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf)**
> A benchmark for evaluating long video understanding, particularly for tasks like Needle-In-the-Haystack-Search that benefit from extended temporal context.

## Relationships

### → VNBench
- **Video understanding** (constructs) — *measured_by*
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)
- **Chronological ordering** (behaviors tasks) — *measured_by*
  > Utilizing VideoNIAH, we compile a video benchmark, VNBench, which includes tasks such as retrieval, ordering, and counting to evaluate three key aspects of video understanding: temporal perception, chronological ordering, and spatio-temporal coherence. (ABSTRACT)
  - [Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)

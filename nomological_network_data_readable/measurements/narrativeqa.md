# NarrativeQA
**Type:** Measurement  
**Referenced in:** 26 papers  

## State of the Field

NarrativeQA is a benchmark consistently used to evaluate question answering, with a prevalent focus on long-context scenarios. Across the provided literature, it is defined as a dataset where the task is to generate free-form answers based on long narrative texts, which are specified as "entire books... and movie scripts" or "full-length novels." Papers use NarrativeQA to measure several capabilities, including `Question answering`, `Long-context processing`, `Open-domain question answering`, and `Length generalization`. The challenge is frequently framed as requiring models to synthesize information and achieve a "cohesive understanding" of these long documents. For instance, some work uses it to "test the model’s ability to leverage long context in zero-shot learning settings" ("Functional Interpolation for Relative Positions improves Long Context Transformers"). Several sources identify NarrativeQA as part of the SCROLLS benchmark, and it is often evaluated alongside other QA datasets such as QASPER and QuALITY.

## Sources

**[Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf)**
> A question-answering dataset where the task is to generate free-form answers based on provided text segments, such as stories or book chapters.

## Relationships

### → NarrativeQA
- **Question answering** (behaviors tasks) — *measured_by*
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **Length generalization** (constructs) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)

### Associated with
- **SCROLLS** (measurements)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)

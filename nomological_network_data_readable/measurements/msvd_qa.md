# MSVD-QA
**Type:** Measurement  
**Referenced in:** 21 papers  
**Also known as:** MSVDQA  

## State of the Field

Across the provided literature, MSVD-QA is consistently characterized as a benchmark for measuring video question answering and the related construct of video understanding. The prevailing usage, as reflected in multiple definitions and relationship evidence, is to assess a model's ability to answer questions about video content. Several sources specify that it is an "open-ended" task that requires models to generate accurate natural language responses. It is frequently employed for zero-shot evaluation, with one definition describing it as a "benchmark used for zero-shot video understanding evaluation." In practice, MSVD-QA is almost always used as part of a larger suite of evaluation tools, commonly appearing alongside MSRVTT-QA, ActivityNet-QA, and TGIF-QA. While the dominant framing connects it to video-specific tasks, a single paper also situates it within the broader category of visual question answering. The benchmark is also identified as being based on the Microsoft Video Description dataset.

## Sources

**[Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf)**
> A video question-answering benchmark used for zero-shot video understanding evaluation.

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf) (as "MSVDQA")**
> MSVD-QA benchmark used to assess answering questions about video content.

## Relationships

### → MSVD-QA
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate AURORACAP on MSVD-QA (Xu et al., 2017), ActivityNet-QA (Yu et al., 2019), MSRVTT-QA (Xu et al., 2017), and iVQA (Yang et al., 2021) for video question answering tasks as shown in Table 4. (Section 2.3)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **Video understanding** (constructs) — *measured_by*
  > Specifically, we showcased Dolphin’s comparison with various methods on MSR-VTT-QA, MSVD-QA, and ActivityNet-QA benchmarks. (Section 5.2)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > Visual Question Answering (VQA): We evaluate the performance of visual question answering on the following benchmark datasets:... We also use MSVD-QA
  - [Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf)

# ScienceQA-IMG
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** SciQA-IMG  

## State of the Field

Across the provided sources, ScienceQA-IMG is consistently described as a multimodal benchmark or dataset for science question answering that involves visual context from images. The prevailing usage of this instrument is to evaluate vision-language tasks, with papers specifically using it to measure visual question answering. It is also reported as a tool for assessing fine-grained visual understanding and language bias, though the provided evidence for the former refers to the benchmark as 'SQA'. One definition further specifies that the dataset assesses 'scientific reasoning from visual content'. In practice, models are evaluated on ScienceQA-IMG using accuracy scores, and one study highlights its selection as a 'reference task for low-resolution needs,' examining performance across different image resolutions. The benchmark appears under slight variations in name, including 'ScienceQA-IMG', 'SciQA-IMG', and 'SQAI'.

## Sources

**[ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering](https://aclanthology.org/2025.emnlp-main.55.pdf)**
> A multimodal science question answering benchmark that includes questions with visual context from images.

**[What You Read Isn’t What You Hear: Linguistic Sensitivity in Deepfake Speech Detection](https://aclanthology.org/2025.emnlp-main.795.pdf) (as "SciQA-IMG")**
> Science Question Answering dataset with image-based questions assessing scientific reasoning from visual content.

## Relationships

### → ScienceQA-IMG
- **Visual question answering** (behaviors tasks) — *measured_by*
  > Table 2: A comprehensive investigation conducted to explore resolution preferences across eight vision-language tasks. For each task, the accuracy scores corresponding to five different resolutions are presented. (Table 2)
  - [What You Read Isn’t What You Hear: Linguistic Sensitivity in Deepfake Speech Detection](https://aclanthology.org/2025.emnlp-main.795.pdf)
- **Language bias** (constructs) — *measured_by*
  - [MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > “TinyGroundingGPT-3B demonstrates superior image understanding capabilities on the VQAv2, GQA, SQA, and POPE benchmarks”
  - [MuCAL: Contrastive Alignment for Preference-DrivenKG-to-Text Generation](https://aclanthology.org/2025.emnlp-main.721.pdf)

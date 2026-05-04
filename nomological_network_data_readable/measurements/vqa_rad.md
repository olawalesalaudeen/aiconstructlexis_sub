# VQA-RAD
**Type:** Measurement  
**Referenced in:** 15 papers  
**Also known as:** Rad-VQA  

## State of the Field

Across the provided literature, VQA-RAD is consistently characterized as a benchmark dataset used to evaluate model performance on "Visual question answering" and, more specifically, "Medical visual question answering." The dataset is composed of radiology images paired with questions and answers, which one paper describes as "clinician-authored." It is frequently used to measure model capabilities alongside other medical VQA benchmarks such as SLAKE and PathVQA. The evaluation format is specified to include both "open-ended" and "closed-ended" questions, with one source noting that performance is assessed on both metrics. While most papers use the name VQA-RAD, it is also referred to as Rad-VQA in one instance. There is a minor discrepancy in the reported size of the dataset; one paper states it contains "315 images and 2,248 QA pairs," while another reports "315 radiology images" and "3,515 clinician-authored QA pairs."

## Sources

**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf)**
> A benchmark dataset for Visual Question Answering (VQA) based on radiology images, used to evaluate a model's ability to answer questions about medical scans.

**[A Training-freeLLM-based Approach to GeneralChinese Character Error Correction](https://aclanthology.org/2025.acl-long.679.pdf) (as "Rad-VQA")**
> A benchmark dataset for medical visual question answering, used to evaluate model performance in both open-ended and closed-ended settings.

## Relationships

### → VQA-RAD
- **Medical visual question answering** (behaviors tasks) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M. (Section 4.1)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M.
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)

# SLAKE
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

Across the provided literature, SLAKE is consistently described and used as a benchmark dataset for evaluating visual question answering (VQA) capabilities, specifically within the medical domain. Its primary application, as evidenced by its relationships, is to measure model performance on the behaviors of "Medical visual question answering" and the broader "Visual question answering." The dataset is characterized as containing radiological images across multiple modalities like CT and MRI, paired with both open- and closed-ended questions. Several sources highlight its detailed annotations, describing it as a "semantically-labeled knowledge-enhanced dataset" with "region-level annotations of organs and diseases." A few papers also note that it is a bilingual (English and Chinese) resource, though one study reports using only the English portion. In practice, SLAKE is frequently used alongside other medical VQA datasets, such as VQA-RAD and PathVQA, to benchmark and compare model performance.

## Sources

**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf)**
> A benchmark dataset for Visual Question Answering (VQA) in the medical domain, containing questions and answers for images across various pathologies and modalities.

## Relationships

### → SLAKE
- **Medical visual question answering** (behaviors tasks) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M. (Section 4.1)
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We benchmark LLaVA-Tri on three biomedical Visual Question Answering (VQA) datasets, VQA-RAD (Lau et al., 2018a), SLAKE (Liu et al., 2021), and PathVQA (He et al., 2020a), to assess the efficacy of aligning the model using MedTrinity-25M.
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)

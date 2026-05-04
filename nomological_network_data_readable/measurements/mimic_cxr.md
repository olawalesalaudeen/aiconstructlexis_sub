# MIMIC-CXR
**Type:** Measurement  
**Referenced in:** 16 papers  

## State of the Field

Across the surveyed literature, MIMIC-CXR is consistently characterized as a large-scale, publicly available dataset containing de-identified chest X-ray images and their corresponding free-text radiology reports. The dataset is described as originating from the Beth Israel Deaconess Medical Center and is used for both training and evaluating models. The most prevalent application of MIMIC-CXR is to measure the performance of models on `Medical report generation` and the closely related task of `Radiology report generation`, with multiple papers stating they use it for evaluation on these tasks. For instance, one study notes, "For English report generation, we evaluate our model on the report generation task for chest X-ray datasets MIMIC-CXR". A less frequent application, mentioned in one paper, is its use for evaluating `Medical visual question answering`. Some definitions also describe its purpose as assessing "visual understanding in clinical settings" and "grounded report generation evaluation".

## Sources

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)**
> A chest X-ray dataset used for medical report generation and grounded report generation evaluation.

## Relationships

### → MIMIC-CXR
- **Medical report generation** (behaviors tasks) — *measured_by*
  > For English report generation, we evaluate our model on the report generation task for chest X-ray datasets MIMIC-CXR (Johnson et al., 2019) and IU-Xray (Demner-Fushman et al., 2016). (Section 5.1)
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
- **Radiology report generation** (behaviors tasks) — *measured_by*
  > We evaluate our model using three publicly available radiology report generation datasets: MIMIC-CXR, CHEXPERT PLUS, and IU X-RAY (Section 4.1)
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **Medical visual question answering** (behaviors tasks) — *measured_by*
  > "We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024)."
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)

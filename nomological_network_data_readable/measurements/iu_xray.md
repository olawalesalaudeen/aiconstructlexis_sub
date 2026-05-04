# IU-Xray
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided sources, IU-Xray is consistently described as a dataset containing chest X-ray images paired with their associated medical or radiology reports. The prevailing usage of this dataset is to evaluate the task of medical report generation, a purpose cited across multiple papers and definitions. Some sources specify this task further as "English report generation" or "radiology report generation." A less common application, mentioned in a smaller subset of the literature, is using IU-Xray to evaluate medical visual question answering. In practice, it is frequently used alongside the MIMIC-CXR dataset for these evaluation purposes. One paper notes a specific operationalization, mentioning the "IU-Xray (Demner-Fushman et al., 2016) dataset containing 590 test samples."

## Sources

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)**
> A dataset of chest X-ray images and associated reports used for evaluating medical report generation.

## Relationships

### → IU-Xray
- **Medical report generation** (behaviors tasks) — *measured_by*
  > For English report generation, we evaluate our model on the report generation task for chest X-ray datasets MIMIC-CXR (Johnson et al., 2019) and IU-Xray (Demner-Fushman et al., 2016). (Section 5.1)
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
- **Medical visual question answering** (behaviors tasks) — *measured_by*
  > "We utilize five medical vision-language datasets for medical VQA and report generation tasks, i.e., MIMIC-CXR (Johnson et al., 2019), IU-Xray (Demner-Fushman et al., 2016), Harvard-FairVLMed (Luo et al., 2024), PMC-OA (Lin et al., 2023a) (we only select the pathology part) and Quilt-1M (Ikezogwo et al., 2024)."
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
- **Radiology report generation** (behaviors tasks) — *measured_by*
  > We evaluate our method on two public datasets, MIMIC-CXR (Johnson et al., 2019) and IU-Xray (Demner-Fushman et al., 2016). (Section 5.1)
  - [Weaving Context Across Images: Improving Vision-Language Models through Focus-Centric Visual Chains](https://aclanthology.org/2025.acl-long.1348.pdf)

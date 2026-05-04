# Medical report generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Across the surveyed literature, medical report generation is consistently defined as the task of generating a detailed, structured textual report describing the findings in a provided medical scan. One paper elaborates on this, specifying that for radiology reports, this includes an "accurate description of findings, location, severity, and comparisons" (D-CoDe: Scaling Image-PretrainedVLMs to Video via Dynamic Compression and Question Decomposition). This behavior is predominantly operationalized and measured using chest X-ray datasets. The most frequently used benchmarks for this task are MIMIC-CXR and IU-Xray, with multiple papers citing their use for evaluation. While specific evaluation methods are not detailed, one source notes that generated reports are assessed with "standard natural language processing (NLP) metrics" (D-CoDe: Scaling Image-PretrainedVLMs to Video via Dynamic Compression and Question Decomposition). In one study, performance on medical report generation is presented alongside visual question answering and medical image classification as an indicator of a model's Versatility.

## Sources

**[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)**
> The task of generating a detailed, structured textual report describing the findings in a provided medical scan.

## Relationships

### Medical report generation →
- **MIMIC-CXR** (measurements) — *measured_by*
  > For English report generation, we evaluate our model on the report generation task for chest X-ray datasets MIMIC-CXR (Johnson et al., 2019) and IU-Xray (Demner-Fushman et al., 2016). (Section 5.1)
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)
- **IU-Xray** (measurements) — *measured_by*
  > For English report generation, we evaluate our model on the report generation task for chest X-ray datasets MIMIC-CXR (Johnson et al., 2019) and IU-Xray (Demner-Fushman et al., 2016). (Section 5.1)
  - [MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf)

### Associated with
- **Versatility** (constructs)
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility. (Abstract)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)

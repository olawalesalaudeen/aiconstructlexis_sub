# Medical image classification
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Disease classification  

## State of the Field

Across the provided literature, medical image classification is most commonly defined as the task of assigning labels related to disease, modality, or organs to medical images. A more focused definition from one paper describes it as detecting and categorizing pathologies or abnormalities, specifically within chest X-rays. This behavior is operationalized using datasets like the Chest-XRay dataset, which, as one paper notes, contains X-ray images for classifying lungs as either healthy or affected by pneumonia. Another source mentions that the task is supported by data containing "modality, organ labels, disease types" for classification. Medical image classification is presented as a "vision-centric" task, often studied alongside other multimodal capabilities such as report generation and visual question answering. The performance on this task is also linked to model versatility, with one study reporting that a model performing well on medical image classification and other tasks showcases this attribute.

## Sources

**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf)**
> Assigning disease, modality, or organ-related labels to medical images.

**[MedRAX: Medical Reasoning Agent for Chest X-ray](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fallahpour25a/fallahpour25a.pdf) (as "Disease classification")**
> Detecting and categorizing pathologies or abnormalities in chest X-rays into predefined diagnostic classes.

## Relationships

### Associated with
- **Versatility** (constructs)
  > Our MedRegA not only enables three region-centric tasks, but also achieves the best performance for visual question answering, report generation and medical image classification over 8 modalities, showcasing significant versatility. (Abstract)
  - [Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/414fd191b3246a19a55741b938380136-Paper-Conference.pdf)

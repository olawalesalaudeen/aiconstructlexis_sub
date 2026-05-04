# MIMIC-III
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, MIMIC-III is consistently described as a large, publicly available dataset containing de-identified health data from patients who stayed in critical care units. The dataset, which includes records like discharge summaries, is frequently used for clinical NLP research and model evaluation. Papers use MIMIC-III to measure model performance on a range of healthcare-related prediction tasks, including time series classification and both disease and medical diagnosis. Specifically, it is used to evaluate mortality prediction, readmission prediction, length-of-stay prediction, phenotype prediction, and drug recommendation. One study operationalizes diagnosis prediction on this dataset as predicting "the CCS codes for the next visit of patients" ("BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare").

## Sources

**[Multimodal Medical Code Tokenizer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25b/su25b.pdf)**
> A publicly available in-patient dataset from the MIMIC (Medical Information Mart for Intensive Care) project, containing de-identified health data associated with patients who stayed in critical care units.

## Relationships

### → MIMIC-III
- **Time series classification** (behaviors tasks) — *measured_by*
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Mortality prediction** (behaviors tasks) — *measured_by*
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Disease diagnosis** (behaviors tasks) — *measured_by*
  - [PKAG-DDI: Pairwise Knowledge-Augmented Language Model for Drug-Drug Interaction Event Text Generation](https://aclanthology.org/2025.acl-long.540.pdf)
- **Medical diagnosis** (behaviors tasks) — *measured_by*
  > The evaluation encompasses five tasks: 1 mortality prediction (MT), 2 readmission prediction (RA), 3 length-of-stay prediction (LOS), 4 phenotype prediction (Pheno), and 5 drug recommendation (DrugRec). ... Table 3 presents the AUPRC values for each baseline and their integration with our MEDTOK for five tasks in two in-patient datasets. (Section 4)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)

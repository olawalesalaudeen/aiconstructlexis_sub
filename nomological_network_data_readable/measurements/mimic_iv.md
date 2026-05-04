# MIMIC-IV
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

MIMIC-IV is consistently described in the provided literature as a large-scale multimodal clinical dataset. Its primary application, as represented in these sources, is to evaluate models on a range of clinical prediction tasks. The most frequently cited applications involve patient outcome prediction, specifically length of stay (LOS), in-hospital mortality, and readmission. Beyond these, papers also use MIMIC-IV to assess performance on phenotype prediction, drug recommendation, and predicting medical codes for future patient visits. Some work frames its use more broadly, applying it to the "full-path clinical diagnosis task" and to evaluate "multimodal fusion strategies." The dataset is also reported to measure capabilities in time series classification, disease diagnosis, and multimodal understanding.

## Sources

**[CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25b/dai25b.pdf)**
> A large-scale multimodal clinical dataset used to evaluate multimodal fusion strategies for patient outcome prediction, including length of stay and in-hospital mortality.

## Relationships

### → MIMIC-IV
- **Medical diagnosis** (behaviors tasks) — *measured_by*
  > The evaluation encompasses five tasks: 1 mortality prediction (MT), 2 readmission prediction (RA), 3 length-of-stay prediction (LOS), 4 phenotype prediction (Pheno), and 5 drug recommendation (DrugRec). ... Table 3 presents the AUPRC values for each baseline and their integration with our MEDTOK for five tasks in two in-patient datasets. (Section 4)
  - [BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25e/tan25e.pdf)
- **Mortality prediction** (behaviors tasks) — *measured_by*
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Time series classification** (behaviors tasks) — *measured_by*
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Disease diagnosis** (behaviors tasks) — *measured_by*
  - [PKAG-DDI: Pairwise Knowledge-Augmented Language Model for Drug-Drug Interaction Event Text Generation](https://aclanthology.org/2025.acl-long.540.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  - [CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25b/dai25b.pdf)

# CheBI-20
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** ChEBI-20  

## State of the Field

Across the provided literature, CheBI-20 is a dataset for molecule-text modeling, though its specific application varies between papers. One line of work defines it for generative tasks, specifically for "text-based molecule generation," where a model creates a molecular sequence from a textual description. In contrast, other papers frame it for analysis and alignment, describing it as a "molecular graph visual question answering dataset" or for use in "molecule-text alignment." This aligns with its documented use as a measurement instrument for the behaviors of `Molecule understanding` and `Molecule captioning`. Some research also employs CheBI-20 for model fine-tuning and for specialized evaluations such as copyright-tracking. The dataset is also noted as being related to MOLERR2FIX.

## Sources

**[3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf)**
> A dataset widely used for the text-based molecule generation task, where the model generates a molecular sequence from a textual description.

**[Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d368eba3fb546ae5d868dae2ecb17200-Paper-Conference.pdf) (as "ChEBI-20")**
> A molecular graph visual question answering dataset used for fine-tuning and copyright-tracking evaluation.

## Relationships

### → CheBI-20
- **Molecule understanding** (behaviors tasks) — *measured_by*
  - [LLaMo: Large Language Model-based Molecular Graph Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee46288ab2aaf5c6e53aebebe719712c-Paper-Conference.pdf)
- **Molecule captioning** (behaviors tasks) — *measured_by*
  - [ConvSearch-R1: Enhancing Query Reformulation for Conversational Search with Reasoning via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1350.pdf)

### Associated with
- **MOLERR2FIX** (measurements)
  - [Mitigating Hallucinations inLM-BasedTTSModels via Distribution Alignment UsingGFlowNets](https://aclanthology.org/2025.emnlp-main.977.pdf)

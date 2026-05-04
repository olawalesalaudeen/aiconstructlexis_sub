# Molecule captioning
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Molecular captioning  

## State of the Field

Across the provided literature, molecule captioning is consistently defined as the task of generating natural language text from a given molecular structure. The generated text is variously described as a "textual description," "name," or "annotation" for the input molecule. One paper explicitly frames this task as the inverse of text-to-molecule generation, where the model receives a molecular structure and must produce a corresponding description. It is mentioned alongside other molecule-related tasks such as molecule-text retrieval. Some work notes that molecule captioning is well-suited for generative models as it involves a "wealth of molecular and textual information" ("RetroInText: A Multimodal Large Language Model Enhanced Framework for Retrosynthetic Planning via In-Context Representation Learning"). To operationalize and evaluate this behavior, the provided sources indicate the use of the CheBI-20 dataset.

## Sources

**[3D-MolT5: Leveraging Discrete Structural Information for Molecule-Text Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d4dc72d715bd6415d356293079adf3d-Paper-Conference.pdf)**
> The observable task of generating textual descriptions or names based on molecular input structures.

**[RetroInText: A Multimodal Large Language Model Enhanced Framework for Retrosynthetic Planning via In-Context Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2fbf1c9bc92e7ef2f6cab2e8a3e09af-Paper-Conference.pdf) (as "Molecular captioning")**
> The task of generating a natural language text description for a given molecule.

## Relationships

### Molecule captioning →
- **CheBI-20** (measurements) — *measured_by*
  - [ConvSearch-R1: Enhancing Query Reformulation for Conversational Search with Reasoning via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1350.pdf)

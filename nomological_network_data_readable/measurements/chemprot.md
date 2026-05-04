# ChemProt
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

ChemProt is consistently described across the provided literature as a labeled dataset in the biomedical domain, used as a measurement instrument for downstream tasks. Papers use it to evaluate model performance on `Text classification` and to assess the broader construct of `Adaptability`, particularly for domain adaptation. The most common operationalization of ChemProt is for relation classification, with a specific focus on "identifying chemical-protein interactions from scientific literature." One study notes that the dataset features "five relation classes," including mutually exclusive categories like 'up regulator' and 'down regulator'. A different framing, found in one paper, utilizes ChemProt for Named Entity Detection, where the goal is to extract "chemical compounds (drugs) and gene and protein-related objects." This work further demonstrates the dataset's flexibility by constructing subsets like `ChemProt-Chem` and `ChemProt-Gene` for these more specific detection tasks.

## Sources

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)**
> A labeled biomedical relation/classification dataset used as one of the downstream domain adaptation tasks.

## Relationships

### → ChemProt
- **Adaptability** (constructs) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)

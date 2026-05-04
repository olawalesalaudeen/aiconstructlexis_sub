# Generality
**Type:** Construct  
**Referenced in:** 8 papers  

## State of the Field

Within the provided literature, Generality is consistently defined as a model's ability to apply newly edited knowledge to rephrased or semantically equivalent prompts, not just the exact one used for the edit. This concept is framed as a property of post-edit models, studied within the context of knowledge editing. As one paper notes, the objective is for an edited model to meet properties including reliability, locality, and generality ("Investigating Pedagogical Teacher and StudentLLMAgents..."). The construct is operationalized and measured using specific benchmarks and tasks. Papers in this set use the CounterFact and zs-RE datasets to assess a model's generality. Additionally, the behavior of Visual question answering is also used as a method for its measurement. The concept is also studied in relation to Catastrophic forgetting.

## Sources

**[Investigating Pedagogical Teacher and StudentLLMAgents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.676.pdf)**
> The ability of a model to apply newly edited knowledge to rephrased or semantically equivalent prompts, not just the exact one used for editing.

## Relationships

### Generality →
- **CounterFact** (measurements) — *measured_by*
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **zs-RE** (measurements) — *measured_by*
  > Results on three metrics for the two datasets using LLAMA2-7B and LLAMA-7B. (Table 1)
  - [A Cognitive Evaluation Benchmark of Image Reasoning and Description for Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Knowledge editing** (behaviors tasks)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Dynamic Model-Bank Test-Time Adaptation for Automatic Speech Recognition](https://aclanthology.org/2025.emnlp-main.1108.pdf)

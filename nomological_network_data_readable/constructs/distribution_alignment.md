# Distribution alignment
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Distributional alignment  

## State of the Field

Across the surveyed literature, "Distribution alignment" is a construct with several distinct definitions, generally centered on matching statistical distributions to improve model learning. The most prevalent framing concerns the correspondence between different datasets, where it is defined as the degree to which selected training data matches the distribution of a target task. In this context, one paper notes that alignment enables "data-efficient finetuning" and can be measured using optimal transport. A related usage applies this concept to knowledge distillation, defining it as a student model's ability to replicate a teacher model's output probability distribution. A different conceptualization treats it as a model's capacity to leverage statistical correlations within in-context data to improve learning efficiency, particularly in studies of in-context learning and retrieval augmented generation. The construct is operationalized and measured using the OpinionQA and GlobalOpinionQA benchmarks. It is also studied in relation to Information retrieval, Generation diversity, and Faithfulness.

## Sources

**[TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)**
> The degree to which the distribution of selected training data matches the distribution of representative examples from a target task, enabling a model to learn the target distribution efficiently.

**[Fine-grained Analysis of In-context Linear Estimation: Data, Architecture, and Beyond](https://proceedings.neurips.cc/paper_files/paper/2024/file/f9dc462382fef56d58279e75de2438f3-Paper-Conference.pdf) (as "Distributional alignment")**
> The model's capacity to leverage statistical correlations within the in-context data, such as between task and feature vectors or between query and demonstration examples, to improve learning efficiency.

## Relationships

### Distribution alignment →
- **OpinionQA** (measurements) — *measured_by*
  - [Understanding Figurative Meaning through Explainable Visual Entailment](https://aclanthology.org/2025.naacl-long.2.pdf)
- **GlobalOpinionQA** (measurements) — *measured_by*
  - [Understanding Figurative Meaning through Explainable Visual Entailment](https://aclanthology.org/2025.naacl-long.2.pdf)

### Associated with
- **Retrieval-augmented generation** (behaviors tasks)
  - [Fine-grained Analysis of In-context Linear Estimation: Data, Architecture, and Beyond](https://proceedings.neurips.cc/paper_files/paper/2024/file/f9dc462382fef56d58279e75de2438f3-Paper-Conference.pdf)
- **Generation diversity** (constructs)
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [REARANK: Reasoning Re-ranking Agent via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.126.pdf)

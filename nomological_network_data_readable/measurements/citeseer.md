# CiteSeer
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, CiteSeer is consistently defined as a real-world citation network dataset where nodes represent scientific papers. The most frequently mentioned application for this dataset is the evaluation of node classification tasks, a use case specified in its definition and confirmed in one source paper. However, the dataset is also shown to be adaptable for other evaluations. At least one paper uses CiteSeer to measure performance on the link prediction task. To facilitate this, the authors note they "modified the Cora and CiteSeer datasets by removing the nodes originally included in the node classification test set" (SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion). Thus, the data shows CiteSeer is operationalized to assess both node classification and link prediction.

## Sources

**[GITA: Graph to Visual and Textual Integration for Vision-Language Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/00295cede6e1600d344b5cd6d9fd4640-Paper-Conference.pdf)**
> A real-world citation network dataset where nodes are scientific papers, used for node classification evaluation.

## Relationships

### → CiteSeer
- **Link prediction** (behaviors tasks) — *measured_by*
  > our model achieved link prediction accuracies of 95.40% on Cora and 76.14% on CiteSeer, indicating the strong generalization capability of our method. (Section 4.2)
  - [SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.269.pdf)

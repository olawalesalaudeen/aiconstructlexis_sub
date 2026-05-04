# Link prediction
**Type:** Behavior  
**Referenced in:** 17 papers  

## State of the Field

Across the provided literature, Link prediction is consistently defined as the task of inferring or predicting connections between nodes in a graph. Some definitions frame this more specifically as predicting "missing relations or entities in a knowledge graph," while others use the more general phrasing of predicting whether an edge exists. The behavior is operationalized and evaluated using several datasets, including Cora, CiteSeer, FB15k-237, and WN18RR. Evaluation procedures involve using removed edges as prediction targets, with performance commonly measured by metrics such as accuracy, Mean Reciprocal Rank (MRR), and Hit@N. Link prediction is frequently studied alongside Node classification and is associated with the broader task of Knowledge graph completion. Furthermore, it is described as a task that "primarily depend[s] on the local reasoning capabilities of the graph structure" (Improving Chemical Understanding ofLLMs viaSMILESParsing). In some contexts, Link prediction is also used as a benchmark task to assess a model's Multi-task capability.

## Sources

**[Large Language Models-guided Dynamic Adaptation for Temporal Knowledge Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0fd17409385ab9304e5019c6a6eb327a-Paper-Conference.pdf)**
> The specific task of predicting missing relations or entities in a knowledge graph, evaluated using metrics like MRR and Hit@N.

## Relationships

### Link prediction →
- **FB15k-237** (measurements) — *measured_by*
  - [HiDe-LLaVA: Hierarchical Decoupling for Continual Instruction Tuning of Multimodal Large Language Model](https://aclanthology.org/2025.acl-long.667.pdf)
- **WN18RR** (measurements) — *measured_by*
  - [HiDe-LLaVA: Hierarchical Decoupling for Continual Instruction Tuning of Multimodal Large Language Model](https://aclanthology.org/2025.acl-long.667.pdf)
- **Cora** (measurements) — *measured_by*
  > our model achieved link prediction accuracies of 95.40% on Cora and 76.14% on CiteSeer, indicating the strong generalization capability of our method. (Section 4.2)
  - [SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **CiteSeer** (measurements) — *measured_by*
  > our model achieved link prediction accuracies of 95.40% on Cora and 76.14% on CiteSeer, indicating the strong generalization capability of our method. (Section 4.2)
  - [SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.269.pdf)

### → Link prediction
- **Multi-task capability** (constructs) — *measured_by*
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)

### Associated with
- **Node classification** (behaviors tasks)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Knowledge graph completion** (behaviors tasks)
  - [Tool Preferences in AgenticLLMs are Unreliable](https://aclanthology.org/2025.emnlp-main.1061.pdf)
- **Local reasoning** (constructs)
  > These tasks [node classification, link prediction, and subgraph classification] primarily depend on the local reasoning capabilities of the graph structure. (Abstract)
  - [Improving Chemical Understanding ofLLMs viaSMILESParsing](https://aclanthology.org/2025.emnlp-main.792.pdf)

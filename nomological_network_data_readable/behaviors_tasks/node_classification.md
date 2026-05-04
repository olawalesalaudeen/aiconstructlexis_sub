# Node classification
**Type:** Behavior  
**Referenced in:** 16 papers  

## State of the Field

Across the provided literature, node classification is consistently defined as the task of assigning a categorical label to nodes within a graph based on their features and structural connectivity. This behavior is operationalized and evaluated using a range of benchmark datasets, with the most frequently mentioned being Cora, PubMed, and ogbn-arxiv. Other datasets cited for measuring this task include Citeseer, Wiki-CS, ogbn-products, Arxiv, Amazon Reviews, and Wikipedia. While the general goal is to label nodes, some definitions refer to assigning a label to "each node," whereas one paper specifies a setup where "only one target node" is classified per graph sample. Node classification is presented as a "typical" node-level learning task and is studied alongside link prediction. Furthermore, some work suggests that performance on this task depends on local reasoning capabilities related to the graph's structure.

## Sources

**[Can Large Language Models Analyze Graphs like Professionals? A Benchmark, Datasets and Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff417c3993894694e88ffc4d3f53d28b-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of assigning a categorical label to each node in a graph based on its features and connectivity.

## Relationships

### Node classification →
- **Cora** (measurements) — *measured_by*
  > Tables 2 compares the performance of various models on the Cora and PubMed datasets, showcasing the effectiveness of different approaches. (Section 4.2)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **PubMed** (measurements) — *measured_by*
  > Tables 2 compares the performance of various models on the Cora and PubMed datasets, showcasing the effectiveness of different approaches. (Section 4.2)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **ogbn-arxiv** (measurements) — *measured_by*
  > "Extensive experiments conducted on three benchmark datasets—ogbn-arxiv, Cora, and PubMed—demonstrate that ExGLM"
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **ogbn-products** (measurements) — *measured_by*
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **Arxiv** (measurements) — *measured_by*
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Amazon Reviews** (measurements) — *measured_by*
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.173.pdf)
- **Wikipedia** (measurements) — *measured_by*
  - [SR-LLM: Rethinking the Structured Representation in Large Language Model](https://aclanthology.org/2025.acl-long.173.pdf)

### Associated with
- **Link prediction** (behaviors tasks)
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Local reasoning** (constructs)
  > These tasks [node classification, link prediction, and subgraph classification] primarily depend on the local reasoning capabilities of the graph structure. (Abstract)
  - [Improving Chemical Understanding ofLLMs viaSMILESParsing](https://aclanthology.org/2025.emnlp-main.792.pdf)

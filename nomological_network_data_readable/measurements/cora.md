# Cora
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** CORA  

## State of the Field

Across the provided literature, Cora is consistently defined as a citation network dataset where nodes represent scientific publications or documents and edges correspond to citation links. Its most prevalent application, mentioned across multiple papers, is to measure the performance of `node classification` on what are described as text-attributed graphs. While node classification is the most common task evaluated with Cora, a smaller set of studies also uses it to measure other behaviors. These include `link prediction`, with one paper reporting specific accuracy scores, and `graph partitioning`. Additionally, a single paper extends its use to assess `perplexity` and `structural understanding`. The dataset is frequently presented as a benchmark alongside others like PubMed and ogbn-arxiv, indicating its common use in experimental evaluations.

## Sources

**[Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)**
> A citation network dataset where nodes represent scientific publications, used to evaluate node classification performance on text-attributed graphs.

**[Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf) (as "CORA")**
> Standard citation network dataset used for node classification, where nodes represent documents and edges represent citation links, used to evaluate annotation and classification performance.

## Relationships

### → Cora
- **Node classification** (behaviors tasks) — *measured_by*
  > Tables 2 compares the performance of various models on the Cora and PubMed datasets, showcasing the effectiveness of different approaches. (Section 4.2)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **Link prediction** (behaviors tasks) — *measured_by*
  > our model achieved link prediction accuracies of 95.40% on Cora and 76.14% on CiteSeer, indicating the strong generalization capability of our method. (Section 4.2)
  - [SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **Graph partitioning** (behaviors tasks) — *measured_by*
  > To validate our approach, we construct multi-scale graph partitioning datasets based on Cora and conduct comprehensive experiments. (Section 5.1)
  - [Improving Chemical Understanding ofLLMs viaSMILESParsing](https://aclanthology.org/2025.emnlp-main.792.pdf)

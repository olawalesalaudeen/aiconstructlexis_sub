# ogbn-arxiv
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** OGBN-ARXIV  

## State of the Field

Across the provided literature, ogbn-arxiv is consistently used as a benchmark dataset to measure the task of Node classification. It is commonly defined as a large-scale, text-attributed citation network where nodes represent academic papers with titles and abstracts, and edges represent citations. A slightly different framing from one paper describes it as a directed graph of arXiv papers from the Open Graph Benchmark. The dataset's large scale is a recurring feature, with one study noting this makes it less scalable for LLMs compared to GNNs. Papers frequently employ it in experiments alongside other graph datasets like Cora and PubMed to evaluate model performance. For example, it has been used to investigate zero-shot classification with models like GPT-3.5, as noted in "Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning".

## Sources

**[Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)**
> Large-scale citation network dataset used for benchmarking node classification in text-attributed graphs, where nodes represent papers with titles and abstracts, and edges represent citations.

**[Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf) (as "OGBN-ARXIV")**
> A large-scale citation network dataset from the Open Graph Benchmark, representing a directed graph of arXiv papers.

## Relationships

### → ogbn-arxiv
- **Node classification** (behaviors tasks) — *measured_by*
  > "Extensive experiments conducted on three benchmark datasets—ogbn-arxiv, Cora, and PubMed—demonstrate that ExGLM"
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)

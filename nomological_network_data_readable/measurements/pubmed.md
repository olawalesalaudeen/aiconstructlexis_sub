# PubMed
**Type:** Measurement  
**Referenced in:** 20 papers  
**Also known as:** PUBMED, Pubmed  

## State of the Field

The prevailing use of PubMed in the provided literature is as a benchmark dataset for graph-based machine learning tasks, most commonly defined as a citation network where nodes represent documents. In this context, it is frequently used to measure `node classification` on text-attributed graphs (TAGs), with several papers describing it as a "widely adopted" or "well-established" dataset for this purpose. One paper also notes its use for both "node-level and edge-level tasks." A more specific definition describes the dataset as comprising "scientific publications from the PubMed database related to diabetes." A smaller line of work treats PubMed not as a graph but as a text corpus for language model evaluation. For instance, one study uses its collection of biomedical abstracts as a "representative of domain corpus" to finetune models. Other applications include measuring `text summarization`, where the task is to summarize author conclusions, and serving as an out-of-domain benchmark to evaluate zero-shot generalization.

## Sources

**[Dissecting learning and forgetting in language model finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c4de749a4bd8802f0b4033d09a7867db-Paper-Conference.pdf)**
> A citation network dataset derived from the PubMed database where nodes are documents, used to evaluate node classification on text-attributed graphs.

**[Label-free Node Classification on Graphs with Large Language Models (LLMs)](https://proceedings.iclr.cc/paper_files/paper/2024/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf) (as "PUBMED")**
> A citation network dataset from the biomedical domain, used for node classification on text-attributed graphs.

**[LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf) (as "Pubmed")**
> A benchmark dataset consisting of scientific publications from the PubMed database related to diabetes, used for node classification.

## Relationships

### → PubMed
- **Node classification** (behaviors tasks) — *measured_by*
  > Tables 2 compares the performance of various models on the Cora and PubMed datasets, showcasing the effectiveness of different approaches. (Section 4.2)
  - [Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks) — *measured_by*
  > We further evaluate the methods on three summarization datasets. ... PubMed (Tang et al., 2023) is a collection of medical scientific articles where the goal is to summarize the conclusions of the authors... (Section 4.1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)

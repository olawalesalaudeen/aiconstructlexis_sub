# Arxiv
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** ArxivCorpus  

## State of the Field

The Arxiv dataset is predominantly characterized as a benchmark representing a directed citation network of Computer Science papers, and in this capacity, it is used to measure `Node classification`. A separate line of work, however, utilizes Arxiv as a text corpus for a range of natural language processing evaluations. These text-based applications include assessing zero-shot language modeling perplexity on paper abstracts and evaluating long-document summarization, with one study noting its "extremely over-length document" poses a challenge for certain methods. The dataset is also employed as an out-of-domain benchmark to evaluate zero-shot generalization and is listed as a measurement instrument for `Multilingual generalization`. Finally, a specific variant named "ArxivCorpus" is defined as a collection of paper abstracts for pretraining models and evaluating text regeneration, using a test set with a temporal split to ensure evaluation on unseen data.

## Sources

**[LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)**
> A benchmark dataset representing a directed citation network of Computer Science papers from the arXiv preprint server, used for evaluating tasks like node classification.

**[Mind the Gesture: EvaluatingAISensitivity to Culturally Offensive Non-Verbal Gestures](https://aclanthology.org/2025.acl-long.1219.pdf) (as "ArxivCorpus")**
> Dataset of Arxiv paper abstracts used for pretraining and evaluating text regeneration, with test sets containing texts published after January 2024 to ensure strict unseen evaluation.

## Relationships

### → Arxiv
- **Node classification** (behaviors tasks) — *measured_by*
  - [LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)

# SCIDOCS
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** SciDocs  

## State of the Field

Across the provided literature, SCIDOCS is consistently characterized as an information retrieval dataset focused on scientific scholarly articles. The most prevalent framing describes it as a component of the BEIR benchmark, where it is used to measure information retrieval performance. Specifically, papers operationalize it as a single-hop retrieval benchmark for evaluating the re-ranking of scientific documents. A less common application is also documented, where one study uses the dataset to generate and evaluate adversarial passages in corpus-poisoning experiments. Researchers also note specific features of the dataset, such as its lack of a separate training set and the observation that a high percentage of its query terms do not appear in the corpus.

## Sources

**[Perplexity Trap: PLM-Based Retrievers Overrate Low Perplexity Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)**
> An information retrieval dataset dedicated to retrieval of scientific scholarly articles.

**[Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf) (as "SciDocs")**
> A BEIR dataset used as a single-hop retrieval benchmark for re-ranking scientific documents.

## Relationships

### → SCIDOCS
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [MoMoE: Mixture of Moderation Experts Framework forAI-Assisted Online Governance](https://aclanthology.org/2025.emnlp-main.639.pdf)

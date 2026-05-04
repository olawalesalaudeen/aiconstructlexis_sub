# Clustering
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Category induction, Code-switching  

## State of the Field

Across the provided literature, Clustering is most commonly defined as the task of grouping a set of texts such that texts within the same group are more similar to each other than to those in other groups. It is frequently positioned as one of several core text embedding tasks, studied alongside classification, retrieval, and reranking. The behavior is primarily operationalized and measured using the MTEB benchmark, which, as one paper notes, evaluates performance by "computing the v-measure score... on text embeddings clustered using k-means." Specific datasets used to evaluate this task include TwentyNewsgroups-Clustering and collections from sources like Arxiv and Reddit. A less common framing, termed "Category induction," describes a similar process of grouping entities into meaningful sets based on shared properties. A completely divergent usage appears in one source where "Code-switching" is defined as alternating between languages, a concept unrelated to grouping by similarity. The data also indicates a correlation between Clustering and Commonsense knowledge, but provides no evidence to elaborate on this relationship.

## Sources

**[Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)**
> The task of grouping a set of texts in such a way that texts in the same group are more similar to each other than to those in other groups.

**[RecBase: Generative Foundation Model Pretraining for Zero-Shot Recommendation](https://aclanthology.org/2025.emnlp-main.787.pdf) (as "Category induction")**
> The process of grouping entities into meaningful sets based on shared properties or clustered embeddings, allowing for overlapping and incomplete categorization.

**[Chart2Code53: A Large-Scale Diverse and Complex Dataset for Enhancing Chart-to-Code Generation](https://aclanthology.org/2025.emnlp-main.800.pdf) (as "Code-switching")**
> The observable linguistic behavior of alternating between two or more languages within a single conversation or utterance, which can be used to bypass safety filters.

## Relationships

### Clustering →
- **MTEB** (measurements) — *measured_by*
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)

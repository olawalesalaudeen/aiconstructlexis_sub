# Books3
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Book3  

## State of the Field

Across the provided literature, Books3 is consistently characterized as a dataset composed of an extensive collection of books, primarily used for evaluating language model performance. It is frequently employed to measure both `Language modeling` and `Length generalization`, with a specific focus on performance on extremely long documents, such as those with 96k-128k tokens. The most common method for this evaluation is calculating perplexity on the dataset, as noted in multiple papers, although one source also mentions using accuracy. While its primary role is evaluation, some work also uses Books3 for training language models, describing it as a "frequently used benchmark". In practice, it is often used alongside other book-based datasets like Gutenberg (PG-19) and other text corpora such as Arxiv. A minor variation in naming, 'Book3', appears in one paper, though it refers to the same underlying data source and usage. The dataset is also noted as being related to The Pile.

## Sources

**[PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training](https://proceedings.iclr.cc/paper_files/paper/2024/file/524ef58c2bd075775861234266e5e020-Paper-Conference.pdf)**
> A dataset consisting of an extensive collection of books, used to evaluate model performance on extremely long documents (e.g., 96k-128k tokens).

**[An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf) (as "Book3")**
> A large dataset of books used for evaluating language modeling performance on long-context sequences.

## Relationships

### → Books3
- **Length generalization** (constructs) — *measured_by*
  - [Scaling Laws of RoPE-based Extrapolation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d33b741600f100b31256c70a46f66ec9-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)

### Associated with
- **The Pile** (measurements)
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)

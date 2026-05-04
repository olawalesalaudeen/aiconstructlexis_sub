# MS MARCO
**Type:** Measurement  
**Referenced in:** 14 papers  

## State of the Field

Across the provided literature, MS MARCO is consistently characterized as a large-scale dataset and benchmark for information retrieval and question answering tasks. Several sources specify that the dataset is derived from real-world user queries from Bing. Its most prevalent application is as an evaluation instrument, where it is used to measure model performance on tasks such as passage ranking, document retrieval in "non-Wikipedia scenarios", and answering questions based on retrieved passages. For instance, one study uses it as a "search-and-retrieve" benchmark to evaluate hallucination (Teaching Language Models to Hallucinate Less with Synthetic Tasks). In addition to evaluation, some work also utilizes MS MARCO for training purposes. One paper notes using only its "question-and-answer pairs" for retriever fine-tuning (RA-DIT: Retrieval-Augmented Dual Instruction Tuning), while another explicitly mentions its dual role in both training retrievers and evaluating their performance.

## Sources

**[RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf)**
> A question answering dataset used for retriever fine-tuning, specifically the question-and-answer pairs.

## Relationships

### → MS MARCO
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction](https://proceedings.iclr.cc/paper_files/paper/2025/file/c44c4afd77d5ee760e7f4bed0c50f878-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Ranking** (behaviors tasks) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **Retrieval effectiveness** (constructs) — *measured_by*
  - [SAFE-SQL: Self-Augmented In-Context Learning with Fine-grained Example Selection for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.963.pdf)

# MSMARCO
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** MSMarco, MARCO QA  

## State of the Field

Across the provided literature, MSMARCO is consistently characterized as a large-scale dataset used for evaluation. Its most prevalent application is for measuring `Information retrieval`, with papers defining it as a tool for assessing tasks like "in-domain retrieval performance" (Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models). Several sources also define and use it as a benchmark for `Reading comprehension` and `Question answering`, including `Open-domain question answering`. A more specific line of work operationalizes MSMARCO as a "passage-ranking benchmark" (BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge) to evaluate `Ranking` in a retrieval setting. The dataset is described as a "large-scale collection of queries and passages," and specific subsets like the TREC Deep Learning tracks (DL19, DL20) and "msmarco-passages" are mentioned. One paper also uses the dataset to measure aspects of `Safety`, demonstrating how a reranker can be backdoored on its passages. Evaluation on the MS MARCO Dev set is reported using the MRR metric.

## Sources

**[PICASO: Permutation-Invariant Context Composition with State Space Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0730b81dbc16cce7e85b519cb7fe5a8d-Paper-Conference.pdf)**
> The Microsoft Machine Reading Comprehension (MSMARCO) dataset, a large-scale collection of queries and passages used for evaluating reading comprehension and information retrieval tasks.

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf) (as "MSMarco")**
> A passage-ranking benchmark used to evaluate reranker judges in a retrieval setting.

**[RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf) (as "MARCO QA")**
> The MS MARCO Question Answering (MARCO QA) dataset, a large-scale benchmark for reading comprehension and question answering.

**[Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf) (as "MS MARCO")**
> The Microsoft Machine Reading Comprehension (MS MARCO) dataset, including its TREC Deep Learning track subsets (DL19, DL20), used here to evaluate in-domain retrieval performance.

## Relationships

### → MSMARCO
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  - [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf)

# CodeSearchNet
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Code Search Net  

## State of the Field

CodeSearchNet is predominantly characterized as a benchmark for evaluating function-level text-to-code retrieval. This task is consistently framed as a semantic search where natural language queries are used to retrieve relevant code snippets. The provided literature shows it is used to measure both code retrieval and the related behavior of ranking, where one study evaluates a reranker on its output. A less frequent but present framing positions CodeSearchNet as a dataset for assessing code generation and code understanding. One source specifies its composition, noting it contains over two million comment-code pairs across six programming languages. The most common usage across the supplied papers is for code retrieval tasks, with its application to code generation being a secondary, less-mentioned use.

## Sources

**[CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf)**
> CodeSearchNet (CSN), a benchmark for function-level text-to-code retrieval using natural language queries and code snippets.

**[EventRAG: EnhancingLLMGeneration with Event Knowledge Graphs](https://aclanthology.org/2025.acl-long.831.pdf) (as "Code Search Net")**
> Dataset for evaluating code generation and understanding, containing code snippets and natural language descriptions across multiple programming languages.

## Relationships

### → CodeSearchNet
- **Code retrieval** (behaviors tasks) — *measured_by*
  > First, we consider CodeSearchNet (CSN) (Husain et al., 2019) and AdvTest (Lu et al., 2021) as benchmarks for function-level text-to-code retrieval, a semantic search task where natural language queries are used to retrieve relevant code snippets. (Section 4.1.1)
  - [CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf)
- **Ranking** (behaviors tasks) — *measured_by*
  > For evaluation, we employ the CodeSearchNet and AdvTest text-to-code retrieval benchmarks... the top 100 results from our code retriever are passed to the reranker, with evaluation conducted using MRR@100.
  - [CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *measured_by*
  - [Selective Aggregation for Low-Rank Adaptation in Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53a37f820d5be5930415d964f4a0187-Paper-Conference.pdf)

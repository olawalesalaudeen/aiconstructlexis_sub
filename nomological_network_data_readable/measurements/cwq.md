# CWQ
**Type:** Measurement  
**Referenced in:** 17 papers  

## State of the Field

Across the provided literature, CWQ (ComplexWebQuestions) is consistently characterized as a benchmark dataset used to evaluate model performance on specific reasoning tasks. The prevailing usage of CWQ is to measure "Knowledge graph question answering" (KGQA), with multiple sources describing it as a "widely used" or "classical" benchmark for this purpose. The dataset is uniformly defined as requiring "multi-hop" reasoning over the Freebase knowledge graph, with one paper specifying this involves "complex 2-4 hop reasoning." A smaller set of papers also position CWQ as a tool for measuring "complex reasoning" and "commonsense knowledge." The dataset is noted to contain 34,689 questions and is often used alongside the WebQSP benchmark, with its questions described as being more complex. Researchers operationalize CWQ by testing their frameworks on it and reporting performance using metrics such as F1 score.

## Sources

**[Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)**
> ComplexWebQuestions, a multi-hop KBQA benchmark used to test knowledge-intensive question answering over a knowledge graph.

## Relationships

### → CWQ
- **Knowledge graph question answering** (behaviors tasks) — *measured_by*
  > "We evaluate reasoning performance on benchmark KGQA datasets used by: WebQSP (Yih et al., 2016) includes 4,737 questions involving simple and two-hop reasoning, while CWQ (Talmor and Berant, 2018) features 34,689 questions requiring complex 2-4 hop reasoning."
  - [Efficient Long Context Language Model Retrieval with Compression](https://aclanthology.org/2025.acl-long.741.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)

# WebQSP
**Type:** Measurement  
**Referenced in:** 22 papers  
**Also known as:** WebQuestionsSP  

## State of the Field

Across the provided literature, WebQSP (WebQuestionsSP) is consistently defined as a benchmark dataset for evaluating Knowledge Base Question Answering (KBQA). Its most prevalent application is to measure performance on KBQA, with several papers also using it to assess multi-hop and complex reasoning over structured knowledge bases. Multiple sources agree that the benchmark is based on the Freebase knowledge base. While the most common definition is general, a less frequent but more detailed one specifies that WebQSP is derived from the WebQuestions dataset and contains natural language questions annotated with their corresponding SPARQL queries. In experimental contexts, it is frequently evaluated alongside other datasets, as one paper notes, "We evaluate the reasoning ability of RoG on two benchmark KGQA datasets: WebQuestionSP (WebQSP) ... and Complex WebQuestions (CWQ)". Some sources provide additional specifics, such as its questions originating from the Google Suggest API or that they "often require multi-entity constraints".

## Sources

**[Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)**
> WebQuestionsSP, a KBQA benchmark used to evaluate question answering over structured knowledge bases.

**[Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.760.pdf) (as "WebQuestionsSP")**
> WebQuestionsSP (WebQSP) is a benchmark dataset for knowledge base question answering derived from WebQuestions, with questions annotated with their corresponding SPARQL queries.

## Relationships

### → WebQSP
- **Knowledge graph question answering** (behaviors tasks) — *measured_by*
  > We evaluate reasoning performance on benchmark KGQA datasets used by: WebQSP (Yih et al., 2016)... (Section 4.1)
  - [Personalized Generation In Large Model Era: A Survey](https://aclanthology.org/2025.acl-long.1202.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf)
- **Multi-hop question answering** (behaviors tasks) — *measured_by*
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)

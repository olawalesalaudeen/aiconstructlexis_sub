# Information synthesis
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Information integration, Information aggregation, Abstraction and aggregation  

## State of the Field

Across the surveyed literature, information synthesis is consistently described as a behavior involving the combination, integration, or aggregation of information from multiple locations or sources. The specific context and goal of this synthesis, however, vary across different lines of work. A common framing defines it as integrating information from diverse sources, such as web pages and knowledge graphs, to "generate a coherent answer" (CRAG - Comprehensive RAG Benchmark). Other usages treat it as the task of collecting and synthesizing information from various parts of a long document for tasks like sorting, or as a database-like operation involving a "semantics-based GROUP BY" on unstructured data (UQE: A Query Engine for Unstructured Databases). A more domain-specific definition involves aggregating patient information from conversation histories to update a clinical understanding. To evaluate this behavior, researchers use benchmarks such as ZeroSCROLLS and 2WikiMultihopQA, and it is also operationalized through tasks like BookSumSort. The concept is also noted as being related to commonsense knowledge.

## Sources

**[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf) (as "Information integration")**
> Aggregating gathered patient information from conversation history to update understanding of the patient condition.

**[Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf) (as "Information aggregation")**
> The task of collecting and synthesizing information from various parts of a long document or multiple documents to perform a task like sorting or ordering.

**[UQE: A Query Engine for Unstructured Databases](https://proceedings.neurips.cc/paper_files/paper/2024/file/34b3a40ec9752c1ae48fe85fef8fe8dc-Paper-Conference.pdf) (as "Abstraction and aggregation")**
> Grouping rows from a database based on an abstract, semantically-derived attribute and then performing an aggregation operation (like counting) on each group.

**[CRAG - Comprehensive RAG Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1435d2d0fca85a84d83ddcb754f58c29-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The process of integrating and combining information from multiple different sources, such as web pages and knowledge graphs, to generate a coherent answer.

## Relationships

### Information synthesis →
- **ZeroSCROLLS** (measurements) — *measured_by*
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **2WikiMultihopQA** (measurements) — *measured_by*
  - [From Scores to Steps: Diagnosing and ImprovingLLMPerformance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.549.pdf)

# Query generation
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Text-to-Cypher generation, Text-to-nGQL generation  

## State of the Field

Across the provided literature, query generation is characterized in two primary ways: as a general capability within retrieval-augmented systems and as a specific semantic parsing task. The more general usage defines it as the production of search queries to fetch external knowledge for retrieval-augmented generation. In this context, performance issues are sometimes attributed to "imprecise query generation," with one paper noting that models can produce "under-specified queries" ("Training a Utility-based Retriever..."). A second, more specific framing treats it as the task of translating natural language questions into executable query languages for graph databases, such as Text-to-Cypher or Text-to-nGQL generation, which is described as a "central focus in semantic parsing" ("SAKI-RAG..."). This behavior is operationalized and measured using datasets tailored to the target query language; for example, the Text-to-Cypher task is evaluated using the Text2Cypher dataset. Functionally, query generation is presented as a component within a larger information retrieval process where a system "iteratively generates queries, retrieves documents, and selects useful documents".

## Sources

**[Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.34.pdf)**
> The observable production of search queries by a model, particularly in the context of retrieval-augmented generation, where queries are used to fetch external knowledge.

**[SAKI-RAG: Mitigating Context Fragmentation in Long-DocumentRAGvia Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.64.pdf) (as "Text-to-Cypher generation")**
> The specific task of translating a natural language question into an executable Cypher query for a graph database.

**[SAKI-RAG: Mitigating Context Fragmentation in Long-DocumentRAGvia Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.64.pdf) (as "Text-to-nGQL generation")**
> The specific task of translating a natural language question into an executable nGQL query for a graph database.

## Relationships

### Query generation →
- **Text2Cypher** (measurements) — *measured_by*
  > For the Text-to-Cypher task, We evaluate our approach on Text2Cypher (Ozsoy et al., 2025), a large-scale dataset released by Neo4j.
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-DocumentRAGvia Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.64.pdf)

### Associated with
- **Information retrieval** (behaviors tasks)
  > Recent works like Search-R1 (Jin et al., 2025) and R1-Searcher (Song et al., 2025) use reinforcement learning to optimize reasoning-based query generation while keeping the retrieval model fixed. (Section 2)
  - [SAFENUDGE: Safeguarding Large Language Models in Real-time with Tunable Safety-Performance Trade-offs](https://aclanthology.org/2025.emnlp-main.1011.pdf)

# Query expansion
**Type:** Behavior  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, query expansion is consistently described as the process of augmenting, reformulating, or generating additional text for an original search query. The prevailing goal of this behavior is to improve retrieval performance and information search, with one paper noting its utility for handling "complex queries." The operationalization of query expansion is frequently tied to the use of large language models (LLMs). As one study notes, "Large language models (LLMs) have been used to generate query expansions augmenting original queries for improving information search" ("Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective"). A specific method described involves using an LLM to sample multiple responses and then concatenating them with the original query. An alternative approach uses Retrieval-Augmented Generation (RAG) to incorporate terms from related documents to broaden the query's scope. The added content is variously defined as "descriptive text," "synonyms," or "related terms." This behavior is consistently positioned as a technique intended to improve information retrieval.

## Sources

**[AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.334.pdf)**
> Generating additional descriptive text based on an original search query to improve retrieval performance by capturing more context.

## Relationships

### Query expansion →
- **Information retrieval** (behaviors tasks) — *causes*
  - [Proxy-Driven Robust Multimodal Sentiment Analysis with Incomplete Data](https://aclanthology.org/2025.acl-long.1076.pdf)

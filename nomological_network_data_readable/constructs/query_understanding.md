# Query understanding
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Conversational query reformulation  

## State of the Field

Across the surveyed literature, query understanding is framed in several distinct ways with no single consensus definition. The most prevalent view treats it as the ability to infer user intent for information retrieval, described as a "critical component in a retrieval system" used to "construct more effective queries" (P-MMEval). A related line of work presents a more specific, observable task called "conversational query reformulation," which clarifies user intent by transforming a query and its conversational history into a "standalone search query" (RAG-Instruct). In contrast, a different conceptualization defines query understanding as an initial processing step within a model, specifically the behavior of interpreting and reiterating a user's query before reasoning begins (fLSA). As the provided data lacks relationships to specific measurement instruments, the ways this construct is measured remain unstated, though one paper frames a related concept as an "observable task".

## Sources

**[P-MMEval: A Parallel Multilingual Multitask Benchmark for Consistent Evaluation ofLLMs](https://aclanthology.org/2025.emnlp-main.243.pdf)**
> The ability to infer the intent of a user's query to determine how to best process it for information retrieval and generation.

**[RAG-Instruct: BoostingLLMs with Diverse Retrieval-Augmented Instructions](https://aclanthology.org/2025.emnlp-main.193.pdf) (as "Conversational query reformulation")**
> The observable task of transforming a user's current query and the preceding conversational history into a self-contained, standalone search query.

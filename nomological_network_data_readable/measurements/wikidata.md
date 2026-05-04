# Wikidata
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** WikiData  

## State of the Field

Across the provided literature, Wikidata is most commonly described as a knowledge graph used as a source of structured data for other datasets and benchmarks. For instance, it is cited as the underlying knowledge graph for datasets such as T-REx, Zero-Shot RE, HotpotQA, and Creak. One paper also uses it as a "multilingual knowledge base" from which to extract an initial list of entities, such as those under the class “food”, to construct a new benchmark. A different line of work treats Wikidata not just as a source, but as a direct evaluation instrument itself. In this context, it is defined as a "general knowledge base schema matching dataset" and is used to measure the behavior of Schema linking. One study specifically uses it to assess a system’s generalizability on structured, open-domain data.

## Sources

**[Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf)**
> A knowledge graph used as the structured knowledge source for several of the evaluated datasets.

**[Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf) (as "WikiData")**
> General knowledge base schema matching dataset used to test the generalization of schema matching approaches on structured open-domain data.

## Relationships

### → Wikidata
- **Schema linking** (behaviors tasks) — *measured_by*
  > Table 2: Table task and benchmark data for evaluation (Table 2)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)

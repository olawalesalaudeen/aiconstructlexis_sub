# FEVEROUS
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Feverous  

## State of the Field

Across the provided literature, FEVEROUS is consistently characterized as a dataset or benchmark for fact verification and claim checking. Its primary task involves verifying complex claims, which some sources state necessitates "multi-hop reasoning for verification" (Information Re-Organization Improves Reasoning in Large Language Models). A defining feature mentioned in nearly all sources is its use of mixed evidence formats, requiring models to reason over both structured data, such as tables, and unstructured text from sentences. Several papers specify that the underlying data is sourced from Wikipedia, with evidence annotated from "either sentences or table cells" (Multilingual Needle in a Haystack...). Consequently, FEVEROUS is used as a measurement instrument for general `Evaluation`, and is also applied more specifically to assess `Table and chart reasoning`, with one paper noting it was "adapted the dataset for open-domain table reasoning" (OpenTab: Advancing Large Language Models as Open-domain Table Reasoners). A smaller number of sources also report its use for measuring `Entity disambiguation` and note its focus on numerical reasoning. The prevailing usage, therefore, positions FEVEROUS as a tool for evaluating a model's ability to integrate and reason over combined textual and tabular information to validate factual statements.

## Sources

**[OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)**
> FEVEROUS, a fact-verification dataset used here in an open-domain table reasoning setting requiring identification of relevant evidence tables.

**[SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf) (as "Feverous")**
> A fact verification benchmark requiring models to verify claims using evidence from semi-structured tables and text, with complex reasoning.

## Relationships

### → FEVEROUS
- **Claim verification** (behaviors tasks) — *measured_by*
  - [Information Re-Organization Improves Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb1a323fa10d4102ff13422476a744ff-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **Table reasoning** (constructs) — *measured_by*
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **Entity disambiguation** (behaviors tasks) — *measured_by*
  - [Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models](https://aclanthology.org/2025.naacl-long.268.pdf)

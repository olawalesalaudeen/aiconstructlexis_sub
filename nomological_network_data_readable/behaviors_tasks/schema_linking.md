# Schema linking
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Table join prediction, Entity alignment, Relation alignment, Schema item grounding, Schema parsing, Schema resolution, Schema matching, Entity matching, Cross-lingual product alignment, Attribute alignment  

## State of the Field

Across the surveyed literature, "Schema linking" is most commonly described as the behavior of identifying and mapping elements from a natural language query to the relevant components of a database schema, such as tables and columns. This process is also referred to as "schema item grounding," "schema parsing," or "schema resolution," and is frequently positioned as a preliminary step that enables `Code generation`, particularly in Text-to-SQL tasks. As one paper notes, this involves "analyzing the test question to detect keywords and phrases that correspond to schema elements" (PhonoThink: Improving Large Language Models’ Reasoning onChinese Phonological Ambiguities). A smaller but related line of work extends this concept to knowledge graphs, defining it as `Entity alignment`, `Relation alignment`, or `Attribute alignment`, which involves matching entities or relations between different knowledge graphs or from a logical form to a knowledge base.

The behavior is operationalized in several ways. In some contexts, it is treated as a binary classification task of determining if two columns are semantically related, termed `Schema matching`. In others, it involves mapping surface forms to canonical identifiers using similarity scoring. The performance of this behavior is measured using benchmarks such as `Wikidata` and tasks within `Data analysis` collections, which include "predicting which columns can be used to join two tables" (LiveBench: A Challenging, Contamination-Limited LLM Benchmark). Schema linking is also reported to influence `Cross-domain generalization` and is studied alongside `Information retrieval`. Some work suggests that abilities like `Semantic understanding` and methods such as `In-context and few-shot learning` can improve schema linking performance.

## Sources

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)**
> The observable behavior of identifying and outputting the specific database tables and columns that are relevant to a given natural language question.

**[LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf) (as "Table join prediction")**
> The task of identifying and creating a valid mapping of columns between two tables to perform a join.

**[From Problem-Solving to Teaching Problem-Solving: AligningLLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.16.pdf) (as "Entity alignment")**
> Mapping surface-form entity names in generated logical forms to their canonical identifiers (mids) in the knowledge base using popularity and similarity scoring.

**[From Problem-Solving to Teaching Problem-Solving: AligningLLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.16.pdf) (as "Relation alignment")**
> Matching relation surface forms in generated logical forms to actual relations in the knowledge base using exact match or semantic similarity (e.g., SimCSE).

**[OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf) (as "Schema item grounding")**
> The observable identification of relevant tables and columns within a database schema for accurate SQL generation, including correct linking during query construction.

**[OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf) (as "Schema parsing")**
> The extraction and identification of necessary tables and columns from a filtered schema to support accurate SQL generation.

**[Iterative Multilingual Spectral Attribute Erasure](https://aclanthology.org/2025.emnlp-main.1489.pdf) (as "Schema resolution")**
> Identifying and grounding database schema elements (tables, fields) in the natural language query to correctly reference them in the SQL output.

**[Towards Robust Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1795.pdf) (as "Schema matching")**
> Determining whether two columns from different tables are semantically related, treated as a binary classification task.

**[KG-FIT: Knowledge Graph Fine-Tuning Upon Open-World Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/f606d45ae7b991988b6eea2af38b7057-Paper-Conference.pdf) (as "Entity matching")**
> Identifying whether entities from different knowledge graphs refer to the same real-world entity.

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Cross-lingual product alignment")**
> The task of identifying the same product across different languages based on its metadata.

**[Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf) (as "Attribute alignment")**
> The task of identifying and matching attributes from different knowledge graphs that have the same semantic meaning, even if their labels differ, often performed using an LLM.

## Relationships

### Schema linking →
- **Code generation** (behaviors tasks) — *causes*
  - [ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)
- **Wikidata** (measurements) — *measured_by*
  > Table 2: Table task and benchmark data for evaluation (Table 2)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **Cross-domain generalization** (constructs) — *causes*
  > Schema-linking is widely recognized as key to improving generalization by adaptively associating queries with database items. (Section 1)
  - [Playpen: An Environment for Exploring Learning From Dialogue Game Feedback](https://aclanthology.org/2025.emnlp-main.1518.pdf)

### → Schema linking
- **Semantic understanding** (constructs) — *causes*
  - [Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf)
- **Data analysis** (behaviors tasks) — *measured_by*
  > “Data Analysis: three tasks using recent datasets from Kaggle and Socrata, specifically, ... predicting which columns can be used to join two tables”
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)

### Associated with
- **Code generation** (behaviors tasks)
  - [OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Candidate generation** (behaviors tasks)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **Iterative refinement** (behaviors tasks)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **Confidence scoring** (behaviors tasks)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
- **Information retrieval** (behaviors tasks)
  > Through error analysis, we identify two major challenges in schema linking: (1) Database Retrieval: accurately selecting the target database from a large schema pool, while effectively filtering out irrelevant ones
  - [OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.51.pdf)

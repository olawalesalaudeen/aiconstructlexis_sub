# Structural understanding
**Type:** Construct  
**Referenced in:** 9 papers  
**Also known as:** Structural awareness, Table structure understanding, Graph structure understanding  

## State of the Field

Across the provided literature, 'structural understanding' is consistently framed as a latent ability of models to comprehend and utilize the organization of various data formats. The specific focus varies, with definitions encompassing the hierarchical and semantic information in documents (termed 'structural awareness'), the alignment of natural language to database schemas, the interpretation of complex table layouts, and the comprehension of knowledge graph embeddings. The most common application appears to be in the context of tables and databases, with one paper noting that "Understanding complex table structures remains a fundamental challenge," especially for "nested/hierarchical tables" ('ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation'). This construct is operationalized and measured through performance on specific benchmarks; for example, the TableEval benchmark is used to evaluate the "understanding of table structures." Other operationalizations are implied through tasks like schema linking for SQL generation and reasoning over subgraphs. Some research suggests that specialized training, such as contrastive learning, can enable models to "better encode semantic hierarchies" ('The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection'). The construct is also positioned as being related to 'long-context understanding' and is reported to influence 'time series forecasting'.

## Sources

**[The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection](https://aclanthology.org/2025.emnlp-main.429.pdf) (as "Structural awareness")**
> The model's latent ability to comprehend and utilize the hierarchical and semantic information embedded in document structures, such as HTML tags, to improve representation quality.

**[PhonoThink: Improving Large Language Models’ Reasoning onChinese Phonological Ambiguities](https://aclanthology.org/2025.emnlp-main.962.pdf)**
> The latent ability to align natural language questions with the structural components of a database schema, including tables, columns, and their relationships, to generate syntactically and semantically valid SQL.

**[ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf) (as "Table structure understanding")**
> The latent ability of an LLM to interpret and reason over complex table layouts, including hierarchical, nested, and concise structures, beyond simple flat tables.

**[Tool Preferences in AgenticLLMs are Unreliable](https://aclanthology.org/2025.emnlp-main.1061.pdf) (as "Graph structure understanding")**
> The degree to which an LLM comprehends the semantic and topological meaning of graph embeddings derived from knowledge graphs, enabling effective reasoning over subgraphs and neighborhoods.

## Relationships

### Structural understanding →
- **Time series forecasting** (behaviors tasks) — *causes*
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)
- **TableEval** (measurements) — *measured_by*
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf)

### Associated with
- **Long-context understanding** (constructs)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.591.pdf)

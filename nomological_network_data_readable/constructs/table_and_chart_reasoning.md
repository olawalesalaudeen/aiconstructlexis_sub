# Table and chart reasoning
**Type:** Construct  
**Referenced in:** 29 papers  
**Also known as:** Table reasoning, Table-based reasoning, Chart reasoning, Cross-table comprehension, Diagram-language alignment, Chart understanding, Diagram understanding, Physical diagram understanding, Chart comprehension, Diagram comprehension, Table understanding, Visual table understanding, Column-level understanding, Multi-table understanding, Table perception  

## State of the Field

Across the surveyed literature, "Table and chart reasoning" is a broad construct referring to a model's latent ability to comprehend, interpret, and perform inference on information presented in structured or visual formats like tables, charts, and diagrams. The most prevalent framing defines this ability in the context of tabular data, involving the comprehension of rows and columns, querying content, and synthesizing information to answer natural language prompts. A parallel line of work addresses visual formats, defining the construct as the capacity to interpret visual elements, understand structure, and perform logical inference on charts and diagrams, often framing it as a multimodal task. Some papers further distinguish between reasoning over single versus multiple tables, with "Multi-table reasoning" requiring the integration of information across relational structures. This construct is operationalized and measured through model performance on a range of benchmarks. Specifically, papers in this set use datasets such as FEVEROUS, WikiTQ, TabFact, WikiTableQuestions, HiTab, and TableBench to evaluate this capability. "Table and chart reasoning" is frequently studied in conjunction with other constructs like `Complex reasoning`, `Mathematical reasoning`, and `Semantic understanding`.

## Sources

**[OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf) (as "Table reasoning")**
> The latent ability of a model to comprehend, query, and synthesize information from structured tabular data to address natural language prompts.

**[Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf) (as "Table-based reasoning")**
> The capacity to solve questions or verification problems by extracting and manipulating information from tables through intermediate reasoning steps.

**[LegalSearchLM: Rethinking Legal Case Retrieval as Legal Elements Generation](https://aclanthology.org/2025.emnlp-main.226.pdf) (as "Chart reasoning")**
> The latent ability of a model to interpret visual chart elements and perform logical inference to answer complex, real-world analytical questions.

**[UniformInformationDensity and Syntactic Reduction: Revisiting *that*-Mentioning inEnglish Complement Clauses](https://aclanthology.org/2025.emnlp-main.1118.pdf) (as "Multi-table reasoning")**
> The ability to understand and integrate information from multiple interrelated tables to answer complex queries that require navigating relational structures.

**[Bias Beware: The Impact of Cognitive Biases onLLM-Driven Product Recommendations](https://aclanthology.org/2025.emnlp-main.1141.pdf) (as "Cross-table comprehension")**
> The ability to understand and reason across multiple interdependent tables, integrating information from different sources into a unified analysis.

**[ChartMoE: Mixture of Diversely Aligned Expert Connector for Chart Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/c33cd281f8cd784626a57de340e43fe4-Paper-Conference.pdf) (as "Chart understanding")**
> The ability of a model to interpret visual charts, comprehend their structure and content, and perform complex tasks based on the information they convey.

**[MAVIS: Mathematical Visual Instruction Tuning with an Automatic Data Engine](https://proceedings.iclr.cc/paper_files/paper/2025/file/db36dcad6baee298a34ffca324b84b09-Paper-Conference.pdf) (as "Diagram-language alignment")**
> The degree to which visual representations of mathematical diagrams are aligned with language representations so the model can correctly interpret diagram content in text form.

**[Sketch2Diagram: Generating Vector Diagrams from Hand-Drawn Sketches](https://proceedings.iclr.cc/paper_files/paper/2025/file/2567c95fd41459a98a73ba893775d22a-Paper-Conference.pdf) (as "Diagram understanding")**
> The latent ability of a model to comprehend the components, layout, and semantic meaning of a diagram from an image.

**[MAPS: Advancing Multi-Modal Reasoning in Expert-Level Physical Science](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0422224da8dc076cab83709b9839b7b-Paper-Conference.pdf) (as "Physical diagram understanding")**
> The perceptual ability to correctly interpret the components, their properties, and their structural relationships within a diagram representing a physical system.

**[DisLoRA: Task-specific Low-Rank Adaptation via Orthogonal Basis from Singular Value Decomposition](https://aclanthology.org/2025.emnlp-main.695.pdf) (as "Chart comprehension")**
> The general ability of a model to understand and interpret information presented in graphical charts.

**[VideoEraser: Concept Erasure in Text-to-Video Diffusion Models](https://aclanthology.org/2025.emnlp-main.305.pdf) (as "Diagram comprehension")**
> The latent ability to interpret and understand the structured information presented in diagrams.

**[TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf) (as "Table understanding")**
> The latent ability of a language model to comprehend and process information presented in a structured tabular format.

**[TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf) (as "Visual table understanding")**
> The model's latent ability to comprehend the structure, content, and semantics of tables presented in a visual format, such as a document image.

**[MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf) (as "Column-level understanding")**
> The ability to interpret the semantic meaning of table columns and their relationships, such as identifying primary and foreign keys.

**[MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf) (as "Multi-table understanding")**
> The latent ability to comprehend information distributed across multiple related tables and use that structure to support downstream task performance.

**[R2I-Bench: Benchmarking Reasoning-Driven Text-to-Image Generation](https://aclanthology.org/2025.emnlp-main.637.pdf) (as "Table perception")**
> The ability to visually recognize and represent table structures and contents from table images.

## Relationships

### Table and chart reasoning →
- **FEVEROUS** (measurements) — *measured_by*
  - [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf)
- **WikiTQ** (measurements) — *measured_by*
  - [Instantly Learning Preference Alignment via In-contextDPO](https://aclanthology.org/2025.naacl-long.9.pdf)
- **TabFact** (measurements) — *measured_by*
  - [Instantly Learning Preference Alignment via In-contextDPO](https://aclanthology.org/2025.naacl-long.9.pdf)
- **WikiTableQuestions** (measurements) — *measured_by*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **HiTab** (measurements) — *measured_by*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **TableBench** (measurements) — *measured_by*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [Instantly Learning Preference Alignment via In-contextDPO](https://aclanthology.org/2025.naacl-long.9.pdf)
- **Table question answering** (behaviors tasks)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Table understanding** (behaviors tasks)
  - [TabPedia: Towards Comprehensive Visual Table Understanding with Concept Synergy](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d97fe65d7a1dc12a05642d9fa4cd578-Paper-Conference.pdf)
- **Semantic understanding** (constructs)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Information extraction** (behaviors tasks)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Temporal reasoning** (constructs)
  - [SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf)

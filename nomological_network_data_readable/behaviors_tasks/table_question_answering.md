# Table question answering
**Type:** Behavior  
**Referenced in:** 22 papers  
**Also known as:** Table-based question answering, Multi-table question answering, Table extraction, Tabular question answering, Free-form table QA, Short-form table QA  

## State of the Field

Across the surveyed literature, Table question answering is most commonly described as the task of generating a natural language answer to a question using information from one or more provided tables. The scope of this behavior varies, with some work focusing on single-table contexts, while a sub-task termed "Multi-table question answering" requires synthesizing information across multiple tables. The required operations also differ, ranging from direct answer retrieval and span extraction to performing arithmetic. A recurring distinction is made based on the expected output, separating "Short-form table QA," which requires "brief, precise answers," from "Free-form table QA," which involves generating "open-ended, paragraph-length answers." The field operationalizes and measures this behavior using several benchmarks; the provided data explicitly states that it is measured by `WikiTableQuestions`. Other papers refer to WikiTQ and FeTaQA as "widely used TableQA benchmarks," with one study linking the former to short-form QA and the latter to free-form QA. This behavior is studied alongside related concepts like `Tabular reasoning` and is sometimes paired with fact verification. A less common framing, termed "Table extraction," defines a related task of producing structured table-like information from source content rather than answering a specific question.

## Sources

**[Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf) (as "Table-based question answering")**
> The observable task of generating a concise, natural language answer to a question using information found within one or more provided tables.

**[MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf) (as "Multi-table question answering")**
> The task of generating a correct answer to a question by retrieving and synthesizing information from multiple provided tables.

**[SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cb240de90aa20207db944c6c88a7cc0-Paper-Conference.pdf) (as "Table extraction")**
> Reading scientific text or tables and producing structured table-like information from the source content.

**[LiveXiv - A Multi-Modal live benchmark based on Arxiv papers content](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eaa1373fe55b223c2dfe1fd29a277d7-Paper-Conference.pdf)**
> Answering questions that require interpreting table content and associated numerical or textual information.

**[Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ffd05ca3cf3985f4572af015b4cfc1e-Paper-Conference.pdf) (as "Tabular question answering")**
> Answering questions grounded in tabular or mixed tabular-text data, including cases requiring arithmetic or span extraction.

**[SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf) (as "Free-form table QA")**
> Generating open-ended, paragraph-length answers grounded in tabular data, requiring synthesis and natural language generation.

**[SNaRe: Domain-aware Data Generation for Low-Resource Event Detection](https://aclanthology.org/2025.emnlp-main.1040.pdf) (as "Short-form table QA")**
> Answering questions with brief, precise answers based on information in a table, often requiring extraction and aggregation of specific cell values.

## Relationships

### Table question answering →
- **WikiTQ** (measurements) — *measured_by*
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
- **FeTaQA** (measurements) — *measured_by*
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
- **WikiTableQuestions** (measurements) — *measured_by*
  - [R-Fairness: Assessing Fairness of Ranking in Subjective Data](https://aclanthology.org/2025.acl-long.1549.pdf)
- **TabFact** (measurements) — *measured_by*
  - [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf)
- **WikiSQL** (measurements) — *measured_by*
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
- **BIG-Bench** (measurements) — *measured_by*
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
- **HiTab** (measurements) — *measured_by*
  - [R2I-Bench: Benchmarking Reasoning-Driven Text-to-Image Generation](https://aclanthology.org/2025.emnlp-main.637.pdf)
- **TableBench** (measurements) — *measured_by*
  - [Towards Robust Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1795.pdf)
- **TableEval** (measurements) — *measured_by*
  - [ExeCoder: Empowering Large Language Models with Executability Representation for Code Translation](https://aclanthology.org/2025.emnlp-main.363.pdf)
- **FinQA** (measurements) — *measured_by*
  - [Towards Robust Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1795.pdf)

### Associated with
- **Table reasoning** (constructs)
  - [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)
- **Tabular reasoning** (constructs)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Semantic reasoning** (constructs)
  - [Improving the Quality of Web-mined Parallel Corpora of Low-Resource Languages using Debiasing Heuristics](https://aclanthology.org/2025.emnlp-main.1436.pdf)

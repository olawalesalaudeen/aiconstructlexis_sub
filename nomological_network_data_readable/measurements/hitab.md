# HiTab
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

HiTab is consistently described across the provided literature as a benchmark dataset for evaluating model performance on complex tables. The dataset is composed of tables sourced from government reports and Wikipedia pages, with one paper specifying it contains 3,597 tables and 10,672 question-answering pairs. The prevailing framing is that HiTab's primary challenge lies in its focus on "hierarchical tables," requiring models to handle "multi-level headers," "implicit relationships," and "complex structural relationships." In practice, papers use HiTab to measure several capabilities, including `Table understanding`, `Table and chart reasoning`, and `Text generation`. These capabilities are operationalized through tasks such as question answering and table transformation. For example, one study uses the benchmark to demonstrate that a new method "boosts QA accuracy" on the dataset. One paper also positions HiTab as a "widely used table reasoning dataset" alongside others in the field.

## Sources

**[LangSAMP: Language-Script Aware Multilingual Pretraining](https://aclanthology.org/2025.acl-long.89.pdf)**
> Benchmark dataset containing complex tables from government reports and Wikipedia pages, used to evaluate table transformation and question answering involving multi-level headers and implicit relationships.

## Relationships

### → HiTab
- **Text generation** (behaviors tasks) — *measured_by*
  - [A Self-Denoising Model for Robust Few-Shot Relation Extraction](https://aclanthology.org/2025.acl-long.1300.pdf)
- **Table question answering** (behaviors tasks) — *measured_by*
  - [R2I-Bench: Benchmarking Reasoning-Driven Text-to-Image Generation](https://aclanthology.org/2025.emnlp-main.637.pdf)
- **Table reasoning** (constructs) — *measured_by*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)

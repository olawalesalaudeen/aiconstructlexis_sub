# DART
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, DART is consistently characterized as a dataset or benchmark for evaluating language models on generation tasks. It is explicitly used to measure both `Text generation` and, more specifically, `Data-to-text generation`. The core task is described with slight variations in terminology, including 'struct-to-text' and 'graph-to-text', but the prevailing usage involves converting structured data into natural language. The input data is specified as structured information such as 'RDF triples', 'tables', or 'knowledge graphs'. The required output is a textual summary, with one paper describing the task as generating a description in 'one or two sentences'. The dataset is noted to be large, containing 82,191 examples, and open-domain. While most sources frame the task as generating text from data, one recurring definition also refers to it as a dataset for 'text-to-data generation'. In experimental contexts, DART is sometimes used alongside other benchmarks like WebNLG17 and WebNLG20.

## Sources

**[Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf)**
> A dataset for text-to-data generation, containing 82,191 examples from various domains to evaluate structured data-to-text tasks.

## Relationships

### → DART
- **Text generation** (behaviors tasks) — *measured_by*
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **Data-to-text generation** (behaviors tasks) — *measured_by*
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)

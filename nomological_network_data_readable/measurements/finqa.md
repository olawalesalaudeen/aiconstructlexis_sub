# FinQA
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the surveyed literature, FinQA is characterized as a benchmark dataset for question answering in the financial domain. The most prevalent operationalization requires models to generate a Python-executable math expression based on questions and financial tables. Papers use FinQA to measure constructs such as `Mathematical reasoning` and `Table understanding`, with one study noting it was developed to "benchmark deep learning models for such numerical reasoning tasks in the financial domain" (MMDocIR: Benchmarking Multimodal Retrieval for Long Documents). While the Python-generation framing is common, a smaller set of work describes the benchmark's focus differently; for instance, one paper states that FinQA assesses "knowledge-based question answering," while another claims it "primarily assess[es] text generation" (Dialect-SQL: An Adaptive Framework for Bridging the Dialect Gap in Text-to-SQL). In experimental setups, FinQA is employed as a held-out dataset to evaluate the generalization ability of methods and is also used to construct other evaluation tasks, such as reranking.

## Sources

**[DAWN-ICL: Strategic Planning of Problem-solving Trajectories for Zero-Shot In-Context Learning](https://aclanthology.org/2025.naacl-long.97.pdf)**
> A held-out dataset that requires generating a Python-executable math expression to answer questions based on financial tables.

## Relationships

### → FinQA
- **Mathematical reasoning** (constructs) — *measured_by*
  > datasets such as FinQA (Chen et al., 2021b) and ConvFinQA (Chen et al., 2022) have been developed to benchmark deep learning models for such numerical reasoning tasks in the financial domain.
  - [MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1577.pdf)
- **Table question answering** (behaviors tasks) — *measured_by*
  - [Towards Robust Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1795.pdf)

# WikiTQ
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

WikiTQ, also known as WikiTableQuestions, is a benchmark frequently used to evaluate a model's reasoning capabilities over structured data. Across the provided literature, it is consistently defined as a dataset of tables from Wikipedia paired with complex, natural-language questions. The relationships indicate that papers use WikiTQ to measure the constructs of "Table understanding" and "Table and chart reasoning". The questions are described as requiring complex operations, with several sources specifying the need for "comparison, aggregation, and arithmetic" to derive an answer ("CABINET: Content Relevance-based Noise Reduction for Table Question Answering"). The expected output is typically a short-form answer or a brief text span. One paper notes the dataset contains "about 2100 HTML tables from Wikipedia and about 22, 033 questions" ("CABINET..."), while another specifies a test set of "4,344 table-question pairs" ("UNDIAL..."). Its application is described as common, with multiple sources referring to it as a "widely-used" or "commonly used" benchmark for table-based reasoning.

## Sources

**[CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)**
> WikiTableQuestions, a benchmark of Wikipedia tables and natural-language questions requiring table reasoning such as comparison, aggregation, and arithmetic.

## Relationships

### → WikiTQ
- **Table question answering** (behaviors tasks) — *measured_by*
  - [CABINET: Content Relevance-based Noise Reduction for Table Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/19a42d5885e25e51852aca8144e5af0d-Paper-Conference.pdf)
- **Table reasoning** (constructs) — *measured_by*
  - [Instantly Learning Preference Alignment via In-contextDPO](https://aclanthology.org/2025.naacl-long.9.pdf)

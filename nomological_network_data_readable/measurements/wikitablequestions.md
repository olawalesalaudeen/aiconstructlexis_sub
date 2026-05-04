# WikiTableQuestions
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** WikiTableQuestion  

## State of the Field

WikiTableQuestions is characterized in the provided literature as a dataset for tasks involving tabular data. Across the supplied papers, it is consistently used to measure the behaviors of "Table question answering" and "Table and chart reasoning". The prevailing description frames it as a benchmark for complex tasks, with one paper specifying that these require "operations such as aggregation, comparison, and arithmetic calculations" ("Triples as the Key..."). This source also refers to it as a "widely recognized" and "commonly used dataset". While its primary use appears to be for evaluation, a different line of work adapts the dataset for model training. Specifically, one study uses it to create "training formats for table-language interleaved learning" and for "training column embeddings" ("Bridging the Semantic Gap..."). In this context, it is mentioned alongside other benchmarks like FetaQA and ToTTo.

## Sources

**[Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf) (as "WikiTableQuestion")**
> A table-question answering dataset adapted here into training formats for table-language interleaved learning.

**[Triples as the Key: Structuring Makes Decomposition and Verification Easier in LLM-based TableQA](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e50b663324972bb8cc7b5c06a059438-Paper-Conference.pdf)**
> A benchmark dataset for complex Table Question Answering tasks that require operations like aggregation, comparison, and arithmetic calculations.

## Relationships

### → WikiTableQuestions
- **Table question answering** (behaviors tasks) — *measured_by*
  - [R-Fairness: Assessing Fairness of Ranking in Subjective Data](https://aclanthology.org/2025.acl-long.1549.pdf)
- **Table reasoning** (constructs) — *measured_by*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)

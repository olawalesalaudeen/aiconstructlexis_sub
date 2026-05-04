# Date Understanding
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Date Understanding is consistently presented as a benchmark task originating from the BigBench suite, with some sources specifying its inclusion in BIG-Bench-Hard. Its primary purpose is to evaluate a model's ability to reason about dates, temporal relationships, and calendar logic, often when this information is presented in natural language. While there is broad agreement on its function, the specific cognitive ability it assesses is framed in several ways across the literature. The most prevalent uses are to operationalize and measure "symbolic reasoning" and "commonsense reasoning," as stated in multiple papers. A smaller number of studies also use it to explicitly assess "logical reasoning." Researchers commonly employ it as an evaluation instrument, sometimes alongside other benchmarks like CommonsenseQA and Object Counting. One paper also connects it to the measurement of "Faithfulness," though this is a less frequently mentioned application in the provided data.

## Sources

**[Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/6733cf15e10e2cd1d59af033c3bb8507-Paper-Conference.pdf)**
> A task from the BigBench suite that tests a model's ability to reason about and answer questions involving dates and temporal information.

## Relationships

### → Date Understanding
- **Logical reasoning** (constructs) — *measured_by*
  > Logical Reasoning: Date Understanding (bench authors, 2023). (Section 4)
  - [Substance Beats Style: Why Beginning Students Fail to Code withLLMs](https://aclanthology.org/2025.naacl-long.434.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.184.pdf)
- **Symbolic reasoning** (constructs) — *measured_by*
  > Symbolic Reasoning. We select four datasets from BigBench (Srivastava et al., 2022) for testing, including Date Understanding, Penguin, Colored Objects and Logical Deduction. (Section 4.1)
  - [CoPL: Collaborative Preference Learning for PersonalizingLLMs](https://aclanthology.org/2025.emnlp-main.651.pdf)

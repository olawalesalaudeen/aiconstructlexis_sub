# Spider
**Type:** Measurement  
**Referenced in:** 34 papers  
**Also known as:** SPIDER  

## State of the Field

Across the provided literature, Spider is consistently described as a large-scale, complex, and cross-domain benchmark for the text-to-SQL task. Its primary use is to evaluate a model's ability to generate syntactically and semantically correct SQL queries from natural language questions over diverse databases. As such, papers use Spider to measure the behavior of `Code generation`, specifically for database queries. Several sources characterize its scale, noting it contains thousands of text-SQL pairs spanning nearly 200 databases and 138 domains, with problems categorized into different difficulty levels (ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL; IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking). One paper also states that the benchmark introduced the Execution Accuracy (EX) metric, which has been adopted by other datasets (Transferable Post-training via Inverse Value Learning). It is frequently studied alongside other text-to-SQL benchmarks such as BIRD and KaggleDBQA. One study highlights its use in a setting 'where there are no unit tests in the problem description' (Teaching Large Language Models to Self-Debug).

## Sources

**[Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)**
> Text-to-SQL benchmark evaluating the ability to generate syntactically and semantically correct SQL queries from natural language questions over complex databases, used here without unit tests.

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf) (as "SPIDER")**
> A widely-used, large-scale, cross-domain benchmark dataset for evaluating Text-to-SQL models, consisting of natural language questions paired with SQL queries across multiple databases.

## Relationships

### → Spider
- **Code generation** (behaviors tasks) — *measured_by*
  > We use six datasets spanning different domains: GLUE for natural language understanding (Wang et al., 2019), DART for RDF-to-text generation (Nan et al., 2021), SAMSum (Gliwa et al., 2019) for summarization, Spider for text-to-SQL generation (Yu et al., 2018), and two vision datasets—CIFAR-10 (Krizhevsky et al., 2009) and CelebA (Liu et al., 2015), with the vision datasets processed by cropping, resizing, and flattening pixel values into space-separated numerical sentences.
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf)

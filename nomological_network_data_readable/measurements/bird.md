# BIRD
**Type:** Measurement  
**Referenced in:** 25 papers  

## State of the Field

Across the provided sources, BIRD is consistently characterized as a large-scale, cross-domain benchmark used to evaluate `Code generation` in the Text-to-SQL domain. A recurring theme is its positioning as a more challenging and realistic instrument than prior datasets, with several papers explicitly contrasting it with Spider. The benchmark's difficulty is attributed to its use of complex, real-world databases spanning dozens of professional domains, as noted in one source stating it contains "95 databases across 37 professional domains." Papers commonly highlight specific challenges it introduces, such as the reliance on external knowledge, the presence of "dirty values" and varied data formats, and the need for value-based reasoning. Its scale is also frequently mentioned, with sources describing it as containing over 12,751 question-SQL pairs. Described as a "standard" and "widely used" benchmark, one paper notes that Execution Accuracy (EX) is a primary metric for evaluating performance on BIRD.

## Sources

**[ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/212b143b5a5d6b88feb0fb1441b9756e-Paper-Conference.pdf)**
> A large-scale, cross-domain Text-to-SQL benchmark designed to be more challenging than previous datasets, featuring complex databases, difficult questions, and reliance on external knowledge.

## Relationships

### → BIRD
- **Code generation** (behaviors tasks) — *measured_by*
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)

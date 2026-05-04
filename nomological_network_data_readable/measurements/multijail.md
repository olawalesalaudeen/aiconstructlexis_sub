# MultiJail
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, MultiJail is consistently defined as a multilingual dataset used for evaluating language models, specifically in the domain of safety. The instrument is designed to measure the behavior of "Harmfulness detection," assessing a model's ability to identify unsafe or adversarial prompts in non-English contexts. Sources describe it as both a "red-teaming dataset" and a "text attack benchmark" that covers nine languages. Papers operationalize MultiJail in two distinct ways: for direct evaluation and as a resource for dataset creation. As an evaluation tool, it is used to benchmark and compare model accuracy, with one study reporting a model achieving "new state-of-the-art performance" on it ("PakBBQ: A Culturally Adapted Bias Benchmark forQA"). As a resource, its queries have been used as "seed data" to construct other datasets, such as CSRT.

## Sources

**[MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)**
> A multilingual red-teaming dataset covering nine languages, used to sample and translate adversarial prompts for evaluating LLM safety in non-English contexts.

## Relationships

### → MultiJail
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  > Table 3 compares the accuracy of detecting harmful prompts for text benchmarks. Table 3(A) shows results for multilingual benchmarks, where OMNIGUARD ... achieves new state-of-the-art performance for 3 benchmarks: MultiJail, RTP-LX, and AyaRedTeaming.
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)

### Associated with
- **CSRT** (measurements)
  > To construct the CSRT dataset for the following experiments in Section 4, we leverage MultiJail (Deng et al., 2024) of 315 queries as seed data in Step 1... (Section 3)
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)

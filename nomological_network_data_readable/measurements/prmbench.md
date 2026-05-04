# PRMBENCH
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** PRMBench  

## State of the Field

Across the provided literature, PRMBENCH is consistently described as a benchmark for evaluating process-level reward models. Its primary function is to assess the step-level correctness of reasoning chains in multi-step problem-solving, with one paper specifying its design is for evaluating "reasoning correctness and error detection" (BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering). Built on the PRM800K corpus, the benchmark is composed of math problems, with sources citing either "6k" or more specifically "6,216 carefully designed problems" distributed across nine error categories. The dataset also contains "83,456 step-level labels" to facilitate its evaluation goals. According to the relationships provided, papers use PRMBENCH to measure model performance across multiple dimensions, including the constructs of `Simplicity`, `Soundness`, and `Sensitivity`. It is also identified as an instrument for conducting `Error analysis`. In practice, it is used in evaluations alongside other datasets, with model performance reported using metrics like Macro-F1 scores.

## Sources

**[BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.212.pdf)**
> Benchmark dataset built on PRM800K corpus with 6k math problems across 9 error categories, designed to evaluate process-level reward models on reasoning correctness and error detection.

**[Avoidance Decoding for Diverse Multi-Branch Story Generation](https://aclanthology.org/2025.emnlp-main.382.pdf) (as "PRMBench")**
> Benchmark for evaluating process-level rewards in reasoning chains, assessing step-level correctness in multi-step problem solving.

## Relationships

### → PRMBENCH
- **Simplicity** (constructs) — *measured_by*
  - [Language Constrained Multimodal Hyper Adapter For Many-to-Many Multimodal Summarization](https://aclanthology.org/2025.acl-long.1230.pdf)
- **Soundness** (constructs) — *measured_by*
  > PRMBENCH comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity. (Section 1)
  - [Language Constrained Multimodal Hyper Adapter For Many-to-Many Multimodal Summarization](https://aclanthology.org/2025.acl-long.1230.pdf)
- **Sensitivity** (constructs) — *measured_by*
  - [Language Constrained Multimodal Hyper Adapter For Many-to-Many Multimodal Summarization](https://aclanthology.org/2025.acl-long.1230.pdf)
- **Error analysis** (behaviors tasks) — *measured_by*
  - [AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning](https://aclanthology.org/2025.emnlp-main.679.pdf)

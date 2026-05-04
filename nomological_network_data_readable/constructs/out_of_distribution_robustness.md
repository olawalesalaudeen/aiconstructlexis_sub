# Out-of-distribution robustness
**Type:** Construct  
**Referenced in:** 3 papers  
**Also known as:** OOD robustness, OOD Robustness  

## State of the Field

Across the surveyed literature, out-of-distribution (OOD) robustness is consistently defined as a model's ability to maintain stable performance when evaluated on data from a distribution that differs from its training data. This is often framed as assessing generalization to "unusual or shifted data domains" ("MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models"). Some work further specifies the types of distributional differences, such as "input-level shift and semantic-level shift" ("CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models"). The construct is considered in contexts like Reinforcement Learning from Human Feedback (RLHF), where reward functions are queried with potentially out-of-distribution samples. To operationalize this construct, researchers in this set use the SST-2 benchmark. The concept is also studied in relation to `Safety` and `Reward overoptimization`.

## Sources

**[MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf) (as "OOD robustness")**
> The ability to maintain performance on unusual or shifted data domains that differ from training distribution.

**[Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf) (as "OOD Robustness")**
> The degree to which model performance remains stable when queried on samples potentially out-of-distribution relative to the training data.

**[CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A specific facet of robustness concerning the model's ability to handle test data whose distributions significantly differ from the training data, including input-level and semantic-level shifts.

## Relationships

### Out-of-distribution robustness →
- **SST-2** (measurements) — *measured_by*
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Robustness** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reward overoptimization** (constructs)
  - [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf)

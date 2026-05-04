# TACRED
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, TACRED is consistently characterized as a large-scale benchmark dataset used to evaluate relation extraction (RE), a task within the broader domain of information extraction. The dataset is frequently described as being derived from the Text Analysis Conference (TAC) Knowledge Base Population (KBP) challenges, with sources specifying it is an English dataset containing 42 distinct relations from news and web text. In experimental settings, TACRED is commonly used to assess model performance, often alongside other benchmarks like FewRel and SemEval. Researchers employ it in various configurations, including few-shot setups, as one paper notes a "5-way 5-shot" evaluation. While its prevailing use is for RE, a less common application involves converting the dataset to a slot filling task "to increase the complexity of the task". Additionally, one paper mentions the existence of variants such as TACRED-Revisit and Re-TACRED.

## Sources

**[BayesPrompt: Prompting Large-Scale Pre-Trained Language Models on Few-shot Inference via Debiased Domain Abstraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/5fcfda9e2a28c62f1ba54bcfa09ebdbc-Paper-Conference.pdf)**
> A large-scale benchmark dataset for relation extraction, derived from the annual Text Analysis Conference (TAC) Knowledge Base Population (KBP) challenges.

## Relationships

### → TACRED
- **Information extraction** (behaviors tasks) — *measured_by*
  > “We conducted experiments on SemEval and three versions of TACRED: SemEval 2010 Task 8 (SemEval) (Hendrickx et al., 2010), TACRED (Zhang et al., 2017), TACRED-Revisit (Alt et al., 2020), Re-TACRED (Stoica et al., 2021).”
  - [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.70.pdf)

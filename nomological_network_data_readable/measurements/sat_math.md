# SAT-Math
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, SAT-Math is a measurement instrument used to evaluate mathematical reasoning in language models. It is defined as a dataset of standardized test math problems from the SAT exam, with evidence from one paper specifying the content consists of problems from the U.S. high-school curriculum. The primary construct it is used to assess is mathematical reasoning, though one paper also includes it under the broader category of scientific reasoning for "English math". Several papers use SAT-Math as a downstream evaluation task, often in conjunction with other math problem-solving datasets like GSM8K, MATH, and AQuA-RAT. As one source snippet notes, performance on these benchmarks can be averaged to represent an overall result for the "math domain". The performance metric associated with this dataset in the provided data is Accuracy (Acc).

## Sources

**[LACA: Improving Cross-lingual Aspect-Based Sentiment Analysis withLLMData Augmentation](https://aclanthology.org/2025.acl-long.42.pdf)**
> Standardized test math problems from the SAT exam, used to evaluate mathematical reasoning under standardized conditions.

## Relationships

### → SAT-Math
- **Mathematical reasoning** (constructs) — *measured_by*
  > the performance for the math domain is the average result of GSM8K (Pass@1) (Cobbe et al., 2021), MATH (Pass@1) (Hendrycks et al., 2021), SAT-Math (Acc) (Zhong et al., 2023), and AQuA-RAT (Acc) (Ling et al., 2017) datasets. (Figure 1)
  - [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2c570b0f9938c7a58a612e5b00af9cc0-Paper-Conference.pdf)

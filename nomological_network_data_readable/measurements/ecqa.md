# ECQA
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, ECQA is consistently presented as a dataset for question answering, though its full name varies slightly, including 'Explainable CommonsenseQA', 'Explanations from Commonsense Knowledge Acquisition', and 'Explanation-based Commonsense Question Answering'. Papers use ECQA to measure both `Commonsense understanding` and `Question answering`. A defining feature mentioned across multiple sources is that the dataset requires models to provide explanations for their answers, not just the final answer. One paper further specifies that it is a 'knowledge QA dataset with Chain-of-Thought (CoT) reasoning' used to evaluate a model's knowledge and reasoning abilities. Its most common application appears to be as an evaluation benchmark for 'explainable commonsense reasoning'. Beyond evaluation, some papers report using ECQA as a source for constructing fine-tuning datasets or as a pre-training task.

## Sources

**[Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)**
> The Explainable CommonsenseQA dataset, which requires models to not only answer commonsense questions but also provide explanations for their answers.

## Relationships

### → ECQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Bridging and Modeling Correlations in Pairwise Data for Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d41760ec1e2db105e63e98393648c763-Paper-Conference.pdf)

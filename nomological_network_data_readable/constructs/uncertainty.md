# Uncertainty
**Type:** Construct  
**Referenced in:** 19 papers  

## State of the Field

Across the surveyed literature, Uncertainty is most commonly characterized as the degree to which a model's predictions are unreliable, ambiguous, or reflect a lack of confidence. This is frequently linked to the general unreliability of model generations, sometimes discussed alongside phenomena like hallucinations. The field operationalizes this construct in several ways, with a prevalent approach being the measurement of entropy in the model's output probability distribution. Other methods include assessing the variability of answers across multiple stochastic generations for the same prompt or identifying specific output patterns, such as when a model's score is close to an ambiguous threshold or it produces a high proportion of 'MAYBE' labels. Some work frames uncertainty as an internal state, noting that these states "carry a lot of information about their uncertainty" ("Cascading Large Language Models for Salient Event Graph Generation"). This construct is often used in active learning to select informative samples for which the model has the most doubt. A more distinct application, found in one paper, treats uncertainty as an indicator of information content within model components to guide model compression. The quantification of uncertainty is also described as a "prominent approach for eliciting truthful answers from large language models" ("Cascading Large Language Models for Salient Event Graph Generation").

## Sources

**[Learnability Matters: Active Learning for Video Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/43069caa6776eac8bca4bfd74d4a476d-Paper-Conference.pdf)**
> The degree to which the model's predictions are unreliable or ambiguous for a given video sample.

## Relationships

### Uncertainty →
- **Conformal Prediction** (measurements) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)

### → Uncertainty
- **Hallucination** (behaviors tasks) — *correlates*
  - [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf)
- **Pairwise comparison** (behaviors tasks) — *causes*
  - [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf)
- **Conformity** (constructs) — *correlates*
  - [Enhancing Character-Level Understanding inLLMs through Token Internal Structure Learning](https://aclanthology.org/2025.acl-long.195.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Consistency** (constructs)
  - [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behaviors tasks)
  - [FactTest: Factuality Testing in Large Language Models with Finite-Sample and Distribution-Free Guarantees](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25a/nie25a.pdf)
- **Sparsity** (constructs)
  - [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.209.pdf)

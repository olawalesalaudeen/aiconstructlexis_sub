# Reasoning quality
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

Within the provided literature, reasoning quality is characterized as the degree to which a model's chain-of-thought process is logically valid, accurate, and comprehensive in its steps. The paper introducing this definition operationalizes the construct through two specific metrics: Recall, which is used to quantify 'reasoning informativeness' by checking for ground-truth solution steps, and Precision, which measures 'faithfulness' by evaluating the accuracy of generated steps. Other work also operationalizes reasoning quality using measurement instruments like `Process Reward Models`, with `Math-Shepherd` cited as one example, and through more general `LLM-based evaluation`. The construct is positioned within a causal network where it is reported to be influenced by `Self-reflection` and, in turn, is suggested to affect `Sampling efficiency`.

## Sources

**[MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)**
> The degree to which a model's chain-of-thought process is logically valid, accurate, and comprehensive in its steps.

## Relationships

### Reasoning quality →
- **Sampling efficiency** (constructs) — *causes*
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.184.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
- **Math-Shepherd** (measurements) — *measured_by*
  > To evaluate the generalization of SpecSearch across thought evaluators, we test it with two PRMs—Math-Shepherd (Wang et al., 2024c) and MATH-psa (Wang et al., 2024a)—on beam search. (Section 5)
  - [Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf)
- **Process Reward Model** (measurements) — *measured_by*
  - [Accelerating Large Language Model Reasoning via Speculative Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25di/wang25di.pdf)

### → Reasoning quality
- **Self-reflection** (behaviors tasks) — *causes*
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)

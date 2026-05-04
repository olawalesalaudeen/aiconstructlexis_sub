# Min-K%
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided sources, Min-K% is consistently defined as a type of membership inference attack. The method operates by averaging the losses of the k% least likely tokens, which are those with the highest loss values. This technique is explicitly based on the assumption "that non-members contain more high-loss outliers" ("Confounding Factors in Relating Model Performance to Morphology"). As an instrument, Min-K% is used to measure the construct of `Privacy leakage`. The provided data also indicates a relationship between Min-K% and the "Min-K% method".

## Sources

**[Confounding Factors in Relating Model Performance to Morphology](https://aclanthology.org/2025.emnlp-main.370.pdf)**
> A membership inference attack that averages the losses of the k% least likely tokens (highest loss) under the assumption that non-members contain more high-loss outliers.

## Relationships

### → Min-K%
- **Privacy leakage** (behaviors tasks) — *measured_by*
  - [Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf)

### Associated with
- **Min-K% method** (measurements)
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)

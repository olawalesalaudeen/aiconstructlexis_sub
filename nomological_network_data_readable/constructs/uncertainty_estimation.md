# Uncertainty estimation
**Type:** Construct  
**Referenced in:** 9 papers  
**Also known as:** Epistemic uncertainty  

## State of the Field

Across the surveyed literature, uncertainty estimation is most commonly framed as a model's ability to assess the reliability of its own outputs or, relatedly, its degree of confidence in a prediction. A more specific, technical framing defines it as 'epistemic uncertainty,' reflecting a lack of knowledge within the model's parameters. The construct is operationalized in several ways, including by calculating the entropy over multiple sampled answers, inferring it from internal probability distributions, or measuring it via Conformal Prediction. This assessment is used to inform model behavior; for example, one paper uses it to 'guide adaptive decision-making in reasoning processes' by determining if more complex exploration is needed. Uncertainty estimation is frequently studied in connection with undesirable model behaviors, as it is shown to correlate with both Hallucination and Conformity. One study explicitly finds that 'LLMs are more likely to conform when they are more uncertain in their own prediction.' The construct is also studied alongside Faithfulness and Consistency and is reported to influence Out-of-distribution detection.

## Sources

**[ExtendingLLMContext Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.29.pdf)**
> The model's ability to assess the reliability of its own reasoning outputs, typically through measures like entropy over multiple sampled answers, to guide adaptive decision-making in reasoning processes.

**[Enhancing Character-Level Understanding inLLMs through Token Internal Structure Learning](https://aclanthology.org/2025.acl-long.195.pdf) (as "Uncertainty")**
> The degree to which a model lacks confidence in its own prediction, inferred from its internal probability distribution or consistency across generations, which increases its susceptibility to external influence.

**[GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.256.pdf) (as "Epistemic uncertainty")**
> Model-specific uncertainty reflecting the lack of knowledge within the LLM’s parameters, related to the gap between parametric and universal knowledge boundaries.

## Relationships

### Uncertainty estimation →
- **Out-of-distribution detection** (behaviors tasks) — *causes*
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)

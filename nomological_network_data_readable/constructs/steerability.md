# Steerability
**Type:** Construct  
**Referenced in:** 7 papers  

## State of the Field

Based on the provided literature, Steerability is defined as the ability to control or direct model predictions by modifying an 'input value profile.' The primary usage of this concept is to enable the simulation of diverse perspectives; as one paper notes, this allows a model to act as a 'jury' of annotators whose 'predictions change in line with semantic profile differences' ('F²Bench: An Open-ended Fairness Evaluation Benchmark forLLMs with Factuality Considerations'). The construct is operationalized and measured using the STEER-BENCH benchmark, which is explicitly designed to 'evaluate population-specific steering in LLMs.' In the network of relationships presented, Steerability is positioned as an outcome of `Interpretability and explainability` in one paper. Another source reports that it can, in turn, cause `Harmful content generation`.

## Sources

**[F²Bench: An Open-ended Fairness Evaluation Benchmark forLLMs with Factuality Considerations](https://aclanthology.org/2025.emnlp-main.106.pdf)**
> The ability to control or direct model predictions by modifying the input value profile, enabling simulation of diverse perspectives.

## Relationships

### Steerability →
- **Harmful content generation** (behaviors tasks) — *causes*
  - [Metadata Conditioning Accelerates Language Model Pre-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25p/gao25p.pdf)
- **STEER-BENCH** (measurements) — *measured_by*
  > we introduce STEER-BENCH, a benchmark designed to evaluate population-specific steering in LLMs. (Section 1)
  - [Unsupervised Word-level Quality Estimation for Machine Translation Through the Lens of Annotators (Dis)agreement](https://aclanthology.org/2025.emnlp-main.925.pdf)

### → Steerability
- **Interpretability and explainability** (constructs) — *causes*
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)

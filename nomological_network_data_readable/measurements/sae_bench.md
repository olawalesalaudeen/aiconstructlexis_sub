# SAE Bench
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** SAEBench  

## State of the Field

SAE Bench is consistently described across the provided literature as an evaluation suite or benchmark for assessing the performance of sparse autoencoders (SAEs). The instrument is used to measure a wide range of SAE-specific metrics, with papers listing capabilities such as feature absorption, probing, concept isolation, spurious correlation removal, and automated interpretability. The provided data explicitly states that SAE Bench is used to measure the construct of `Interpretability and explainability`, with one source noting its evaluations also span `feature disentanglement` and `practical applications like unlearning`. In practice, researchers use the benchmark to compare different SAE architectures, such as Matryoshka SAEs versus baseline SAEs, and to evaluate models that incorporate SAEs. One paper characterizes it as a benchmark of metrics that are "faithful to possible real world use cases," highlighting an applied focus. The suite provides a standardized way to evaluate SAEs across multiple tasks and models.

## Sources

**[Learning Multi-Level Features with Matryoshka Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bussmann25a/bussmann25a.pdf)**
> Evaluation suite for sparse autoencoders that includes metrics for feature absorption, splitting, composition, probing, and concept isolation across multiple tasks and models.

**[Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf) (as "SAEBench")**
> SAEBench, a benchmark suite for evaluating sparse autoencoders on downstream SAE-specific metrics such as spurious correlation removal, targeted probe perturbation, sparse probing, automated interpretability, and feature absorption.

## Relationships

### → SAE Bench
- **Interpretability and explainability** (constructs) — *measured_by*
  > To address the core challenge of measuring how effectively a model and SAE work together, Karvonen et al. (2024) introduce SAEBench, a benchmark of SAE metrics that are faithful to possible real world use cases. (Section 5.1)
  - [Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/leask25a/leask25a.pdf)

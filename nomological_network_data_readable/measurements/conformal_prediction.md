# Conformal Prediction
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Conformal prediction  

## State of the Field

Across the provided literature, Conformal Prediction is consistently framed as a method for uncertainty quantification. It is described as a technique that constructs a set of outputs or a prediction interval with a statistically guaranteed probability of containing the correct answer. Several sources characterize it as a model-agnostic, distribution-free, and post-hoc method, making it applicable to black-box LLMs. As a measurement instrument, Conformal Prediction is used to operationalize both `Uncertainty estimation` and `Evaluation`. This usage is supported by one study which notes it is "a promising way to quantify the uncertainty of an LLM judge" (Interdisciplinary Research in Conversation: A Case Study in Computational Morphology for Language Documentation). The method is also reported to be used to improve reliability in generation and is studied in relation to `Faithfulness`.

## Sources

**[GradOT: Training-free Gradient-preserving Offsite-tuning for Large Language Models](https://aclanthology.org/2025.acl-long.256.pdf)**
> A method that quantifies uncertainty by identifying a set of outputs with a guaranteed probability of containing the correct answer, applicable to black-box LLMs and used to improve reliability in generation.

**[Interdisciplinary Research in Conversation: A Case Study in Computational Morphology for Language Documentation](https://aclanthology.org/2025.emnlp-main.569.pdf) (as "Conformal prediction")**
> A distribution-free, post-hoc uncertainty quantification method that constructs prediction intervals with statistically guaranteed coverage for LLM-based evaluations.

## Relationships

### → Conformal Prediction
- **Uncertainty** (constructs) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Can Transformers Do Enumerative Geometry?](https://proceedings.iclr.cc/paper_files/paper/2025/file/aee2f03ecb2b2c1ea55a43946b651cfd-Paper-Conference.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)

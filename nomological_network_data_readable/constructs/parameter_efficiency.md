# Parameter efficiency
**Type:** Construct  
**Referenced in:** 30 papers  
**Also known as:** Parametric efficiency  

## State of the Field

Across the surveyed literature, parameter efficiency is predominantly defined as a model's ability to achieve high performance while updating a minimal fraction of its parameters during fine-tuning. This is frequently operationalized through methods like low-rank adaptations and modular designs, with some studies reporting updates to as little as "less than 1% of the... model parameters" ("Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE for Instruction Tuning"). The construct is measured by assessing performance on benchmarks like GLUE and SuperGLUE, where a method might achieve "comparable performance... while using only half the parameters" of another approach ("AID: Adaptive Integration of Detectors for SafeAIwith Language Models"). A less common framing expands the concept beyond fine-tuning to include overall model size for "efficient deployment on memory-constrained devices" ("Direct Preference Optimization of Video Large Multimodal Models from Language Model Reward"). A single paper uses the term "parametric efficiency" to refer to a smaller model's performance when augmented with non-parametric techniques like retrieval. Parameter efficiency is often discussed in relation to a model's "expressive power," suggesting a potential trade-off. Some work also proposes that integrating mechanisms for relational reasoning can lead to gains in parameter efficiency.

## Sources

**[Breaking Physical and Linguistic Borders: Multilingual Federated Prompt Tuning for Low-Resource Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e9034dd5420660d86c8c360c35a895e-Paper-Conference.pdf)**
> The property of a model to achieve high performance while updating a minimal number of parameters during fine-tuning, often through low-rank or modular designs.

**[Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf) (as "Parametric efficiency")**
> The model's performance relative to its number of parameters, particularly the ability of a smaller model to achieve high performance through non-parametric means like retrieval.

## Relationships

### Parameter efficiency →
- **GLUE** (measurements) — *measured_by*
  > Our method achieves comparable performance to LoRA on the General Language Understanding Evaluation (GLUE) benchmark while using only half the parameters. (Section 1)
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **SuperGLUE** (measurements) — *measured_by*
  > We extended our evaluation to the more challenging SuperGLUE benchmark... SSMLoRA achieves comparable or superior performance across most tasks while utilizing only half the parameters of traditional approaches. (Section 4.6)
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)

### → Parameter efficiency
- **Relational reasoning** (constructs) — *causes*
  > Our results demonstrate that integrating explicit relational computational mechanisms into the Transformer architecture leads to significant performance gains in terms of data efficiency and parameter efficiency. (Section 1)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)

### Associated with
- **Expressive power** (constructs)
  > frequency-domain decomposition with carefully selected frequency components can surpass the expressivity of traditional low-rank-based methods
  - [SLTrain: a sparse plus low rank approach for parameter and memory efficient pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/d63cf0622eed012a17fe88fced64dcb8-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks)
  - [Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf)

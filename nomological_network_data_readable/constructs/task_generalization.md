# Task generalization
**Type:** Construct  
**Referenced in:** 30 papers  
**Also known as:** Cross-task generalization, Multi-task generalization, General task-solving ability, Single-task generalization, Generalization to new tasks, Generalization to unseen tasks, Task-level generalization, Unseen task generalization, Cross-task knowledge transfer  

## State of the Field

Across the surveyed literature, Task generalization is most commonly described as a model's capacity to perform effectively on new or unseen tasks that were not included in its training or fine-tuning data. This ability is frequently characterized by the transfer of learned capabilities to different tasks, domains, or data distributions, often without requiring task-specific retraining, a condition specified in definitions of 'Cross-task generalization' and 'Generality'. While the core idea of performing on unseen tasks is consistent, usage varies: 'Multi-task generalization' often refers to maintaining performance across a diverse set of tasks within a unified architecture, whereas 'Task-level generalization' is used in the context of robotic policies adapting to novel simulation scenarios. A less common framing, 'Single-task generalization', diverges from this by focusing on a model's performance on a single, specific task after parameter-efficient fine-tuning. To operationalize this construct, researchers evaluate models on broad, multi-task benchmarks. For instance, the MMLU benchmark, which covers 57 distinct tasks, is explicitly used to measure a model's 'general task-solving abilities' and performance on 'previously unseen tasks'. The construct is also studied in relation to other phenomena, with some work positing that it is influenced by factors such as 'Parameter interference' and 'Trajectory retrieval'.

## Sources

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)**
> The capacity of the model to transfer learned capabilities across a wide variety of distinct image-processing tasks without task-specific fine-tuning.

**[LLMs as Zero-shot Graph Learners: Alignment of GNN Representations with LLM Token Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b77d3a82b59e9d9899370b378087faf-Paper-Conference.pdf) (as "Cross-task generalization")**
> The ability of a model trained on a specific source task, such as node classification, to perform well on a different, unseen target task, such as link prediction, without additional fine-tuning.

**[GenRL: Multimodal-foundation world models for generalization in embodied agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/3076133f08b40607d00a8f48f6acd71c-Paper-Conference.pdf) (as "Multi-task generalization")**
> The ability of an embodied agent to adapt learned behavior to new tasks across domains and prompts beyond the training distribution.

**[Large Language and Protein Assistant for Protein-Protein Interactions Prediction](https://aclanthology.org/2025.acl-long.555.pdf) (as "General task-solving ability")**
> The model's preserved competence across diverse domains and tasks beyond the specific one it has been fine-tuned on, reflecting robustness and transferability.

**[Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25c/zhuang25c.pdf) (as "Single-task generalization")**
> The ability of a model to perform well on a single, specific downstream task after parameter-efficient fine-tuning.

**[Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf) (as "Generality")**
> The ability of a method or model to perform effectively across a variety of different datasets and task types without task-specific training.

**[GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/143ea4a156ef64f32d4d905206cf32e1-Paper-Conference.pdf) (as "Task-level generalization")**
> The latent ability of a robotic policy to perform well on unseen tasks after training on a diverse set of simulation tasks, reflecting broad conceptual understanding rather than overfitting to specific instances.

**[Instructive Decoding: Instruction-Tuned Large Language Models are Self-Refiner from Noisy Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f5c76187c28e8d9d3b938d0c504436c-Paper-Conference.pdf) (as "Unseen task generalization")**
> The model's ability to perform effectively on tasks that were not part of its training set, based only on provided instructions.

**[Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE for Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/6d00071564ec447466fc4577743cf1b3-Paper-Conference.pdf) (as "Generalization to unseen tasks")**
> The model's ability to perform well on tasks and task categories that were not included in its fine-tuning data.

**[In-Context Learning through the Bayesian Prism](https://proceedings.iclr.cc/paper_files/paper/2024/file/d81cd83e7f6748af351485d73f305483-Paper-Conference.pdf) (as "Generalization to new tasks")**
> The ability to perform well on function classes not seen during pretraining, which arises when the pretraining task distribution is sufficiently diverse and represents a deviation from strict Bayesian prediction.

**[LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/27e5626cabdbb6cd5c56ce4114ff93e4-Paper-Conference.pdf) (as "Cross-task knowledge transfer")**
> The ability of a model to leverage information learned from a set of source tasks to improve learning and performance on new, unseen target tasks.

## Relationships

### Task generalization →
- **MMLU** (measurements) — *measured_by*
  > We further evaluate the LLMs before and after M2MS instruction tuning on the MMLU evaluation dataset (Hendrycks et al., 2021). The MMLU dataset covers 57 tasks including elementary mathematics, US history, computer science, law, etc, and is designed to evaluate models’ world knowledge and problem-solving ability. (Section 6)
  - [Rethinking Channel Dimensions to Isolate Outliers for Low-bit Weight Quantization of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/374050dc3f211267bd6bf0ea24eae184-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **MathQA** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)

### → Task generalization
- **Trajectory retrieval** (behaviors tasks) — *causes*
  - [Enhancing Language Model Agents using Diversity of Thoughts](https://proceedings.iclr.cc/paper_files/paper/2025/file/737ab809016b2c79086374f9c8a11831-Paper-Conference.pdf)
- **Parameter interference** (constructs) — *causes*
  - [Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf)
- **Chain-of-thought reasoning** (constructs) — *causes*
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)

### Associated with
- **Instruction following** (constructs)
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks)
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
- **Compositional generalization** (constructs)
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)

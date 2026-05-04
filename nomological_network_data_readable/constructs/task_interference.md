# Task interference
**Type:** Construct  
**Referenced in:** 13 papers  
**Also known as:** Negative transfer, Tool knowledge deletion, In-context interference, Inter-task interference  

## State of the Field

Task interference is most commonly described as a phenomenon where a model's performance on certain tasks degrades due to conflicting signals from handling multiple capabilities. This construct is frequently studied in two primary settings: multi-task learning, where models are trained jointly on diverse tasks, and model merging, where separately fine-tuned models are combined. While several papers use the term "task interference," related labels such as "negative transfer" and "parameter interference" are also used to describe this performance degradation. A smaller line of work applies the concept to more specific scenarios, such as "in-context interference," where performance deteriorates with an increasing number of in-context demonstrations, or "tool knowledge deletion," which frames it as the targeted removal of a capability. The construct is primarily operationalized by observing performance degradation on tasks when they are trained or merged with others. One paper suggests measuring it via "changes in internal activations induced by merging" ("No Task Left Behind"). Some work posits that interference is caused by a failure of "weight disentanglement," where fine-tuning modifies parameters that are critical for other tasks. The concept is also studied alongside "Catastrophic forgetting" and "Knowledge forgetting".

## Sources

**[MoME: Mixture of Multimodal Experts for Generalist Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4a3a14b9536806a0522930007c5512f7-Paper-Conference.pdf)**
> A latent phenomenon in multi-task learning where a model's performance on certain tasks degrades due to conflicting learning signals from being trained on a diverse mixture of other tasks.

**[Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf) (as "Negative transfer")**
> A phenomenon where training on diverse or unrelated tasks or data instances leads to a degradation in model performance, as opposed to synergistic learning.

**[Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf) (as "Tool knowledge deletion")**
> The latent ability of a model to fully remove its internalized capability to use specific tools, such that it behaves as if it had never learned them.

**[Whoever Started the interference Should End It: Guiding Data-Free Model Merging via Task Vectors](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25h/cheng25h.pdf) (as "Parameter interference")**
> A latent phenomenon in model merging where parameter conflicts between different source models cause performance degradation in the final unified model.

**[No Task Left Behind: Isotropic Model Merging with Common and Task-Specific Subspaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/marczak25a/marczak25a.pdf) (as "Inter-task interference")**
> The phenomenon where the process of learning or combining capabilities for one task negatively impacts performance on other tasks within a multi-task model.

**[LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ruoss25a/ruoss25a.pdf) (as "In-context interference")**
> The latent tendency for model performance to degrade as the number of in-context demonstrations increases, due to suboptimal action selection rather than format errors.

## Relationships

### → Task interference
- **Weight disentanglement** (constructs) — *causes*
  > Task interference occurs when fine-tuning modifies parameters that are critical to other tasks, resulting in unintended behavioral shifts. To prevent this, data from disjoint regions in the input space (representing different tasks) should affect only their corresponding regions in the activation space. Ortiz-Jimenez et al. (2023) formalized this concept as weight disentanglement. (Section 1)
  - [Efficient Model Editing with Task-Localized Sparse Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/96f5de31e8e3d19cbcd3a7397b8dce57-Paper-Conference.pdf)

### Associated with
- **Catastrophic forgetting** (behaviors tasks)
  - [LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [Merge then Realign: Simple and Effective Modality-Incremental Continual Learning for MultimodalLLMs](https://aclanthology.org/2025.emnlp-main.666.pdf)

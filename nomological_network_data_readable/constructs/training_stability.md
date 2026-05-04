# Training stability
**Type:** Construct  
**Referenced in:** 22 papers  
**Also known as:** Training dynamics stability, Training instability  

## State of the Field

Across the surveyed literature, training stability is predominantly defined as a property of the training process characterized by smooth convergence and the absence of divergent behaviors. The most common framing, found in numerous papers, centers on avoiding issues like loss spikes, escalating gradient norms, and the frequent need for interventions such as gradient clipping. This construct is operationalized by observing several indicators of its inverse, instability, which include sudden increases in KL divergence, oscillating training curves, and performance degradation on the training set itself. Conversely, stability is evidenced by consistent increases in reward, stable value predictions in reinforcement learning, and loss curves that decline smoothly, as one paper notes, "The loss of ‘Zero-initialized’ declines much faster at the beginning, and finally converges to zero" (LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention). This concept is applied across various contexts, including pre-training, fine-tuning, and reinforcement learning with human feedback. A less common, more mechanistic definition treats stability as the degree to which internal model states like activations, gradients, and weight updates remain well-scaled. Papers frequently investigate how stability is affected by choices of optimizers, initialization strategies, regularization techniques, and finetuning methods like LoRA.

## Sources

**[$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf)**
> The property of the training process characterized by smooth convergence and infrequent need for interventions like gradient clipping to prevent divergence or loss spikes.

**[Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf) (as "Training dynamics stability")**
> The degree to which activations, gradients, and weight updates remain well-scaled and do not vanish or explode as sparsity or width changes.

**[People who frequently useChatGPTfor writing tasks are accurate and robust detectors ofAI-generated text](https://aclanthology.org/2025.acl-long.268.pdf) (as "Training instability")**
> A phenomenon during model training characterized by issues like loss spikes, escalating gradient norms, and divergent updates, which hinder effective model convergence.

## Relationships

### → Training stability
- **Knowledge retention** (constructs) — *causes*
  - [CPPO: Continual Learning for Reinforcement Learning with Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf)
- **Slow thinking** (constructs) — *causes*
  - [PKU-SafeRLHF: Towards Multi-Level Safety Alignment forLLMs with Human Preference](https://aclanthology.org/2025.acl-long.1545.pdf)

### Associated with
- **Generalization** (constructs)
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)

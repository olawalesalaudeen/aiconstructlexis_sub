# Weak-to-strong generalization
**Type:** Construct  
**Referenced in:** 15 papers  
**Also known as:** Weak to strong generalization, Weak-to-Strong generalization, Weak-to-strong transition  

## State of the Field

The prevailing framing of weak-to-strong generalization across the provided literature is a phenomenon where a more capable model surpasses the performance of a weaker supervisor after being trained on data labeled by that weaker model. This construct is operationalized through a specific training setup where, as one paper puts it, "weak supervision from weak models can effectively stimulate the potential of the stronger model" to generalize beyond the supervisor's knowledge (`Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization`). Most sources describe the goal as the strong model learning the "task’s intent and rules" rather than merely replicating the weak model's outputs (`Weak to Strong Generalization for Large Language Models with Multi-capabilities`). Some papers frame this as the strong model's ability to "recover its full capabilities," though it is also noted that "errors in weak labels limit the performance" (`Bayesian WeakS-to-Strong from Text Classification to Generation`). A distinct, minority framing appears as "Weak-to-strong transition," defining it as the latent potential of underperforming models to become top performers through "collaborative search" rather than direct supervision (`Model Swarms...`). The construct is studied alongside `Generalization` and `Self-correction`. It is also reported to have an inverse correlation with `Model similarity`, where greater similarity between the weak supervisor and the initial strong model is associated with less performance improvement from the training.

## Sources

**[Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)**
> The phenomenon where training on weaker demonstrations or weaker supervision still yields performance above the weak source policy.

**[Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf) (as "Weak to strong generalization")**
> The ability of a more powerful model to learn a task and surpass the performance of a weaker supervisor model by training on data labeled by that weaker model.

**[Bayesian WeakS-to-Strong from Text Classification to Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/495e55f361708bedbab5d81f92048dcd-Paper-Conference.pdf) (as "Weak-to-Strong generalization")**
> The ability of a stronger model to recover its full capabilities when supervised only by the labels from a weaker, less capable model.

**[Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf) (as "Weak-to-strong transition")**
> The latent potential of initially underperforming LLM experts to become top-performing models through collaborative search, indicating untapped or implicit expertise.

## Relationships

### → Weak-to-strong generalization
- **Model similarity** (constructs) — *correlates*
  > for all model combinations, similarity between the weak supervisor and initial strong student inversely correlates with the improvement obtained from weak-to-strong training (r = −0.85). (Section 4.2)
  - [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf)

### Associated with
- **Generalization** (constructs)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Critique** (behaviors tasks)
  - [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf)

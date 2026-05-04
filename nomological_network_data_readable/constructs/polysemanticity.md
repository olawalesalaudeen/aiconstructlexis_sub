# Polysemanticity
**Type:** Construct  
**Referenced in:** 10 papers  
**Also known as:** Neuronal entanglement, Feature superposition, Semantic multimodality  

## State of the Field

Across the surveyed literature, polysemanticity is most commonly defined as the phenomenon where individual neurons in a neural network activate in multiple, semantically distinct and unrelated contexts. This concept is sometimes extended beyond neurons to other model components, with one study identifying an "interpretably polysemantic attention head" that implements multiple functions (Successor Heads: Recurring, Interpretable Attention Heads In The Wild). The most frequently cited consequence of polysemanticity is that it hinders mechanistic interpretability, with multiple papers framing it as a "central obstacle" to understanding model internals and identifying disentangled features. A smaller set of papers introduces related concepts, such as "feature superposition," where a model represents more features than its dimensions allow, and "neuronal entanglement," described as a "manifestation of polysemanticity" (Wasserstein Distances, Neuronal Entanglement, and Sparsity). While direct measurement instruments for polysemanticity are not detailed, one paper proposes modeling it as an "OR of different concepts" (Evaluating Neuron Explanations: A Unified Framework with Sanity Checks). Beyond its widely discussed relationship with interpretability, polysemanticity is also linked to redundancy, with one source suggesting it enables efficient and robust representations that "maximize the model’s capacity" (EmoAgent: Assessing and Safeguarding Human-AIInteraction for Mental Health Safety).

## Sources

**[Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf)**
> The phenomenon where individual neurons in a neural network activate in multiple, semantically distinct contexts, hindering interpretability.

**[Mechanistic Permutability: Match Features Across Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/d1422213c9f2bdd5178b77d166fba86a-Paper-Conference.pdf) (as "Feature superposition")**
> The latent property that a model represents more features than its hidden dimensions can uniquely encode, causing features to be entangled in a non-orthogonal basis.

**[Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf) (as "Neuronal entanglement")**
> The degree to which a neuron must differentiate between similar input vectors and map them to different output values, a manifestation of polysemanticity.

**[ExLM: Rethinking the Impact of $\texttt[MASK]$ Tokens in Masked Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25q/zheng25q.pdf) (as "Semantic multimodality")**
> The degree to which a corrupted context leads to multiple plausible predictions for masked tokens, reflecting ambiguity in the model's learned semantic representations.

## Relationships

### Associated with
- **Interpretability and explainability** (constructs)
  > A central obstacle to mechanistic interpretability is polysemanticity, where individual neurons encode multiple, unrelated concepts (Olah et al., 2020). Specifically, we refer to the hidden neurons from the multi-layer perceptron (MLPs) in Transformers. Such polysemantic neurons lack clear, singular roles, making it difficult to identify disentangled features or factors in neural networks.
  - [Mixture of Experts Made Intrinsically Interpretable](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ag/yang25ag.pdf)
- **Mechanistic interpretability** (measurements)
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
- **Redundancy** (constructs)
  > Marshall and Kirchner (2024) connect information theory with polysemanticity where polysemantic code learned by LLMs is not only efficient but also favors redundancy for robustness (Fig. 2 of their paper).
  - [EmoAgent: Assessing and Safeguarding Human-AIInteraction for Mental Health Safety](https://aclanthology.org/2025.emnlp-main.595.pdf)

# Path patching
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** Path Patching  

## State of the Field

Across the provided literature, Path patching is consistently characterized as a causal intervention and mechanistic interpretability method for identifying influential components within a neural network. The technique operates by replacing, or "patching," the internal activations of specific components, most commonly attention heads, from a reference model run into a counterfactual run with a different input. By measuring the effect of this intervention on the final output, researchers aim to identify components with direct causal effects on model predictions. The prevailing use of path patching is to discover computational "circuits" and localize decision-making for various capabilities. For instance, papers report using it to find the circuits for indirect object identification and entity tracking, identify heads responsible for mathematical computation, and localize components for commonsense reasoning. It is also applied to measure the importance of components for phenomena like sycophancy and option symbol bias. Some sources describe it as a "more surgical variant of activation patching," and it is sometimes used in conjunction with other methods like logit attribution.

## Sources

**[Circuit Component Reuse Across Tasks in Transformer Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ffbfbcf4ad7304d57158b046525e46c-Paper-Conference.pdf)**
> A more surgical variant of activation patching used to discover circuits by intervening on specific paths within the model's computation graph.

**[Fine-Tuning Enhances Existing Mechanisms: A Case Study on Entity Tracking](https://proceedings.iclr.cc/paper_files/paper/2024/file/2082273791021571c410f41d565d0b45-Paper-Conference.pdf) (as "Path Patching")**
> A mechanistic interpretability method that identifies causal components in neural networks by measuring the effect of patching activations between different inputs, used here to discover the entity tracking circuit.

## Relationships

### Associated with
- **Sycophancy** (constructs)
  - [Causally Motivated Sycophancy Mitigation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a52b0d191b619477cc798d544f4f0e4b-Paper-Conference.pdf)
- **Logit attribution** (measurements)
  - [The Same but Different: Structural Similarities and Differences in Multilingual Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/edd00cead3425393baf13004de993017-Paper-Conference.pdf)

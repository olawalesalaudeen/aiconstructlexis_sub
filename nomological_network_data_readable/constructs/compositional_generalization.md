# Compositional generalization
**Type:** Construct  
**Referenced in:** 30 papers  

## State of the Field

Across the provided literature, compositional generalization is consistently defined as a model's capacity to generalize to novel combinations of familiar components, concepts, or skills that were not explicitly seen together during training. The components being combined are framed at various levels of granularity, ranging from linguistic elements like verbs and subjects to higher-level abilities such as image understanding and language generation. The construct is frequently operationalized in the context of semantic parsing and program synthesis, where models are evaluated on their ability to generate valid programs or derivations for new combinations of known structures. Measurement is conducted using specific evaluations like SKILL-MIX, which is designed to assess the ability to combine skills, and datasets like GroundCocoa, described as a "hard evaluation set to benchmark compositional generalization in LLMs." Other work operationalizes it in robotics by composing simple motor skills, or in agentic tasks by combining interactions across multiple GUIs and APIs. For example, one study frames it as the ability to perform "image-based poem writing even without having image-poem pairs in their training data" (MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models). While presented as a common type of generalization, some sources note that models still struggle with this capability and that performance can be "highly dependent on both architecture and task properties" (Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?).

## Sources

**[ExeDec: Execution Decomposition for Compositional Generalization in Neural Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/c43b2989b1ba055aa713a4abbe4a8b05-Paper-Conference.pdf)**
> The model's capacity to generalize its understanding to novel combinations of concepts (like verbs, subjects, and objects) that were not seen during training.

## Relationships

### Compositional generalization →
- **Generalization** (constructs) — *causes*
  - [MapNav: A Novel Memory Representation via Annotated Semantic Maps forVLM-based Vision-and-Language Navigation](https://aclanthology.org/2025.acl-long.639.pdf)
- **GrailQA** (measurements) — *measured_by*
  - [Certainty in Uncertainty: Reasoning over Uncertain Knowledge Graphs with Statistical Guarantees](https://aclanthology.org/2025.emnlp-main.442.pdf)

### → Compositional generalization
- **In-context learning** (constructs) — *causes*
  - [Attention as a Hypernetwork](https://proceedings.iclr.cc/paper_files/paper/2025/file/abfa542f546df3c6c35695ec8d5bf4b9-Paper-Conference.pdf)

### Associated with
- **Multimodal understanding** (constructs)
  - [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/50623630a2372839c078474efa6c0cb8-Paper-Conference.pdf)
- **Safety alignment** (constructs)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **Abstract reasoning** (constructs)
  - [Attention as a Hypernetwork](https://proceedings.iclr.cc/paper_files/paper/2025/file/abfa542f546df3c6c35695ec8d5bf4b9-Paper-Conference.pdf)
- **Task generalization** (constructs)
  - [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf)
- **Robustness** (constructs)
  - [Coarse-to-Fine Grounded Memory forLLMAgent Planning](https://aclanthology.org/2025.emnlp-main.660.pdf)
- **Mathematical reasoning** (constructs)
  - [RLAE: Reinforcement Learning-Assisted Ensemble forLLMs](https://aclanthology.org/2025.emnlp-main.681.pdf)

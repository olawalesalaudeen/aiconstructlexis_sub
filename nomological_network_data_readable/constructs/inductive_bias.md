# Inductive bias
**Type:** Construct  
**Referenced in:** 16 papers  
**Also known as:** Geometric inductive bias  

## State of the Field

Across the surveyed literature, inductive bias is consistently defined as an inherent property of a model that predisposes it to favor certain solutions or generalizations over others. This property is most commonly attributed to a model's architecture, such as a 'looped transformer' or 'butterfly structure', as well as its training method or the use of pre-trained models. The construct is primarily operationalized by observing its influence on model behaviors, with a recurring focus on its relationship with generalization. For example, some papers argue that a desirable inductive bias 'improves its generalization abilities', and its effects can be revealed through performance on tasks like length generalization. While the connection to generalization is prevalent, inductive bias is also linked to commonsense knowledge and understanding, though these relationships are less detailed in the provided data. A specialized variant, 'geometric inductive bias', is described in the context of protein modeling as the capacity to capture spatial relationships. Despite its frequent discussion, some work notes that the specific inductive biases behind certain behaviors 'are not clearly understood', while other research questions whether common architectures truly encode 'distinctive' inductive biases.

## Sources

**[In-Context Learning through the Bayesian Prism](https://proceedings.iclr.cc/paper_files/paper/2024/file/d81cd83e7f6748af351485d73f305483-Paper-Conference.pdf)**
> An inherent property of a model or training method that causes it to prefer certain solutions or generalizations over others, influencing its performance on new tasks.

**[Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf) (as "Geometric inductive bias")**
> The model's inherent architectural capacity to capture spatial and geometric relationships among protein residues, such as pairwise distances and angular constraints, which are critical for accurate structure prediction.

## Relationships

### Inductive bias →
- **Generalization** (constructs) — *causes*
  > This suggests a desirable inductive bias of RAPTR that improves its generalization abilities beyond perplexity. (Section 4)
  - [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf)

### Associated with
- **Length generalization** (constructs)
  > The short validation set reveals an architecture’s inductive bias in the absence of any disambiguating information about how it should generalize to longer lengths, as in the experiments of Del´etang et al. (2023). (Section 4)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Generalization** (constructs)
  > Our results indicate that common LLM architectures and training setups might encode very similar inductive biases, freeing practitioners to optimize them for training efficiency without adversely affecting downstream generalization. (Section 1)
  - [LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mayilvahanan25a/mayilvahanan25a.pdf)
- **Commonsense understanding** (constructs)
  - [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf)

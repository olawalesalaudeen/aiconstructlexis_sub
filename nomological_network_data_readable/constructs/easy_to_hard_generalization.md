# Easy-to-hard generalization
**Type:** Construct  
**Referenced in:** 3 papers  
**Also known as:** Simple-to-hard generalization  

## State of the Field

The ability of a model to learn to solve difficult problems by training on solutions to simpler problems, without requiring direct supervision on the harder instances.

## Sources

**[Self-Improving Transformers Overcome Easy-to-Hard and Length Generalization Challenges](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25d/lee25d.pdf)**
> The ability of a model to learn to solve difficult problems by training on solutions to simpler problems, without requiring direct supervision on the harder instances.

**[Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf) (as "Simple-to-hard generalization")**
> The latent ability of a model to generalize from training on simpler instances of a task to performing well on more complex, unseen instances, particularly involving longer or more intricate reasoning chains.

## Relationships

### Associated with
- **Mathematical reasoning** (constructs)
  - [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf)
- **Length generalization** (constructs)
  > Our findings suggest that self-improvement is not limited to length generalization but also enables easy-to-hard generalization, where a model trained on simpler tasks successfully learns harder tasks without additional supervision. (Section 1)
  - [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf)
- **Modality imbalance** (constructs)
  > We observe that current models can S2H generalize on text – when trained to read short sequences from small LaTeX-formatted tables, the models can read longer paths from larger tables, also provided in LaTeX code. However, they fail to length-generalize on images. To address the generalization gap and imbalanced learning of different modalities, our goal is to transfer the generalization behavior from text to image modality. (Figure 1)
  - [Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25j/park25j.pdf)

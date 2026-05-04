# SlimPajama
**Type:** Measurement  
**Referenced in:** 25 papers  
**Also known as:** Slimpajama  

## State of the Field

Across the surveyed literature, SlimPajama is most commonly characterized as a large text corpus used as a data source for various stages of model development. The prevailing definition describes it as a pre-training data source, while a more specific, less frequent definition clarifies it as "a cleaned and deduplicated version of RedPajama" with diverse sources including C4, ArXiv, GitHub, and Books. Its primary application is in `Language model pre-training`, where it is used for both initial training and for "continual pre-training" to recover model performance after modifications. Several papers also use subsets of SlimPajama for post-training procedures, such as for "post-prune recovery," with data samples ranging from 0.5B to 10B tokens. One study leverages its categorical composition, selecting specific subsets like "StackExchange, Github Codes, ArXiv, and Book" to simulate different topic preferences. While primarily described as a training corpus in definitions and usage snippets, the provided relationship data also positions SlimPajama as a measurement instrument. In this capacity, it is reported as being used to measure the behaviors of `Language model pre-training`, `Language modeling`, and `Instruction fine-tuning`.

## Sources

**[Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)**
> A large text corpus used as the pre-training data source from which files are selected.

**[Beware of Calibration Data for Pruning Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ede933e10afa991a10b6f36b6522129-Paper-Conference.pdf) (as "Slimpajama")**
> A cleaned and deduplicated version of the RedPajama dataset, serving as a high-quality pre-training corpus with diverse sources.

## Relationships

### → SlimPajama
- **Language modeling** (behaviors tasks) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [On the Duality between Gradient Transformations and Adapters](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hennigen25a/hennigen25a.pdf)

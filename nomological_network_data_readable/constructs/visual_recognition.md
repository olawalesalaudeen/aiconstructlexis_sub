# Visual recognition
**Type:** Construct  
**Referenced in:** 12 papers  
**Also known as:** Object recognition, Attribute recognition  

## State of the Field

The most common framing of visual recognition in the provided literature is as a general ability to identify and classify elements such as objects and text within an image. Some work offers more specific definitions, focusing on the latent ability to distinguish objects in scenes, identify object properties like color and shape (termed "attribute recognition"), or recognize relevant landmarks before performing a task. This construct is operationalized and measured using several instruments; papers report using the AMBER, VTAB-1k, and FGVC benchmarks to evaluate it. One study provides a concrete operationalization, measuring visual recognition accuracy by a model's ability to recognize "the 4 cards from the input image" ("SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training"). Across the surveyed work, models are often described as having strong object and attribute recognition abilities, although one paper notes that "GPT4O struggles more with distinguishing colors than other attributes" ("Task Me Anything"). Visual recognition is frequently studied in relation to other concepts like visual grounding, object detection, and visual perception. One paper proposes a directional relationship, suggesting that visual recognition contributes to the broader capability of visual understanding.

## Sources

**[WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The general ability to identify and classify objects, text, and other elements within an image.

**[VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf) (as "Object recognition")**
> The latent ability to identify and distinguish objects in visual scenes.

**[Task Me Anything](https://proceedings.neurips.cc/paper_files/paper/2024/file/237ffa9a473eff1c66d085dba7f813ba-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Attribute recognition")**
> The latent ability of a model to identify the properties of objects, such as their color, material, shape, or state.

## Relationships

### Visual recognition →
- **Visual understanding** (constructs) — *causes*
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **AMBER** (measurements) — *measured_by*
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **VTAB-1k** (measurements) — *measured_by*
  > We evaluate WeGeFT on the VTAB-1k benchmark (Zhai et al., 2019) and the fine-grained visual classification (FGVC) benchmark...
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)
- **FGVC** (measurements) — *measured_by*
  > We evaluate WeGeFT on the VTAB-1k benchmark (Zhai et al., 2019) and the fine-grained visual classification (FGVC) benchmark...
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)

### Associated with
- **Visual grounding** (constructs)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Object detection** (behaviors tasks)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  - [Needle In A Video Haystack: A Scalable  Synthetic Evaluator for Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf)

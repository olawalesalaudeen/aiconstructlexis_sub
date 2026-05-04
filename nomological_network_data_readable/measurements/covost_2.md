# CoVoST 2
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** CoVoST2, CoVoST-2  

## State of the Field

Across the provided literature, CoVoST 2 is consistently characterized as a multilingual corpus or benchmark dataset for speech-to-text translation. It is primarily used to measure `Machine translation`, and is also reported as an instrument for evaluating `Speech recognition` and `Cross-lingual alignment`. The dataset serves a dual purpose in research, being used for both training and evaluating models, with some studies explicitly collecting data from its training and test splits. Its multilingual nature is a recurring feature; different papers report using it to translate English into multiple "typologically diverse languages," or focus on specific subsets like French-English and German-English. The corpus is described as being derived from Common Voice and is considered a "general-domain speech translation benchmark." The specific language configurations vary, with one study selecting 14 non-English languages to pair bidirectionally with English, creating 28 distinct translation directions.

## Sources

**[SpaRE: Enhancing Spatial Reasoning in Vision-Language Models with Synthetic Data](https://aclanthology.org/2025.acl-long.388.pdf)**
> A benchmark dataset for evaluating speech-to-text translation, containing English speech examples to be translated into multiple typologically diverse languages.

**[An Empirical Study of Many-to-Many Summarization with Large Language Models](https://aclanthology.org/2025.acl-long.556.pdf) (as "CoVoST2")**
> A large-scale multilingual speech-to-text translation corpus (Common Voice Speech-to-Text) used for training and evaluating speech translation models.

**[Glider: Global and Local Instruction-Driven Expert Router](https://aclanthology.org/2025.emnlp-main.320.pdf) (as "CoVoST-2")**
> A multilingual speech-to-text translation corpus derived from Common Voice, used in the CoVoGER benchmark to generate N-best lists for 28 source-target language directions.

## Relationships

### → CoVoST 2
- **Machine translation** (behaviors tasks) — *measured_by*
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **Speech recognition** (behaviors tasks) — *measured_by*
  - [The Power of Many: Multi-Agent Multimodal Models for Cultural Image Captioning](https://aclanthology.org/2025.naacl-long.153.pdf)
- **Cross-lingual alignment** (constructs) — *measured_by*
  - [Robust Adaptation of Large Multimodal Models for Retrieval Augmented Hateful Meme Detection](https://aclanthology.org/2025.emnlp-main.1216.pdf)

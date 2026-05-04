# GenEval
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

GenEval is consistently described in the provided literature as a benchmark for evaluating text-to-image generation models. Its primary purpose is to assess a model's ability to generate an image that accurately depicts a given text prompt, a function one paper describes as examining "a model’s ability to generate an accurate depiction of the prompt" ('Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model'). A more specific framing characterizes it as a metric that assesses the "quality and alignment of generated images with respect to input text, based on human preferences and semantic accuracy" ('Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads'). Across the surveyed work, GenEval is used to operationalize and measure both `Visual generation` and `Image generation` capabilities. In practice, researchers report quantitative results, such as "a GenEval score of 0.58" ('Orthus...'), and use the benchmark to compare the performance of different models, with DALL-E 2 and SDXL appearing as common points of comparison.

## Sources

**[Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/12678c3948153f4bc391f51e2082bd6e-Paper-Conference.pdf)**
> A benchmark designed to evaluate a model's ability to generate an image that is an accurate depiction of a given prompt.

## Relationships

### → GenEval
- **Visual generation** (constructs) — *measured_by*
  > For visual understanding and generation, Orthus achieves a GenEval score of 0.58 and an MME-P score of 1265.8 using 7B parameters... (Abstract)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  > "On the GenEval (Ghosh et al., 2023) benchmark, our model outperforms other popular models"
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **Multimodal generation** (constructs) — *measured_by*
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)

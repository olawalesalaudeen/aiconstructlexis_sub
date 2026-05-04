# Flickr30k
**Type:** Measurement  
**Referenced in:** 45 papers  
**Also known as:** Flickr30K, FLICKR30K  

## State of the Field

Across the provided literature, Flickr30k is predominantly characterized as a benchmark with two main applications: image captioning and image-text retrieval. The dataset is consistently defined as containing 30,000 images from Flickr, each paired with multiple descriptive captions. Its most frequent use is to measure `Image captioning`, where papers evaluate models on tasks like "image-level caption ability" and "zero-shot caption generation." A second, nearly as prevalent, application is the measurement of `Cross-modal retrieval`, where models must match images to corresponding captions. A smaller number of studies also use Flickr30k to evaluate `Image generation`. In isolated cases, it is used to assess broader capabilities such as `Visual perception` and `Multimodal understanding`. The benchmark is frequently employed in zero-shot evaluation settings, though one paper also investigates its few-shot performance, observing that it "decreases with examples given" (MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning).

## Sources

**[Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf)**
> Image-text retrieval benchmark where models match images to corresponding captions or vice versa.

**[MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/41128e5b3a7622da5b17588757599077-Paper-Conference.pdf) (as "Flickr30K")**
> Image captioning dataset with 30,000 images and associated captions, used to evaluate vision-to-text generation and in-context learning effects.

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf) (as "FLICKR30K")**
> An image captioning dataset consisting of 30,000 images collected from Flickr, each with multiple descriptive captions.

## Relationships

### → Flickr30k
- **Image captioning** (behaviors tasks) — *measured_by*
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Visual perception** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)

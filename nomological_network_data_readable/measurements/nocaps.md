# NoCaps
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** NOCAPS, Nocaps  

## State of the Field

Across the provided literature, NoCaps is consistently described as a benchmark dataset for evaluating image captioning. The most prevalent theme is its use for assessing the generalization of vision-language models, specifically in a zero-shot context. Papers frequently define its purpose as testing a model's ability to generate captions for images containing novel objects or content not seen during training. Consequently, it is widely used to measure the behavior of `Image captioning`. A smaller line of work also uses NoCaps to evaluate the transferability and robustness of methods on out-of-domain images, particularly for measuring `Object hallucination`. As one study states, it is used "To evaluate object hallucination in visual caption." One paper also notes that the dataset is derived from Open Images. In practice, it is often evaluated alongside other captioning benchmarks such as MSCOCO and Flickr30K.

## Sources

**[Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)**
> Zero-shot image captioning benchmark dataset used to evaluate generalization of vision-language models on novel image content not seen during training.

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf) (as "NOCAPS")**
> A large-scale image captioning dataset designed to test a model's ability to describe novel objects not seen frequently in training data.

**[Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf) (as "Nocaps")**
> The Novel Object Captioning (Nocaps) dataset, used to evaluate the transferability and robustness of hallucination mitigation methods on out-of-domain images.

## Relationships

### → NoCaps
- **Image captioning** (behaviors tasks) — *measured_by*
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > To evaluate object hallucination in visual caption, we use images from the COCO validation and Nocaps (Agrawal et al., 2019) datasets (Section 5.1).
  - [Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf)

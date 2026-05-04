# COCO Caption
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** COCO Captions, COCO-Cap, COCO-Caption, COCO-Captions, COCO-Capation  

## State of the Field

Across the surveyed literature, COCO Caption is predominantly characterized as a large-scale benchmark dataset for evaluating image captioning. It is consistently defined as being based on the Common Objects in Context (COCO) collection, with one paper specifying that it contains over 330,000 images and provides five human-generated captions per image. The most common application is to measure the `Image captioning` behavior, assessing a model's capability to generate textual descriptions for images, often in the context of fine-tuning. A less frequent but distinct usage is also documented, where the dataset's captions serve as a source of prompts for evaluating `Image generation` tasks. The instrument is also listed as a measure for `Visual understanding` and `Fine-grained understanding`, though the provided evidence for these is less detailed than for its primary use in captioning.

## Sources

**[A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d355518527578ce26b80da96e9fc2750-Paper-Conference.pdf)**
> A benchmark dataset used to evaluate the capability of models to generate textual descriptions for images.

**[Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf) (as "COCO Captions")**
> A dataset of image captions (from the Common Objects in Context dataset) used here as a source of prompts for evaluating text-to-image generation tasks.

**[AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf) (as "COCO-Cap")**
> A large-scale image captioning benchmark based on the Common Objects in Context (COCO) dataset.

**[Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hahn25a/hahn25a.pdf) (as "COCO-Captions")**
> A large-scale object detection, segmentation, and captioning dataset, where the captioning portion provides multiple short, human-generated descriptions for each image.

**[LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf) (as "COCO-Caption")**
> A dataset based on the Common Objects in Context (COCO) collection, used for evaluating image captioning models.

**[Learn from Downstream and Be Yourself in Multimodal Large Language Models Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25q/huang25q.pdf) (as "COCO-Capation")**
> Image captioning benchmark used to assess a model's ability to generate descriptive text from images during fine-tuning.

## Relationships

### → COCO Caption
- **Image captioning** (behaviors tasks) — *measured_by*
  > Comparison with the state-of-the-art Multimodal Large Language Model (MLLM) Fine-Tuning Solutions on the image caption task: Flickr30k and COCO-Capation datasets (Table 5).
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Image generation** (behaviors tasks) — *measured_by*
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **Fine-grained understanding** (constructs) — *measured_by*
  - [ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering](https://aclanthology.org/2025.emnlp-main.55.pdf)

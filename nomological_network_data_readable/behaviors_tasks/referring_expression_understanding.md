# Referring expression understanding
**Type:** Behavior  
**Referenced in:** 34 papers  
**Also known as:** Referring expression segmentation, Referring segmentation, Referring expression comprehension, Referring description, Referring reasoning, Referring image segmentation, Visual referring, Referring object part segmentation, Referring  

## State of the Field

Across the surveyed literature, "Referring expression understanding" is most commonly framed as the behavior of localizing a specific object or region in an image based on a natural language description. This is operationalized under various names, including "referring expression segmentation," "referring segmentation," and "referring expression comprehension," with the model's output typically being a segmentation mask or a bounding box. The performance of this behavior is predominantly measured using the RefCOCO, RefCOCO+, and RefCOCOg benchmarks, where correctness can be determined by an Intersection over Union (IoU) threshold, as one paper notes "a prediction is considered correct if the IoU between the predicted and ground truth bounding boxes exceeds 0.5" (Text4Seg: Reimagining Image Segmentation as Text Generation). A smaller body of work conceptualizes the task in reverse, defining it as generating a textual description for a given visual region, a behavior evaluated on Ferret-Bench. Other alternative framings apply the concept to 3D object part segmentation, measured on datasets like Talk2Car, or to user interface elements, involving tasks like OCR and widget classification. The behavior is frequently studied alongside `Visual grounding` and is described as requiring both `spatial reasoning` and `semantic reasoning`. One study also reports a correlation between performance on this task and a model's score on the HellaSwag reasoning benchmark.

## Sources

**[Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf) (as "Referring expression segmentation")**
> The task of segmenting the specific object or region in an image that is described by a given natural language expression.

**[Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf) (as "Referring expression comprehension")**
> Identifying the referred object by generating a mask and deriving a bounding box that matches the language query.

**[Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf) (as "Referring segmentation")**
> The task of segmenting an object in an image based on a natural language description.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Referring description")**
> An observable task, evaluated on Ferret-Bench, where the model provides a textual description corresponding to a visual prompt.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Referring reasoning")**
> An observable task, evaluated on Ferret-Bench, where the model performs reasoning based on information within a visually prompted region.

**[Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3769fddee1b20552d2490c4ff18b136-Paper-Conference.pdf) (as "Referring image segmentation")**
> The task of segmenting a specific object or region in an image based on a natural language description.

**[ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf) (as "Visual referring")**
> Given an image and a referred region, the model produces a detailed natural-language description of that region.

**[3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds](https://proceedings.iclr.cc/paper_files/paper/2025/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf) (as "Referring object part segmentation")**
> The pre-training task of predicting a binary mask for a specific component of a 3D object, given a referring expression that names the component.

**[Ferret-UI 2: Mastering Universal User Interface Understanding Across Platforms](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7baab9bb701848e75f3cc119bdf57bc-Paper-Conference.pdf) (as "Referring")**
> The observable task of identifying or describing a specific UI element based on its properties, such as recognizing text within a bounding box or classifying a widget's type.

## Relationships

### Referring expression understanding →
- **RefCOCO** (measurements) — *measured_by*
  > For referring expression segmentation (RES), we follow standard evaluation protocols (Lai et al., 2024; Xia et al., 2024) and assess our method using the refCOCO series. (Section 4.2)
  - [GENOME: Generative Neuro-Symbolic Visual Reasoning by Growing and Reusing Modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/088d99765bc121c6df215da7d45bc4e9-Paper-Conference.pdf)
- **RefCOCOg** (measurements) — *measured_by*
  > For referring expression segmentation (RES), we follow standard evaluation protocols (Lai et al., 2024; Xia et al., 2024) and assess our method using the refCOCO series. (Section 4.2)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Ferret-Bench** (measurements) — *measured_by*
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Talk2Car** (measurements) — *measured_by*
  > Talk2Car (Deruyttere et al., 2019) is a 3D referring expression comprehension dataset of various driving scenarios. (Section 4.1)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **RefCOCO/g/+** (measurements) — *measured_by*
  > In Table 4, we compare CUBE-LLM to the state-of-the-arts in Referring Expression Comprehension (REC) benchmark on refCOCO/+/g (Yu et al., 2016) dataset. (Section 4.4)
  - [Language-Image Models with 3D Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a829e299ebc1c1615ddb09e98fb6ce8-Paper-Conference.pdf)

### → Referring expression understanding
- **HellaSwag** (measurements) — *correlates*
  > “Further analysis shows a Pearson correlation of 0.88 between the LLM’s original performance on reasoning benchmarks, measured by the HellaSwag score (Zellers et al., 2019), and REC performance”
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)

### Associated with
- **Visual grounding** (constructs)
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)
- **Spatial understanding** (constructs)
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Referring expression generation** (behaviors tasks)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
- **Multimodal alignment** (constructs)
  - [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual perception** (constructs)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Relational reasoning** (constructs)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual recognition** (constructs)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Spatial reasoning** (constructs)
  > Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Semantic reasoning** (constructs)
  > Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Object detection** (behaviors tasks)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)

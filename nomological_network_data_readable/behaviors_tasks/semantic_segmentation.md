# Semantic segmentation
**Type:** Behavior  
**Referenced in:** 30 papers  
**Also known as:** Object segmentation, Segmentation, Instance segmentation, Medical image segmentation, Open-vocabulary segmentation, Visual segmentation, Affordance segmentation, Multi-object referring segmentation, Multi-target segmentation, Part-level segmentation  

## State of the Field

Across the provided literature, semantic segmentation is most commonly defined as the task of partitioning an image into multiple segments, typically by classifying each pixel into a predefined set of semantic categories or generating pixel-level masks for objects. While this general framing is prevalent, the literature also describes several specialized sub-tasks. A recurring distinction is made between semantic segmentation and instance segmentation, with the latter focused on delineating each distinct object instance. Other variants include "open-vocabulary segmentation" for handling labels not seen during training, "medical image segmentation" for identifying pathological areas, and "affordance segmentation" for marking an object's functional regions. Some work extends the task's complexity, introducing "multi-target" or "multi-object referring segmentation" to generate masks for multiple objects from a single instruction, and "part-level segmentation" for specific parts of an object. This behavior is operationalized and evaluated using a variety of benchmarks, with ADE20K and COCO being the most frequently cited datasets for this purpose, alongside LVIS, PASCAL VOC, Pascal Context, and ScanNet. One paper proposes a different operationalization, framing "image segmentation as a text generation problem" ("Text4Seg: Reimagining Image Segmentation as Text Generation"). Conceptually, semantic segmentation is studied in the context of broader capabilities like "Visual perception" and "Semantic understanding," and is also related to "Visual grounding" and "Image restoration."

## Sources

**[EAGLE: Efficient Adaptive Geometry-based Learning in Cross-view Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/f84ceafb242f0de36f8c49452fbae6de-Paper-Conference.pdf)**
> The task of classifying each pixel in an image into a predefined set of semantic categories.

**[DeiSAM: Segment Anything with Deictic Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ddcfaad1cb72ce6f1a365e8f1ecf791-Paper-Conference.pdf) (as "Object segmentation")**
> The action of generating pixel-level masks for specific objects within a visual input.

**[MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf) (as "Image segmentation")**
> Partitioning an image into object masks or regions corresponding to specific objects.

**[Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Segmentation")**
> Delineating biological structures in microscopy images at the instance or semantic level.

**[Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf) (as "Instance segmentation")**
> The task of detecting and delineating each distinct object instance in an image with a pixel-level mask.

**[Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf) (as "Open-vocabulary segmentation")**
> The task of segmenting image regions corresponding to a set of textual labels that were not necessarily seen during training.

**[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf) (as "Medical image segmentation")**
> Identifying and delineating regions of interest or pathological areas in medical images.

**[Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf) (as "Visual segmentation")**
> The task of partitioning a digital image into multiple segments to simplify its representation or locate specific objects.

**[ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf) (as "Multi-object referring segmentation")**
> The observable task of generating instance segmentation masks for multiple referred objects in an image.

**[3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds](https://proceedings.iclr.cc/paper_files/paper/2025/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf) (as "Affordance segmentation")**
> Predicting a binary mask that marks the functional regions of an object relevant to a query.

**[MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8661ab3440964c27794607f0ea73624-Paper-Conference.pdf) (as "Multi-target segmentation")**
> The observable behavior of simultaneously generating distinct segmentation masks for multiple target entities within a single image based on one instruction.

**[MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8661ab3440964c27794607f0ea73624-Paper-Conference.pdf) (as "Part-level segmentation")**
> The task of generating a segmentation mask for a specific part of an object, rather than the entire object.

## Relationships

### Semantic segmentation →
- **ADE20K** (measurements) — *measured_by*
  > We evaluate the model’s performance on ADE20K (A-150) (Zhou et al., 2019), PASCAL Context 59 (PC-59) (Mottaghi et al., 2014), and PASCAL VOC 20 (PAS-20) (Everingham, 2009) datasets, using mIoU as the evaluation metric. (Section 4.5)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **PASCAL VOC** (measurements) — *measured_by*
  - [Leveraging Hallucinations to Reduce Manual Prompt Dependency in Promptable Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1e1ad233411e25b54bb5df3a0576c2c-Paper-Conference.pdf)
- **Pascal Context** (measurements) — *measured_by*
  - [Leveraging Hallucinations to Reduce Manual Prompt Dependency in Promptable Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c1e1ad233411e25b54bb5df3a0576c2c-Paper-Conference.pdf)
- **Hypersim** (measurements) — *measured_by*
  - [4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities](https://proceedings.neurips.cc/paper_files/paper/2024/file/71883294314045d60c900113a359934b-Paper-Conference.pdf)
- **ScanNet** (measurements) — *measured_by*
  - [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf)
- **LVIS** (measurements) — *measured_by*
  - [Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf)

### Associated with
- **Semantic understanding** (constructs)
  - [Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c67fc501a50977947c5bebbc39ca8f6-Paper-Conference.pdf)
- **Visual perception** (constructs)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Image restoration** (behaviors tasks)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Visual grounding** (constructs)
  > flexible switching between referring expression segmentation, open-vocabulary segmentation, and other visual grounding tasks. (Section 1)
  - [Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)

# Object detection
**Type:** Behavior  
**Referenced in:** 32 papers  
**Also known as:** Fine-grained detection, 3D detection, Species detection, Tool detection, Face detection, Keypoint detection, Open-vocabulary detection, Object name generation  

## State of the Field

Across the provided literature, object detection is predominantly defined as the task of identifying and localizing objects within an image, most frequently operationalized by outputting bounding box coordinates and class labels. The performance of models on this task is commonly evaluated using datasets such as MS-COCO, COCO, and PASCAL VOC. While this general form is widely discussed, several papers define more specialized versions, including `3D detection` for localizing objects in 3D space, `tool detection` for surgical instruments, `species detection` in audio recordings, and `open-vocabulary detection` for handling arbitrary category names. Some work breaks the task down further, defining component behaviors like `bounding box prediction` for localization and `object name generation` for producing free-form textual labels. A recurring challenge noted is performance degradation when models encounter unseen data due to what one paper calls "domain discrepancy" (DA-Ada: Learning Domain-Aware Adapter for Domain Adaptive Object Detection). Object detection is frequently studied alongside other visual tasks such as visual perception, visual grounding, and referring expression understanding. A single source also suggests that multimodal alignment can influence its performance.

## Sources

**[Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)**
> The task of identifying and localizing objects within an image by outputting bounding box coordinates.

**[A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Fine-grained detection")**
> The task of identifying specific, localized areas of manipulation within a forged image, rather than just making a binary real/fake judgment.

**[NatureLM-audio: an Audio-Language Foundation Model for Bioacoustics](https://proceedings.iclr.cc/paper_files/paper/2025/file/36c20807317ae6cb3817acd554da2d32-Paper-Conference.pdf) (as "Species detection")**
> Determining whether a specified species is present in an audio recording, or outputting none when absent.

**[Recognize Any Surgical Object: Unleashing the Power of Weakly-Supervised Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/53d3f45797970d323bd8a0d379c525aa-Paper-Conference.pdf) (as "Tool detection")**
> The task of identifying and localizing surgical tools within an image or video frame.

**[MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf) (as "3D detection")**
> The task of identifying and localizing objects within a 3D space based on visual information from multiple images.

**[Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf) (as "Face detection")**
> Detecting human faces in images and returning their bounding boxes.

**[Adapt-$\infty$: Scalable Continual Multimodal Instruction Tuning via Dynamic Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf) (as "Keypoint detection")**
> The task of identifying and localizing specific key points of objects within an image.

**[Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf) (as "Object name generation")**
> The model produces free-form textual names for detected objects without relying on a fixed vocabulary.

**[Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf) (as "Bounding box prediction")**
> The task of generating rectangular coordinates that localize an object within an image.

**[Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf) (as "Open-vocabulary detection")**
> The task of detecting objects in an image from an arbitrary, open set of category names provided as text at inference time.

## Relationships

### Object detection →
- **COCO** (measurements) — *measured_by*
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
- **PASCAL VOC** (measurements) — *measured_by*
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)

### → Object detection
- **Multimodal alignment** (constructs) — *causes*
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)

### Associated with
- **Visual perception** (constructs)
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Visual grounding** (constructs)
  - [Lumen: Unleashing Versatile Vision-Centric Capabilities of Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/946ecab300b0695fe24b53a92e632935-Paper-Conference.pdf)
- **Visual recognition** (constructs)
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Image restoration** (behaviors tasks)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Open-vocabulary object detection** (behaviors tasks)
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)
- **Localization** (constructs)
  - [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf)

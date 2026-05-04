# Visual perception
**Type:** Construct  
**Referenced in:** 46 papers  
**Also known as:** Low-level visual perception, Vision perception  

## State of the Field

Across the surveyed literature, visual perception is most commonly defined as a model's latent ability to interpret and understand a wide range of visual information, from natural images and videos to complex diagrams, charts, and graphical user interfaces (GUIs). A more specific framing, described as 'low-level visual perception,' focuses on the ability to answer questions about basic attributes like distortions, color, and lighting. The construct is operationalized and measured through model performance on numerous benchmarks, including VQA-v2, GQA, MME, POPE, and Q-Bench, as well as through broader tasks like visual question answering and image captioning. Several papers position visual perception as a component of higher-order cognition, with one study noting that a model's superiority is 'mainly attributed to its enhanced visual perception and mathematical reasoning' (MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts). Deficits in this ability are reported to have downstream consequences, as multiple sources state that a gap in perception causes `Hallucination`. Furthermore, some work suggests that errors in perception can negatively impact `Abstract reasoning` and that enhanced perception improves performance on tasks like `Optical character recognition`. The quality of visual perception is also discussed in relation to technical factors, such as input resolution, and is sometimes framed as a trade-off against language capabilities, particularly in smaller models.

## Sources

**[Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision](https://proceedings.iclr.cc/paper_files/paper/2024/file/363d4c97bb411e4b07612915b76c06ae-Paper-Conference.pdf) (as "Low-level visual perception")**
> The ability of a model to accurately respond to questions about low-level visual attributes such as distortions, color, lighting, and composition.

**[MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://proceedings.iclr.cc/paper_files/paper/2024/file/663bce02a0050c4a11f1eb8a7f1429d3-Paper-Conference.pdf)**
> The latent ability to accurately interpret and understand visual information such as diagrams, charts, plots, and natural images, especially in the context of mathematical reasoning.

**[GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf) (as "Vision perception")**
> The latent quality of visual input interpretation, influenced by resolution, keyframe granularity, and visual encoding.

## Relationships

### Visual perception →
- **VQA-v2** (measurements) — *measured_by*
  > VQA-v2 (Goyal et al., 2017b) and GQA (Hudson & Manning, 2019) assess the visual perception capabilities of models through open-ended short answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > VQA-v2 (Goyal et al., 2017b) and GQA (Hudson & Manning, 2019) assess the visual perception capabilities of models through open-ended short answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  > MME (Fu et al., 2023) assesses the visual perception of models with yes/no questions. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > This gap in perception causes hallucinations, resulting in incorrect responses. (Section 4.1)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Q-Bench** (measurements) — *measured_by*
  - [TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf)
- **Abstract reasoning** (constructs) — *causes*
  > A single error in visual feature perception can impact reasoning since the correct pattern must apply to all puzzle shapes. (Section 6)
  - [MARVEL: Multidimensional Abstraction and Reasoning through Visual Evaluation and Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/529d8b3a23991e83db07f21727256374-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Flickr30k** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VizWiz** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMVP** (measurements) — *measured_by*
  > We extensively evaluated DEEM on both our newly constructed RobustVQA benchmark and other well-known benchmarks, POPE and MMVP, for visual hallucination and perception respectively.
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Optical character recognition** (behaviors tasks) — *causes*
  > Recent work indicates that enhanced visual perception significantly reduces hallucinations and improves performance on resolution-sensitive tasks, such as optical character recognition and document analysis. (ABSTRACT)
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)
- **Document understanding** (constructs) — *causes*
  - [Eagle: Exploring The Design Space for Multimodal LLMs with Mixture of Encoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/e78457d4a04b8565f1fe5077df13cddb-Paper-Conference.pdf)

### → Visual perception
- **Multimodal alignment** (constructs) — *causes*
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)

### Associated with
- **Object detection** (behaviors tasks)
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Visual understanding** (constructs)
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  > Visual perception is assessed through image captioning, where VLMs produce descriptions of the input images, or visual-question answering (VQA), where VLMs are asked to answer questions pertaining to the images. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Image captioning** (behaviors tasks)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Semantic segmentation** (behaviors tasks)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Pose estimation** (behaviors tasks)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Visual recognition** (constructs)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf)

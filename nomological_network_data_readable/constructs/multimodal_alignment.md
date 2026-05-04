# Multimodal alignment
**Type:** Construct  
**Referenced in:** 72 papers  
**Also known as:** Cross-modal alignment, Text-image alignment, Vision-language alignment, Multi-modal alignment, Cross-modal knowledge alignment, Cross-modality alignment, Cross-modal semantic alignment, Text-video alignment, Video-language alignment, Image-text alignment, Audio-visual alignment, Visual-language alignment, Visual-text alignment, Image-text modality alignment, Visual-linguistic alignment, Text alignment, Vision-text alignment, Visual-textual token alignment  

## State of the Field

Across the surveyed literature, multimodal alignment is most commonly described as a model's latent ability to connect and integrate information from different modalities, primarily vision and language, into a shared semantic space or coherent joint representation. The prevailing goal is to ensure that representations from different modalities "encode equivalent semantic information" ("Bridging Vision and Language Spaces with Assignment Prediction"), enabling interoperability. While the vision-text pairing is the most frequent, the concept is also applied to other modalities, including video-language, audio-visual, and specialized data like EEG-text and molecular graphs. A smaller set of work extends this framing to cross-lingual semantic alignment. The field operationalizes this construct using a range of measurement instruments; papers report using benchmarks like ImageNet-1k and COCO, automated metrics such as CLIP score and CHAIR, and evaluation procedures including LLM-as-a-judge and human evaluation to assess it. Improved alignment is reported to influence visual perception and performance on tasks like object detection. Conversely, poor alignment is frequently associated with model failures, particularly object hallucination, with some work stating that "The misalignment between image and text semantics is a significant cause of hallucinations" ("CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs").

## Sources

**[Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf) (as "Cross-modal alignment")**
> The latent ability of a model to ensure that representations from different modalities (e.g., vision and language) encode equivalent semantic information, enabling interoperability between them.

**[Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf) (as "Vision-language alignment")**
> The latent ability of a model to integrate and relate visual and linguistic information into a coherent joint representation, enabling understanding of multimodal inputs.

**[Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf)**
> The latent ability of a model to connect and integrate information from visual and textual modalities, creating a shared semantic space.

**[AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf) (as "Text-image alignment")**
> The degree to which the generated image semantically corresponds to the input caption, reflecting accurate interpretation of visual concepts from text.

**[What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf) (as "Multi-modal alignment")**
> The degree to which a vision-language model forms semantically aligned representations across modalities, enabling effective use of multi-modal context.

**[ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Modality alignment")**
> The degree to which a model effectively bridges and correlates information between visual and textual representations internally.

**[TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf) (as "Cross-modal knowledge alignment")**
> The ability to correctly associate textual concepts, especially knowledge-intensive ones like landmarks or species, with their corresponding visual representations.

**[MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a559a5a8aa5ae6682ced009ad97cdb16-Paper-Conference.pdf) (as "Cross-modality alignment")**
> The extent to which a model correctly integrates and reasons over information from different modalities, such as medical images and text, rather than relying on one while ignoring the other.

**[CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf) (as "Cross-modal semantic alignment")**
> The degree to which a model's internal representations for images and their corresponding textual descriptions are congruent in semantic space.

**[Mufu:  Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf) (as "Cross-lingual semantic alignment")**
> The ability to map and align meaning between different languages at a semantic level, beyond simple lexical or orthographic similarity.

**[$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf) (as "Video-language alignment")**
> The degree to which a model's textual outputs accurately and coherently correspond to the semantic content of a given video input.

**[GRADEO: Towards Human-Like Evaluation for Text-to-Video Generation via Multi-Step Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mou25a/mou25a.pdf) (as "Text-video alignment")**
> The degree to which a generated video accurately reflects the objects, counts, colors, styles, actions, and other specifications described in the input text prompt.

**[ICLCIPHERS: Quantifying ”Learning” in In-Context Learning via Substitution Ciphers](https://aclanthology.org/2025.emnlp-main.1317.pdf) (as "Image-text alignment")**
> The latent ability to match visual content with textual instructions and responses so that answers are consistent with the image.

**[SPEAttention: Making Attention Equivariant to Semantic-Preserving Permutation for Code Processing](https://aclanthology.org/2025.emnlp-main.333.pdf) (as "Audio-visual alignment")**
> The latent ability to integrate and synchronize information across auditory and visual modalities, such as linking spoken words to visual characters, objects, or on-screen text, or aligning audio segments with corresponding video frames.

**[Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.605.pdf) (as "Visual-language alignment")**
> The degree to which a model integrates visual percepts with linguistic representations to produce contextually grounded responses.

**[Debatable Intelligence: BenchmarkingLLMJudges via Debate Speech Evaluation](https://aclanthology.org/2025.emnlp-main.954.pdf) (as "Visual-text alignment")**
> The latent capacity of a VLLM to identify and leverage correspondences between visual content and textual input, ensuring that relevant visual tokens are aligned with the semantic context of the question or prompt.

**[Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf) (as "Image-text modality alignment")**
> The degree to which a model correctly associates textual concepts with corresponding visual evidence in an image, forming the basis for cross-modal understanding.

**[Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf) (as "Visual-linguistic alignment")**
> The latent ability of a model to correctly associate textual descriptions with corresponding visual regions in an image.

**[VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf) (as "Text alignment")**
> The degree to which the model's internal representations of visual content are semantically aligned with corresponding textual descriptions.

**[Parrot: Multilingual Visual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25ad/sun25ad.pdf) (as "Visual-textual token alignment")**
> The degree to which visual features extracted from images are semantically aligned with textual tokens in a given language, enabling coherent multimodal understanding and generation.

**[Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf) (as "Vision-text alignment")**
> The degree to which a model's textual outputs accurately correspond to the visual elements and context present in an image.

## Relationships

### Multimodal alignment →
- **ImageNet-1k** (measurements) — *measured_by*
  > “We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the validation sets from CC3M, MSCOCO as well as the ImageNet-1K, CIFAR-100, and CIFAR-10 test datasets.”
  - [Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e25d87b8a42ee3f0d5b3ef741ca13031-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf)
- **CLIP score** (measurements) — *measured_by*
  - [AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [YouDream: Generating Anatomically Controllable Consistent Text-to-3D Animals](https://proceedings.neurips.cc/paper_files/paper/2024/file/6fe5d7a2de090168917425fe89a6c1b8-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *causes*
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **CHAIR** (measurements) — *measured_by*
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)
- **Pick-a-Pic** (measurements) — *measured_by*
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [Are Large Vision Language Models Good Game Players?](https://proceedings.iclr.cc/paper_files/paper/2025/file/27881a19f100fdbf57f0ba1c3d499b08-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > This eventually leads to an increasingly blurred feature during the final layers of the LLM, which weakens the cross-modal alignment between visual and textual cues, ultimately resulting in suboptimal performance and higher degrees of hallucination (Fig. 1).
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Visual perception** (constructs) — *causes*
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **Object detection** (behaviors tasks) — *causes*
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)
- **Medical diagnosis** (behaviors tasks) — *causes*
  - [EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gijsen25a/gijsen25a.pdf)
- **Training efficiency** (constructs) — *causes*
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)

### → Multimodal alignment
- **Modality alignment** (constructs) — *measured_by*
  - [Diff-eRank: A Novel Rank-Based Metric for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/45cc967d7899616f51993b7b363d35b5-Paper-Conference.pdf)
- **Self-reflection** (behaviors tasks) — *causes*
  - [Aligning Audio-Visual Joint Representations with an Agentic Workflow](https://proceedings.neurips.cc/paper_files/paper/2024/file/6c0ff499edc529c7d8c9f05c7c0ccb82-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf)

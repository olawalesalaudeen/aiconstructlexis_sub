# Cross-modal retrieval
**Type:** Behavior  
**Referenced in:** 43 papers  
**Also known as:** Image-text matching, Image-caption matching, Multimodal retrieval, Compositional image-text matching, Audio-to-text retrieval, Text-to-audio retrieval, Image-text retrieval, Text-image retrieval, Text-to-image retrieval, Text-to-video retrieval, Video-to-text retrieval, Video retrieval, Composed image retrieval, Visual question answering retrieval, Image retrieval, Image-to-text retrieval, Long-text-image retrieval, Short-text-image retrieval  

## State of the Field

Cross-modal retrieval is a widely studied behavior predominantly defined as retrieving content from one modality based on a query from another. The most common operationalization involves image and text pairs—in both text-to-image and image-to-text directions—though the concept also extends to video, audio, and knowledge graphs. The task is framed in several ways, from general image-text matching that produces a similarity score to more specific binary choice tasks like image-caption matching. Some work focuses on compositional challenges, using distractors to test beyond simple "bag of words" behavior, while a less common framing defines it as locating a specific fact or image within a long multimodal document. To measure this behavior, researchers employ a variety of benchmarks, with Flickr30k and MS-COCO appearing most frequently in the provided data; other datasets like AudioCaps and MSRVTT are used for audio and video retrieval respectively. Performance on these tasks is often used as a measure for broader constructs such as `Multimodal understanding` and `Long-context understanding`. The behavior is also studied alongside `Modality bias`, and one paper reports that `Ranking` can be used to improve retrieval accuracy by reranking candidates.

## Sources

**[BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a5a9f5c15632e9f52c9c1ba4134f13c-Paper-Conference.pdf)**
> Retrieving content from one modality (e.g., image) based on input from another modality (e.g., text), including both image-to-text and text-to-image directions.

**[DevBench: A multimodal developmental benchmark for language learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8d987b2981388c99c7eab6095d1d29fd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image-text matching")**
> The general task of determining the correspondence or similarity between a given image and a piece of text, often by producing a score.

**[VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf) (as "Image-caption matching")**
> Selecting the correct caption for an image or the correct image for a caption from two alternatives.

**[Needle In A Multimodal Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/24a8968affe71ffe4067d022b9d16566-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multimodal retrieval")**
> Answering questions by locating a specific inserted fact, statement, or image within a long multimodal document.

**[TripletCLIP:  Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf) (as "Compositional image-text matching")**
> The task of correctly identifying the matching image-text pair from a set of distractors that involve compositional changes in objects, attributes, or relations.

**[Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf) (as "Audio-to-text retrieval")**
> Given an audio input, the model retrieves the matching text caption from a candidate set.

**[Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf) (as "Text-to-audio retrieval")**
> Given a text caption, the model retrieves the matching audio sample from a candidate set.

**[TIGeR: Unifying Text-to-Image Generation and Retrieval with Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0a9bc5536c595ee44a72b575b258d141-Paper-Conference.pdf) (as "Text-to-image retrieval")**
> The task of selecting and returning an existing image from a database that best matches a given textual description.

**[Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf) (as "Text-to-video retrieval")**
> Ranking videos given a textual query.

**[Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf) (as "Video-to-text retrieval")**
> Retrieving relevant text descriptions from a collection based on a video query.

**[Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf) (as "Video retrieval")**
> Retrieving videos that are relevant to a textual query, including partially relevant videos from a larger collection.

**[Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf) (as "Image-text retrieval")**
> The task of selecting the most relevant text caption for a given image from a set of candidates, or vice-versa.

**[LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf) (as "Text-image retrieval")**
> Retrieving images or text items based on cross-modal similarity between text and images.

**[MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf) (as "Composed image retrieval")**
> The observable task of retrieving a target image based on a query that combines a source image with a textual description of desired modifications.

**[MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf) (as "Visual question answering retrieval")**
> The observable task of retrieving a document (e.g., text or an image-description pair) that contains the answer to a question posed about a given image.

**[MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf) (as "Image retrieval")**
> The task of finding and selecting a correct target image from a set of candidates based on a query, such as matching a sketch to a natural image.

**[LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf) (as "Image-to-text retrieval")**
> Given an image, finding the most semantically similar text description from a collection of candidate texts.

**[LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf) (as "Long-text-image retrieval")**
> The task of retrieving the correct image from a set given a long, detailed text query, or retrieving the correct text given an image.

**[LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf) (as "Short-text-image retrieval")**
> The task of retrieving the correct image from a set given a short, concise text query, or retrieving the correct text given an image.

## Relationships

### Cross-modal retrieval →
- **Flickr30k** (measurements) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Visual dialogue** (behaviors tasks) — *measured_by*
  - [Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf)
- **WINOGROUND** (measurements) — *measured_by*
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)
- **Clotho** (measurements) — *measured_by*
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **AudioCaps** (measurements) — *measured_by*
  - [Learning Spatially-Aware Language and Audio Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/3acc054949b6948d4444b35d412cab56-Paper-Conference.pdf)
- **Flickr30k Entities** (measurements) — *measured_by*
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **CUB-200-2011** (measurements) — *measured_by*
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **ImageNet-1k** (measurements) — *measured_by*
  - [4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities](https://proceedings.neurips.cc/paper_files/paper/2024/file/71883294314045d60c900113a359934b-Paper-Conference.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **MSRVTT** (measurements) — *measured_by*
  - [A Multilingual, Culture-First Approach to Addressing Misgendering inLLMApplications](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **MSVD** (measurements) — *measured_by*
  - [A Multilingual, Culture-First Approach to Addressing Misgendering inLLMApplications](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **LSMDC** (measurements) — *measured_by*
  - [A Multilingual, Culture-First Approach to Addressing Misgendering inLLMApplications](https://aclanthology.org/2025.emnlp-main.1588.pdf)
- **DiDeMo** (measurements) — *measured_by*
  - [A Multilingual, Culture-First Approach to Addressing Misgendering inLLMApplications](https://aclanthology.org/2025.emnlp-main.1588.pdf)

### → Cross-modal retrieval
- **Multimodal understanding** (constructs) — *measured_by*
  - [Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
- **Ranking** (behaviors tasks) — *causes*
  > We find that MLLMs can be used as zero-shot rerankers to further boost retrieval accuracy in challenging tasks that require the understanding of multimodal queries, such as ... composed image retrieval. (Section 6)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
- **Video captioning** (behaviors tasks) — *causes*
  - [IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents](https://proceedings.neurips.cc/paper_files/paper/2024/file/e3301977b92f28e32639ec99eb08f4a1-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Modality bias** (constructs)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
- **Decision-making** (constructs)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [Natural Language Inference Improves Compositionality in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eeec4dffcfe4912482ffbf2ab8ddb41-Paper-Conference.pdf)

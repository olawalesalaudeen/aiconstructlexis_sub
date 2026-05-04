# Image generation
**Type:** Behavior  
**Referenced in:** 77 papers  
**Also known as:** Text-to-image generation, Image synthesis, Subject-driven generation, Scientific text-to-image generation, Chest X-ray generation, Banner ad generation, Adversarial example generation  

## State of the Field

Across the surveyed literature, image generation is predominantly defined as the behavior of producing realistic images from conditioning signals, most commonly textual prompts but also class labels. A number of papers focus on more specific variants of this task, such as 'text-to-image generation,' 'subject-driven generation' which requires faithfulness to reference images, and domain-specific applications like creating scientific visualizations or medical chest X-rays. This behavior is most frequently operationalized using the MS-COCO dataset, with ImageNet-1k and Flickr30k also being used for evaluation. Performance is further assessed through automated metrics like CLIP score, dedicated benchmarks such as GenEval, and human-centric methods including direct human evaluation and using LLMs as judges. The literature connects image generation to related concepts like semantic alignment and visual reasoning, and it is often studied as a component of the broader capability of 'multimodal generation.' Some work also explores societal aspects, with one study noting fairness concerns where a model was "found to diversify race and gender appearances in images even when prompts specified historical settings" (ELABORATION: A Comprehensive Benchmark on Human-LLMCompetitive Programming). In a departure from this visual focus, one paper uses the term 'adversarial example generation' to describe a purely textual task of creating modified sentence pairs to test model robustness.

## Sources

**[Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)**
> Producing realistic images from class labels or other conditioning signals using a generative model.

**[Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf) (as "Text-to-image generation")**
> Creating static visual content from textual prompts.

**[Enhancing LLM Reasoning via Vision-Augmented Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/328c922d068dd4ccb23cec5c64e6c7fc-Paper-Conference.pdf) (as "Image synthesis")**
> Creating an image from a textual problem description using a drawing or generation tool.

**[Bridging The Gap between Low-rank and Orthogonal Adaptation via Householder Reflection Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf) (as "Subject-driven generation")**
> Generating images of a specified subject that remain faithful to reference images while matching a text prompt.

**[ScImage: How good are multimodal large language models at scientific text-to-image generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/146b5b0feb14fe8e630669ad1faba25e-Paper-Conference.pdf) (as "Scientific text-to-image generation")**
> The observable task of producing a scientific visualization, such as a figure, chart, or plot, based on a textual description.

**[MedRAX: Medical Reasoning Agent for Chest X-ray](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fallahpour25a/fallahpour25a.pdf) (as "Chest X-ray generation")**
> Synthesizing realistic chest X-ray images from textual descriptions of anatomical features and pathologies.

**[Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.214.pdf) (as "Banner ad generation")**
> The end-to-end process of creating a complete advertising banner from a multimodal request that includes a brand logo and textual requirements.

**[MS-RAG: Simple and Effective Multi-Semantic Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1152.pdf) (as "Adversarial example generation")**
> The process of creating modified sentence pairs by replacing words with antonyms to test model robustness and logical consistency.

## Relationships

### Image generation →
- **MS-COCO** (measurements) — *measured_by*
  > We use two benchmarks: MS-COCO (Lin et al., 2014) Karpathy test split and Flickr30K (Plummer et al., 2015). (Section 3.2)
  - [Kosmos-G: Generating Images in Context with Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b2fe1ee8d936ac08dd26f2ff58986c8f-Paper-Conference.pdf)
- **ImageNet-1k** (measurements) — *measured_by*
  - [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf)
- **Flickr30k** (measurements) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf)
- **COCO Caption** (measurements) — *measured_by*
  - [Vitron: A Unified Pixel-level Vision LLM for Understanding, Generating, Segmenting, Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/68bad5506f0f9eea7ae75f01ae00d5e2-Paper-Conference.pdf)
- **GenEval** (measurements) — *measured_by*
  > "On the GenEval (Ghosh et al., 2023) benchmark, our model outperforms other popular models"
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > Additionally, following the GPT-4V metric introduced in Section 4.2, we randomly select a subset of 3,000 our generated images for GPT-4V evaluation.
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **CLIP score** (measurements) — *measured_by*
  > For text-to-image (T2I) generation, earlier methods primarily rely on the Inception score (Salimans et al., 2016) and Fr´echet inception distance (Heusel et al., 2017). More recent works propose reference-free metrics for robust automatic evaluation of T2I and image captioning, with notable examples being CLIP-Score (Hessel et al., 2021) and PickScore (Kirstain et al., 2023).
  - [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf)

### → Image generation
- **Multimodal generation** (constructs) — *measured_by*
  - [Making LLaMA SEE and Draw with SEED Tokenizer](https://proceedings.iclr.cc/paper_files/paper/2024/file/97011c648eda678424f9292dadeae72e-Paper-Conference.pdf)
- **Query rewriting** (behaviors tasks) — *causes*
  - [LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf)

### Associated with
- **Visual generation** (constructs)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Semantic alignment** (constructs)
  - [Token Merging for Training-Free Semantic Binding in Text-to-Image Synthesis](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8ce25dcb2cb0eb8a24b492bf3e84695-Paper-Conference.pdf)
- **Visual reasoning** (constructs)
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)

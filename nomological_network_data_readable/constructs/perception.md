# Perception
**Type:** Construct  
**Referenced in:** 33 papers  
**Also known as:** Perception capability, Perceptual capability, Sensation, Perception ability, Perceptual understanding  

## State of the Field

Across the surveyed literature, the prevailing definition of Perception is a model's latent ability to extract and interpret visual information from images to support downstream tasks. While this general framing is common, a few papers offer more specific conceptualizations, such as focusing on visual information in document screenshots or defining it as "Sensation," the capacity to perceive basic details like count, color, and OCR. Perception is frequently positioned as a foundational capability, with one paper noting that it is "predominantly encoded in the early layers of the model." It is often studied alongside or contrasted with other constructs like cognition, reasoning, and abstract reasoning. The field operationalizes and measures this construct through a wide array of benchmarks. The MME benchmark is frequently cited as an instrument for evaluating both perception and cognition abilities. Other measurement instruments mentioned include RealWorldQA, MMStar, MMBench, SEED-Bench, and MNIST. This construct is also linked to behaviors like visual question answering and is studied in relation to object hallucination, with one source suggesting that enhancing perception can help alleviate hallucinations.

## Sources

**[Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)**
> The latent ability to extract and interpret visual information from images in order to support downstream multimodal tasks.

**[Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf) (as "Perception capability")**
> The model's general ability to correctly interpret and understand visual information from an image.

**[MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Perceptual capability")**
> The ability to extract and interpret visual information from document screenshots, including charts, images, and layout cues.

**[Unveiling the Tapestry of Consistency in Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f094ba0f5ce1720466342f78031bdb-Paper-Conference.pdf) (as "Sensation")**
> The fundamental capability of LVLMs to perceive basic visual details such as count, color, OCR, and scene categories.

**[Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2372bb107ef0ba85e47c6a2dc7dafda-Paper-Conference.pdf) (as "Perception ability")**
> The model's fundamental capability to interpret and understand visual information across various contexts, styles, and scenarios.

**[VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf) (as "Perceptual understanding")**
> The latent ability to accurately interpret visual content and extract relevant properties from images.

## Relationships

### Perception →
- **MME** (measurements) — *measured_by*
  > MME evaluates VLMs with 14 sub-tasks that encompass cognition and perception abilities. (Section 3.2)
  - [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)
- **MMStar** (measurements) — *measured_by*
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
- **RealWorldQA** (measurements) — *measured_by*
  > The perception-focused benchmarks include RealWorldQA, CV-Bench and BLINK (Section 4)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **SEED-Bench** (measurements) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **ScienceQA** (measurements) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **VizWiz** (measurements) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **MNIST** (measurements) — *measured_by*
  > The perception capability is tested on CIFAR-10/100 (Krizhevsky et al., 2009) and MNIST (Deng, 2012). (Section 4.1)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **BLINK** (measurements) — *measured_by*
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Image captioning** (behaviors tasks)
  - [Is Your Multimodal Language Model Oversensitive to Safe Queries?](https://proceedings.iclr.cc/paper_files/paper/2025/file/50d4f8ff0416cedfe0771b7ad947a197-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  > Our hypothesis is that “General VQA” primarily evaluates perception ability and knowledge recall, while “Math VQA” assesses perception ability and reasoning ability.
  - [Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25cm/chen25cm.pdf)
- **Object hallucination** (behaviors tasks)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Cognition** (constructs)
  - [Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Object recognition** (behaviors tasks)
  - [AI-Assisted Human Evaluation of Machine Translation](https://aclanthology.org/2025.naacl-long.256.pdf)
- **Decision-making** (constructs)
  - [Competing Large Language Models in Multi-Agent Gaming Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/a46adbe2f0ca0e16ef8857e188991ad7-Paper-Conference.pdf)
- **Abstract reasoning** (constructs)
  > Analogical reasoning consists of diverse atomic abilities; perceptual understanding, mapping abstract relationships between visual contents (Gentner, 1983), and transferring relational patterns to novel cases. (Section 1)
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)

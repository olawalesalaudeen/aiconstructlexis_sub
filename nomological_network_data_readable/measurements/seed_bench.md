# SEED-Bench
**Type:** Measurement  
**Referenced in:** 35 papers  
**Also known as:** SEEDBench, SEEDbench, SeedBench  

## State of the Field

SEED-Bench is a benchmark frequently used to evaluate the multimodal comprehension performance of large language models. Across the provided literature, it is most commonly positioned as an instrument for measuring `Visual question answering`. Other papers use it to assess a wider range of capabilities, including `multimodal understanding`, `visual understanding`, `perception`, `commonsense knowledge`, and `visual instruction following`. The benchmark is consistently characterized by its format of comprehensive multiple-choice questions, with one source specifying it covers nine distinct dimensions and uses MCQ accuracy as its metric. A more detailed definition states it assesses tasks like "instance interaction, text understanding, and spatial relations." SEED-Bench is often used in conjunction with other evaluation tools such as MME and MM-Bench for model comparison and to, as one paper notes, "expose performance limitations of LVLMs" ("Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping"). In at least one instance, its images were used as a source for constructing another benchmark, ConBench.

## Sources

**[Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf)**
> A benchmark used in the paper to evaluate multimodal comprehension performance.

**[Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf) (as "SEEDBench")**
> An evaluation benchmark for Large Vision-Language Models that assesses a broad spectrum of cognitive and comprehension tasks, including instance interaction, text understanding, and spatial relations, through multiple-choice questions.

**[Fine-Grained Verifiers: Preference Modeling as Next-token Prediction in Vision-Language Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/7c1f8ca17d2f0bdf82c73abafb577837-Paper-Conference.pdf) (as "SEEDbench")**
> A comprehensive vision-language benchmark used to evaluate model performance.

**[CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf) (as "SEED")**
> SEED-Bench (SEED) is a benchmark for evaluating multimodal models on their ability to comprehend complex visual scenes.

**[Unveiling the Tapestry of Consistency in Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f094ba0f5ce1720466342f78031bdb-Paper-Conference.pdf) (as "SeedBench")**
> A benchmark for multimodal large language models featuring comprehensive multiple-choice questions, used as a source of images for ConBench.

## Relationships

### → SEED-Bench
- **Visual question answering** (behaviors tasks) — *measured_by*
  > Table 2: Evaluated tasks with corresponding dataset and MLLM. Task Dataset MLLM Captioning COCO Karpathy Test (Karpathy & Fei-Fei, 2015) LLaMA-Adapter (Zhang et al., 2024a) VQA SEED-Bench (Li et al., 2023a) Honeybee (Cha et al., 2024)
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Perception** (constructs) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)

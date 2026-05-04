# ScienceQA
**Type:** Measurement  
**Referenced in:** 77 papers  
**Also known as:** SCIENCEQA  

## State of the Field

ScienceQA is predominantly characterized as a multimodal, multiple-choice question answering benchmark designed to assess reasoning in scientific contexts. The most common definition describes it as a tool for evaluating "scientific reasoning across diverse domains." The provided data indicates that its samples typically contain a question with multiple options, an answer, and both visual and textual contexts, with some sources specifying the inclusion of diagrams, background lectures, and explanations. Across the surveyed literature, ScienceQA is most frequently used to measure the behavior of `Visual question answering (VQA)`. It is also commonly employed to evaluate the construct of `Scientific reasoning`. A smaller set of studies uses it to assess related capabilities such as `Multimodal reasoning`, `Visual reasoning`, and general `Question answering`. One paper notes that while not all questions are accompanied by an image, their evaluation focuses specifically on the subset that is.

## Sources

**[At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)**
> Multiple-choice question answering benchmark assessing scientific reasoning across diverse domains.

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf) (as "SCIENCEQA")**
> A science question-answering benchmark with multiple-choice questions, some accompanied by images and optional lecture/context text.

## Relationships

### → ScienceQA
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We perform Visual Question Answering (VQA) on ScienceQA (Lu et al., 2022), classification on CIFAR-10 (Krizhevsky et al., 2009), captioning on Flickr30K (Young et al., 2014) and facial attribute recognition on CelebA (Liu et al., 2018). (Section 4.1)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)
- **Scientific reasoning** (constructs) — *measured_by*
  > We use the ScienceQA dataset (Lu et al., 2022) to evaluate the scientific reasoning ability of the model. (Section 3.1)
  - [At Which Training Stage Does Code Data Help LLMs Reasoning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c2aa1e456ea543997f6927295196381-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > We directly utilize ScienceQA’s multi-modal training set to fine-tune LLaMA-Adapter, and conduct in-domain testing. (Section 3.3)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > “we follow the datasets and tuning orders of the CoIN benchmark ... including ScienceQA”
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  - [What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf)
- **Scientific question answering** (behaviors tasks) — *measured_by*
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Knowledge reasoning** (constructs) — *measured_by*
  - [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://proceedings.neurips.cc/paper_files/paper/2024/file/01025a4e79355bb37a10ba39605944b5-Paper-Conference.pdf)
- **Perception** (constructs) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > "We utilize 7 widely used multimodal datasets to evaluate the performance, including ... ScienceQA (SQA)"
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)

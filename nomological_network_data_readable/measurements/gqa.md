# GQA
**Type:** Measurement  
**Referenced in:** 82 papers  

## State of the Field

Across the provided literature, GQA is consistently characterized as a benchmark dataset for visual question answering (VQA). Its most frequently noted feature is the evaluation of complex reasoning, with definitions and snippets repeatedly describing its questions as "compositional" and "multi-hop." Several sources specify that the dataset is constructed using scene graph structures and structured or "SQL-like" reasoning paths to generate these complex question-answer pairs about real-world images. The primary use of GQA is to measure `visual question answering` and the broader capabilities of `visual understanding` and `multimodal understanding`. A smaller set of studies also employs GQA to assess more specific constructs, including `compositional reasoning`, `relational reasoning`, `spatial reasoning`, and `visual perception`. It is frequently evaluated alongside other VQA benchmarks such as VQAv2 and OK-VQA, and at least one paper uses it for out-of-domain evaluation.

## Sources

**[CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)**
> A benchmark dataset for compositional visual question answering, featuring complex, multi-hop questions about real-world images.

## Relationships

### → GQA
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “GQA is a popular compositional visual reasoning dataset with synthesis multi-hop questions, making it suitable for multi-step reasoning.”
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > Our method demonstrates superior image understanding capabilities, achieving the 80.0%, 63.0%, 48.6%, 70.9%, and 58.8% performance on VQAv2, GQA, VisWiz, SQAI, and VQAT, respectively.
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > Following LLaVA (Liu et al., 2024b), we evaluate the multimodal understanding capabilities of Show-o on POPE, MME, Flickr30k, VQAv2, GQA, and MMMU benchmarks. (Section 4.1)
  - [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/45f0d179ef7e10eb7366550cd4e574ae-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > we assess the learned generalization ability on OKVQA (Marino et al., 2019), TextVQA (Singh et al., 2019), GQA (Hudson & Manning, 2019), and OCRVQA (Mishra et al., 2019) (Section 4.1).
  - [SearchLVLMs: A Plug-and-Play Framework for Augmenting Large Vision-Language Models by Searching Up-to-Date Internet Knowledge](https://proceedings.neurips.cc/paper_files/paper/2024/file/76954b4a44e158e738b4c64494977c6a-Paper-Conference.pdf)
- **Visual perception** (constructs) — *measured_by*
  > VQA-v2 (Goyal et al., 2017b) and GQA (Hudson & Manning, 2019) assess the visual perception capabilities of models through open-ended short answers. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > “TinyGroundingGPT-3B demonstrates superior image understanding capabilities on the VQAv2, GQA, SQA, and POPE benchmarks”
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Perception** (constructs) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual dialogue** (behaviors tasks) — *measured_by*
  - [Delta-CoMe: Training-Free Delta-Compression with Mixed-Precision for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/37664246a1e07e212ddacea6e5a523f2-Paper-Conference.pdf)
- **Spatial reasoning** (constructs) — *measured_by*
  > GQA Hudson & Manning (2019) validates spatial reasoning
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Answer generation** (behaviors tasks) — *measured_by*
  - [Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.248.pdf)
- **Relational reasoning** (constructs) — *measured_by*
  > “for general VQA tasks, we use VizWiz (Gurari et al., 2018) and GQA (Hudson & Manning, 2019) to test general visual understanding and relational reasoning.”
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > we evaluate its performance using Qwen-2.5-VL-7B (Team, 2025) on 500 multiple-choice samples from both GQA (Hudson and Manning, 2019) and the image-based subset of ScienceQA (Lu et al., 2022).
  - [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-TurnLLMJailbreaks](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  > GQA (Hudson and Manning, 2019) for compositional reasoning and real-world visual understanding (Section 4.1).
  - [Matter-of-Fact: A Benchmark for Verifying the Feasibility of Literature-Supported Claims in Materials Science](https://aclanthology.org/2025.emnlp-main.204.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)

### Associated with
- **Compositional reasoning** (constructs)
  > The GQA problems are more complex and require compositional reasoning to answer
  - [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf)
- **Visual reasoning** (constructs)
  > GQA for visual reasoning and ScienceQA for science knowledge
  - [LogiCoL: Logically-Informed Contrastive Learning for Set-based Dense Retrieval](https://aclanthology.org/2025.emnlp-main.609.pdf)

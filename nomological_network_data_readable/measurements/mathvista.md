# MathVista
**Type:** Measurement  
**Referenced in:** 72 papers  
**Also known as:** MATHVISTA  

## State of the Field

MathVista is predominantly characterized as a benchmark for evaluating mathematical reasoning, specifically within visual or multimodal contexts. Across the provided literature, it is most frequently used to assess the construct of `mathematical reasoning`, with some papers also using it to measure `visual reasoning`, `multimodal reasoning`, and `commonsense knowledge`. The benchmark is operationalized through what one paper describes as "puzzles that involve images" (Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads), requiring a joint understanding of visual data like diagrams and quantitative problem-solving. One source further specifies that it categorizes problems by reasoning type—such as logical, arithmetic, and geometric—and by image context, including natural images and scientific figures. A recurring focus in several papers is its geometry problem-solving task, which is sometimes evaluated on a specific "testmini" split. While its primary focus is mathematical, one paper notes that the benchmark also includes "general visual question answering tasks" (Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging). In addition to its use as an evaluation tool, MathVista is also cited as a data source in at least one instance.

## Sources

**[Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "MATHVISTA")**
> A benchmark for mathematical reasoning in LVLMs that involves puzzles with images and categorizes problems by reasoning type and image context.

**[G-LLaVA: Solving Geometric Problem with Multi-Modal Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/09afabe33dc7db66530dea6483b22e5d-Paper-Conference.pdf)**
> A benchmark for evaluating mathematical reasoning capabilities of large models, which includes a specific task for geometry problem solving.

## Relationships

### → MathVista
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Evaluating Large Vision-and-Language Models on Children's Mathematical Olympiads](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc12fb3d4033ad72d33a51f1d0ab5d0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > We perform experiments on two widely used multimodal mathematical reasoning benchmarks: MATHVISTA (Lu et al., 2024b) and WE-MATH (Qiao et al., 2024). (Section 4.1)
  - [RAG-Critic: Leveraging Automated Critic-Guided Agentic Workflow for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.180.pdf)
- **Chart and diagram understanding** (behaviors tasks) — *measured_by*
  - [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [Enhancing Large Vision Language Models with Self-Training on Image Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf)

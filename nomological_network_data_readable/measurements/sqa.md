# SQA
**Type:** Measurement  
**Referenced in:** 18 papers  

## State of the Field

Across the provided literature, the acronym "SQA" refers to at least three distinct benchmarks, with one usage being most prevalent. The most common framing identifies SQA as the Science Question Answering (or ScienceQA) dataset, a vision-language benchmark for answering science questions that require complex reasoning and often involve a diagram. In this context, SQA is frequently used to measure `visual question answering` and `multimodal reasoning`, as well as `visual understanding` and `scientific knowledge`. A smaller line of work, however, uses SQA to denote the Sequential Question Answering dataset, which is described as a benchmark for multi-turn, table-based question answering. A third, distinct usage appears in one paper where SQA refers to a benchmark for `3D question answering` based on over 650 indoor scenes. This 3D QA version is noted to include questions about `spatial relationships`.

## Sources

**[Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/08487598819cba9feca884ef0d442950-Paper-Conference.pdf)**
> The Science Question Answering (SQA) dataset, which involves answering science questions that require complex reasoning and often an accompanying diagram.

## Relationships

### → SQA
- **Visual question answering** (behaviors tasks) — *measured_by*
  > we evaluate γ-MoD on six image question answering benchmarks: VQAv2 (Goyal et al., 2017), VizWiz (Gurari et al., 2018), TextVQA (Singh et al., 2019), SQA (Lu et al., 2022), GQA (Hudson & Manning, 2019) and SEED (Ge et al., 2023). (Section 5.1)
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > We evaluate LWM on standard benchmarks for image and short video understanding, with results presented in Table 5. (Section 4.3.2)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **Spoken question answering** (behaviors tasks) — *measured_by*
  > “the model is fine-tuned using both our curated speech question answering (SQA) dataset and the original visual question answering (VQA) datasets from LLaVA”
  - [VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.248.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Instance-Selection-Inspired Undersampling Strategies for Bias Reduction in Small and Large Language Models for Binary Text Classification](https://aclanthology.org/2025.acl-long.459.pdf)
- **3D question answering** (behaviors tasks) — *measured_by*
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)

### Associated with
- **Spatial reasoning** (constructs)
  > It encompasses a diverse range of question types, including object identification, spatial relationships, scene-level understanding, and general reasoning. (Section 5)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)

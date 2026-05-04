# MMMU
**Type:** Measurement  
**Referenced in:** 89 papers  
**Also known as:** MMMU Validation Set, MMMU Benchmark  

## State of the Field

Across the surveyed literature, MMMU is consistently described as a massive, multi-discipline, and multimodal benchmark. Its prevailing use is to evaluate models on complex tasks requiring expert, college-level knowledge and reasoning across a wide range of academic domains, as one paper notes it contains "challenging college-level subject questions." The benchmark is most frequently employed to measure `multimodal understanding`, `visual understanding`, and general `reasoning` abilities. Papers also use it to assess more specific capabilities, including `visual question answering`, `logical reasoning`, and even the analysis of scientific diagrams. In practice, researchers commonly evaluate models using the multiple-choice questions from the MMMU validation set, often in conjunction with other instruments like MMBench and MME. While its primary function is evaluative, one study reports a strong correlation between model performance on MMMU and `hallucination` rates. Although almost universally defined as a general "understanding" benchmark, a single paper refers to it as a "Mathematics Understanding" benchmark, representing a minority framing. Overall, the data positions MMMU as a comprehensive instrument for assessing advanced, knowledge-intensive capabilities in vision-language models.

## Sources

**[Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf)**
> MMMU (Yue et al., 2024) is a massive multi-discipline multimodal understanding benchmark used to evaluate the general performance of Vision-Language Assistants after applying debiasing methods.

**[COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf) (as "MMMU Validation Set")**
> The validation set of the Massively Multitask Multimodal Understanding benchmark, which evaluates models on college-level problems requiring expert knowledge across various domains.

**[2025.emnlp-main.263.checklist](https://aclanthology.org/attachments/2025.emnlp-main.263.checklist.pdf) (as "MMMU Benchmark")**
> MMMU Benchmark is a multimodal benchmark referenced as an existing artifact used in the paper's evaluation context.

## Relationships

### → MMMU
- **Multimodal understanding** (constructs) — *measured_by*
  > General Multimodal Tasks. MMMU (Yue et al., 2024a), MMBench (Liu et al., 2023b) and VQA-V2 (Goyal et al., 2017). We also include RefCOCO+(REC) (Yu et al., 2016) to evaluate the grounding capability in natural image scenarios.
  - [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > We further validate our findings in a multi-modal setting using the vision-language model LLaVa (Liu et al., 2023) on the MMMU (Yue et al., 2024) visual question answering benchmark, see Appendix A.8. (Section 3.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > “For image understanding, we evaluate LLaVA-1.5 and LLaVA-NeXT on (a) diverse multimodal benchmarks: POPE (Li et al., 2023c), GQA (Hudson & Manning, 2019), MMBench (Liu et al., 2023b), VizWiz (Gurari et al., 2018), SEEDBench (Li et al., 2023a), ScienceQA (Lu et al., 2022), MMMU (Yue et al., 2024)”
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  > The experimental results on MMMU demonstrate that MIA-DPO enhances the LLaVA-v1.5’s reasoning ability on multi-image problems. (Section 4.2)
  - [Benchmarking Generative Models on Computational Thinking Tests in Elementary Visual Programming](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d5e00006b65fcc55c3c1798da821663-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
- **Multi-image reasoning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Hallucination** (behaviors tasks) — *correlates*
  > We also include self-reported MMMU (Yue et al., 2024) results to demonstrate their significant correlation with hallucination rates: the Pearson correlation between −log HT and MMMU score is 0.902 with a p-value of 3.45×10−4. (Table 2)
  - [TLDR: Token-Level Detective Reward Model for Large Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70217f4d06e57a2395f03b4bc136361a-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > MMMU (Yue et al., 2024), which tests multimodal models on large-scale multidisciplinary tasks requiring advanced subject matter knowledge and reasoning skills. (Section 3.1)
  - [TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf)
- **Multi-image understanding** (constructs) — *measured_by*
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)
- **Chart and diagram understanding** (behaviors tasks) — *measured_by*
  > To align our research focus, we conduct experiments on several sub-categories of MMMU that consists exclusively of scientific diagrams (Section 4).
  - [Chain-of-region: Visual Language Models Need  Details for Diagram Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/464012c83279e19be4cd42c25f341c92-Paper-Conference.pdf)
- **Multiple-choice visual question answering** (behaviors tasks) — *measured_by*
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
- **Fine-grained understanding** (constructs) — *measured_by*
  - [ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering](https://aclanthology.org/2025.emnlp-main.55.pdf)
- **Cognitive ability** (constructs) — *measured_by*
  > we use scores from the MMMU benchmark (Yue et al., 2024) as an indicator of models’ cognitive ability, as MMMU is specifically designed to evaluate comprehensive cognitive skills of MLLMs. (Section 6)
  - [Understanding the Modality Gap: An Empirical Study on the Speech-Text Alignment Mechanism of Large Speech Language Models](https://aclanthology.org/2025.emnlp-main.263.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [RAVEN: Query-Guided Representation Alignment for Question Answering over Audio, Video, Embedded Sensors, and Natural Language](https://aclanthology.org/2025.emnlp-main.97.pdf)

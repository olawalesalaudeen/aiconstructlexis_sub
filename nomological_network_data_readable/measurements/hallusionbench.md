# HallusionBench
**Type:** Measurement  
**Referenced in:** 20 papers  

## State of the Field

HallusionBench is consistently defined and used as a benchmark for assessing hallucination in multimodal and vision-language models. Its primary application is to measure several specific forms of this phenomenon, with papers stating that it evaluates "object illusion," "visual hallucinations," "language hallucinations," and "knowledge hallucinations." One paper specifies its focus is on "understanding visually misleading figures." The benchmark is operationalized as a visual question answering (VQA) task, with one source noting it contains 346 images and 1129 questions, while another mentions it evaluates across dimensions like question type and difficulty. While its main purpose is hallucination detection, a smaller number of papers also employ HallusionBench to evaluate broader capabilities such as "Visual question answering" and "Visual reasoning." In practice, it is frequently used in evaluation suites alongside other hallucination-focused instruments like POPE and CHAIR.

## Sources

**[Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)**
> HallusionBench is a benchmark for assessing hallucination in multimodal models.

## Relationships

### → HallusionBench
- **Hallucination** (behaviors tasks) — *measured_by*
  > We evaluate our each variant of ROSS mainly on (i) hallucination: POPE (Li et al., 2023c) and HallusionBench (Guan et al., 2024) (Section 5.1)
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Factuality** (constructs) — *measured_by*
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “Additionally, we evaluate performance on specific-domain VQA tasks, which include ChartQA (Masry et al., 2022), LLaVABench (Liu et al., 2024c), and HallusionBench (Guan et al., 2023).” (Section 4.1)
  - [Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25am/wu25am.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > "we conduct experiments across four benchmarks: Multi-modal Large Language Model Evaluation (MME) (Yin et al., 2023) , Massive Multi-discipline Multi-modal Understanding and Reasoning (MMMU) (Yue et al., 2023), MathVista (Wang et al., 2024), and HallusionBench (Liu et al., 2023a)"
  - [When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using SmallVLMs](https://aclanthology.org/2025.emnlp-main.1614.pdf)

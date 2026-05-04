# NLVR2
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

NLVR2 is consistently characterized across the provided literature as a benchmark for evaluation. The prevailing usage of NLVR2 is to measure 'visual reasoning' and 'multi-image understanding', with some work also using it to assess the broader capability of 'visual understanding'. The benchmark's structure is defined by its use of 'pairs of real-world photographs' and 'natural language statements'. This operationalizes the evaluation task as reasoning over these 'paired visual inputs' to determine the veracity of a related statement. In practice, it is cited as one of several 'multi-image benchmarks' used in model evaluations, as highlighted in the paper "MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models".

## Sources

**[HEMM: Holistic Evaluation of Multimodal Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b6e5dae3acb4cfdfe5928a6eff174ee-Paper-Datasets_and_Benchmarks_Track.pdf)**
> An extension of the NLVR dataset that uses pairs of real-world photographs and natural language statements to test visual reasoning.

## Relationships

### → NLVR2
- **Multi-image understanding** (constructs) — *measured_by*
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)

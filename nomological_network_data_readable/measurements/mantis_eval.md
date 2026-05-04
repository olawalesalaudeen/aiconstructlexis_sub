# Mantis-Eval
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** Mantis, MANTIS  

## State of the Field

Mantis-Eval is predominantly characterized as an evaluation dataset or benchmark for assessing model performance on multi-image inputs. Across the provided literature, it is most frequently used to measure "multi-image understanding" and "multi-image reasoning," with some papers also using it to evaluate broader capabilities like "visual question answering" and "multimodal reasoning." The benchmark is described as a human-annotated set of 207 examples designed to test diverse skills. For instance, one paper notes it targets "size perceptions and weight comparisons," while another states it is designed for skills such as "co-reference, reasoning, and comparison." This usage for performance comparison is a recurring theme, as seen in one study that compares various VLMs on the dataset. A contrasting view appears in a single paper where "MANTIS" is defined not as an evaluation tool, but as a multimodal instruction-tuning dataset used for continual training.

## Sources

**[JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf)**
> An evaluation dataset for multi-image visual reasoning used for performance comparison.

**[MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf) (as "Mantis")**
> A multi-image benchmark used to assess performance on multi-image inputs.

**[Adapt-$\infty$: Scalable Continual Multimodal Instruction Tuning via Dynamic Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf) (as "MANTIS")**
> A multimodal instruction-tuning dataset used as one timestep in the continual training sequence.

## Relationships

### → Mantis-Eval
- **Multi-image understanding** (constructs) — *measured_by*
  > First, we select five multi-image benchmarks: MMMU (Yue et al., 2024), BLINK (Fu et al., 2024), Mantis (Jiang et al., 2024), NLVR2 (Suhr et al., 2018), and MVBench (Li et al., 2024c). (Section 4.1)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **Multi-image reasoning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Understanding** (constructs) — *measured_by*
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)

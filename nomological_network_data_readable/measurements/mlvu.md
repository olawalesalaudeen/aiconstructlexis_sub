# MLVU
**Type:** Measurement  
**Referenced in:** 11 papers  

## State of the Field

MLVU is consistently characterized across the provided literature as a benchmark for evaluating model capabilities on long videos. Its most prevalent application is to measure `video understanding`, with several papers specifying its use for assessing "long video understanding ability" on content ranging from three minutes to two hours. The benchmark is operationalized through question-answering tasks; it is defined as a "multi-task video understanding benchmark" that evaluates models on "diverse question-answering tasks," with one definition noting it assesses "multiple-choice performance." Consequently, a number of papers also explicitly use MLVU to measure `video question answering`. A less frequent application, mentioned in one paper, is the measurement of `multimodal understanding`, where its full name is cited as "Multi-Task Long Video Understanding."

## Sources

**[Exploring the Design Space of Visual Context Representation in Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/24e2320097bdf179e2b2719c6df2f448-Paper-Conference.pdf)**
> A long-video understanding benchmark used to evaluate multiple-choice performance on video understanding tasks.

## Relationships

### → MLVU
- **Video understanding** (constructs) — *measured_by*
  > We select several long video understanding benchmarks for evaluation, including Event-Bench (Du et al., 2024) (only with the challenging episodic reasoning task), VNBench (Zhao et al., 2024), MLVU (Zhou et al., 2024), and VideoMME (Fu et al., 2024). (Section 2)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks) — *measured_by*
  > To evaluate FRAME-VOYAGER, we plug it into two versions of the state-of-the-art Video-LLM named VILA (VILA-8B and VILA-40B, Lin et al. (2024b)) and conduct experiments on four widely-used Video Question Answering benchmarks, Video-MME (Fu et al., 2024a), MLVU (Zhou et al., 2024), NextQA (Xiao et al., 2021) and ActivityNet-QA (Yu et al., 2019). (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Oryx MLLM: On-Demand Spatial-Temporal Understanding at Arbitrary Resolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/d480a9c2164e76e40ae03076e9d5b6d8-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > In Table 6, we provide results zero-shot transferring to the computer vision domain, evaluating NAMMs with a Llava Next Video 7B model (Zhang et al., 2024b) on LongVideoBench (Wu et al., 2024) and Multi-Task Long Video Understanding (MLVU) (Zhou et al., 2024). (Section 4.2)
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)

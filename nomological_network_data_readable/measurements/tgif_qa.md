# TGIF-QA
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, TGIF-QA is consistently used as a benchmark to measure the behavior of video question answering. A single paper also frames it as a tool for evaluating the broader capability of video understanding. The benchmark is uniformly described as being based on animated GIFs from the Tumblr GIF (TGIF) dataset. There is some variation in its stated focus; one definition specifies that it targets tasks like "repetition counting and state transition recognition," while a more common framing across two other papers is that it is designed to assess "temporal and causal reasoning" in short video clips. In practice, it is frequently deployed alongside other video QA benchmarks such as MSVD-QA, MSRVTT-QA, and ActivityNet-QA. One source snippet further characterizes it as an "open-ended" benchmark.

## Sources

**[Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)**
> A video question answering benchmark based on the Tumblr GIF (TGIF) dataset, focusing on tasks like repetition counting and state transition recognition.

## Relationships

### → TGIF-QA
- **Video question answering** (behaviors tasks) — *measured_by*
  > ...as well as four video QA benchmarks: MVSD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2016), TGIF-QA (Jang et al., 2017), and ActivityNet-QA (Caba Heilbron et al., 2015). (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **Video understanding** (constructs) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)

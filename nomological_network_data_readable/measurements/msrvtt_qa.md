# MSRVTT-QA
**Type:** Measurement  
**Referenced in:** 15 papers  
**Also known as:** MSRVTTQA  

## State of the Field

MSRVTT-QA is consistently characterized across the provided literature as a benchmark used to measure the behavior of video question answering. All definitions state that it is derived from or based on the MSR-VTT dataset. The prevailing usage is to evaluate a model's general comprehension of video content through associated questions. A more specific framing, found in one paper, describes it as an "open-ended video question answering benchmark" that assesses "zero-shot generalization in video understanding" ("SoundMind:RL-Incentivized Logic Reasoning for Audio-Language Models"). In practice, papers frequently use MSRVTT-QA for evaluation alongside other instruments like MSVD-QA, ActivityNet-QA, and TGIF-QA. The benchmark is also shown to be used in few-shot evaluation settings, as one study reports a "4-shot" performance comparison ("Emu: Generative Pretraining in Multimodality").

## Sources

**[AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)**
> A video question answering benchmark derived from the MSR-VTT dataset.

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf) (as "MSRVTTQA")**
> Video question answering benchmark based on MSRVTT, testing comprehension of video content with associated questions.

## Relationships

### → MSRVTT-QA
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate AURORACAP on MSVD-QA (Xu et al., 2017), ActivityNet-QA (Yu et al., 2019), MSRVTT-QA (Xu et al., 2017), and iVQA (Yang et al., 2021) for video question answering tasks as shown in Table 4. (Section 2.3)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **Video understanding** (constructs) — *measured_by*
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)

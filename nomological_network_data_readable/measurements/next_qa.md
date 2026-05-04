# NExT-QA
**Type:** Measurement  
**Referenced in:** 20 papers  
**Also known as:** Next-QA  

## State of the Field

Across the provided literature, NExT-QA is consistently characterized as a video question answering (VideoQA) benchmark. Its primary stated purpose is to evaluate specific reasoning capabilities, with nearly all definitions highlighting its focus on causal and temporal reasoning; a smaller number of sources also mention descriptive reasoning. The benchmark is operationalized as a multiple-choice question answering task where models must answer questions about video events, often involving everyday activities with complex dependencies. Papers frequently use NExT-QA to measure the broader constructs of `Video understanding` and `Video question answering`. While several sources describe it as a tool for evaluating long-video understanding, one paper notes its videos have an average duration of 44 seconds. It is often evaluated alongside other VideoQA instruments such as MSVD-QA, STAR, and Perception Test, and one source notes the existence of a subset, NExT-GQA, which includes timestamp annotations.

## Sources

**[Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)**
> NExT-QA is a video question answering benchmark used to evaluate long-video understanding, including causal and temporal reasoning.

**[On Behalf of the Stakeholders: Trends inNLPModel Interpretability in the Era ofLLMs](https://aclanthology.org/2025.naacl-long.30.pdf) (as "Next-QA")**
> Video question answering benchmark requiring causal and temporal reasoning to answer questions about video events.

## Relationships

### → NExT-QA
- **Video question answering** (behaviors tasks) — *measured_by*
  > We evaluate on two video question answering datasets focused on long-form videos: EgoSchema (Mangalam et al., 2023) and NExT-QA (Xiao et al., 2021). (Section 5)
  - [CREMA: Generalizable and Efficient Video-Language Reasoning via Multimodal Modular Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9079234614422c036c5a92bb8ec04c4-Paper-Conference.pdf)
- **Video understanding** (constructs) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
- **Causal reasoning** (constructs) — *measured_by*
  - [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by ModellingMiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.82.pdf)
- **Temporal reasoning** (constructs) — *measured_by*
  - [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by ModellingMiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.82.pdf)

# Video question answering
**Type:** Behavior  
**Referenced in:** 64 papers  
**Also known as:** Tideo question answering, Long-video question answering  

## State of the Field

Across the provided literature, video question answering is predominantly defined as the task of answering natural language questions that require understanding the dynamic visual and temporal content of a video. The field operationalizes this behavior using a wide array of benchmarks, with ActivityNet-QA, MSVD-QA, MSR-VTT-QA, NExT-QA, and TGIF-QA being the most frequently cited instruments for evaluation. The task format varies across studies; it is commonly set up as either a multiple-choice selection problem or an open-ended text generation task. A specific sub-task, long-video question answering, is also identified, while a less common variant, "Tideo question answering," is described in one paper as a pre-alignment task using textual representations of videos. One paper notes a common implementation strategy is to "sample frames uniformly from a video, thereby recasting the problem as a task to understand multi-image sequences" ("SurveyPilot: an Agentic Framework for Automated Human Opinion Collection from Social Media"). However, another study points out that models can "struggle with video question answering when the question and answer correspond to different time segments" ("ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos"). This behavior is studied alongside video understanding, instruction following, spatial understanding, and uncertainty handling.

## Sources

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)**
> Answering questions that require understanding of dynamic visual content from videos.

**[TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf) (as "Tideo question answering")**
> A pre-alignment task where the model answers a question based on the content of a "textual video" (Tideo).

**[Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf) (as "Long-video question answering")**
> Answering questions about long videos, typically by selecting among candidate answers or generating a textual response.

## Relationships

### Video question answering →
- **ActivityNet-QA** (measurements) — *measured_by*
  > We evaluate AURORACAP on MSVD-QA (Xu et al., 2017), ActivityNet-QA (Yu et al., 2019), MSRVTT-QA (Xu et al., 2017), and iVQA (Yang et al., 2021) for video question answering tasks as shown in Table 4. (Section 2.3)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **MSVD-QA** (measurements) — *measured_by*
  > We evaluate AURORACAP on MSVD-QA (Xu et al., 2017), ActivityNet-QA (Yu et al., 2019), MSRVTT-QA (Xu et al., 2017), and iVQA (Yang et al., 2021) for video question answering tasks as shown in Table 4. (Section 2.3)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **MSRVTT-QA** (measurements) — *measured_by*
  > We evaluate AURORACAP on MSVD-QA (Xu et al., 2017), ActivityNet-QA (Yu et al., 2019), MSRVTT-QA (Xu et al., 2017), and iVQA (Yang et al., 2021) for video question answering tasks as shown in Table 4. (Section 2.3)
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **Video-MME** (measurements) — *measured_by*
  > We consider two multiple-choice VideoQA datasets: Video-MME (VMME) (Fu et al., 2024) and NExT-QA (Xiao et al., 2021)), and two open-ended VideoQA datasets (e.g., MUSIC-AVQA (Li et al., 2022a) and MSVD (Chen & Dolan, 2011))
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **NExT-QA** (measurements) — *measured_by*
  > We evaluate on two video question answering datasets focused on long-form videos: EgoSchema (Mangalam et al., 2023) and NExT-QA (Xiao et al., 2021). (Section 5)
  - [CREMA: Generalizable and Efficient Video-Language Reasoning via Multimodal Modular Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9079234614422c036c5a92bb8ec04c4-Paper-Conference.pdf)
- **TGIF-QA** (measurements) — *measured_by*
  > ...as well as four video QA benchmarks: MVSD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2016), TGIF-QA (Jang et al., 2017), and ActivityNet-QA (Caba Heilbron et al., 2015). (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **EgoSchema** (measurements) — *measured_by*
  > We evaluate on two video question answering datasets focused on long-form videos: EgoSchema (Mangalam et al., 2023) and NExT-QA (Xiao et al., 2021). (Section 5)
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
- **NExTQA** (measurements) — *measured_by*
  > We evaluate Emu on a broad range of vision-language tasks including image captioning (MS-COCO (Chen et al., 2015)), image question answering (VQAv2 (Goyal et al., 2017), OKVQA (Marino et al., 2019), VizWiz (Gurari et al., 2018)), visual dialog (VisDial (Das et al., 2017)), video question answering (MSRVTTQA (Xu et al., 2017), MSVDQA (Xu et al., 2017), NextQA (Xiao et al., 2021)) and text2image generation(MS-COCO (Lin et al., 2014)).
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **MLVU** (measurements) — *measured_by*
  > To evaluate FRAME-VOYAGER, we plug it into two versions of the state-of-the-art Video-LLM named VILA (VILA-8B and VILA-40B, Lin et al. (2024b)) and conduct experiments on four widely-used Video Question Answering benchmarks, Video-MME (Fu et al., 2024a), MLVU (Zhou et al., 2024), NextQA (Xiao et al., 2021) and ActivityNet-QA (Yu et al., 2019). (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Video-ChatGPT benchmark** (measurements) — *measured_by*
  - [Artemis:  Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > The second method involves models freely generating answers, which are then evaluated by GPT-4. Given the question, correct answer, and model’s prediction, GPT-4 returns a True or False judgment.
  - [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf)
- **MVSD-QA** (measurements) — *measured_by*
  > ...as well as four video QA benchmarks: MVSD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2016), TGIF-QA (Jang et al., 2017), and ActivityNet-QA (Caba Heilbron et al., 2015). (Section 4.2)
  - [Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf)
- **TempCompass** (measurements) — *measured_by*
  > Examples of several VideoQA benchmarks. We examine four existing representative benchmarks and ours: VITATECS, MVBench, TempCompass, ReXTime, and TOMATO.
  - [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://proceedings.iclr.cc/paper_files/paper/2025/file/e789cfc9389048df4a0a44d4086e0dc2-Paper-Conference.pdf)
- **LongVideoBench** (measurements) — *measured_by*
  > We also evaluate MVU on the LongVideoBench dataset which contains even longer videos (Section 5.1)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **MUSIC-AVQA** (measurements) — *measured_by*
  > We consider two multiple-choice VideoQA datasets: Video-MME (VMME) (Fu et al., 2024) and NExT-QA (Xiao et al., 2021)), and two open-ended VideoQA datasets (e.g., MUSIC-AVQA (Li et al., 2022a) and MSVD (Chen & Dolan, 2011))
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **MSVD** (measurements) — *measured_by*
  > We consider two multiple-choice VideoQA datasets: Video-MME (VMME) (Fu et al., 2024) and NExT-QA (Xiao et al., 2021)), and two open-ended VideoQA datasets (e.g., MUSIC-AVQA (Li et al., 2022a) and MSVD (Chen & Dolan, 2011))
  - [Sample then Identify: A General Framework for Risk Control and Assessment in Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1722a6bd1023c026a3d6a570fb3af75-Paper-Conference.pdf)
- **STAR** (measurements) — *measured_by*
  > We evaluate the LTR framework on 11 VideoQA benchmarks, including... STAR (Wu et al., 2023)... (Section 4.1)
  - [Modularized Self-Reflected Video Reasoner for Multimodal LLM with Application to Video Question Answering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/song25g/song25g.pdf)
- **MSR-VTT-QA** (measurements) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [$\mathcalVista\mathcalDPO$: Video Hierarchical Spatial-Temporal Direct Preference Optimization for Large Video Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25g/huang25g.pdf)

### Associated with
- **Temporal reasoning** (constructs)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Causal reasoning** (constructs)
  - [Understanding Long Videos with Multimodal Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f591824a3bd840f74947fcda304c945-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Video understanding** (constructs)
  > When it comes to video question answering (VideoQA), models must not only capture the static features in frames but also understand temporal dynamics, such as object movements and interactions over time, especially in 3D space. (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Instruction following** (constructs)
  > In some failure cases observed in the model, we found that prompting the model to generate a comprehensive caption for the video input can lead to outputs that include the correct answer. This phenomenon may be attributed to a disruption in the model's instruction-following capabilities during the training.
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
- **Video summarization** (behaviors tasks)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Spatial understanding** (constructs)
  > We annotate 98 videos and provide 882 question-answer pairs that target three types of questions: 1) descriptive questions regarding the attributes of the objects (colour, shape, number), 2) spatial Understanding about the position of items and their relation to other items, and 3) adversarial questions about items not present in the video.
  - [Dehumanizing Machines: Mitigating Anthropomorphic Behaviors in Text Generation Systems](https://aclanthology.org/2025.acl-long.1260.pdf)
- **Uncertainty handling** (constructs)
  > Adversarial questions, which cannot be answered based on the information provided in the video, help assess whether models hallucinate responses or can reliably acknowledge uncertainty—a critical safety feature for assistive technologies.
  - [Dehumanizing Machines: Mitigating Anthropomorphic Behaviors in Text Generation Systems](https://aclanthology.org/2025.acl-long.1260.pdf)

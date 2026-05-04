# Video understanding
**Type:** Construct  
**Referenced in:** 54 papers  
**Also known as:** Long video comprehension, Video comprehension, Long-video understanding, Long video understanding, Long-range video understanding, Impossible video understanding  

## State of the Field

Across the surveyed literature, "Video understanding" is most commonly defined as a model's ability to comprehend and interpret the content, context, and events within a video, with some papers using "video comprehension" interchangeably. While many sources frame this as a latent ability, a smaller set of papers defines it as an observable task, such as generating descriptions or answering questions. A distinct line of work focuses on "long video understanding," which specifically involves reasoning over extended sequences, plots, and temporal dynamics. One paper introduces a specialized variant, "impossible video understanding," defined as the ability to detect and explain counterfactual events.

The field operationalizes this construct primarily through performance on a wide array of video question answering benchmarks. The most frequently used instruments to measure video understanding are Video-MME, EgoSchema, MVBench, and MLVU. Other commonly cited evaluation datasets include ActivityNet-QA, LongVideoBench, and MSVD-QA. Several papers explicitly state that benchmarks like MLVU and Video-MME, which feature videos ranging from minutes to hours, are used to assess the specific ability of "long video understanding." The construct is studied alongside related tasks like video question answering and video detailed captioning, and some work suggests it is influenced by capabilities such as temporal video grounding.

## Sources

**[Vript: A Video Is Worth Thousands of Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/6903a5aaece71b76623245fc6e32f01b-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The ability of a model to comprehend and interpret the content, context, and events within a video.

**[Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf) (as "Video comprehension")**
> The general capability of a model to understand and interpret the content of a video.

**[Teaching Human Behavior Improves Content Understanding Abilities Of VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/f0d8e47e50fa0ef219c61d6fb9f2a4b3-Paper-Conference.pdf) (as "Long video comprehension")**
> The capacity to understand and reason over extended video sequences, including plot, relationships, and temporal dynamics.

**[$∞$-Video: A Training-Free Approach to Long Video Understanding via Continuous-Time Memory Consolidation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/santos25a/santos25a.pdf) (as "Long-video understanding")**
> The ability of a model to process, comprehend, and reason about video content that extends beyond a short time frame, often requiring the integration of information over long durations.

**[Artemis:  Towards Referential Understanding in Complex Videos](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8ec6e5eb9b52bae998dc534713848d-Paper-Conference.pdf) (as "Long video understanding")**
> The task of processing and comprehending videos that are significantly longer than typical short clips, often by segmenting the video and summarizing the content of each segment.

**[Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf) (as "Long-range video understanding")**
> Comprehending and reasoning over extended video sequences.

**[Impossible Videos](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25a/bai25a.pdf) (as "Impossible video understanding")**
> The observable ability of a model to detect, classify, or explain why a video depicts an impossible or counterfactual event, based on visual and temporal analysis.

## Relationships

### Video understanding →
- **Video-MME** (measurements) — *measured_by*
  > in the video understanding benchmark Video-MME (Fu et al., 2024)
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **EgoSchema** (measurements) — *measured_by*
  > “and (b) multi-choice video question answering benchmarks: NExT-QA (Xiao et al., 2021), IntentQA (Li et al., 2023b), and EgoSchema (Mangalam et al., 2024).”
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
- **MVBench** (measurements) — *measured_by*
  > We evaluate LLaVA-Mini on image and video understanding tasks. Experiments are conducted on 11 image benchmarks and 7 video benchmarks... Table 3: Performance on MVBench
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MLVU** (measurements) — *measured_by*
  > We select several long video understanding benchmarks for evaluation, including Event-Bench (Du et al., 2024) (only with the challenging episodic reasoning task), VNBench (Zhao et al., 2024), MLVU (Zhou et al., 2024), and VideoMME (Fu et al., 2024). (Section 2)
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **ActivityNet-QA** (measurements) — *measured_by*
  > Specifically, we showcased Dolphin’s comparison with various methods on MSR-VTT-QA, MSVD-QA, and ActivityNet-QA benchmarks. (Section 5.2)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **LongVideoBench** (measurements) — *measured_by*
  > We also evaluate the performance of mPLUG-Owl3 on video and multi-image benchmarks (including NextQA (Xiao et al., 2021), MVBench (Li et al., 2023c) VideoMME (Fu et al., 2024a), LongVideoBench (Wu et al., 2024) and MLVU (Zhou et al., 2024)), as it is capable of processing multiple images with an interleaved format.
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **MSVD-QA** (measurements) — *measured_by*
  > Specifically, we showcased Dolphin’s comparison with various methods on MSR-VTT-QA, MSVD-QA, and ActivityNet-QA benchmarks. (Section 5.2)
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **MSRVTT-QA** (measurements) — *measured_by*
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **NExT-QA** (measurements) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [Streaming Long Video Understanding with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ce06e9293c3d8e6cb3f80b4157f875-Paper-Conference.pdf)
- **TempCompass** (measurements) — *measured_by*
  > we adopt the fine-grained temporal understanding benchmark, TempCompass (Liu et al., 2024b) (Multiple-Choice subset), diagnosing multi-facet basic video temporal understanding abilities. (Section 4.1)
  - [ShareGPT4Video: Improving Video Understanding and Generation with Better Captions](https://proceedings.neurips.cc/paper_files/paper/2024/file/22a7476e4fd36818777c47e666f61a41-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMBench-Video** (measurements) — *measured_by*
  > In addition, we rigorously assess the performance of our Video-UTR on the recently introduced and exceptionally demanding long-range video understanding benchmark, MVBench-Video. (Section 4.4)
  - [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Perception Test** (measurements) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Event-Bench** (measurements) — *measured_by*
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **VNBench** (measurements) — *measured_by*
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Video-ChatGPT benchmark** (measurements) — *measured_by*
  - [Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)
- **TVQA** (measurements) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **NExTQA** (measurements) — *measured_by*
  - [mPLUG-Owl3: Towards Long Image-Sequence Understanding in Multi-Modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f50f282a3093d36471008b045bd478af-Paper-Conference.pdf)
- **MVSD-QA** (measurements) — *measured_by*
  > we show that while Video-LLMs show a steady increase in performance on standard video understanding and QA benchmarks (MVSD-QA (Xu et al., 2017b), MSRVTT-QA (Xu et al., 2016), ActivityNet-QA (Yu et al., 2019)), their performance on our unanswerable question evaluation benchmark highlights a contrasting outcome (Figure 1-(a)).
  - [Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d77402f07113388562f5b51eaee89573-Paper-Conference.pdf)
- **MSVD** (measurements) — *measured_by*
  > We evaluate LWM on standard benchmarks for image and short video understanding, with results presented in Table 5.
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **MSRVTT** (measurements) — *measured_by*
  > We evaluate LWM on standard benchmarks for image and short video understanding, with results presented in Table 5.
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **TGIF** (measurements) — *measured_by*
  > We evaluate LWM on standard benchmarks for image and short video understanding, with results presented in Table 5.
  - [World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf)
- **TGIF-QA** (measurements) — *measured_by*
  > We evaluate our model on a comprehensive suite of video understanding benchmarks, including the open-ended MSVD-QA (Xu et al., 2017), MSRVTT-QA (Xu et al., 2017), TGIF (Jang et al., 2017), and ActivityNet-QA (Yu et al., 2019), as well as the multiple-choice benchmarks NExT-QA (Xiao et al., 2021), VLEP (Lei et al., 2020), TVQA (Lei et al., 2018), and Perception Test (Pătrăucean et al., 2023).
  - [Unifying Specialized Visual Encoders for Video Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chung25a/chung25a.pdf)
- **InfiniBench** (measurements) — *measured_by*
  - [3DS: Medical Domain Adaptation ofLLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.984.pdf)

### → Video understanding
- **Temporal video grounding** (behaviors tasks) — *causes*
  - [TimeSuite: Improving MLLMs for Long Video Understanding via Grounded Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e8309c9ca683e11672e3dbcd4b87776-Paper-Conference.pdf)
- **Temporal reasoning** (constructs) — *causes*
  - [Temporal Reasoning Transfer from Text to Video](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7eecb72574b043ad0c69ea296212450-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [EmoDynamiX: Emotional Support Dialogue Strategy Prediction by ModellingMiXed Emotions and Discourse Dynamics](https://aclanthology.org/2025.naacl-long.82.pdf)

### Associated with
- **Video question answering** (behaviors tasks)
  > When it comes to video question answering (VideoQA), models must not only capture the static features in frames but also understand temporal dynamics, such as object movements and interactions over time, especially in 3D space. (Section 1)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **Video detailed captioning** (behaviors tasks)
  > Video detailed captioning is a key task which aims to generate comprehensive and coherent textual descriptions of video content, benefiting both video understanding and generation. (Abstract)
  - [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aebc17b683792a17dd4a24fcb038ba6-Paper-Conference.pdf)
- **Long-context processing** (constructs)
  - [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e163450c1ae3167832971e6da29f38d-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  - [Just Go Parallel: Improving the Multilingual Capabilities of Large Language Models](https://aclanthology.org/2025.acl-long.1603.pdf)

# Action recognition
**Type:** Behavior  
**Referenced in:** 20 papers  
**Also known as:** Surgical phase recognition, Fine-grained keystep recognition, Step recognition, Activity recognition, Sport recognition, Sports recognition, Action labeling from video, Phase recognition, Accident recognition, Video action recognition  

## State of the Field

Across the surveyed literature, action recognition is most commonly defined as the task of classifying human actions within video clips. This behavior is frequently operationalized using established benchmarks; the provided data shows it is measured by Something-Something V2, ActivityNet, and UCF-101. Some work also reformulates the classification task as a multiple-choice problem for evaluation. While the general definition is prevalent, the concept is applied across numerous specialized domains, including highly specific contexts such as surgical phase recognition, where frames are classified into procedural phases, and accident recognition in traffic videos. The granularity of the recognized action also varies, from identifying individual steps in instructional videos (step recognition) to more detailed fine-grained keystep recognition. A smaller set of papers extends the concept beyond general video to include identifying activities or sports in static images, or labeling user interactions like 'click' and 'type' from screen recordings. Researchers use this task to evaluate a model's video understanding capabilities, with one paper describing it as a way to "assess the VidLMs’ capability to successfully navigate and solve simpler objectives" (ViLMA: A Zero-Shot Benchmark for Linguistic and Temporal Grounding in Video-Language Models).

## Sources

**[Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf)**
> Classifying human actions in video clips using learned token representations as input or training targets.

**[Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation](https://proceedings.neurips.cc/paper_files/paper/2024/file/de0f2a9943b7bd060e5c10c2fb2654f3-Paper-Conference.pdf) (as "Surgical phase recognition")**
> The task of classifying individual frames from a surgical video into a set of predefined procedural phases, such as 'Preparation' or 'ClippingCutting'.

**[VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf) (as "Fine-grained keystep recognition")**
> The task of identifying and labeling specific, detailed steps within a larger procedural activity shown in a video.

**[VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf) (as "Step recognition")**
> The task of identifying the individual steps of a procedure shown in an instructional video.

**[Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf) (as "Activity recognition")**
> The task of identifying and naming the primary action or event occurring in an image.

**[Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf) (as "Sport recognition")**
> The task of identifying the specific sport being played in an image.

**[AgentStudio: A Toolkit for Building General Virtual Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/172fe9f8cc55953bad5c24774bf0142b-Paper-Conference.pdf) (as "Action labeling from video")**
> The observable task of producing a sequence of discrete action labels (e.g., 'click', 'type') that corresponds to the user interactions shown in a screen recording video.

**[SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf) (as "Sports recognition")**
> The task of identifying the specific sport being played in a video clip.

**[Recognize Any Surgical Object: Unleashing the Power of Weakly-Supervised Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/53d3f45797970d323bd8a0d379c525aa-Paper-Conference.pdf) (as "Phase recognition")**
> Predicting the surgical phase depicted in a video or image sequence.

**[TAU-106K: A New Dataset for Comprehensive Understanding of Traffic Accident](https://proceedings.iclr.cc/paper_files/paper/2025/file/b33ad9d46ab2a23b6783d954121d26e3-Paper-Conference.pdf) (as "Accident recognition")**
> The task of classifying a given image or video clip as either containing a traffic accident ('Accident') or not ('Normal').

**[RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf) (as "Video action recognition")**
> The task of identifying and classifying human actions or activities within video clips.

## Relationships

### Action recognition →
- **Something-Something V2** (measurements) — *measured_by*
  > For the action recognition task, we incorporate two baselines: Adaframe (Wu et al., 2019) and MGSampler (Zhi et al., 2021), and evaluate them alongside VILAMP on three benchmarks: ActivityNet (Caba Heilbron et al., 2015), Something-Something V2 (Sth-V2) (Goyal et al., 2017), and UCF-101 (Soomro et al., 2012). (Section 5.4)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **ActivityNet** (measurements) — *measured_by*
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **UCF-101** (measurements) — *measured_by*
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)

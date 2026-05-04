# Fine-grained visual understanding
**Type:** Construct  
**Referenced in:** 21 papers  
**Also known as:** Perception of small visual details, Fine-grained recognition, Granular visual recognition, Detailed scene understanding, Fine-grained visual recognition, Fine-grained visual recognition capability, Fine-grained image comprehension  

## State of the Field

Across the surveyed literature, fine-grained visual understanding is most commonly defined as the ability to perceive and interpret small, pixel-level, or subtle semantic details within an image, as opposed to understanding only high-level objects and scenes. Some papers specify this as the capability to discern differences between visually similar objects or to identify subordinate-level categories, such as specific animal species. A smaller body of work extends the concept to video, focusing on perceiving subtle differences in motion. The types of details this construct encompasses are varied, including object keypoints, small or irregular visual elements, and text within images. One paper makes a distinction between 'granular visual recognition' (perception) and 'fine-grained visual reasoning,' a more complex process that depends on this perceptual ability. This construct is operationalized and measured using a range of benchmarks. A frequently cited method involves 'OCR-extensive' or 'text-rich' datasets like TextVQA, DocVQA, and OCRBench, which are noted to 'require fine-grained visual information.' Other 'detail-sensitive' benchmarks such as POPE are also used, in addition to general visual question answering and multimodal evaluation suites like VQA-v2, GQA, and MMBench.

## Sources

**[KptLLM: Unveiling the Power of Large Language Model for Keypoint Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe692980c5d9732cf153ce27947653a7-Paper-Conference.pdf)**
> The ability to perceive and interpret small, pixel-level semantic details within an image, as opposed to only understanding high-level objects and scenes.

**[MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf) (as "Perception of small visual details")**
> The ability to accurately identify and interpret fine-grained details or small objects within an image, a specific facet of visual perception.

**[Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf) (as "Granular visual recognition")**
> The latent ability of a model to perceive and identify small, occluded, or fine-grained details within an image.

**[Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf) (as "Fine-grained visual reasoning")**
> The model's ability to perform complex reasoning that depends on the precise understanding of small or detailed visual elements.

**[Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf) (as "Detailed scene understanding")**
> The model's ability to perceive and interpret fine-grained visual details within an image, such as small objects or intricate patterns.

**[Mini-Monkey: Alleviating the Semantic Sawtooth Effect for Lightweight MLLMs via Complementary Image Pyramid](https://proceedings.iclr.cc/paper_files/paper/2025/file/d52b3500a00748169dd4dad80fb75357-Paper-Conference.pdf) (as "Fine-grained recognition")**
> The latent ability to correctly identify small, irregular, or text-like visual elements in images.

**[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf) (as "Fine-grained visual recognition")**
> The capability of a model to discern subtle and detailed differences between visually similar objects or scenes.

**[Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfa2f1555d46b553827af4e1557f3c9a-Paper-Conference.pdf) (as "Fine-grained visual recognition capability")**
> The latent ability of a model to correctly identify subordinate-level categories of objects within a broader super-category, such as specific species of animals or models of aircraft.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Fine-grained image comprehension")**
> The model's ability to understand specific details, objects, and their attributes within an image at a level more detailed than a global summary.

## Relationships

### Fine-grained visual understanding →
- **VQA-v2** (measurements) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > “TinyGroundingGPT-3B demonstrates superior image understanding capabilities on the VQAv2, GQA, SQA, and POPE benchmarks”
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  > We evaluated TinyGroundingGPT on seven benchmarks, providing a comprehensive assessment of its performance across various metrics. (Table 2: Comparison of MLLMs on image understanding benchmarks.)
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **TextVQA** (measurements) — *measured_by*
  > We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA, V∗, POPE, DocVQA)... (Sec. 6)
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **DocVQA** (measurements) — *measured_by*
  > “We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA 2 (Singh et al., 2019), V∗ (Wu and Xie, 2023), POPE (Li et al., 2023c), DocVQA (Mathew et al., 2021))”
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **STAR** (measurements) — *measured_by*
  - [TOPA: Extending Large Language Models for Video Understanding via Text-Only Pre-Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ae94013da7cd459402fd77874e09ee3-Paper-Conference.pdf)
- **VizWiz** (measurements) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **MM-Vet** (measurements) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **POPE** (measurements) — *measured_by*
  > “We evaluate their effectiveness in improving the perception of smaller visual concepts on 4 detail-sensitive datasets (TextVQA 2 (Singh et al., 2019), V∗ (Wu and Xie, 2023), POPE (Li et al., 2023c), DocVQA (Mathew et al., 2021))”
  - [MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aaa0ac4253da75faf9b0dc0dda062612-Paper-Conference.pdf)
- **OCRBench** (measurements) — *measured_by*
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **InfoVQA** (measurements) — *measured_by*
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **ChartQA** (measurements) — *measured_by*
  > To evaluate the impact of this masking on the performance of LMMs, we select a set of OCR-extensive benchmarks (DocVQA (Mathew et al., 2021), ChartQA (Masry et al., 2022), InfoVQA (Mathew et al., 2022), OCRBench (Liu et al., 2024c), TextVQA (Singh et al., 2019)) that require fine-grained visual information, thus being highly sensitive to potential information loss in vision tokens
  - [Streamline Without Sacrifice - Squeeze out Computation Redundancy in LMM](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25s/wu25s.pdf)
- **ScienceQA-IMG** (measurements) — *measured_by*
  > “TinyGroundingGPT-3B demonstrates superior image understanding capabilities on the VQAv2, GQA, SQA, and POPE benchmarks”
  - [MuCAL: Contrastive Alignment for Preference-DrivenKG-to-Text Generation](https://aclanthology.org/2025.emnlp-main.721.pdf)
- **MME** (measurements) — *measured_by*
  > We evaluated TinyGroundingGPT on seven benchmarks, providing a comprehensive assessment of its performance across various metrics. (Table 2: Comparison of MLLMs on image understanding benchmarks.)
  - [MuCAL: Contrastive Alignment for Preference-DrivenKG-to-Text Generation](https://aclanthology.org/2025.emnlp-main.721.pdf)

### Associated with
- **Fine-grained visual reasoning** (constructs)
  - [Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf)

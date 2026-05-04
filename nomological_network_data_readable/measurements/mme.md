# MME
**Type:** Measurement  
**Referenced in:** 100 papers  

## State of the Field

Across the surveyed literature, MME is consistently described as a comprehensive vision-language benchmark used to evaluate multimodal large language models. The most prevalent framing, found in numerous definitions and usage contexts, is that the instrument is designed to measure two primary facets of model capability: perception and cognition. This evaluation is operationalized across 14 distinct sub-tasks, which are frequently characterized as a form of visual question answering (VQA). One paper specifies that these tasks require simple 'yes' or 'no' answers based on single-image instructions. Papers most commonly use MME to assess general constructs like visual understanding, multimodal understanding, and VQA capabilities. A notable secondary application is the measurement of hallucination, with some studies using specific MME subtasks—such as those related to object existence, counting, and color—to evaluate object hallucination in particular. The benchmark is also used to a lesser extent to measure visual reasoning and helpfulness.

## Sources

**[Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)**
> Vision-language benchmark evaluating cognition and perception abilities across 14 sub-tasks, including OCR, color, counting, and scene understanding.

## Relationships

### → MME
- **Visual understanding** (constructs) — *measured_by*
  > “We compare LLaVA-Mini with LLaVA-v1.5 across 11 benchmarks to thoroughly assess the performance of LLaVA-Mini with minimal vision tokens.”
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > We conduct experiments on MME (Fu et al., 2023), MMB (Liu et al., 2023c), and MMBCN. Each encompasses various sub-tasks, enabling comprehensive evaluation of multimodal understanding and reasoning capabilities. (Section 4.1)
  - [DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > DeCo also achieves better results on MME, which evaluates the multifaceted VQA capabilities of LLaVA-1.5. (Section 4.3)
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
- **Perception** (constructs) — *measured_by*
  > MME evaluates VLMs with 14 sub-tasks that encompass cognition and perception abilities. (Section 3.2)
  - [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  > “MME (Fu et al., 2023) and MMBench (Liu et al., 2023b) benchmarks are employed to assess the LVLM’s general ability.”
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > MME (Fu et al., 2024) provides a benchmark for assessing LVLMs across various tasks. Following Yin et al. (2023), we evaluate hallucination using four subtasks: Existence, Count, Position, and Color
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Cognition** (constructs) — *measured_by*
  > MME (Fu et al., 2023) offers evaluation of perception and cognition on 14 tasks (Section 2)
  - [Fine-tuning Multimodal LLMs to Follow Zero-shot Demonstrative Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb5b08f912600de3de07c6503599ba8-Paper-Conference.pdf)
- **Visual perception** (constructs) — *measured_by*
  > MME (Fu et al., 2023) assesses the visual perception of models with yes/no questions. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > "MME ... are both robust and holistic evaluations of MLLMs"
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [Feast Your Eyes:  Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > Besides language commands, by incorporating an image encoder, our approach can be simply extended to a Multi-modal LLM for image-conditioned instruction following, which achieves superior multi-modal reasoning capacity on several popular benchmarks (MME, MMBench, LVLM-eHub). (Abstract)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf)
- **Knowledge** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Object counting** (behaviors tasks) — *measured_by*
  > Following Yin et al. (2023), we evaluate hallucination using four subtasks: Existence, Count, Position, and Color, with performance measured by the combined metric of accuracy and accuracy+ (Section 4.1).
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks) — *measured_by*
  > “The MLLM-specific benchmarks are POPE Li et al. (2023c), MME Fu et al. (2023), MMB Liu et al. (2023d), SEED Li et al. (2023a) and MM-Vet Yu et al. (2023). Compared to common VL evaluations, these benchmarks aim to evaluate MLLMs from various aspects, such as fine-grained reasoning and visual hallucination.”
  - [Routing Experts: Learning to Route Dynamic Experts in Existing Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49a4829a2ccaaa4706cc82e68c39a9c6-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > “For multimodal helpfulness benchmarks, we use MMBench (Liu et al., 2023d), MME (Fu et al., 2024), and SEEDBench (Li et al., 2023a).”
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Knowledge retention** (constructs) — *measured_by*
  - [Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  > We evaluated TinyGroundingGPT on seven benchmarks, providing a comprehensive assessment of its performance across various metrics. (Table 2: Comparison of MLLMs on image understanding benchmarks.)
  - [MuCAL: Contrastive Alignment for Preference-DrivenKG-to-Text Generation](https://aclanthology.org/2025.emnlp-main.721.pdf)

# Multimodal reasoning
**Type:** Construct  
**Referenced in:** 73 papers  
**Also known as:** Cross-modal reasoning, Multi-modal reasoning, X-modal reasoning, Cross-modal consistency reasoning, Audio-visual reasoning, Contrastive cross-modal reasoning, Cross-modal arithmetic, Multimodal problem solving, Image understanding and reasoning, Video understanding and reasoning  

## State of the Field

The prevailing usage in the provided literature frames multimodal reasoning as a model's capacity to integrate information from multiple modalities—most commonly text and images—to draw conclusions and perform complex tasks. While this text-and-vision pairing is dominant, some definitions broaden the scope to include audio, video, tables, and even stylistic elements like colors and fonts. A recurring sub-theme, often labeled "cross-modal reasoning," specifically focuses on the ability to assess the semantic consistency and alignment between different modalities. More specialized framings also appear, such as "audio-visual reasoning" for processing video streams and "contrastive cross-modal reasoning" for selecting the best modality to satisfy a prompt. The field operationalizes this construct through a wide array of evaluation instruments, with papers frequently using benchmarks like MMBench, ScienceQA, MathVista, and MMMU to measure performance. These evaluations often involve tasks in domains like mathematical problem-solving, scientific question answering, and software engineering. Multimodal reasoning is studied alongside behaviors such as object counting and visual question answering. One paper also suggests it can enhance visual grounding by helping models generate interpretable region proposals.

## Sources

**[VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/518046d86bbc41a0707727c38301ad8e-Paper-Conference.pdf) (as "Cross-modal reasoning")**
> The latent ability to infer whether visual content and textual labels are semantically consistent by combining evidence across modalities.

**[LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/7f70331dbe58ad59d83941dfa7d975aa-Paper-Conference.pdf)**
> The capacity to draw conclusions and make inferences by integrating information from both visual and textual inputs in a coherent manner.

**[LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf) (as "Multi-modal reasoning")**
> The capacity of a model to process, integrate, and reason about information from multiple modalities, such as text and images, to perform complex tasks.

**[LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf) (as "X-modal reasoning")**
> The ability of a model to reason and perform tasks that involve integrating information from multiple, different modalities, such as text, image, video, and audio.

**[MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d6c53fe062716387ff0df73cc53de60c-Paper-Conference.pdf) (as "Cross-modal consistency reasoning")**
> The latent ability to judge the semantic alignment and consistency between textual and visual modalities.

**[video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25x/sun25x.pdf) (as "Audio-visual reasoning")**
> The model's ability to perform logical inference by integrating and jointly processing information from both auditory and visual streams in a video.

**[FairGen: Controlling Sensitive Attributes for Fair Generations in Diffusion Models via Adaptive Latent Guidance](https://aclanthology.org/2025.emnlp-main.1288.pdf) (as "Contrastive cross-modal reasoning")**
> The ability to reason contrastively across multiple modalities to select the one that best satisfies a natural language prompt.

**[LLMs can see and hear without any training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ashutosh25a/ashutosh25a.pdf) (as "Cross-modal arithmetic")**
> Combining representations from different modalities (e.g., image and audio) by inverting them into text, merging the textual descriptions, and generating a new output (e.g., image) from the combined prompt.

**[Visual Contextual Attack: JailbreakingMLLMs with Image-Driven Context Injection](https://aclanthology.org/2025.emnlp-main.488.pdf) (as "Multimodal problem solving")**
> Solving problems that require integrating information from both text and images, such as interpreting diagrams to compute geometric properties.

**[Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf) (as "Image understanding and reasoning")**
> Producing responses that demonstrate comprehension and logical inference based on visual inputs, such as diagrams or scenes.

**[Thinking Out Loud: Do Reasoning Models Know When They’re Right?](https://aclanthology.org/2025.emnlp-main.74.pdf) (as "Video understanding and reasoning")**
> Interpreting and drawing conclusions from dynamic visual sequences, such as videos, involving perception, comprehension, and adaptation.

## Relationships

### Multimodal reasoning →
- **MMBench** (measurements) — *measured_by*
  > Besides language commands, by incorporating an image encoder, our approach can be simply extended to a Multi-modal LLM for image-conditioned instruction following, which achieves superior multi-modal reasoning capacity on several popular benchmarks (MME, MMBench, LVLM-eHub). (Abstract)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **ScienceQA** (measurements) — *measured_by*
  > We directly utilize ScienceQA’s multi-modal training set to fine-tune LLaMA-Adapter, and conduct in-domain testing. (Section 3.3)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **MMMU** (measurements) — *measured_by*
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
- **MathVista** (measurements) — *measured_by*
  > We perform experiments on two widely used multimodal mathematical reasoning benchmarks: MATHVISTA (Lu et al., 2024b) and WE-MATH (Qiao et al., 2024). (Section 4.1)
  - [RAG-Critic: Leveraging Automated Critic-Guided Agentic Workflow for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.180.pdf)
- **MME** (measurements) — *measured_by*
  > Besides language commands, by incorporating an image encoder, our approach can be simply extended to a Multi-modal LLM for image-conditioned instruction following, which achieves superior multi-modal reasoning capacity on several popular benchmarks (MME, MMBench, LVLM-eHub). (Abstract)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Hateful Memes** (measurements) — *measured_by*
  - [Q-VLM: Post-training Quantization for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cffbaf4f47546ece96bb42c0edda40ee-Paper-Conference.pdf)
- **SQA** (measurements) — *measured_by*
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **VQA-v2** (measurements) — *measured_by*
  - [Discovering Sparsity Allocation for  Layer-wise Pruning of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ff997469ac66cf893c4183efeb22212a-Paper-Conference.pdf)
- **MMStar** (measurements) — *measured_by*
  > Our experimental results on 5 different multimodal reasoning benchmarks, including Math-Vista, M3CoT, MMStar, MMBench and AI2D, show that this strategy, which incorporates both optimized static design choices and dynamic adjustments, effectively mitigates exploration loss during training and enhances performance universally for models with varied sizes such as MiniCPM-V-2.5 (8B), Phi-3.5-Vision (4B) and InternVL2 (2B). (Section 1)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **Mantis-Eval** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ChartMimic** (measurements) — *measured_by*
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > we evaluate its performance using Qwen-2.5-VL-7B (Team, 2025) on 500 multiple-choice samples from both GQA (Hudson and Manning, 2019) and the image-based subset of ScienceQA (Lu et al., 2022).
  - [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-TurnLLMJailbreaks](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **WE-MATH** (measurements) — *measured_by*
  > We perform experiments on two widely used multimodal mathematical reasoning benchmarks: MATHVISTA (Lu et al., 2024b) and WE-MATH (Qiao et al., 2024). (Section 4.1)
  - [RAG-Critic: Leveraging Automated Critic-Guided Agentic Workflow for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.180.pdf)
- **Visual grounding** (constructs) — *causes*
  > In the reasoning stage, RSVP employs multimodal chain-of-thought visual prompts to help MLLMs understand queries and infer targets, generating interpretable region proposals that enhance visual grounding. (Section 1)
  - [QDTSynth: Quality-Driven Formal Theorem Synthesis for Enhancing Proving Performance ofLLMs](https://aclanthology.org/2025.acl-long.715.pdf)
- **MMMU-Pro** (measurements) — *measured_by*
  > Experiments demonstrate that training MLLMs on our dataset not only significantly improves reasoning capabilities, achieving state-of-the-art performance on benchmarks such as MathVerse (+8.1%), MMMU-Pro (+7%), and MuirBench (+13.3%) (Section 1).
  - [CART: A Generative Cross-Modal Retrieval Framework With Coarse-To-Fine Semantic Modeling](https://aclanthology.org/2025.acl-long.736.pdf)
- **AI2D** (measurements) — *measured_by*
  > Our experimental results on 5 different multimodal reasoning benchmarks, including Math-Vista, M3CoT, MMStar, MMBench and AI2D, show that this strategy, which incorporates both optimized static design choices and dynamic adjustments, effectively mitigates exploration loss during training and enhances performance universally for models with varied sizes such as MiniCPM-V-2.5 (8B), Phi-3.5-Vision (4B) and InternVL2 (2B). (Section 1)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)

### Associated with
- **Object counting** (behaviors tasks)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks)
  - [Q-VLM: Post-training Quantization for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cffbaf4f47546ece96bb42c0edda40ee-Paper-Conference.pdf)
- **Text-to-speech synthesis** (behaviors tasks)
  - [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf)

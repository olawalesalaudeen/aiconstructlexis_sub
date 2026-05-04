# MMStar
**Type:** Measurement  
**Referenced in:** 25 papers  

## State of the Field

MMStar is most commonly described as a single-image benchmark for evaluating visual-language understanding, though other definitions characterize it as a multimodal benchmark for general reasoning, comprehension, and mathematical reasoning. Across the provided literature, MMStar is used to measure a wide range of model capabilities, from general constructs like 'visual understanding' and 'multimodal reasoning' to more specific abilities. One paper details that its scores can be broken down into 'coarse perception (CP), fine-grained perception (FP), instance reasoning (IR), logical reasoning (LR), science and technology (ST), and mathematics (MA)'. The emphasis on mathematical abilities is also present in work that groups it with other math-related benchmarks. Additionally, it is explicitly categorized as a benchmark for 'visual question answering'. The data consistently shows MMStar being operationalized as a multifaceted evaluation tool for a spectrum of abilities from perception to complex reasoning.

## Sources

**[MIA-DPO: Multi-Image Augmented Direct Preference Optimization For Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/557a20663907ed637c2807f608d5bec2-Paper-Conference.pdf)**
> A single-image benchmark used to evaluate visual-language understanding.

## Relationships

### → MMStar
- **Logical reasoning** (constructs) — *measured_by*
  > The evaluation dataset is MMStar. (Figure 1 Caption)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Fine-grained perception** (constructs) — *measured_by*
  > The evaluation dataset is MMStar. (Figure 1 Caption)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Instance reasoning** (constructs) — *measured_by*
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  > The performance of LLaVA-Next-LLaMA3-8B model with merged task vectors across math-related Benchmarks: MathVista ..., MathVerse ..., MMStar ..., DynaMath ..., MathVision ... (Table 2)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Perception** (constructs) — *measured_by*
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “We select 6 VQA benchmarks covering both perception and reasoning.”
  - [Seeing the Image: Prioritizing Visual Correlation by Contrastive Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Coarse perception** (constructs) — *measured_by*
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Data leakage** (constructs) — *measured_by*
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > Our experimental results on 5 different multimodal reasoning benchmarks, including Math-Vista, M3CoT, MMStar, MMBench and AI2D, show that this strategy, which incorporates both optimized static design choices and dynamic adjustments, effectively mitigates exploration loss during training and enhances performance universally for models with varied sizes such as MiniCPM-V-2.5 (8B), Phi-3.5-Vision (4B) and InternVL2 (2B). (Section 1)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **Visual grounding** (constructs) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > To assess their visual understanding capability, numerous benchmarks have been developed, focusing on question-answering tasks, such as MMVet (Yu et al., 2023), MMStar (Chen et al., 2024a), and MMMU (Yue et al., 2024). (Section 1)
  - [Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c6af791af7ef0f3e02bccef011211ca5-Paper-Conference.pdf)

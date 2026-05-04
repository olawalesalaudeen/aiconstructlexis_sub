# AI2D
**Type:** Measurement  
**Referenced in:** 37 papers  

## State of the Field

Across the provided literature, AI2D (Allen Institute for AI Diagrams) is consistently characterized as an established benchmark dataset. The most common definition describes it as a tool for "diagram understanding and question answering." A recurring theme is its application to evaluating reasoning, with some papers specifying its focus on "scientific reasoning" from diagrams and scientific illustrations. Papers use AI2D to operationalize and measure several capabilities, most frequently `Chart and diagram understanding`, with evidence describing its use for assessing "science diagram comprehension" and "diagram interpretation." The benchmark is also commonly employed to evaluate `Visual reasoning` and `Multimodal reasoning`. Furthermore, it is used to assess `Visual question answering`, and one source notes it is a "multiple-choice benchmark." Other capabilities measured by AI2D include `Visual understanding`, `Natural language understanding`, and `Multimodal perception`.

## Sources

**[LiveXiv - A Multi-Modal live benchmark based on Arxiv papers content](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eaa1373fe55b223c2dfe1fd29a277d7-Paper-Conference.pdf)**
> The Allen Institute for AI Diagrams (AI2D) benchmark, an established dataset for diagram understanding and question answering.

## Relationships

### → AI2D
- **Chart and diagram understanding** (behaviors tasks) — *measured_by*
  > AI2D (Kembhavi et al., 2016), a multiple-choice benchmark, evaluates the model capabilities for science diagram comprehension. (Section 4.1)
  - [Prism: A Framework for Decoupling and Assessing the Capabilities of VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cac9e747a1d480c78312226959566cef-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [MoVA: Adapting Mixture of Vision Experts to Multimodal Context](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb0fea29f7aa6ede17e906ac6a225f34-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  - [OMG-LLaVA: Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/83eb86be3e2f9fd66c44d9073c51ba4d-Paper-Conference.pdf)
- **Document understanding** (constructs) — *measured_by*
  - [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25eb/wang25eb.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > To estimate the downstream error Y (N, C), we test our trained VLMs on a suite of nine commonly used benchmarks for evaluating visual reasoning: MME (Fu et al., 2024), GQA (Hudson & Manning, 2019), AI2D (Kembhavi et al., 2016), MMBench (Liu et al., 2024c), MMMU (Yue et al., 2023), ScienceQA (Lu et al., 2022), MathVista (Lu et al., 2024), POPE (Li et al., 2023c), and ChartQA (Masry et al., 2022). (Section 3.2)
  - [Inference Optimal VLMs Need Fewer Visual Tokens and More Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef748b4544e8f12d608fd28bbf04177f-Paper-Conference.pdf)
- **Multiple-choice visual question answering** (behaviors tasks) — *measured_by*
  - [Ranked from Within: Ranking Large Multimodal Models Without Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tu25a/tu25a.pdf)
- **Multimodal reasoning** (constructs) — *measured_by*
  > Our experimental results on 5 different multimodal reasoning benchmarks, including Math-Vista, M3CoT, MMStar, MMBench and AI2D, show that this strategy, which incorporates both optimized static design choices and dynamic adjustments, effectively mitigates exploration loss during training and enhances performance universally for models with varied sizes such as MiniCPM-V-2.5 (8B), Phi-3.5-Vision (4B) and InternVL2 (2B). (Section 1)
  - [Diving into Self-Evolving Training for Multimodal Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aj/liu25aj.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)

# MMVP
**Type:** Measurement  
**Referenced in:** 17 papers  

## State of the Field

MMVP is most commonly characterized as a benchmark for evaluating the fine-grained visual recognition capabilities of vision-language models. Its design is frequently described as using "pairs of visually similar (CLIP-blind) images, each with a binary-option question" ("Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models"). However, one paper notes that the benchmark is "not in paired image-text format" and required manual conversion, indicating some ambiguity in its operationalization ("EfficientQAT: Efficient Quantization-Aware Training for Large Language Models"). Across the surveyed literature, MMVP is most prevalently used to measure `Visual understanding`, with related constructs such as `Fine-grained visual recognition`, `Visual perception`, and `Fine-grained perception` also being common targets of evaluation. Specifically, it is used to test a model's ability to "capture visual details like object existence, orientation, and counting" ("EfficientQAT...") and determine spatial relationships. A smaller number of papers frame its use more broadly for assessing general `Visual question answering` or `Multimodal understanding`. Other capabilities like `Visual grounding` and `Compositional reasoning` are also measured with MMVP, but appear less frequently in this set of sources. One paper offers a distinct description, referring to it as the "Massively Multimodal Video Pretraining benchmark" ("ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering").

## Sources

**[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)**
> A benchmark that evaluates the fine-grained visual recognition capabilities of LVLMs using pairs of visually similar (CLIP-blind) images, each with a binary-option question.

## Relationships

### → MMVP
- **Visual understanding** (constructs) — *measured_by*
  > Furthermore, we also use the vision-centric vision understanding benchmarks, such as MMVP (Tong et al., 2024b), RealWorldQA (xAI, 2024) and CVBench-2D (Tong et al., 2024a). (Section 4.1)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *measured_by*
  - [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  - [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)
- **Fine-grained understanding** (constructs) — *measured_by*
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  - [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fb82011040977c7712409fbdb5456647-Paper-Conference.pdf)
- **Visual perception** (constructs) — *measured_by*
  > We extensively evaluated DEEM on both our newly constructed RobustVQA benchmark and other well-known benchmarks, POPE and MMVP, for visual hallucination and perception respectively.
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
- **Fine-grained visual recognition** (behaviors tasks) — *measured_by*
  > MMVP (Tong et al., 2024) collects CLIP-blind pairs and evaluates the fine-grained visual recognition capabilities of LVLMs (Section 4.1).
  - [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > To evaluate multimodal understanding capabilities, we conduct evaluations on six widely-used benchmarks: RealworldQA (XAI, 2024), MMVP (Tong et al., 2024b), ScienceQA (Lu et al., 2022), VStar (Wu and Xie, 2023), MME (Fu et al., 2024), and POPE (Li et al., 2023b). (Section 4.2)
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **Fine-grained perception** (constructs) — *measured_by*
  > Among these benchmarks, MMVP mainly focuses on fine-grained perception. (Section 4.1)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  > General VQA: Assessing visual perception and reasoning abilities through single-image question answering, including MMBench (Liu et al., 2025b), MME (Fu et al., 2023), and MMVP (Zhong et al., 2023). (Section 4.5).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)

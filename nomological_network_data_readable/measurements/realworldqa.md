# RealWorldQA
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** RealworldQA  

## State of the Field

RealWorldQA is predominantly described as a benchmark designed to assess practical, real-world visual understanding using questions based on images. Across the surveyed work, it is most frequently used to measure the constructs of "Visual understanding" and "Multimodal understanding." Papers also use it to evaluate related capabilities such as "Perception," "Multimodal perception," and "Commonsense knowledge." A more specific framing, present in one paper, defines the dataset as being tailored to assess "basic real-world spatial understanding" through multiple-choice questions based on anonymized images, with accuracy as the evaluation metric. Beyond measuring specific constructs, RealWorldQA is also included in broader evaluations of "general multimodal performance" and the "general capability" of models in real-world question answering. One study also employs it to measure a model's utility preservation following safety interventions.

## Sources

**[CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf) (as "RealworldQA")**
> A dataset designed to assess an LMM's basic spatial understanding in real-world contexts through multiple-choice questions based on anonymized outdoor and indoor images.

**[Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)**
> A benchmark featuring questions about real-world images to assess practical, real-world visual understanding.

## Relationships

### → RealWorldQA
- **Perception** (constructs) — *measured_by*
  > The perception-focused benchmarks include RealWorldQA, CV-Bench and BLINK (Section 4)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > Furthermore, we also use the vision-centric vision understanding benchmarks, such as MMVP (Tong et al., 2024b), RealWorldQA (xAI, 2024) and CVBench-2D (Tong et al., 2024a). (Section 4.1)
  - [Dynamic-LLaVA: Efficient Multimodal Large Language Models via Dynamic Vision-language Context Sparsification](https://proceedings.iclr.cc/paper_files/paper/2025/file/aeafb73dfed3007ec5299be1604d6f99-Paper-Conference.pdf)
- **Multimodal perception** (constructs) — *measured_by*
  - [MODA: MOdular Duplex Attention for Multimodal Perception, Cognition, and Emotion Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cg/zhang25cg.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > “We evaluate the visual question answering abilities of ChatVLA using Vlmevalkit ... on ... RealworldQA ...”
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)

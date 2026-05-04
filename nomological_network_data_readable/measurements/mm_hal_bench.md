# MM-Hal-Bench
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** MMHAL-Bench  

## State of the Field

Across the provided literature, MM-Hal-Bench is consistently defined as a benchmark designed to assess hallucination in multimodal models, particularly Large Vision-Language Models (LVLMs). Its most frequently cited application is the measurement of `Hallucination`, with some papers also specifying its use for `Visual hallucination` and `Object hallucination`. One paper notes that the benchmark evaluates models "beyond object hallucination," while others use it to assess related constructs like `Attribute recognition` and `Faithfulness`. The benchmark is consistently described as containing 96 questions or "carefully designed image-question pairs" organized into 8 categories. These categories cover a variety of scenarios, with papers frequently mentioning types such as object attributes, adversarial objects, counting, and spatial relations. For evaluation, some sources state that MM-Hal-Bench uses GPT-4 to assess model outputs. One paper elaborates that this process involves comparing model responses against human responses and object labels to determine response quality and hallucination rates.

## Sources

**[LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf) (as "MMHal-Bench")**
> MMHal-Bench is a benchmark designed to assess hallucination in multimodal models across a variety of scenarios.

**[Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf) (as "MMHAL-Bench")**
> A benchmark for evaluating multimodal hallucination across multiple question types, including object attributes, adversarial objects, comparisons, counting, spatial relations, environment, holistic description, and others.

**[CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)**
> A hallucination-based benchmark containing 96 questions across 8 categories such as object attribute, adversarial object, and counting.

## Relationships

### → MM-Hal-Bench
- **Hallucination** (behaviors tasks) — *measured_by*
  > Moreover, we conduct experiments on several hallucination benchmarks such as ... MMHal-Bench (Sun et al., 2023). (Section 4.1)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf)
- **Visual hallucination** (behaviors tasks) — *measured_by*
  > Visual hallucination task evaluates whether the response of the model is consistent with the image content to ensure the trustworthiness and reliability of the model. We use CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023c), and MMHal-Bench (Sun et al., 2023).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **Attribute recognition** (behaviors tasks) — *measured_by*
  > "MMHAL-Bench (Sun et al., 2023): This benchmark evaluates LVLMs beyond object hallucination and contains eight question types: object attributes, adversarial objects, comparisons, counting, spatial relations, environment, holistic description, and others."
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
- **Object hallucination** (behaviors tasks) — *measured_by*
  > we benchmark VTI on the MMHAL dataset with the evaluations of eight different hallucination types.
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)

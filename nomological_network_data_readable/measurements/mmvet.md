# MMVet
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

Across the provided literature, MMVet is consistently described as a multimodal benchmark for evaluating the capabilities of large vision-language models (LVLMs). Its most frequently stated purpose is to assess "visual question answering," a use case explicitly supported by both definitions and relationship evidence. Several papers also characterize it more broadly as a tool for evaluating "multi-modal reasoning," "fine-grained understanding," and "alignment performance" in complex scenarios. A distinguishing feature noted in one paper is that "MMVet is open-ended," which contrasts it with other, closed-ended benchmarks. In practice, it is often deployed as part of a larger evaluation suite alongside instruments like LLaVABench, MMBench, and MathVista. Researchers use it to report quantitative model performance, as one study notes that a particular model "achieves 64.5% on MMVet."

## Sources

**[Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)**
> A multimodal benchmark used in the paper to evaluate LVLMs on visual question answering tasks.

## Relationships

### → MMVet
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “We selected five popular benchmarks to assess current LVLMs, encompassing Yes/No Questions (MME), Multiple Choice Questions (MMBench, SEEDBench), and Visual Question Answering (MMvet, LLaVABench).”
  - [WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences](https://proceedings.neurips.cc/paper_files/paper/2024/file/563991b5c8b45fe75bea42db738223b2-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.564.pdf)

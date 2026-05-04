# LLaVA-Bench-in-the-Wild
**Type:** Measurement  
**Referenced in:** 31 papers  
**Also known as:** llava-bench-in-the-wild, LLaVA Bench, LLaVA-in-the-wild, LLaVA-wild, LLaVA-Wild, LLaVABench, LLaVA-Bench Wild  

## State of the Field

Across the provided literature, LLaVA-Bench-in-the-Wild, also referred to by variants like LLaVA-Bench and LLaVA-Wild, is predominantly characterized as an evaluation benchmark for assessing large vision-language models. Its most common application is to measure performance on open-ended tasks in unconstrained, "in-the-wild" settings, focusing on multimodal dialogue and image understanding. Papers use this instrument to evaluate a range of capabilities, most frequently visual question answering, complex reasoning, and open-ended question answering. It is also reported to assess visual instruction following, helpfulness, detailed image description, and long-form text generation. The benchmark is described as containing "challenging multimodal images and questions," with one source specifying it includes "24 images featuring complex scenes, memes, paintings, and sketches, along with 60 challenging questions." A recurring feature of its operationalization is the use of a more advanced model for scoring, with several papers noting the use of "GPT-4V-aided assessment" or "GPT-4o for response evaluation." While most sources frame it as a general capability benchmark, a less common use is to "introduce visual distribution shifts by varying visual input semantics" for model evaluation. Overall, the benchmark is consistently positioned to evaluate how models handle complex, conversational, and reasoning-based queries about diverse, real-world images.

## Sources

**[Dense Connector for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/3a10c46572628d58cb44fb705f25cbbf-Paper-Conference.pdf)**
> An evaluation benchmark for open-ended multimodal dialogue and image understanding in unconstrained settings.

**[SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf) (as "llava-bench-in-the-wild")**
> Benchmark for evaluating multimodal language models on image-based tasks and questions.

**[Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf) (as "LLaVA-Bench")**
> LLaVA-Bench is a benchmark containing challenging multimodal images and questions used to evaluate LVLM responses, including GPT-4V-aided assessment.

**[ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf) (as "LLaVA Bench")**
> A conversational VQA benchmark containing questions about conversations, detailed descriptions, and complex reasoning.

**[Unhackable Temporal Reward for Scalable Video MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e5b9a51dcd78528795584860797fdb-Paper-Conference.pdf) (as "LLaVA-wild")**
> An image understanding benchmark for evaluating performance on in-the-wild visual questions.

**[CHiP: Cross-modal Hierarchical Direct Preference Optimization for Multimodal LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c73e9595126794186536cfbbed012f-Paper-Conference.pdf) (as "LLaVA-Wild")**
> A dataset used for general capability evaluation of multimodal models, often scored using a stronger model as an evaluator.

**[TaskGalaxy: Scaling Multi-modal Instruction Fine-tuning with Tens of Thousands Vision Task Types](https://proceedings.iclr.cc/paper_files/paper/2025/file/e885e5bc6e13b9dd8f80bc5482b1fa2f-Paper-Conference.pdf) (as "LLaVA-in-the-wild")**
> A benchmark evaluating visual conversation abilities and leveraging GPT-4o for response evaluation.

**[Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf) (as "LLaVABench")**
> An evaluation benchmark used to assess Large Vision-Language Models on visual question answering tasks.

**[Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf) (as "LLaVA-Bench Wild")**
> A benchmark dataset used to introduce visual distribution shifts by varying visual input semantics for evaluating multimodal large language models.

## Relationships

### → LLaVA-Bench-in-the-Wild
- **Visual question answering** (behaviors tasks) — *measured_by*
  > “We selected five popular benchmarks to assess current LVLMs, encompassing Yes/No Questions (MME), Multiple Choice Questions (MMBench, SEEDBench), and Visual Question Answering (MMvet, LLaVABench).”
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  - [Artificial Impressions: Evaluating Large Language Model Behavior Through the Lens of Trait Impressions](https://aclanthology.org/2025.emnlp-main.982.pdf)
- **Open-ended question answering** (behaviors tasks) — *measured_by*
  > we mainly used LLaVA v1.5 (Liu et al., 2024a) and LLaVA NeXT (Liu et al., 2024b) in 7B and 13B sizes and evaluated them on the LLaVA-Bench COCO and LLaVA-Bench Wild (Liu et al., 2023) datasets to assess open-ended generation quality.
  - [Understanding Multimodal LLMs Under Distribution Shifts: An Information-Theoretic Approach](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oh25a/oh25a.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > LLaVA-Bench-in-the-Wild (Liu et al., 2024), which examines the helpfulness of VLMs in aspects like instruction following and complex reasoning (Section 5.2)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  > LLaVA-Bench-in-the-Wild (Liu et al., 2024), which examines the helpfulness of VLMs in aspects like instruction following and complex reasoning (Section 5.2)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
- **Detailed image description** (behaviors tasks) — *measured_by*
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)

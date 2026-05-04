# MixEval
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, MixEval is consistently described as a hybrid evaluation benchmark for large language models, designed to provide a comprehensive assessment of their capabilities across a diverse mix of tasks. The benchmark is defined as combining 18 ground-truth-based tasks, with one source noting it "collects data from numerous QA datasets under real-world data distribution" ("Unnatural Languages Are Not Bugs but Features for LLMs"). Papers use MixEval to measure a wide array of model attributes, most commonly for evaluating `Alignment`, `Instruction following`, and `Problem-solving`. It is also used to assess more specific capabilities such as `Conversational ability` (for "generalist chat capabilities"), `Adversarial robustness` (specifically "jailbreak robustness"), `Faithfulness`, and `Commonsense knowledge`. In a different framing, one paper categorizes MixEval as a `Classification` benchmark. One study reports that the benchmark has a "0.96 correlation to human preferences" ("RMB: Comprehensively benchmarking reward models in LLM alignment").

## Sources

**[RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)**
> A hybrid evaluation benchmark for language models that combines 18 ground-truth-based tasks.

## Relationships

### → MixEval
- **Adversarial robustness** (constructs) — *measured_by*
  > We also evaluate on the MixEval (Ni et al., 2024) benchmark, which contains downstream tasks, and assess jailbreak robustness; additional details are provided in Appendices F and G.
  - [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  > "We evaluate alignment effectiveness using three benchmarks: (1) MixEval ..."
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Classification** (behaviors tasks) — *measured_by*
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **Instruction following** (constructs) — *measured_by*
  > We evaluate all variants on Length-controlled (LC) AlpacaEval 2.0 (Li et al., 2023) and MixEval (Ni et al., 2024). MixEval is a ground-truth-based benchmark that collects data from numerous QA datasets under real-world data distribution.
  - [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf)
- **Conversational ability** (constructs) — *measured_by*
  > For generalist chat capabilities, we use MixEval, AlpacaEval2, and MTBench with GPT-4o-mini as the judge LLM (Ni et al., 2024; Dubois et al., 2024; Zheng et al., 2023). (Section 3.1)
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  > These benchmarks collectively provide a comprehensive assessment of the models’ instruction-following and problem-solving capabilities. (Section 5. Main Results)
  - [LLM Alignment as Retriever Optimization: An Information Retrieval Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25k/jin25k.pdf)

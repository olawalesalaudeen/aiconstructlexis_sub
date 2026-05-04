# LogiQA
**Type:** Measurement  
**Referenced in:** 43 papers  
**Also known as:** Logiqa  

## State of the Field

The prevailing usage of LogiQA across the provided literature is as a benchmark to measure logical reasoning in language models. Most papers operationalize it as a multiple-choice question-answering dataset where models must select the correct option based on a given logical text passage. Several sources add detail, noting that the content is derived from logic puzzles or, as one paper states, "expert-written questions for testing human logical reasoning" (Self-calibration for Language Model Quantization and Pruning). The types of reasoning it is said to evaluate include deductive, inductive, and abductive inference. A smaller line of work frames LogiQA differently, positioning it as an instrument for evaluating commonsense reasoning or understanding. Beyond these primary uses, it is also categorized more broadly as a reading comprehension task and is used in at least one study to assess model generalization.

## Sources

**[DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)**
> A dataset for logical reasoning, where models must choose the correct option for a question based on a given logical text passage.

**[Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf) (as "Logiqa")**
> A benchmark dataset for evaluating commonsense reasoning capabilities in language models.

## Relationships

### → LogiQA
- **Logical reasoning** (constructs) — *measured_by*
  > We investigate two open-source LLMs Mistral 7B instruct (Jiang et al., 2023) and LLaMA3 8B instruct (Touvron et al., 2023) and Qwen 2-7B-Instruct (Bai et al., 2023) on two logical benchmarks (LogiQA, BBH) and two mathematics benchmarks (GSM8K and MATH). (Section 4.1)
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)

### Associated with
- **MR-Ben** (measurements)
  - [MR-Ben: A Meta-Reasoning Benchmark for Evaluating System-2 Thinking in LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/d81cb1f4dc6e13aeb45553f80b3d6837-Paper-Conference.pdf)

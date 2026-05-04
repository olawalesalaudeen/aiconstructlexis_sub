# Super-Natural Instructions
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** SuperNI, SuperNI Benchmark  

## State of the Field

Across the provided literature, Super-Natural Instructions is predominantly characterized as a large and diverse benchmark designed to evaluate the general instruction-following capabilities of language models. Most definitions describe it as a collection of numerous NLP tasks, with one source specifying over 1600, that are accompanied by expert-written instructions. The benchmark is consistently used to measure performance on both `text generation` and `text classification` tasks, with one paper noting a selection of tasks across categories like dialogue generation, question answering, and summarization. A more specific line of work frames it as a benchmark for `continual learning`, using it to construct task sequences and, as one paper notes, to "evaluate cross-task generation and conflict." In this context, one source describes using a subset of 15 NLP tasks to evaluate general continual learning performance. In addition to these applications, Super-Natural Instructions is also reported to be used for assessing model `generalization`, `translation capability`, `commonsense knowledge`, and performance after `instruction fine-tuning`.

## Sources

**[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf) (as "SuperNI")**
> A collection of NLP tasks with expert-written instructions used to build continual instruction tuning task sequences and evaluate cross-task generation and conflict.

**[LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)**
> A large and diverse benchmark dataset containing over 1600 NLP tasks, designed to evaluate the general instruction-following capabilities of language models across both classification and generation formats.

**[Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf) (as "SuperNI Benchmark")**
> A comprehensive continual learning benchmark consisting of 15 NLP tasks across categories such as dialogue generation, information extraction, question answering, summarization, and sentiment analysis, used to evaluate general CL performance.

## Relationships

### → Super-Natural Instructions
- **Text generation** (behaviors tasks) — *measured_by*
  > These sequences consist of pure generation tasks, pure classification tasks and mixed sequences containing both generation and classification tasks. (Section 3)
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > These sequences consist of pure generation tasks, pure classification tasks and mixed sequences containing both generation and classification tasks. (Section 3)
  - [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/bcbc0f660d2dde42f9d1d0ecb14a6f9a-Paper-Conference.pdf)
- **Translation capability** (constructs) — *measured_by*
  - [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [DA-KD: Difficulty-Aware Knowledge Distillation for Efficient Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25c/he25c.pdf)
- **Generalization** (constructs) — *measured_by*
  > Experiments on synthetic pre-training and real-world instruction tuning tasks demonstrate that PEARL effectively mitigates permutation attacks and enhances performance. Notably, despite being trained on fewer shots and shorter contexts, PEARL achieves performance gains of up to 40% when scaled to many-shot and long-context scenarios, highlighting its efficiency and generalization capabilities.
  - [PEARL: Towards Permutation-Resilient LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad8e1915f66161581bb127ccf01092e-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [PEARL: Towards Permutation-Resilient LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad8e1915f66161581bb127ccf01092e-Paper-Conference.pdf)
- **Continual learning** (constructs) — *measured_by*
  > We conducted experiments on two CL benchmarks, including SuperNI Benchmark (Wang et al., 2022a) and Long Sequence Benchmark (Razdaibiedina et al., 2023). (Section 4.1).
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)

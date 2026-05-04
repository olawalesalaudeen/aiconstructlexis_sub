# MuSR
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** MUSR  

## State of the Field

Across the provided literature, MuSR is consistently described as a benchmark for evaluating reasoning in large language models. The most common definition specifies its purpose as assessing reasoning over social or multi-step scenarios, while a less frequent framing describes it more broadly as evaluating reasoning-oriented performance. It is frequently situated within the context of the Hugging Face Open LLM Leaderboard, where it is used alongside other benchmarks like GPQA, BBH, and MMLU-Pro. Papers use MuSR to measure several constructs, including social reasoning, commonsense understanding, language proficiency, and logical reasoning. One paper characterizes it as a "semi-symbolic reasoning benchmark" for probing "soft-reasoning performance," and another notes that its tasks require the "application of logical rules to reach the answer." Operationally, the benchmark is presented in a multiple-choice format.

## Sources

**[Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf) (as "MUSR")**
> A benchmark included in Open LLM Leaderboard v2 for evaluating reasoning over social or multi-step scenarios.

**[Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)**
> A benchmark from the Open LLM Leaderboard used to evaluate reasoning-oriented performance.

## Relationships

### MuSR →
- **Human evaluation** (measurements) — *measured_by*
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *measured_by*
  > These datasets require the application of logical rules to reach the answer... (MuSR Murder Mysteries)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)

### → MuSR
- **Commonsense reasoning** (constructs) — *measured_by*
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Social reasoning** (constructs) — *measured_by*
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **Language proficiency** (constructs) — *measured_by*
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)

### Associated with
- **Commonsense reasoning** (constructs)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)

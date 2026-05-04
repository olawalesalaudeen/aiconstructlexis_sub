# LogiQA 2.0
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** LogiQA 2  

## State of the Field

Across the provided sources, LogiQA 2.0 is consistently defined as a benchmark dataset designed to evaluate the logical reasoning capabilities of language models. The benchmark is most commonly operationalized as a multiple-choice question answering task, with one paper noting its questions are derived from professional exams requiring deductive reasoning. The prevailing use of LogiQA 2.0 is to measure logical reasoning. A smaller set of papers also employs it to assess broader constructs, such as generalization beyond the pretraining distribution and cognitive ability, where it is included in an 'executive-skills' evaluation subset. Researchers apply the benchmark in various evaluation settings, including 0-shot, 5-shot, and fine-tuning contexts. One study also situates it within the common-sense reasoning domains of the LLM Evaluation Harness.

## Sources

**[Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf) (as "LogiQA2")**
> A benchmark for logical question answering, requiring models to perform logical reasoning over text.

**[Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf) (as "LogiQA 2")**
> A logical reasoning benchmark used in a 5-shot evaluation setting.

**[Eval](https://aclanthology.org/2025.acl-long.1086.pdf)**
> LogiQA 2.0 is a benchmark dataset designed to evaluate a model's logical reasoning capabilities.

## Relationships

### → LogiQA 2.0
- **Generalization** (constructs) — *measured_by*
  > To assess generalization beyond the pretraining distribution, we evaluate models on a series of diverse reasoning tasks in a 5-shot setting, including LogiQA Liu et al. (2020), LogiQA 2 Liu et al. (2023), SciQ Welbl et al. (2017), and PiQA Bisk et al. (2020). (Section 6.1)
  - [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf)
- **Cognitive ability** (constructs) — *measured_by*
  > Executive includes LogiQA 2.0, CLadder, and WinoGrande (Table 2).
  - [Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://aclanthology.org/2025.emnlp-main.1517.pdf)

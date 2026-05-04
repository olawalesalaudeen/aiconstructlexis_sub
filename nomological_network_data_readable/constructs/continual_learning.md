# Continual learning
**Type:** Construct  
**Referenced in:** 16 papers  
**Also known as:** Lifelong learning, Continuous learning capability, Complementary learning  

## State of the Field

Across the surveyed literature, "Continual learning" is most commonly defined as a model's ability to acquire new skills and knowledge over time from new data. A central component of this definition, present in most sources, is the constraint that this learning must not degrade performance on previously learned tasks. This challenge is consistently identified as "Catastrophic forgetting," which multiple papers frame as a primary problem that continual learning methods must address. Some papers specify that this learning happens incrementally from "streaming data" or a "sequence of tasks," with one study focusing on "modality-incremental" learning.

While "Continual learning" is the prevailing term, a few papers use "Lifelong learning" to describe a similar capacity for continuous knowledge acquisition, particularly in "open-world" environments. A minority of definitions present distinct framings, such as "Continuous learning capability," which specifies that new information is integrated without parameter updates, and "Complementary learning," which involves two models learning divergent representations. The construct is operationalized through evaluations on a series of tasks or datasets. Papers report using benchmarks such as SQuAD v1.1, HotpotQA, PG-19, and the Super-Natural Instructions benchmark to measure a model's continual learning performance. Beyond its strong association with catastrophic forgetting, continual learning is also studied in relation to "Knowledge transferability," "Few-shot learning," and "Information extraction." Additionally, one paper suggests that "Causal inference" can enable lifelong learning by allowing an agent to continually expand its knowledge of an environment.

## Sources

**[Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf)**
> The ability of a model to acquire new skills and knowledge over time from new data without degrading performance on previously learned tasks.

**[ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf) (as "Lifelong learning")**
> The agent's capacity to continuously acquire and integrate new knowledge and skills from ongoing interaction with an open-world environment.

**[Continuously Updating Digital Twins using Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/amad25a/amad25a.pdf) (as "Continuous learning capability")**
> The latent ability of a model to integrate new information, such as updated data or knowledge, without requiring parameter updates or re-training, enabling persistent relevance in evolving environments.

**[MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf) (as "Complementary learning")**
> The capacity of two peer models to learn divergent yet mutually beneficial representations by exchanging asymmetric importance weights based on their individual training dynamics, thereby reducing mutual error reinforcement.

## Relationships

### Continual learning →
- **Generalization** (constructs) — *causes*
  - [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  > “Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA to inject more complex, multi-hop reasoning data after simpler QA”
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  > “Continual Fine-Tuning: (a) SQuAD (Rajpurkar et al., 2016) paired with HotpotQA to inject more complex, multi-hop reasoning data after simpler QA”
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **PG-19** (measurements) — *measured_by*
  > We consider the problem of episodal continual learning (Kirkpatrick et al., 2017; Nguyen et al., 2017) where each episode’s data, yn, is one of 20 books from the PG19 (Rae et al., 2019) dataset
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
- **Super-Natural Instructions** (measurements) — *measured_by*
  > We conducted experiments on two CL benchmarks, including SuperNI Benchmark (Wang et al., 2022a) and Long Sequence Benchmark (Razdaibiedina et al., 2023). (Section 4.1).
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)

### → Continual learning
- **Causal inference** (behaviors tasks) — *causes*
  > Newly discovered items enable the execution of new unknown actions and the CD on these actions. This iterative process ensures the lifelong learning through continuous engagement and adaptation.
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)

### Associated with
- **Catastrophic forgetting** (behaviors tasks)
  > “Continual Fine-Tuning (Madotto et al., 2021; Wu et al., 2024), which incrementally incorporates new knowledge while mitigating catastrophic forgetting.”
  - [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf)
- **Knowledge transfer** (constructs)
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)
- **Few-shot learning** (measurements)
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Information extraction** (behaviors tasks)
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)

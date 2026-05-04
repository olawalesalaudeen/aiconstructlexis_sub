# Pre-training data detection
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Training data detection, Pretraining data detection  

## State of the Field

Across the provided literature, pre-training data detection is consistently defined as the observable task of classifying whether a given text sample was part of a language model's training or pre-training corpus. The common approach involves analyzing a model's output statistics to design a scoring function that can distinguish between training and non-training data. The papers describe this task as receiving growing attention, citing its relevance for issues like "copyright violation and test data contamination" and its use in "high-reliability applications". To operationalize and measure this behavior, researchers frequently use dedicated benchmarks, with WikiMIA and MIMIR being commonly cited as evaluation instruments. Other datasets mentioned for this purpose include BookTection, BookMIA, and The Pile. The literature also connects this behavior to other phenomena; for example, one paper notes a "common view" that its effectiveness is "closely tied to the level of training-data memorization or overfitting" exhibited by the model. The task is also studied in the context of privacy.

## Sources

**[Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)**
> The observable task of determining whether a given text sample was part of a large language model's pre-training corpus by analyzing the model's output statistics.

**[A Statistical Approach for Controlled Training Data Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/c859b99b5d717c9035e79d43dfd69435-Paper-Conference.pdf) (as "Training data detection")**
> The observable task of classifying a given text sample as either having been part of the model's training set or not.

**[Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf) (as "Pretraining data detection")**
> The observable task of classifying whether a given text sequence was included in a language model's pretraining dataset.

## Relationships

### Pre-training data detection →
- **WikiMIA** (measurements) — *measured_by*
  > WIKIMIA is a dataset specifically designed to evaluate TDD algorithms on large language models.
  - [Detecting Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf)
- **MIMIR** (measurements) — *measured_by*
  > We focus on two benchmarks (and the only two to our knowledge) for pre-training data detection, WikiMIA (Shi et al., 2024) and MIMIR (Duan et al., 2024).
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
- **BookTection** (measurements) — *measured_by*
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **BookMIA** (measurements) — *measured_by*
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **The Pile** (measurements) — *measured_by*
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)

### Associated with
- **Memorization** (constructs)
  > A common view is that the effectiveness of TDD is closely tied to the level of training-data memorization or overfitting exhibited by the target model during training (Yeom et al., 2018; Long et al., 2018).
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
- **Privacy** (constructs)
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
- **Overfitting** (constructs)
  > A common view is that the effectiveness of TDD is closely tied to the level of training-data memorization or overfitting exhibited by the target model during training (Yeom et al., 2018; Long et al., 2018).
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)

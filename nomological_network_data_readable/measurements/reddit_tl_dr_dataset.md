# Reddit TL;DR dataset
**Type:** Measurement  
**Referenced in:** 27 papers  
**Also known as:** TL;DR dataset, Reddit TL;DR, Reddit summarization dataset, TL;DR summarization, TL;DR comparison data, Reddit TL;DR Summarization  

## State of the Field

The Reddit TL;DR dataset is predominantly characterized across the provided literature as a benchmark for evaluating text summarization. It is consistently defined as a collection of Reddit posts paired with human-written, concise summaries, which are sometimes noted to have been judged by human evaluators for quality and informativeness. Its most frequent application is to measure text summarization capabilities, with some papers specifying its use for evaluating abstractive summarization. A smaller body of work also employs the dataset to assess human preference alignment and general generation quality, while one study uses a subset of its subreddits to evaluate model generalization. Operationally, the dataset is used throughout the model development lifecycle for tasks including supervised fine-tuning, reward modeling, and reinforcement learning optimization. It also serves as a common testbed for evaluating the training dynamics and performance of various preference optimization algorithms and offline RLHF methods.

## Sources

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf) (as "TL;DR")**
> A benchmark dataset used for evaluating the quality of text summarization.

**[A Common Pitfall of Margin-based Language Model Alignment: Gradient Entanglement](https://proceedings.iclr.cc/paper_files/paper/2025/file/10272bfd0371ef960ec557ed6c866058-Paper-Conference.pdf) (as "TL;DR dataset")**
> A dataset consisting of Reddit posts and their summaries, used in this paper to evaluate the training dynamics of various preference optimization algorithms. The full name is 'Too Long; Didn't Read'.

**[Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf) (as "Reddit TL;DR")**
> A summarization dataset consisting of Reddit posts and several corresponding short summaries, which have been judged for quality and informativeness by human evaluators.

**[Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)**
> A dataset consisting of Reddit posts and their human-written summaries (Stiennon et al., 2020), used for training and evaluating summarization models.

**[InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf) (as "Reddit summarization dataset")**
> A dataset also known as the TL;DR dataset, containing Reddit posts and their corresponding human-written summaries, used for training and evaluating text summarization models.

**[Symmetric Reinforcement Learning Loss for Robust Learning on Diverse Tasks and Model Scales](https://raw.githubusercontent.com/mlresearch/v267/main/assets/byun25a/byun25a.pdf) (as "TL;DR summarization")**
> Summarization task requiring models to generate concise summaries of Reddit posts, used here as an RLHF benchmark with a learned reward model.

**[GRAM: A Generative Foundation Reward Model for Reward Generalization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ad/wang25ad.pdf) (as "TL;DR comparison data")**
> A dataset composed of summarization response pairs used for domain-specific pre-training of a reward model.

**[RoSTE: An Efficient Quantization-Aware Supervised Fine-Tuning Approach for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25n/wei25n.pdf) (as "Reddit TL;DR Summarization")**
> A summarization benchmark based on the Reddit TL;DR dataset used to evaluate fine-tuned LLMs on generating concise summaries of posts.

## Relationships

### → Reddit TL;DR dataset
- **Text summarization** (behaviors tasks) — *measured_by*
  > We evaluate MA-RLHF on three different datasets for open-ended generation tasks: TL;DR (Stiennon et al., 2020) dataset for text summarization, Anthropic Helpful and Harmless (HH-RLHF) (Bai et al., 2022) for dialogue generation, and WebGPT Comparison (Nakano et al., 2021) for question answering.
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf)
- **Generalization** (constructs) — *measured_by*
  > To evaluate the generalization ability of the aligned models on out-of-distribution data, we fine-tune the models using only posts from the relationship and relationship advice subreddits of the Reddit TL;DR (Stiennon et al., 2020) dataset. (Section 6)
  - [Variational Best-of-N Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/402542c2341e5d2eadc1dd0891275901-Paper-Conference.pdf)
- **Abstractive summarization** (behaviors tasks) — *measured_by*
  - [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf)

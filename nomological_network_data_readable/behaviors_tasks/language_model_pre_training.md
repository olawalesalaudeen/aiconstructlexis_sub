# Language model pre-training
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Pre-training, Language model estimation, Continual pretraining, Pretraining, Continued pretraining, Language model pretraining  

## State of the Field

Across the surveyed literature, language model pre-training is most commonly defined as the task of training a large language model "from scratch" on a large corpus of text. The stated purpose of this process is to learn general language representations or to minimize training loss. A less frequent, more abstract framing describes the task as "Estimating a probability distribution over strings from observed text samples" (The Foundations of Tokenization: Statistical and Computational Concerns). A distinct line of work discusses "continual" or "continued" pre-training, which involves further training an already pretrained model on new or task-specific data, starting from existing parameters rather than random initialization. This behavior is operationalized in studies by training models on various large text corpora, with C4 being a frequently cited dataset, alongside others like OpenWebText, The Pile, and WikiText-103. The performance of models after pre-training is sometimes assessed using downstream benchmarks, including ARC, HellaSwag, COPA, and SciQ. Language model pre-training is also studied in relation to concepts such as training efficiency, catastrophic forgetting, and faithfulness.

## Sources

**[Adam-mini: Use Fewer Learning Rates To Gain More](https://proceedings.iclr.cc/paper_files/paper/2025/file/45ae878717399e6f62d57c65f052cd46-Paper-Conference.pdf) (as "Pre-training")**
> Training a language model from scratch on large text corpora to minimize training loss over many tokens.

**[Cut Your Losses in Large-Vocabulary Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa963ac256590bb7ad5fc26c68229a3a-Paper-Conference.pdf) (as "Pretraining")**
> The initial, large-scale training phase of a language model on a general text corpus, used here as an experimental setting to evaluate the impact of the proposed loss function on model convergence and validation perplexity.

**[The Foundations of Tokenization: Statistical and Computational Concerns](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3748cdac932d91f0a51a37db90dec50-Paper-Conference.pdf) (as "Language model estimation")**
> Estimating a probability distribution over strings from observed text samples.

**[Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf) (as "Continual pretraining")**
> The observable process of further training an already pretrained model on a new dataset, typically a mixture of the original pretraining data and data from a new target domain.

**[Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf) (as "Continued pretraining")**
> Training a model further on task-dependent data after a generic pretraining phase.

**[COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf) (as "Language model pretraining")**
> The task of training a large language model from scratch on a large corpus of text data.

**[On the Optimization Landscape of Low Rank Adaptation Methods for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c34262c35aa5f8c1a091822cbb2020c2-Paper-Conference.pdf)**
> The task of training a large language model from scratch on a large corpus of text to learn general language representations.

## Relationships

### Language model pre-training →
- **C4** (measurements) — *measured_by*
  > “we pre-train a series of auto-regressive language models ... on the C4 dataset”
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **OpenWebText** (measurements) — *measured_by*
  - [Adam-mini: Use Fewer Learning Rates To Gain More](https://proceedings.iclr.cc/paper_files/paper/2025/file/45ae878717399e6f62d57c65f052cd46-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **The Pile** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **COPA** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **SlimPajama** (measurements) — *measured_by*
  - [On the Duality between Gradient Transformations and Adapters](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hennigen25a/hennigen25a.pdf)

### Associated with
- **Training efficiency** (constructs)
  - [How Does Critical Batch Size Scale in Pre-training?](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6f14f95d9c9443927638bcd5d917a7a-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)

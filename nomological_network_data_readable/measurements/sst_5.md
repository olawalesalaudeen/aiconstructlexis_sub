# SST-5
**Type:** Measurement  
**Referenced in:** 22 papers  
**Also known as:** SST5  

## State of the Field

Across the provided literature, SST-5 is consistently characterized as a benchmark for fine-grained sentiment classification. It is frequently identified by its full name, the Stanford Sentiment Treebank, and is defined by its use of five sentiment labels, which several papers specify range from "very negative to very positive" for classifying movie reviews. The predominant application of SST-5 is to measure the behavior of sentiment analysis. Beyond this primary use, it is also employed to evaluate in-context and few-shot learning, sentiment steering, and, in one instance, commonsense knowledge. The benchmark is utilized across different evaluation settings; some studies use it to assess "fine-tuned model performance" for models like RoBERTa-Large, while others apply it to "few-shot classification tasks". A less common framing treats SST-5 as one of several "multiple-choice tasks" for evaluating text generation. One paper also notes its use for "sentiment steering". In summary, while its core identity as a five-class sentiment benchmark is stable, its application varies, serving as a tool to measure a range of model capabilities.

## Sources

**[Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)**
> A five-class sentiment classification benchmark used to evaluate fine-tuned model performance.

**[Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf) (as "SST5")**
> Stanford Sentiment Treebank (SST5) is a benchmark for fine-grained sentiment classification with five labels (from very negative to very positive).

## Relationships

### → SST-5
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  > We select five datasets spanning diverse domains: ... sst5 (Socher et al., 2013) for sentiment classification; (Section 4.1.1)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Sentiment steering** (behaviors tasks) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)

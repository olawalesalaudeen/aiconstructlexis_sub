# Few-shot prompting
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, few-shot prompting is predominantly defined as a method for a model to learn a task from a small number of input-output examples provided directly in the prompt, without any updates to the model's weights. This technique is also referred to as "in-context learning (ICL)" in some work. It is most commonly operationalized as an evaluation procedure where task demonstrations, such as "(question, SQL) pairs," are prepended to the input to guide the model's response. The number of examples varies across studies, with papers mentioning the use of one, two, three, five, and up to fifty examples. The method is used to elicit task performance in areas like arithmetic, classification, and reasoning, and to assess a model's in-context learning capability. Few-shot prompting is frequently studied in contrast to zero-shot and chain-of-thought prompting. While most papers frame it as an evaluation method, a less common perspective treats it as an "interactive behavior" where models use in-context analogies to guide reasoning. The provided data also indicates it is related to iterative refinement and is reported to cause both generalization and input regurgitation.

## Sources

**[Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)**
> Attempting to learn a task from a few input-output examples provided in the prompt, without updating model weights.

## Relationships

### Few-shot prompting →
- **Generalization** (constructs) — *causes*
  - [Continuously Learning, Adapting, and Improving: A Dual-Process Approach to Autonomous Driving](https://proceedings.neurips.cc/paper_files/paper/2024/file/df04a35d907e894d59d4eab1f92bc87b-Paper-Conference.pdf)
- **APPS** (measurements) — *measured_by*
  - [DeFT: Decoding with Flash Tree-attention for Efficient Tree-structured LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6df53f082619d02b9fad64a022e5de3-Paper-Conference.pdf)
- **Input regurgitation** (behaviors tasks) — *causes*
  - [Vision-Language Models Create Cross-Modal Task Representations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25c/luo25c.pdf)

### Associated with
- **Critique** (behaviors tasks)
  - [Teaching Large Language Models to Self-Debug](https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf)

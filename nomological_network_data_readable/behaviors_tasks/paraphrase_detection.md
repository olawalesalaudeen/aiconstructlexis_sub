# Paraphrase detection
**Type:** Behavior  
**Referenced in:** 21 papers  
**Also known as:** Duplication detection, Alignment detection  

## State of the Field

Across the provided literature, paraphrase detection is predominantly defined as the task of determining whether two sentences are paraphrases of each other or share the same meaning. A few papers use alternative names like 'duplication detection' when applied to questions or documents, or 'alignment detection' for classifying informal and formal statements as semantically aligned. The most common operationalization of this behavior is as a binary classification task, with the MRPC and QQP datasets being the most frequently cited instruments for evaluation. One paper explicitly connects this task to the broader concept of 'semantic similarity'. While the classification framing is prevalent, a less common approach reformulates the task as generation, where a model is prompted to "generate a sentence that either supports or contradicts the meaning of a given sentence" (Adapting Large Language Models via Reading Comprehension). Paraphrase detection is often studied as one of several natural language understanding tasks, alongside sentiment analysis, grammatical judgment, and natural language inference.

## Sources

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)**
> The observable task of determining whether two sentences are paraphrases of each other.

**[World Model on Million-Length Video And Language With Blockwise RingAttention](https://proceedings.iclr.cc/paper_files/paper/2025/file/71859ac75d53879d9bbd2f4b77b59929-Paper-Conference.pdf) (as "Duplication detection")**
> The task of identifying whether two questions or documents are semantically equivalent or duplicates.

**[Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf) (as "Paraphrase identification")**
> The observable task of determining whether two sentences have the same meaning.

**[FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf) (as "Alignment detection")**
> The task of classifying a given pair of informal and formal statements as either semantically aligned or misaligned based on a predefined threshold.

## Relationships

### Paraphrase detection →
- **MRPC** (measurements) — *measured_by*
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
- **QQP** (measurements) — *measured_by*
  - [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25en/wang25en.pdf)

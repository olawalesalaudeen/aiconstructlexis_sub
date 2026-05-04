# CoQA
**Type:** Measurement  
**Referenced in:** 24 papers  
**Also known as:** COQA  

## State of the Field

CoQA, or Conversational Question Answering, is consistently described across the provided literature as a dataset or benchmark for evaluation. Its prevailing use is to measure `Conversational question answering` and the broader capability of `Question answering`, often in an "open-book" format where models use a supporting context paragraph to answer questions. Several papers also use CoQA to evaluate `Reading comprehension` and `Information extraction`, with one source specifying its use for "fact extraction" and another labeling it an "extractive question answering task." There is disagreement in the literature regarding the relationship between questions in the dataset. One paper states that the task requires answering "a series of interconnected questions that appear in a conversation" (ExpeTrans:LLMs Are Experiential Transfer Learners), while another uses it specifically "for the Independent setting, where the questions are not related to each other" (SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering). A smaller number of papers also use CoQA to assess `Text generation` and `Commonsense knowledge`.

## Sources

**[BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)**
> CoQA (Conversational Question Answering) is an open-book conversational question answering dataset used for evaluation.

**[HShare: Fast LLM Decoding by Hierarchical Key-Value Sharing](https://proceedings.iclr.cc/paper_files/paper/2025/file/de7dc701a2882088f3136139949e1d05-Paper-Conference.pdf) (as "COQA")**
> The Conversational Question Answering benchmark, a dataset designed to evaluate dialogue-based question-answering systems.

## Relationships

### → CoQA
- **Question answering** (behaviors tasks) — *measured_by*
  > “for the Independent setting, where the questions are not related to each other, we use the CoQA (Reddy et al., 2019)”
  - [MiniCache: KV Cache Compression in Depth Dimension for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fd0705710bf01b88a60a3d479ea341d9-Paper-Conference.pdf)
- **Conversational question answering** (behaviors tasks) — *measured_by*
  > “Conversational Q&A (CoQA) (Reddy et al., 2019): Short-answer questions based on conversational text.”
  - [SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Think before you speak: Training Language Models With Pause Tokens](https://proceedings.iclr.cc/paper_files/paper/2024/file/76917808731dae9e6d62c2a7a6afb542-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks) — *measured_by*
  > “We use all 500 examples (each with 10 to 25 questions) from the validation set to demonstrate how writing style affects fact extraction.”
  - [EnhancingChinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1155.pdf)

# FEVER
**Type:** Measurement  
**Referenced in:** 29 papers  

## State of the Field

Across the provided literature, FEVER is consistently defined as a benchmark for fact verification. The central task requires a model to classify a given claim as "Supported," "Refuted," or "NotEnoughInfo" based on evidence sourced from Wikipedia. The predominant use of FEVER is to evaluate a model's ability to perform fact-checking and determine the veracity of claims. Some papers broaden this scope, using the benchmark to test a model's general "world knowledge and factuality" or its "factual consistency." A less common framing, mentioned by one paper, positions it as a benchmark for natural language inference. Beyond evaluation, FEVER is also employed as a dataset for model training, for instance, as part of a "RAG fine-tuning mixture." As one study notes, it is considered "one of the largest and most widely-used datasets for fact verification" and is frequently used in experiments alongside other knowledge-intensive tasks.

## Sources

**[BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)**
> The Fact Extraction and VERification (FEVER) benchmark is a dataset for fact verification, consisting of claims that need to be classified as Supported, Refuted, or NotEnoughInfo based on evidence from Wikipedia.

## Relationships

### → FEVER
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
- **Fact checking** (behaviors tasks) — *measured_by*
  - [BTR: Binary Token Representations for Efficient Retrieval Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c0f721d329c1a10546869c783e866fb7-Paper-Conference.pdf)

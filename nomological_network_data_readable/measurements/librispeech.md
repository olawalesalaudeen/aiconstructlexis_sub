# LibriSpeech
**Type:** Measurement  
**Referenced in:** 18 papers  
**Also known as:** Librispeech  

## State of the Field

Across the provided literature, LibriSpeech is consistently characterized as a large-scale corpus of read English speech, frequently noted to be derived from audiobooks from the LibriVox project and containing approximately 960 to 1000 hours of data. The most common application of this dataset is to measure `Speech recognition`, with multiple papers using it to evaluate Automatic Speech Recognition (ASR) performance on its various test sets. Beyond ASR, LibriSpeech is also used to assess other capabilities, including `Data reconstruction`, phone recognition, and, in one instance, `Faithfulness`. Researchers operationalize the dataset by employing specific subsets for distinct purposes, such as using the "960-hour training set" for pre-training and various "dev" and "test" sets like "dev-clean" and "test-other" for evaluation. The data is also used for training tokenizers, estimating mutual information, and as prompts for speech continuation tasks, as noted in "A Variational Framework for Improving Naturalness in Generative Spoken Language Models". While some definitions frame it broadly as a corpus for tasks like compression, the prevailing usage in this set of papers is as a benchmark for training and evaluating speech processing models.

## Sources

**[Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf)**
> A large corpus of read English speech, from which chunks are extracted to create a 1GB audio dataset for compression experiments.

**[Aligned Better, Listen Better for Audio-Visual Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c79d6ed1788653643a1ac67b6ea32a7-Paper-Conference.pdf) (as "Librispeech")**
> A speech recognition dataset used for closed-ended audio evaluation.

## Relationships

### → LibriSpeech
- **Speech recognition** (behaviors tasks) — *measured_by*
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **Speech reconstruction** (behaviors tasks) — *measured_by*
  - [SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/86d1ab582afb247ccaa84bec4a7e24f7-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.734.pdf)

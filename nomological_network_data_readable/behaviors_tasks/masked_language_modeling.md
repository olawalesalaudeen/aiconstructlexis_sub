# Masked language modeling
**Type:** Behavior  
**Referenced in:** 19 papers  
**Also known as:** Masked token prediction  

## State of the Field

Across the surveyed literature, Masked language modeling (MLM) is predominantly characterized as a self-supervised pre-training objective for language models. The task is consistently defined as predicting original tokens at positions that have been randomly masked in an input sequence, with some definitions specifying the use of a special `[MASK]` symbol and bidirectional context. One paper notes a common implementation of "masking 15% tokens for training" ("Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs"). The primary stated purpose of this pre-training is to learn robust representations, and one paper suggests this task leads to language understanding. The downstream performance of models trained with this objective is evaluated using the GLUE benchmark. While its main application is pre-training, where it is often contrasted with "next token prediction", a smaller body of work applies MLM to other problems, such as reformulating relation extraction or computing loss on specific probe sentences. The behavior is also studied in relation to `Adaptability` and is considered a form of `Language modeling`.

## Sources

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)**
> Predicting original tokens at masked positions in an input sequence.

**[CODE REPRESENTATION LEARNING AT SCALE](https://proceedings.iclr.cc/paper_files/paper/2024/file/cfbba5249393100ada0bfb37557d2fd9-Paper-Conference.pdf) (as "Masked token prediction")**
> The observable pretraining task of predicting the original identity of a token that has been replaced by a special [MASK] symbol, based on its surrounding bidirectional context.

## Relationships

### Masked language modeling →
- **Language understanding** (behaviors tasks) — *causes*
  - [Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf)
- **GLUE** (measurements) — *measured_by*
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)

### Associated with
- **Adaptability** (constructs)
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [Enhancing Efficiency and Exploration in Reinforcement Learning forLLMs](https://aclanthology.org/2025.emnlp-main.76.pdf)

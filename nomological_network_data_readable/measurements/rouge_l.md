# ROUGE-L
**Type:** Measurement  
**Referenced in:** 28 papers  
**Also known as:** Rouge-L  

## State of the Field

Across the provided literature, ROUGE-L is consistently described as an evaluation metric that measures the similarity between a generated text and a reference text by computing their longest common subsequence. The most prevalent definition characterizes it as an n-gram-based metric, while a smaller set of papers describe it more simply as an "overlap-based metric." Its primary function is to assess the quality of model outputs, and it is used to operationalize several concepts, most commonly correctness, precision, and summarization quality. For instance, some studies define a generated text as correct or "admissible" if its ROUGE-L score exceeds a predefined threshold. Less frequent applications include measuring content homogenization, key point alignment, and overfitting. ROUGE-L is frequently used alongside embedding-based metrics like BERTScore, where it is explicitly positioned to assess "lexical similarity" or "token overlap" as opposed to semantic similarity. As one paper notes, higher scores indicate that a model's responses "contain a significantly larger portion of the same words in the same order" (NEFTune: Noisy Embeddings Improve Instruction Finetuning).

## Sources

**[Does Writing with Language Models Reduce Content Diversity?](https://proceedings.iclr.cc/paper_files/paper/2024/file/02dec8877fb7c6aa9a79f81661baca7c-Paper-Conference.pdf) (as "Rouge-L")**
> Overlap-based metric that measures similarity between texts using longest common subsequence, used here to compute homogenization and key point alignment.

**[Conformal Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf)**
> An n-gram-based evaluation metric that computes the longest common subsequence between generated and reference texts to assess correctness.

## Relationships

### → ROUGE-L
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Seq1F1B: Efficient Sequence-Level Pipeline Parallelism for Large Language Model Training](https://aclanthology.org/2025.naacl-long.455.pdf)

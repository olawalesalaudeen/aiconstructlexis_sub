# Abstractive summarization
**Type:** Behavior  
**Referenced in:** 15 papers  

## State of the Field

Across the provided literature, abstractive summarization is consistently defined as the task of generating a concise and coherent summary that captures the main ideas of a source document. A recurring element in these definitions is that the generated summary can use novel phrasing, paraphrasing, or compression, and is not constrained to using only phrases from the original text. The behavior is operationalized and evaluated using several datasets, with the most frequently cited measurement instrument being the XSum dataset, which one paper describes as requiring the generation of single-sentence summaries from articles. Other datasets used to measure this behavior include XLSum, CNN/DailyMail, the Reddit TL;DR dataset, and DialogSum. Abstractive summarization is frequently studied in relation to hallucination, with one paper noting that "LLMs frequently hallucinate on abstractive summarization tasks" (Teaching Language Models to Hallucinate Less with Synthetic Tasks). The task is also contrasted with extractive summarization and is applied in contexts like document-based question-answering, meeting summarization, and clinical report generation.

## Sources

**[On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)**
> The task of generating a concise and coherent summary that captures the main ideas of a source document, potentially using novel phrasing.

## Relationships

### Abstractive summarization →
- **XSum** (measurements) — *measured_by*
  > We start by evaluating GKD on an abstractive summarization task of generating a summary that captures salient ideas of the input document. To do so, we use the XSum dataset (Narayan et al., 2018) (Section 4.1).
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
- **XLSum** (measurements) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **CNN/DailyMail** (measurements) — *measured_by*
  - [R-BPE: ImprovingBPE-Tokenizers with Token Reuse](https://aclanthology.org/2025.emnlp-main.1170.pdf)
- **Reddit TL;DR dataset** (measurements) — *measured_by*
  - [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
- **Extractive summarization** (behaviors tasks)
  - [MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf)

# BioASQ
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, BioASQ is consistently characterized as a dataset for question answering (QA) within the biomedical or medical domain. It is used to measure the `Question answering` capabilities of models, with one paper specifying its use for "PubMed-based biomedical QA for specialized domains." The dataset is described as containing various question formats, including factoid, list, yes/no, and summary questions. While one source also lists BioASQ as a tool for measuring `Text generation`, no supporting evidence for this usage is provided in the data. The operationalization of the dataset varies across studies; some use it to evaluate retrieval-augmented systems on long-form answers, while another explicitly disregards long answers to "assess the precision of the short responses." Beyond direct evaluation, BioASQ also serves as a component in other research instruments, being included in the MIRAGE benchmark and used as a source to create contexts for the FaithEval benchmark.

## Sources

**[FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)**
> A dataset for biomedical semantic indexing and question answering, used as a source for creating contexts in the FaithEval benchmark.

## Relationships

### → BioASQ
- **Question answering** (behaviors tasks) — *measured_by*
  > We evaluate RAG performance across three datasets spanning different reasoning complexities and domain-specificity... BioASQ (Task 11B) (Krithara et al., 2023): PubMed-based biomedical QA for specialized domains. (Section 3.3)
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)

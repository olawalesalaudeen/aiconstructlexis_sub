# Qasper
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** QASPER  

## State of the Field

Across the provided literature, Qasper is consistently characterized as a question-answering benchmark or dataset based on a corpus of full-text scientific papers, specifically from the natural language processing domain. The most prevalent definition identifies it as part of the SCROLL benchmark and highlights that questions may be unanswerable from the provided text. Papers use Qasper to measure several behaviors, most commonly `Question answering` and `Document question answering` over long documents. It is also used to assess `Information retrieval` and, in at least one instance, `Length generalization`. The dataset is described as containing a mix of abstractive, extractive, and yes/no questions, requiring what one paper calls "complex reasoning about claims made in multiple sections." As one study notes, it "includes 5,049 questions across 1,585 NLP papers" ("RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"). Several sources also mention its use alongside other long-document QA datasets, such as NarrativeQA and QuALITY.

## Sources

**[RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf) (as "QASPER")**
> QASPER is a question-answering benchmark over full NLP papers, used here to assess retrieval and answering over long scientific documents.

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)**
> A dataset from the SCROLL benchmark for question answering about scientific papers, where questions may be unanswerable from the provided abstract or full text.

## Relationships

### → Qasper
- **Question answering** (behaviors tasks) — *measured_by*
  - [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Document question answering** (behaviors tasks) — *measured_by*
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [Steering Knowledge Selection Behaviours inLLMs viaSAE-Based Representation Engineering](https://aclanthology.org/2025.naacl-long.265.pdf)

### Associated with
- **SCROLLS** (measurements)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)

# SCROLLS
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** SCROLL, Scrolls, (Zero)SCROLLS  

## State of the Field

Across the provided literature, SCROLLS (Standardized Compendium of Re-evaluated Long Language-modeling Sets) is consistently presented as a benchmark suite for evaluating language models on tasks involving long texts. Its primary stated purpose is to measure constructs such as "Long-context understanding" and "Long-context processing." Several papers define its goal as assessing a model's ability to "reason over and synthesize information from long texts" ("In-Context Pretraining: Language Modeling Beyond Document Boundaries"). The benchmark operationalizes this evaluation through a collection of tasks, most commonly cited as question answering and summarization, with some sources also including classification. One definition specifies that the suite contains seven different datasets. A recurring characterization is that SCROLLS uses "realistic tasks that require processing long inputs collected from real-world scenarios" ("Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack"). Some sources mention it alongside a related benchmark, ZeroSCROLLS, and one notes that its tasks have average input lengths ranging from 1.7k to 49.3k tokens. In practice, researchers use SCROLLS for finetuning experiments and to evaluate model performance on long sequences.

## Sources

**[Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf)**
> Standardized Compendium of Re-evaluated Long Language-modeling Sets (SCROLLS) is a benchmark suite of seven datasets for evaluating models on long-text tasks such as question answering and summarization.

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf) (as "SCROLL")**
> A benchmark suite for evaluating the ability of language models to reason over and synthesize information from long texts.

**[BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Scrolls")**
> A benchmark for standardized comparison over long language sequences, consisting of tasks like QA, classification, and summarization.

**[Stress-Testing Long-Context Language Models with Lifelong ICL and Task Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cc8db5884a7474b4771762b6f0c8ee1-Paper-Datasets_and_Benchmarks_Track.pdf) (as "(Zero)SCROLLS")**
> A benchmark consisting of realistic tasks that require processing long inputs from real-world scenarios, such as summarization and question answering.

## Relationships

### → SCROLLS
- **Long-context reasoning** (constructs) — *measured_by*
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)

### Associated with
- **QMSum** (measurements)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **Qasper** (measurements)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **NarrativeQA** (measurements)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)

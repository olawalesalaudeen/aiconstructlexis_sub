# XSum
**Type:** Measurement  
**Referenced in:** 83 papers  
**Also known as:** XSUM, Xsum, xSum, X-SUM  

## State of the Field

Across the surveyed literature, XSum is predominantly characterized as a benchmark for abstractive and extreme text summarization. The core task, as defined by most papers, involves generating a concise, single-sentence summary from a news article, with many sources specifying the articles are from the BBC. Consequently, its most frequent application is to measure the behavior of `Text summarization` and, more specifically, `Abstractive summarization`, with numerous studies using it to evaluate and fine-tune models. A secondary line of work utilizes XSum in the context of machine-generated text detection, where it serves as a source of human-written news text or as a domain for evaluating detection methods. A few papers offer more specific framings, describing it as a "non-argumentative summarization task" or a tool to assess "generative coherence and fluency," while another uses it for hallucination evaluation.

## Sources

**[Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy](https://proceedings.iclr.cc/paper_files/paper/2024/file/e537e071277a2e5fefaa78f87500c7b4-Paper-Conference.pdf)**
> A summarization benchmark consisting of news articles paired with abstractive summaries.

**[DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf) (as "Xsum")**
> The Extreme Summarization dataset, used for evaluating abstractive text summarization systems.

**[Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf) (as "XSUM")**
> A benchmark for extreme summarization, where the task is to generate a short, one-sentence summary of a news article.

**[OpenDebateEvidence: A Massive-Scale Argument Mining and Summarization Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c630d28df1cff44314d5798f82e02ec-Paper-Datasets_and_Benchmarks_Track.pdf) (as "xSum")**
> A dataset designed for single-sentence news summarization, used to evaluate models on a non-argumentative summarization task.

**[What Happened inLLMs Layers when Trained for Fast vs. Slow Thinking: A Gradient Perspective](https://aclanthology.org/2025.acl-long.1546.pdf) (as "X-SUM")**
> A dataset for evaluating abstractive summarization of single-sentence summaries of news articles in English, used to assess generative coherence and fluency.

## Relationships

### → XSum
- **Text summarization** (behaviors tasks) — *measured_by*
  > Table 4a presents hallucination evaluation on summarization datasets XSum (Narayan et al., 2018), CNN/DM (See et al., 2017), and MultiNews (Fabbri et al., 2019). (Section 3.6)
  - [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf)
- **Abstractive summarization** (behaviors tasks) — *measured_by*
  > We start by evaluating GKD on an abstractive summarization task of generating a summary that captures salient ideas of the input document. To do so, we use the XSum dataset (Narayan et al., 2018) (Section 4.1).
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [LiteASR: Efficient Automatic Speech Recognition with Low-Rank Approximation](https://aclanthology.org/2025.emnlp-main.170.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **QuALITY** (measurements) — *measured_by*
  - [Faster Cascades via Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/6f43166f50f26e8d8f3edc5545b0749f-Paper-Conference.pdf)
- **Document summarization** (behaviors tasks) — *measured_by*
  > We evaluate PbT on three tasks with five benchmarks: ...document summarization (XSum (Narayan et al., 2018) and CNNDM (Hermann et al., 2015))... (Section 4)
  - [Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf)

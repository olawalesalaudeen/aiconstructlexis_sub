# LongEval
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** LONGEVAL  

## State of the Field

The provided literature presents two distinct characterizations of the LongEval benchmark. The prevailing usage, found across multiple papers, defines LongEval as an instrument for measuring the long-context performance of language models. In this context, it is operationalized through tasks such as topic retrieval and line retrieval with varying prompt lengths, and is used to assess the construct of Information retrieval. One paper describes this version as "one of the pioneer work which includes various long context retrieval tasks" (CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis). A different use of the name "LONGEVAL" appears in a smaller set of the provided work, where it is defined as a benchmark for evaluating long document summarization factuality on scientific texts. This version is used to measure the construct of Faithfulness, with performance assessed via "summary-level correlation metrics" such as Kendall’s Tau. Additionally, the long-context retrieval version of the benchmark is noted to have "inspired the StreamEval dataset" (Efficient Streaming Language Models with Attention Sinks).

## Sources

**[Efficient Streaming Language Models with Attention Sinks](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Paper-Conference.pdf)**
> A benchmark designed to measure the long-context performance of language models, consisting of topic retrieval and line retrieval tasks with varying prompt lengths.

**[COVE:COntext andVEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.103.pdf) (as "LONGEVAL")**
> Evaluation benchmark for long document summarization factuality, used to assess performance on scientific texts with summary-level correlation metrics.

## Relationships

### → LongEval
- **Long-context understanding** (constructs) — *measured_by*
  - [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [COVE:COntext andVEracity prediction for out-of-context images](https://aclanthology.org/2025.naacl-long.103.pdf)

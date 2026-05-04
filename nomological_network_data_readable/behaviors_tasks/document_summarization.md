# Document summarization
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Document Summarization  

## State of the Field

Across the provided literature, document summarization is most frequently defined as the task of generating a concise summary from one or more long documents. A smaller body of work offers more specific framings, such as comprehending a document's substance to produce a "succinct and cohesive summary" (Benchmarking LLMs via Uncertainty Quantification), or generating summaries from a context containing multiple concatenated documents. As an observable behavior, this task is operationalized and measured using several benchmarks. Papers in this set use LongBench, ZeroSCROLLS, HaluEval, CNN/DailyMail, and XSum to evaluate document summarization performance. For instance, LongBench is described as a tool for assessing "long-context understanding" that includes a dedicated summarization task category. The types of inputs mentioned for these tasks include academic papers, government reports, manuals, and loan agreements. The behavior is often framed as a task "requiring extensive context retention" (Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs) and is studied alongside long-context processing.

## Sources

**[Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)**
> The task of generating a concise summary of one or more long documents.

**[Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Document Summarization")**
> Comprehending the substance and context of a given document and producing a succinct and cohesive summary.

## Relationships

### Document summarization →
- **LongBench** (measurements) — *measured_by*
  > ZeroSCROLLS (Shaham et al., 2023) and LongBench (Bai et al., 2023) tackle tasks like long-document QA and query-based summarization. (Section 5)
  - [$\text{D}_{2}\text{O}$: Dynamic Discriminative Operations for Efficient Long-Context Inference of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d862f7f5445255090de13b825b880d59-Paper-Conference.pdf)
- **HaluEval** (measurements) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ZeroSCROLLS** (measurements) — *measured_by*
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
- **CNN/DailyMail** (measurements) — *measured_by*
  - [Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **XSum** (measurements) — *measured_by*
  > We evaluate PbT on three tasks with five benchmarks: ...document summarization (XSum (Narayan et al., 2018) and CNNDM (Hermann et al., 2015))... (Section 4)
  - [Reading Between the Prompts: How Stereotypes ShapeLLM’s Implicit Personalization](https://aclanthology.org/2025.emnlp-main.1030.pdf)

### → Document summarization
- **Long-context understanding** (constructs) — *causes*
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)

### Associated with
- **Long-context understanding** (constructs)
  - [CanLLMs Generate and Solve Linguistic Olympiad Puzzles?](https://aclanthology.org/2025.emnlp-main.970.pdf)

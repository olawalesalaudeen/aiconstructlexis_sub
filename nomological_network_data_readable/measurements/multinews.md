# MultiNews
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Multi-News  

## State of the Field

Across the provided literature, MultiNews is consistently characterized as a benchmark dataset for evaluating multi-document summarization. Its primary application is to measure the behavior of `Text summarization`, a use case supported by multiple papers. The definitions are in strong agreement, describing it as a tool for assessing tasks that require the synthesis of information from several documents. One paper provides specific details on its composition, stating it "consists of 56k news articles and summary pairs where the news articles are extracted from newser.com and the summary is written by professional editors" (GraphRouter: A Graph-based Router for LLM Selections). In practice, it is used to operationalize a "Summarization task" for model performance comparisons. Additionally, some papers situate MultiNews as a component of the LongBench benchmark suite, where it is used to evaluate multi-document summarization alongside other tasks.

## Sources

**[GraphRouter: A Graph-based Router for LLM Selections](https://proceedings.iclr.cc/paper_files/paper/2025/file/41b6674c28a9b93ec8d22a53ca25bc3b-Paper-Conference.pdf) (as "Multi-News")**
> A benchmark dataset for multi-document summarization, consisting of news articles and human-written summaries from newser.com.

**[APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)**
> A dataset used for evaluating summarization tasks requiring synthesis of multiple documents.

## Relationships

### → MultiNews
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Accelerating Blockwise Parallel Language Models with Draft Refinement](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c9629e718d931e8d4d240378aa1d3bf-Paper-Conference.pdf)

### Associated with
- **LongBench** (measurements)
  > “Following CacheBlend, we evaluate on four LongBench datasets (Bai et al., 2024): 2WikiMQA (multi-document question answering), MuSiQue (multi-document question answering), SAMSum (few-shot instruction following), and MultiNews (multi-document summarization). We also include HotpotQA (multi-document question answering) from LongBench”
  - [EPIC: Efficient Position-Independent Caching for Serving Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25j/hu25j.pdf)

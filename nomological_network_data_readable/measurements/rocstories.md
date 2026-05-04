# ROCStories
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** ROC Stories, RocStories  

## State of the Field

Across the provided literature, ROCStories is consistently described as a dataset composed of five-sentence stories, but it is operationalized for different evaluation purposes. A prevalent application is for story generation, where it is used to assess a model's ability to produce coherent narratives. This is framed in one paper as a "title-to-story generation" task and in another as a more general evaluation of "open-ended conditional generation." In contrast, a separate line of work uses ROCStories to measure text infilling performance. This is operationalized by masking a middle sentence and evaluating the generated replacement, with one study specifically mentioning the use of perplexity (PPL) for this evaluation. This application is further supported by its documented use as a measurement instrument for the behavior of "Text infilling." Thus, while the dataset's core content of short, commonsense stories is agreed upon, it is used to evaluate distinct model capabilities ranging from conditional generation to story completion.

## Sources

**[The Impact of Token Granularity on the Predictive Power of Language Model Surprisal](https://aclanthology.org/2025.acl-long.210.pdf)**
> A dataset for title-to-story generation, used to evaluate a model's ability to generate coherent, five-sentence narrative stories from a given title.

**[Benchmarking Long-Context Language Models on Long Code Understanding](https://aclanthology.org/2025.acl-long.1325.pdf) (as "ROC Stories")**
> Story completion dataset used to evaluate infilling performance by masking a middle sentence and assessing coherence of generated replacements.

**[Judging Quality Across Languages: A Multilingual Approach to Pretraining Data Filtering with Language Models](https://aclanthology.org/2025.emnlp-main.450.pdf) (as "RocStories")**
> A dataset for story generation, consisting of five-sentence commonsense stories, used to evaluate open-ended conditional generation.

## Relationships

### → ROCStories
- **Text infilling** (behaviors tasks) — *measured_by*
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)

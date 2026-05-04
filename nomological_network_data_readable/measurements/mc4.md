# MC4
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** mC4  

## State of the Field

Across the provided literature, MC4 is consistently described as a large, multilingual dataset derived from web crawls, with the most common name being the 'multilingual Colossal Clean Crawled Corpus'. It serves multiple functions in the research process, from model training to evaluation and analysis. Some papers use it as a data source for pre-training distillation, while others position it as a benchmark for evaluating multilingual pre-training behavior, computing model perplexity across languages, or reporting validation loss. Beyond these uses, researchers also employ MC4 to approximate entity frequency in pre-training data, verify model reconstruction quality, and record feature activations. A frequently mentioned characteristic is its coverage of a mix of high-, medium-, and low-resource languages. This linguistic diversity is a noted feature, with one paper highlighting the data imbalance by stating the corpus 'contains 2733 billion English tokens but only 1 billion Swahili tokens.'

## Sources

**[DEPT: Decoupled Embeddings for Pre-training Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/20ceffa1fcec0f882868e5b891e3e7fa-Paper-Conference.pdf)**
> A multilingual web-crawl corpus used here as a benchmark spanning high-, medium-, and low-resource languages for evaluating multilingual pre-training behavior.

**[Improving Language Model Distillation through Hidden State Matching](https://proceedings.iclr.cc/paper_files/paper/2025/file/2fb462e23667ad5e6471a4e9af8e4774-Paper-Conference.pdf) (as "mC4")**
> The multilingual Colossal Clean Crawled Corpus, a large multilingual dataset used for the pre-training distillation stage of the experiments.

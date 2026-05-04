# Financial Phrasebank
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Financial PhraseBank, FPB  

## State of the Field

Across the provided literature, Financial Phrasebank is consistently characterized as a benchmark dataset used for sentiment analysis within the financial domain. The dataset is described as containing sentences from financial news or financial text that are annotated for sentiment, with one source specifying the labels as "positive, negative, or neutral." The prevailing use of this instrument is to measure the behavior of `Text classification`, and it is frequently cited as a standard benchmark for this purpose. Papers use it to assess "classification performance in domain-specific language understanding" and to evaluate proposed methods against other text classification benchmarks. The task is framed as both sentiment analysis and, more broadly, sentence classification.

## Sources

**[Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf)**
> A benchmark dataset for text classification consisting of sentences from financial news, annotated for sentiment.

**[MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf) (as "Financial PhraseBank")**
> Sentiment analysis dataset for financial text, used to assess classification performance in domain-specific language understanding.

**[Large Language Models are Demonstration Pre-Selectors for Themselves](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25i/jin25i.pdf) (as "FPB")**
> The Financial PhraseBank, a dataset for sentiment analysis of financial news, categorized into positive, negative, or neutral.

## Relationships

### → Financial Phrasebank
- **Text classification** (behaviors tasks) — *measured_by*
  > We assessed our proposed methods by comparing them with standard loss functions across several text classification benchmarks, including Financial Phrasebank (Financial) (Malo et al., 2014), irony detection (Tweet Irony) (Van Hee et al., 2018), and the MRPC dataset from GLUE (Wang et al., 2018).
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)

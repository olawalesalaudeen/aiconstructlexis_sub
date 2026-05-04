# Amazon Polarity
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Amazon, AMAZON  

## State of the Field

Across the provided literature, the dataset referred to as "Amazon" or "Amazon Polarity" is most commonly used as a benchmark for text classification, specifically for evaluating sentiment analysis of product reviews. Several papers frame it this way, with one study noting its use for "sentiment analysis (SST-2 (Socher et al., 2013), Amazon and Yelp (Zhang et al., 2015a))" ("In-Context Pretraining: Language Modeling Beyond Document Boundaries"). This prevailing usage positions it as a standard NLP classification dataset. However, a few papers present alternative operationalizations under the "Amazon" name. One paper describes it as a product search dataset with an associated knowledge graph containing relations like "products viewed or purchased together" ("Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective"). Another study uses it as a product co-purchasing network for node classification tasks. A third, distinct usage treats it as a temporal point process benchmark, where the goal is "to predict the timestamp and category... of the next reviewed product" ("LAST SToP for Modeling Asynchronous Time Series"). These varied applications show the dataset is used to measure several different phenomena beyond its most frequent application in sentiment analysis.

## Sources

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf) (as "Amazon")**
> A benchmark dataset for text classification, specifically for sentiment analysis of product reviews.

**[Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective](https://aclanthology.org/2025.naacl-long.216.pdf) (as "AMAZON")**
> A product search dataset from the STaRK benchmark, where documents are derived from product reviews and Q&A records, and a knowledge graph contains relations like 'products viewed together'.

**[Relating Misfit to Gain in Weak-to-Strong Generalization Beyond the Squared Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mulgund25a/mulgund25a.pdf)**
> A sentiment classification benchmark used here as an NLP classification dataset.

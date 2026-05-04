# CoNLL-2003
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** CoNLL2003, CoNLL’03, CoNLL03  

## State of the Field

Across the provided literature, CoNLL-2003 is consistently characterized as a benchmark dataset for Named Entity Recognition (NER). It is described as an English, "flat" NER dataset derived from news articles. The prevailing use of CoNLL-2003 is to evaluate a model's ability to perform `Information extraction`, specifically by identifying and classifying named entities into predefined categories. Most sources specify that the dataset contains four entity types—persons, locations, organizations, and miscellaneous—although one definition lists only three. The data is also noted to be tagged using the "IOB scheme." While its primary application is for NER, a smaller line of work uses it to evaluate "token-level representation learning" through tasks like NER, chunking, and POS tagging. Another paper more broadly frames it as a dataset "widely used for benchmarking sequence labeling models."

## Sources

**[An Efficient Task-Oriented Dialogue Policy: Evolutionary Reinforcement Learning Injected by Elite Individuals](https://aclanthology.org/2025.acl-long.172.pdf) (as "CoNLL2003")**
> Named entity recognition dataset that evaluates a model’s ability to identify and classify named entities in text into predefined categories such as person, organization, and location.

**[Benchmarking Long-Context Language Models on Long Code Understanding](https://aclanthology.org/2025.acl-long.1325.pdf)**
> Named entity recognition dataset used to evaluate token-level representation learning through tasks like NER, chunking, and POS tagging.

**[GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.288.pdf) (as "CoNLL’03")**
> An English flat Named Entity Recognition (NER) dataset widely used for benchmarking sequence labeling models.

**[Seeing the Same Story Differently:Framing‐Divergent Event Coreference for Computational Framing Analysis](https://aclanthology.org/2025.emnlp-main.1441.pdf) (as "CoNLL03")**
> A benchmark dataset for named entity recognition derived from news articles, containing entities of four types: persons, locations, organizations, and miscellaneous.

## Relationships

### → CoNLL-2003
- **Information extraction** (behaviors tasks) — *measured_by*
  > English flat NER datasets (CoNLL’03 (Sang and De Meulder, 2003) and MIT-Movie (Liu et al., 2013)); (Section 4.1)
  - [Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf)

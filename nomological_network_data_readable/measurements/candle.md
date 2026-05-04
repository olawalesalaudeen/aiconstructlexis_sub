# Candle
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** CANDLE  

## State of the Field

The prevailing usage of Candle in the provided literature is as a measurement instrument for assessing cultural knowledge in language models. Most papers operationalize it as a benchmark or dataset, with one source describing it as a large-scale (1.1M samples) multiple-choice question benchmark focused on "cultural norms and commonsense knowledge." It is explicitly used to measure the construct of "Cultural knowledge" and is also characterized as a dataset for "culture-specific items (CSIs)." One study notes a limitation, stating that "CANDLE considers only a limited set of facets that may not fully represent Indian culture." In a distinct usage, one paper describes Candle not as a benchmark but as an "international research program studying various human values," which is used alongside the World Values Survey to select sensitive topics for dataset creation.

## Sources

**[A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.388.pdf)**
> An international research program studying various human values, used alongside the World Values Survey to select sensitive topics for dataset creation.

**[Word Salad Chopper: Reasoning Models Waste A Ton Of Decoding Budget On Useless Repetitions, Self-Knowingly](https://aclanthology.org/2025.emnlp-main.1706.pdf) (as "CANDLE")**
> A prior dataset for culture-specific items that extracts cultural commonsense knowledge from web-scale corpora, used here as a baseline for comparison in cultural adaptation evaluation.

## Relationships

### → Candle
- **Cultural knowledge** (constructs) — *measured_by*
  > Fine-tuning with CULTUREINSTRUCT outperforms the base LLMs significantly on multiple types of cultural benchmarks, including: (i) benchmarks for general cultural knowledge - CULTURALBENCH (Chiu et al., 2024), CANDLE (Nguyen et al., 2023), and ETICOR (Dwivedi et al., 2023) (Section 4.1)
  - [ManaTTSPersian: a recipe for creatingTTSdatasets for lower resource languages](https://aclanthology.org/2025.naacl-long.465.pdf)

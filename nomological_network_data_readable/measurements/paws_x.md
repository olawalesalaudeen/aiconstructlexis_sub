# PAWS-X
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided sources, PAWS-X is consistently described as a multilingual or cross-lingual benchmark used to measure the behavior of paraphrase identification. The core task requires a model to determine if two sentences have the same meaning, with one paper specifying this involves distinguishing semantically equivalent sentences from near-duplicates. The dataset is characterized as containing "adversarially constructed paraphrase pairs" and provides paired sentences across multiple languages, with one source mentioning seven. While its primary application is for paraphrase identification, a few papers also position PAWS-X more broadly as a benchmark for natural language understanding (NLU). It is sometimes included in assessments alongside other benchmarks that cover a range of abilities, such as reasoning and generation. Therefore, its prevailing use is to operationalize and evaluate a model's ability to recognize paraphrases in a multilingual context.

## Sources

**[Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)**
> A multilingual benchmark for paraphrase identification, requiring the model to determine if two sentences have the same meaning.

## Relationships

### → PAWS-X
- **Paraphrase identification** (behaviors tasks) — *measured_by*
  > We perform zero-shot evaluation on six tasks that test the LLMs ability on reasoning (Xstorycloze, Xcopa) (Ponti et al., 2020), coreference resolution (Xwinograd) (Muennighoff et al., 2023), reading comprehension (Lambada) (Paperno et al., 2016), natural language understanding (XNLI) (Conneau et al., 2018), and paraphrasing (PAWS-X) (Yang et al., 2019). (Section 4)
  - [Simple Yet Effective: An Information-Theoretic Approach to Multi-LLMUncertainty Quantification](https://aclanthology.org/2025.emnlp-main.1552.pdf)

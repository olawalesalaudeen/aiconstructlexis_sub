# Translation capability
**Type:** Construct  
**Referenced in:** 7 papers  
**Also known as:** Machine translation capability, Translation ability, Translation performance  

## State of the Field

Across the surveyed literature, **Translation capability** is most commonly defined as a model's latent or underlying capacity for accurate and fluent translation between languages. This construct is operationalized by evaluating model outputs on translation tasks, with one paper explicitly using the Super-Natural Instructions benchmark for this purpose. A recurring theme is that this capability can emerge even when models are trained on non-parallel data, as one study notes that "Multilingual large language models (LLM) trained on non-parallel data yield impressive translation capabilities" (The Reasonableness Behind Unreasonable Translation Capability of Large Language Model). However, the influence of training data composition is also discussed, with some work suggesting that "the amount of bilingual signal" or "word alignment data" affects the capability. While most definitions are general, a smaller set of papers frames the concept in specific contexts, such as its development in low-resource settings or its transferability to speech translation tasks. The term is sometimes used interchangeably with "translation performance" and is also studied in relation to "Knowledge transferability".

## Sources

**[A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b9536e186a77feff516893a5f393f7a-Paper-Conference.pdf)**
> The underlying capacity of a model to accurately and fluently translate between languages, inferred from performance across diverse translation directions.

**[SURVEYFORGE: On the Outline Heuristics, Memory-Driven Generation, and Multi-dimensional Evaluation for Automated Survey Writing](https://aclanthology.org/2025.acl-long.610.pdf) (as "Machine translation capability")**
> The latent ability of a large language model to translate text between different languages, which can be transferred to improve performance on speech translation tasks.

**[Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf) (as "Translation ability")**
> The latent capacity to produce correct target-language translations from source-language input across low-resource settings.

**[An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf) (as "Translation performance")**
> The capability of a language model to accurately and fluently translate text from a source language to a target language.

## Relationships

### Translation capability →
- **Super-Natural Instructions** (measurements) — *measured_by*
  - [An Auditing Test to Detect Behavioral Shift in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7af140f516c9f57050f7359bf53bc8f0-Paper-Conference.pdf)

### Associated with
- **Knowledge transferability** (constructs)
  - [Assessing Reliability and Political Bias InLLMs’ Judgements of Formal and Material Inferences With Partisan Conclusions](https://aclanthology.org/2025.acl-long.1451.pdf)

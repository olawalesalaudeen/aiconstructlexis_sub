# GlobalOpinionQA
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** GLOBALOPINIONQA  

## State of the Field

GlobalOpinionQA is consistently described across papers as a dataset or benchmark composed of questions and answers from cross-national surveys, specifically the World Values Survey and the PEW Global Attitudes Survey. Its prevailing use is to evaluate how opinions expressed by language models align with aggregated human opinions from different countries. The provided literature uses the instrument to measure several constructs, including `societal bias`, `distribution alignment`, and `personalization`. For example, one paper uses it to "identify model bias in representing diverse viewpoints" by comparing model outputs to population-level data. Another study adapts the dataset to measure `personalization` by treating each country as a distinct "user" and converting the survey's answer distributions into single, most-probable answers. Operationally, it is a multiple-choice question-answering dataset, and some researchers use it as a "template for consistency" when formatting survey data for LLM evaluation. The dataset is noted to contain approximately 2,500 questions and is also used for sampling countries to maintain geographical and GDP-level diversity.

## Sources

**[FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.598.pdf)**
> A dataset of questions and answers from cross-national surveys (World Values Survey and PEW Global Attitudes Survey) designed to capture diverse perspectives on global issues.

**[ManaTTSPersian: a recipe for creatingTTSdatasets for lower resource languages](https://aclanthology.org/2025.naacl-long.465.pdf) (as "GLOBALOPINIONQA")**
> Benchmark aggregating Pew Global Attitudes Survey and World Values Survey to assess alignment of model responses with human opinions across regions.

## Relationships

### → GlobalOpinionQA
- **Distribution alignment** (constructs) — *measured_by*
  - [Understanding Figurative Meaning through Explainable Visual Entailment](https://aclanthology.org/2025.naacl-long.2.pdf)
- **Societal bias** (constructs) — *measured_by*
  > GlobalOpinionQA (Durmus et al., 2024) uses multiple-choice questions to assess the opinions stated by a model relative to aggregated population opinions from different countries. The goal is to identify model bias in representing diverse viewpoints. (Section 3)
  - [Mixture of Multimodal Adapters for Sentiment Analysis](https://aclanthology.org/2025.naacl-long.91.pdf)
- **Personalization** (constructs) — *measured_by*
  > For GlobalOpinionQA, since the dataset originally included the answer distribution by multiple respondents in the same country, we converted it to have a single answer by selecting the choice with the highest probability. It results in 920 training and 1,317 test QA pairs across 46 countries. We consider each country as a specific user. (Section 4.1)
  - [FollowIR: Evaluating and Teaching Information Retrieval Models to Follow Instructions](https://aclanthology.org/2025.naacl-long.598.pdf)

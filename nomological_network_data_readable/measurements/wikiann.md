# WikiAnn
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** WikiANN  

## State of the Field

Across the provided sources, WikiAnn is consistently characterized as a multilingual dataset used to evaluate named entity recognition (NER). It is explicitly positioned as a measurement instrument for the broader construct of Information extraction. The dataset is described as being extracted from Wikipedia, though sources vary on its exact scope, with one definition citing 282 languages and another mentioning 176. A recurring application is the evaluation of model performance on low-resource languages; one paper specifically uses it to test models on Sino-Tibetan languages, noting they "amount to 131K name mentions" (LLMs as Meta-Reviewers’ Assistants: A Case Study). Another paper frames its use more broadly for "crosslingual sequence labeling evaluation" (Takin-VC: Expressive Zero-Shot Voice Conversion via Adaptive Hybrid Content Encoding and Enhanced Timbre Modeling). As an operationalization of NER performance, one study details running experiments with ChatGPT on the dataset.

## Sources

**[LLMs as Meta-Reviewers’ Assistants: A Case Study](https://aclanthology.org/2025.naacl-long.396.pdf)**
> Named entity recognition (NER) dataset covering 282 languages, used to evaluate model performance on low-resource Sino-Tibetan languages.

**[Takin-VC: Expressive Zero-Shot Voice Conversion via Adaptive Hybrid Content Encoding and Enhanced Timbre Modeling](https://aclanthology.org/2025.acl-long.88.pdf) (as "WikiANN")**
> Named entity recognition dataset extracted from Wikipedia, used for crosslingual sequence labeling evaluation.

## Relationships

### → WikiAnn
- **Information extraction** (behaviors tasks) — *measured_by*
  - [LLMs as Meta-Reviewers’ Assistants: A Case Study](https://aclanthology.org/2025.naacl-long.396.pdf)

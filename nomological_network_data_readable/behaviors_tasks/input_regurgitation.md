# Input regurgitation
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Contextual copying, In-context copying  

## State of the Field

Input regurgitation is consistently described across the provided literature as the observable behavior of a language model reproducing verbatim or near-verbatim content from its input context. The framing of this behavior, however, varies across different studies. Some work treats it as a fundamental capability for precise retrieval, with one paper noting it is "one of the most fundamental abilities of language models" ("WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks"). In this view, it is operationalized through tasks where the model's objective is to "output the suffix of the queried prefix". Another line of work frames it as a desired ability in specific domains, such as accurately copying predefined code elements like function names and parameters ("CxGGEC: Construction-Guided Grammatical Error Correction"). In contrast, a different perspective treats input regurgitation as a potential failure, explicitly linking it to privacy risks, as "LLMs are likely to leak the augmented contexts if they were trained on them" ("500xCompressor: Generalized Prompt Compression for Large Language Models"). One paper also reports that the behavior can be caused by few-shot prompting.

## Sources

**[CxGGEC: Construction-Guided Grammatical Error Correction](https://aclanthology.org/2025.acl-long.308.pdf) (as "Contextual copying")**
> Accurately reproducing specific code elements (e.g., function names, parameters) from the input context regardless of their position, testing permutation-invariant retrieval.

**[WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf) (as "In-context copying")**
> The observable behavior of reproducing a specific token sequence from earlier in the input when prompted, demonstrating precise retrieval from long contexts.

**[500xCompressor: Generalized Prompt Compression for Large Language Models](https://aclanthology.org/2025.acl-long.1220.pdf)**
> The observable behavior where an LLM reproduces verbatim or near-verbatim portions of the augmented input context in its output, potentially indicating privacy leakage.

## Relationships

### → Input regurgitation
- **Few-shot prompting** (measurements) — *causes*
  - [Vision-Language Models Create Cross-Modal Task Representations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25c/luo25c.pdf)

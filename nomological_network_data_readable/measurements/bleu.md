# BLEU
**Type:** Measurement  
**Referenced in:** 21 papers  

## State of the Field

Across the provided literature, BLEU is consistently defined as a metric that measures the similarity between a generated text and one or more reference texts based on n-gram overlap. Its most prevalent application is evaluating the quality of machine translation, where it is used to assess "fluency and idiom translation" and overall "translation quality." However, its use extends to other text generation tasks, including text revision, the evaluation of code review comments, and multi-document question answering. Papers operationalize it at different granularities, such as at the "sentence-level and document-level." While widely used as a proxy for "fluency and syntactic similarity," one paper cautions that it can be a "misleading" metric for tasks like analogical reasoning, as it "can assign inflated similarity scores to fallacious answers" due to its insensitivity to deeper meaning. In practice, BLEU is frequently reported alongside other evaluation metrics, such as ROUGE-L, BERTScore, and COMET.

## Sources

**[Arabic Dataset forLLMSafeguard Evaluation](https://aclanthology.org/2025.naacl-long.286.pdf)**
> A string similarity metric used to evaluate the overlap between generated and reference solutions in analogy tasks, though noted as potentially misleading due to insensitivity to meaningful analogical reasoning.

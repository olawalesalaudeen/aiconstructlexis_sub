# Veracity prediction
**Type:** Behavior  
**Referenced in:** 3 papers  

## State of the Field

Veracity prediction is consistently framed as a classification task where a model judges the truthfulness of a claim based on provided evidence. The operationalization of this task varies across the surveyed literature, particularly in the types of claims evaluated and the classification labels used. One prevalent approach treats it as a binary classification for image captions, with labels such as `{accurate, OOC}` (out-of-context), based on an associated image and external evidence. Another common framing involves producing a binary `{Supported, Refuted}` judgment for a complex textual claim. A third variation expands the label set to `{supported, refuted, or not enough information}` for claims in specialized domains like health, which are evaluated against scientific evidence. The task is explicitly situated within automated fact-checking (AFC) research. One study also describes an alternative setup where models are prompted "without any evidence to test whether it already has parametric knowledge about the claims" (Multi3Hate: Multimodal, Multilingual, and Multicultural Hate Speech Detection with Vision–Language Models).

## Sources

**[From Allies to Adversaries: ManipulatingLLMTool-Calling through Adversarial Injection](https://aclanthology.org/2025.naacl-long.102.pdf)**
> The task of classifying a claim, such as an image caption, as either accurate or out-of-context (OOC) based on an associated image and external evidence.

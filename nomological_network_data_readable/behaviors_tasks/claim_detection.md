# Claim detection
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

In the provided literature, claim detection is characterized as the task of identifying whether a sentence contains a claim that requires fact-checking or related labeling. This task is positioned as "the first step" in a broader verification process. The behavior is operationalized at the sentence level, with one paper noting the creation of a dataset using annotated transcripts from YouTube Short videos. Another source applies the concept to "review comments" to determine if they contain a claim, which is described as a "subjective opinion". This task is explicitly related to the concept of verifiability, where identifying a claim is a prerequisite for evaluating how well it is substantiated.

## Sources

**[MixLoRA-DSI: Dynamically Expandable Mixture-of-LoRAExperts for Rehearsal-Free Generative Retrieval over Dynamic Corpora](https://aclanthology.org/2025.emnlp-main.21.pdf)**
> Identifying whether a transcript sentence contains a claim that should be labeled for fact-checking or related categories.

## Relationships

### Associated with
- **Verifiability** (constructs)
  > This aspect [Verifiability] evaluates whether a review comment contains a claim (i.e., a subjective opinion) and how well it is substantiated. The first step is to determine whether the comment includes any claims. (Section 3.1)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1476.pdf)

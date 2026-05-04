# Semantic consistency
**Type:** Construct  
**Referenced in:** 20 papers  
**Also known as:** Visual-semantic consistency, Semantic coherence  

## State of the Field

Across the provided literature, semantic consistency is predominantly framed as the preservation of meaning under various transformations. The most common definition concerns a model's ability to produce consistent outputs when presented with semantically equivalent but syntactically different inputs, such as paraphrased questions or perturbed symbolic programs. For instance, one study notes that models can "generate contradictory outputs when presented with prompts with similar or equivalent semantics" (LeveragingLLMFor Synchronizing Information Across Multilingual Tables). A related line of work extends this concept to consistency across different data modalities, defining it as the alignment between visual and textual representations or across text, fusion, and visible modalities.

The operationalization of semantic consistency frequently involves measuring the similarity of model outputs. Common measurement techniques include calculating the "cosine similarity between answer embeddings" for responses to varied phrasings of the same question or computing an "average pairwise semantic similarity" among repeated generations for a single prompt. One paper also describes a benchmark, PopQA-TP, used for assessing this ability. A less frequent framing, termed "semantic coherence," is treated as a latent quality of a model's output, evaluated by human judges on its logical consistency and contextual relevance. Another specific application involves ensuring a refined prompt does not lose context or narrow the focus of the original prompt.

## Sources

**[FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf) (as "Visual-semantic consistency")**
> The degree to which the model's visual representations maintain a coherent and meaningful alignment with their corresponding semantic (textual) representations across different levels of granularity.

**[Empowering Visible-Infrared Person Re-Identification with Large Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d4ee9e805cc90f636c66778225181036-Paper-Conference.pdf)**
> The extent to which representations preserve the same underlying meaning across text, fusion, and visible modalities.

**[Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf) (as "Semantic coherence")**
> The latent quality of a model's generated output to be logically consistent, contextually relevant, and meaningful in relation to the input.

## Relationships

### Semantic consistency →
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf)

### Associated with
- **Autoformalization** (behaviors tasks)
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)

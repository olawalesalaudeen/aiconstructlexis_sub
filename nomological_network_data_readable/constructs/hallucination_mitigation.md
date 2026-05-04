# Hallucination mitigation
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Hallucination reduction  

## State of the Field

Across the surveyed literature, hallucination mitigation is broadly characterized as a model's capacity to avoid generating false or unsupported content. The most prevalent definition frames this as a "latent ability" to refrain from producing such content, especially when faced with ambiguous or unanswerable questions and guided by demonstrations. A more specific framing, found in one paper, defines it as the "degree to which a model avoids generating factually incorrect or unsupported medical information," such as "recommending antibiotics for viral infections." This construct is operationalized and measured using the AMBER benchmark, which is reported to evaluate various hallucination types, including those of existence, attribute, and relation. Several techniques are associated with achieving this mitigation; for instance, retrieval-augmented generation (RAG) is described as a "promising technology" for grounding outputs in retrieved evidence. Other cited methods include multimodal in-context learning, which is noted to reduce hallucination over zero-shot inference, and the use of vector retrieval with a structured medical knowledge graph to improve factual consistency.

## Sources

**[Emergence of Episodic Memory in Transformers: Characterizing Changes in Temporal Structure of Attention Scores During Training](https://aclanthology.org/2025.naacl-long.449.pdf)**
> The latent ability of a model to refrain from generating false or unsupported content, particularly in response to ambiguous or unanswerable queries, when guided by appropriate demonstrations.

**[Quantized but Deceptive? A Multi-Dimensional Truthfulness Evaluation of QuantizedLLMs](https://aclanthology.org/2025.emnlp-main.1549.pdf) (as "Hallucination reduction")**
> The degree to which a model avoids generating factually incorrect or unsupported medical information during consultation.

## Relationships

### Hallucination mitigation →
- **AMBER** (measurements) — *measured_by*
  > “AMBER (Wang et al., 2023) provides a discriminative way to evaluate various types of hallucination including existence, attribute and relation”
  - [Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning](https://aclanthology.org/2025.naacl-long.170.pdf)

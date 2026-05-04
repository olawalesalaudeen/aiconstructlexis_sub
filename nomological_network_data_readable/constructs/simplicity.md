# Simplicity
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Layness, Pipeline simplicity  

## State of the Field

Across the provided literature, Simplicity is predominantly framed as a latent trait reflecting a model's ability to reduce linguistic and conceptual complexity, making text accessible to a general, non-expert audience. One paper uses the term 'Layness' to describe this same quality, defined as the degree to which text is suitable for non-experts. A distinct and less common framing, 'Pipeline simplicity,' refers to an architectural design principle favoring simpler model structures. The field operationalizes the primary, text-based definition of Simplicity through several methods. Human evaluation is a common approach, with papers describing the use of annotators to rate simplicity or layness on a 5-point Likert scale. Automatic evaluation is also employed, with the SARI metric being explicitly cited for this purpose. Other reported measurement instruments include LLM-based evaluation and the PRMBENCH benchmark. One study further specifies that simplicity can be assessed either as a raw quality of the output or as a 'relative simplicity gain when compared to the input complex sentence.'

## Sources

**[On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)**
> The latent trait reflecting a model's ability to reduce linguistic and conceptual complexity, making text accessible to non-experts without domain knowledge.

**[VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf) (as "Layness")**
> The degree to which the generated text is suitable and understandable for a general, non-expert audience.

**[VISaGE: Understanding Visual Generics and Exceptions](https://aclanthology.org/2025.emnlp-main.1656.pdf) (as "Pipeline simplicity")**
> The design principle that simpler architectures with fewer processing stages tend to be more effective and robust when paired with strong language and embedding models, avoiding unnecessary complexity.

## Relationships

### Simplicity →
- **Human evaluation** (measurements) — *measured_by*
  > Using a 1-5 Likert scale, the judges are asked to rate the model output based on five criteria: comprehensiveness, layness, meaning preservation, conciseness, and fluency. (Section 5.3.3).
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **SARI** (measurements) — *measured_by*
  > We evaluate DSPT5 with other SOTA LLMs using the following automatic evaluation metrics... (4) Simplicity: SARI (Xu et al., 2016a). (Section 5.2)
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.327.pdf)
- **PRMBENCH** (measurements) — *measured_by*
  - [Language Constrained Multimodal Hyper Adapter For Many-to-Many Multimodal Summarization](https://aclanthology.org/2025.acl-long.1230.pdf)

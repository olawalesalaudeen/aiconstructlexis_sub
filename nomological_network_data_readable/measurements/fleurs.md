# FLEURS
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Fleurs  

## State of the Field

Across the provided literature, FLEURS is consistently characterized as a multilingual speech benchmark with a dual application. It is used to measure both speech recognition and machine translation, specifically automatic speech translation (AST). Some sources define it primarily for testing speech recognition models, with one paper operationalizing this by computing Word Error Rate (WER) on the English subset of the dataset. Other papers define and use it as a multilingual speech translation benchmark, for instance, to evaluate translation between English and German, Spanish, and French. The dataset is described as "massively multilingual," covering "speech for 102 languages." Its role as a foundational instrument is also noted, as it serves as the basis for FLEURS-ASL, an extension developed to support American Sign Language.

## Sources

**[Elevating LegalLLMResponses: Harnessing Trainable Logical Structures and Semantic Knowledge with Legal Reasoning](https://aclanthology.org/2025.naacl-long.291.pdf) (as "Fleurs")**
> The Few-shot Learning Evaluation of Universal Representations of Speech dataset, a multilingual speech benchmark used for testing speech recognition models.

**[Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.314.pdf)**
> A multilingual speech translation benchmark used here to evaluate translation between English and German, Spanish, and French in both directions.

## Relationships

### → FLEURS
- **Speech recognition** (behaviors tasks) — *measured_by*
  - [TokenSkip: Controllable Chain-of-Thought Compression inLLMs](https://aclanthology.org/2025.emnlp-main.166.pdf)
- **Machine translation** (behaviors tasks) — *measured_by*
  - [TokenSkip: Controllable Chain-of-Thought Compression inLLMs](https://aclanthology.org/2025.emnlp-main.166.pdf)

### Associated with
- **FLEURS-ASL** (measurements)
  > In this paper, we introduce FLEURS-ASL, an extension of FLORES/FLEURS to support their ﬁrst sign language, American Sign Language. (Section 1)
  - [Examining and Adapting Time for Multilingual Classification via Mixture of Temporal Experts](https://aclanthology.org/2025.naacl-long.314.pdf)

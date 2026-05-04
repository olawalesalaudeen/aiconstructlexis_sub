# Definition generation
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Terminology explanation, Entity description generation  

## State of the Field

Across the surveyed literature, definition generation is a behavior involving the production of explanatory text for a given term, word, or entity. The most common framing is generating a natural language definition for a target word based on its usage in a specific context, with stated goals of ensuring the output is grammatical, fluent, and faithful. A related application is generating "accessible explanations" of specialized terminology to support non-expert users. A different operationalization, termed "Entity description generation," involves producing a more structured output—a title and an opening sentence—for an entity by conditioning the generation on retrieved contextual passages from sources like Wikipedia. The quality of the generated text is a recurring theme, and one paper reports using an `LLM-as-a-judge` to "provide qualitative insights into the quality of generated descriptions" ("Concept-pedia: a Wide-coverage Semantically-annotated Multimodal Dataset"). This behavior is studied in relation to `Hallucination`, as errors in generation can manifest as "gross hallucinations." It is also associated with `Knowledge transferability`.

## Sources

**[Concept-pedia: a Wide-coverage Semantically-annotated Multimodal Dataset](https://aclanthology.org/2025.emnlp-main.1746.pdf) (as "Entity description generation")**
> Producing a title and definition (opening sentence) for an entity mention by generating text conditioned on retrieved contextual passages.

**[Towards Author-informedNLP: Mind the Social Bias](https://aclanthology.org/2025.emnlp-main.1765.pdf) (as "Terminology explanation")**
> Generating accessible explanations of specialized or unfamiliar terms to support non-expert users in evaluating factual consistency.

**[Jigsaw-Puzzles: From Seeing to Understanding to Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1321.pdf)**
> Producing a natural language definition for a target word given its usage in context, ensuring grammaticality, fluency, and faithfulness to meaning.

## Relationships

### Definition generation →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > we employ a Large Language Model (LLM) as a judge (LLM-as-a-Judge) (Gu et al., 2024) to provide qualitative insights into the quality of generated descriptions (Section 5.4).
  - [Concept-pedia: a Wide-coverage Semantically-annotated Multimodal Dataset](https://aclanthology.org/2025.emnlp-main.1746.pdf)

### Associated with
- **Knowledge transferability** (constructs)
  - [Jigsaw-Puzzles: From Seeing to Understanding to Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1321.pdf)
- **Hallucination** (behaviors tasks)
  > “the improved accuracy of the definitions, which helps minimize the hallucinations occasionally observed in the pre-trained model.”
  - [MicroEdit: Neuron-level Knowledge Disentanglement and Localization in Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.1720.pdf)

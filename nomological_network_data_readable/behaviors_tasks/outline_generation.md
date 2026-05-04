# Outline generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Based on the provided literature, outline generation is characterized as the task of creating a structured plan or hierarchy of sections for a document before the full content is written. This process is operationalized as a generation step that uses retrieved information and an input topic to produce the outline, a procedure one paper formalizes as `O = Generate(I, T)`. The concept is studied in relation to structured output generation, where the outline functions as a preliminary scaffold for subsequent tasks. For instance, one study describes using LLMs "to construct a structured presentation outline of multiple entries." This generated outline then serves as a guide for creating other content, as another paper notes that "slides are generated iteratively" based on the outline from a previous phase.

## Sources

**[Refusal-Aware Red Teaming: Exposing Inconsistency in Safety Evaluations](https://aclanthology.org/2025.emnlp-main.50.pdf)**
> The task of creating a structured plan or hierarchy of sections for an article based on retrieved information before writing the full content.

## Relationships

### Associated with
- **Structured output generation** (behaviors tasks)
  > Guided by the presentation outline from the previous phase, slides are generated iteratively. (Section 2.3)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.728.pdf)

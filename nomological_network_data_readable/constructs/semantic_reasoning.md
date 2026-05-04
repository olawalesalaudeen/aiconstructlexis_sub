# Semantic reasoning
**Type:** Construct  
**Referenced in:** 12 papers  

## State of the Field

Across the provided literature, semantic reasoning is framed in two distinct ways, with no single prevailing definition. One line of work defines it as a model's capacity to understand language instructions in relation to objects and actions in an environment, particularly in the context of robotics and "long-horizon planning." This form of the construct is operationalized through tasks like Referring Expression Comprehension, which requires using both spatial and semantic reasoning to localize an object from a textual query. A different framing treats semantic reasoning as a latent ability for multi-step inference to connect concepts that are not explicitly stated in text. In this view, it is associated with Chain-of-Thought (CoT) prompting to identify "implicit targets" and is categorized as a subtype of Text-Based Reasoning, which depends on linguistic evidence. The reliability of this latter form of reasoning is noted to potentially "vary across model families and domain shifts." The concept is also studied alongside table understanding, though the nature of this relationship is not specified.

## Sources

**[HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3bfee3bc6639c36e6e7b058db909f760-Paper-Conference.pdf)**
> The model's capacity to understand and reason about the meaning of language instructions and their relationship to objects and actions in the environment.

## Relationships

### Associated with
- **Referring expression understanding** (behaviors tasks)
  > Referring Expression Comprehension (REC) (Mao et al., 2016), which involves localizing an object in an image based on a complex textual query, requiring both spatial and semantic reasoning.
  - [LLM-wrapper: Black-Box Semantic-Aware Adaptation of Vision-Language Models for Referring Expression Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb8f2d4e90018c0fae060dff09a91ce3-Paper-Conference.pdf)
- **Text-based reasoning** (constructs)
  > The first broad category, Text-Based (TB) Reasoning, includes explanations that depend solely on surface-level linguistic evidence found within the premise and hypothesis, without appealing to world knowledge. Six subtypes are defined: Coreference, Syntactic, Semantic, Pragmatic, Absence of Mention and Logic Conflict. (Section 3.1)
  - [MPCG: Multi-Round Persona-Conditioned Generation for Modeling the Evolution of Misinformation withLLMs](https://aclanthology.org/2025.emnlp-main.1728.pdf)
- **Table question answering** (behaviors tasks)
  - [Improving the Quality of Web-mined Parallel Corpora of Low-Resource Languages using Debiasing Heuristics](https://aclanthology.org/2025.emnlp-main.1436.pdf)

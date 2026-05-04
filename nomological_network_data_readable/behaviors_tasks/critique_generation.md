# Critique generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Across the surveyed literature, critique generation is consistently framed as the behavior of a model producing textual feedback on another model's output. The most prevalent definition describes this as producing an explanation that identifies specific error spans in a generated sentence and suggests fixes, with one paper detailing a subtask that "generates a critique ci detailing the error span... and suggest a fix" ("Palette of Language Models: A Solver for Controlled Text Generation"). Other work offers a more structured view, defining the critique space as comprising an analysis of strengths and weaknesses, actionable suggestions, and a final judgment of correctness. A more general definition simply casts it as producing natural language feedback on the quality of a response. Operationally, this behavior is elicited by training models, sometimes referred to as "critic models", to generate critiques for a given input and response. The provided research also positions critique generation as having a directional relationship with other concepts; it is reported to influence Reward Modeling, Commonsense knowledge, and Self-correction.

## Sources

**[Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)**
> The observable behavior of producing a textual explanation that identifies error spans in a generated sentence and suggests fixes.

## Relationships

### Critique generation →
- **Reward Modeling** (measurements) — *causes*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Self-correction** (behaviors tasks) — *causes*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)

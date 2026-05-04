# Flexibility
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, the construct of Flexibility is framed in two distinct ways. The most prevalent usage defines it as a guardrail model's ability to adapt to new or unseen safety categories without requiring complete retraining. This form of flexibility is operationalized by modifying a model's knowledge base or reasoning structure, as one paper notes its system "can effectively adapt to unseen safety categories by simply editing the reasoning graph" ($R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning). This adaptability is reported to be enhanced by both Logical reasoning and Prompt engineering. A different line of work treats Flexibility as "the tendency to produce ideas that span multiple distinct semantic categories" (On the Same Wavelength? Evaluating Pragmatic Reasoning in Language Models across Broad Concepts). In this context, it is measured by counting the number of distinct semantic categories in responses, a metric also referred to as a "Creativity Quotient (CQ)". This creativity-focused version of Flexibility is shown to correlate with Originality. Thus, the term's application diverges between the architectural adaptability of safety systems and the semantic diversity of generated content.

## Sources

**[$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)**
> The ability of a guardrail model to adapt to new or unseen safety categories without requiring complete retraining, often by modifying its knowledge base or reasoning structure.

## Relationships

### Flexibility →
- **Originality** (constructs) — *correlates*
  > “For convergent validity, MUSESCORER’s normalized originality scores {Othresh_i} correlate strongly with Creativity Quotient (CQ) scores in socialmuse24. CQ is a flexibility measure that captures the diversity of semantic categories.”
  - [On the Same Wavelength? Evaluating Pragmatic Reasoning in Language Models across Broad Concepts](https://aclanthology.org/2025.emnlp-main.1009.pdf)

### → Flexibility
- **Prompt engineering** (behaviors tasks) — *causes*
  > VGD enhances the interpretability, generalization, and flexibility of prompt generation without the need for additional training. (Section 1)
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Logical reasoning** (constructs) — *causes*
  > The grounding knowledge and principled reasoning procedure enable R2-Guard to be effective, robust against jailbreak attacks, and flexible given new safety categories. (Abstract)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)

# Textual bias
**Type:** Construct  
**Referenced in:** 3 papers  
**Also known as:** Text bias  

## State of the Field

Across the provided literature, textual bias is consistently characterized as a form of modality bias where a model's performance is predominantly influenced by its textual input. The concept is framed in two ways: one paper defines it narrowly as the "latent tendency" of a model to "preferentially rely on textual input over audio evidence when the two modalities conflict," leading to "severe performance degradation." A second, broader definition describes it as any multimodal context where performance is predominantly driven by textual features. This latter framing is also applied to datasets, with one study noting a "strong textual bias in these datasets, where over 90% of the samples require textual input... for correct classification." The construct is operationalized and measured through human evaluation, as one paper states that "Human annotation also verifies that around 80% samples in both datasets are textually biased."

## Sources

**[CalligraphicOCRforChinese Calligraphy Recognition](https://aclanthology.org/2025.emnlp-main.246.pdf) (as "Text bias")**
> The latent tendency of a model to preferentially rely on textual input over audio evidence when the two modalities conflict, even when the text is misleading.

**[Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf)**
> A specific form of modality bias where a model's performance is predominantly influenced by textual features, even in a multimodal context.

## Relationships

### Textual bias →
- **Human evaluation** (measurements) — *measured_by*
  > “Human annotation also verifies that around 80% samples in both datasets are textually biased, which supports our findings.”
  - [Evaluating the Evaluators: Are readability metrics good measures of readability?](https://aclanthology.org/2025.emnlp-main.1226.pdf)

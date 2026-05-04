# Model uncertainty
**Type:** Construct  
**Referenced in:** 3 papers  

## State of the Field

Model uncertainty is presented as a construct representing a model's latent confidence in its next-token predictions. The provided data consistently operationalizes this concept by measuring the entropy of the model's output probability distribution, with one paper specifying the formula Ht = H(P(Xt|x<t)). This measurement is used to determine when to apply interventions during generation; as one study notes, "when uncertainty is high, guidance signals are selectively introduced," whereas no action is taken if the model is considered confident below a certain entropy threshold. Furthermore, model uncertainty is reported to have a "strong positive correlation" with hallucination. This relationship is leveraged in research that "encourages the model to discover more deterministic and optimal decoding paths" as a means to improve performance.

## Sources

**[ImproveLLM-as-a-Judge Ability as a General Ability](https://aclanthology.org/2025.emnlp-main.713.pdf)**
> The latent level of confidence a model has in its next-token predictions, inferred from the entropy of its output probability distribution, which influences where interventions are applied.

## Relationships

### → Model uncertainty
- **Hallucination** (behaviors tasks) — *correlates*
  > we first conduct an uncertainty analysis, revealing a strong positive correlation between hallucination and model uncertainty. (Abstract)
  - [CIKT: A Collaborative and Iterative Knowledge Tracing Framework with Large Language Models](https://aclanthology.org/2025.emnlp-main.976.pdf)

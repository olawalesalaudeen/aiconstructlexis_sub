# Predictive uncertainty
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Prediction uncertainty  

## State of the Field

Across the provided literature, predictive uncertainty is consistently framed as the degree of confidence or ambiguity in a large language model's predictions. The most common operationalization involves measuring the entropy of the model's output probability distribution, where higher entropy indicates greater uncertainty. Another method mentioned, CAMIA, analyzes the model's transition from an initial state of high ambiguity to confident predictions during token generation. This uncertainty is reported to increase in response to ambiguous or complex prefixes, which may cause a model to "rely on specific memorized sequences encountered during training" ("Confounding Factors in Relating Model Performance to Morphology"). Other work notes that factors like "harmful knowledge" and introspection can also influence uncertainty levels. Predictive uncertainty is studied in relation to the behavior of hallucination, though the nature of the link is described differently across papers. One source suggests that predictive uncertainty causes hallucination, while another reports a correlation between the two.

## Sources

**[Information Integration in Large Language Models is Gated by Linguistic Structural Markers](https://aclanthology.org/2025.emnlp-main.352.pdf) (as "Prediction uncertainty")**
> The degree of confidence in a model's predictions, often measured by the entropy of its output probability distribution, where higher entropy indicates greater uncertainty.

**[Confounding Factors in Relating Model Performance to Morphology](https://aclanthology.org/2025.emnlp-main.370.pdf)**
> The degree of ambiguity in the model's next-token predictions, which decreases more rapidly for memorized sequences as the model resolves uncertainty through recall.

## Relationships

### Predictive uncertainty →
- **Hallucination** (behaviors tasks) — *causes*
  - [Improving Uncertainty Estimation through Semantically Diverse Language Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf)

### → Predictive uncertainty
- **Hallucination** (behaviors tasks) — *correlates*
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)

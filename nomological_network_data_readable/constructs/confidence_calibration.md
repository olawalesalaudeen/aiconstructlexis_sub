# Confidence calibration
**Type:** Construct  
**Referenced in:** 96 papers  
**Also known as:** Calibration, Miscalibration, QA-calibration, Belief calibration  

## State of the Field

Across the surveyed literature, confidence calibration is most commonly defined as the degree to which a model's expressed confidence aligns with its actual correctness. The prevailing view is that for a well-calibrated model, predictions assigned a certain confidence level should be correct at a corresponding rate. While this core definition is widespread, a smaller line of work introduces more specific framings, such as "belief calibration," which connects confidence to a statement's truthfulness, and "QA-calibration," which requires the alignment to hold across distinct groups of questions and answers. The concept is also frequently discussed alongside "uncertainty estimation," which is described as a model's capacity to evaluate the reliability of its own predictions.

Researchers operationalize this construct by comparing model-generated confidence scores—often derived from output probabilities, logits, or entropy—to observed accuracy on tasks like text classification. The most commonly mentioned metric for this evaluation is the Expected Calibration Error (ECE). There is a notable disagreement within the provided sources regarding the calibration of contemporary models. Several papers state that models are often "poorly calibrated" or "overconfident," particularly after fine-tuning. In contrast, other studies assert that large language models are "fairly well calibrated," with confidence serving as a reliable proxy for correctness. The stated purpose for studying calibration is to enhance model trustworthiness and mitigate biases.

## Sources

**[Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf) (as "Calibration")**
> The degree to which a model's predicted probabilities reflect true likelihoods of correctness, particularly in the presence of contextual biases from prompts or in-context examples.

**[Bayesian Low-rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/07c256a163a7559186ec1c71e95b9ec9-Paper-Conference.pdf) (as "Uncertainty estimation")**
> The latent capacity of a model to estimate the reliability of its own predictions, typically measured via entropy or confidence scores, used here to guide dynamic fusion decisions.

**[LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf) (as "Confidence estimation")**
> Deriving a numerical measure of a model's certainty in its generated output, either at the token, sequence, or claim level.

**[Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf) (as "Miscalibration")**
> The degree to which a model's output probabilities are poorly aligned with the true likelihood of correctness, leading to unreliable confidence scores.

**[Selective Generation for Controllable Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5a6815122f533193a022cbc41786c1cc-Paper-Conference.pdf)**
> The degree to which a model's expressed confidence in its predictions aligns with its actual correctness.

**[QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf) (as "QA-calibration")**
> A latent property where a model's confidence scores match its actual accuracy conditional on specific groups of question-and-answer pairs, ensuring reliability across different topics or user contexts.

**[ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.158.pdf) (as "Belief calibration")**
> The extent to which the model's expressed confidence in a statement matches the statement's actual truthfulness.

## Relationships

### Associated with
- **Overconfidence** (constructs)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
- **Reliability** (constructs)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)

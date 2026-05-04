# Perspective taking
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Perspective separation  

## State of the Field

Across the provided literature, perspective taking is predominantly characterized as the ability to understand a scene from a viewpoint other than one's own. This concept is framed in multiple ways: as a capacity for 'mental simulation' (Core Knowledge Deficits in Multi-Modal Language Models), as an internal ability to 'distinguish and represent cognitive information from different agents' points of view' under the name 'perspective separation' (From Black Boxes to Transparent Minds...), and as the task of describing what is visible from a specified viewpoint in an image (MIA-Bench...). The construct is operationalized and measured through different methods. One approach involves behavioral evaluation, where models are prompted to adopt a specific viewpoint, for instance, 'imagine you are the lady in the image, describe what you can see' (MIA-Bench...). Another line of work measures it internally by using linear probing to 'identify attention heads that are sensitive to perspective separation' within a model's representations (From Black Boxes to Transparent Minds...). Perspective taking is studied in relation to Theory of Mind, with one paper noting that the ability to distinguish perspectives provides 'evidence of ToM capabilities' (From Black Boxes to Transparent Minds...). One study suggests that models perform 'markedly worse than humans' on this ability, attributing it to a 'limited capacity for mental simulation' (Core Knowledge Deficits in Multi-Modal Language Models).

## Sources

**[Core Knowledge Deficits in Multi-Modal Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25p/li25p.pdf)**
> The ability to mentally simulate and understand a scene from a different viewpoint than one's own.

**[From Black Boxes to Transparent Minds: Evaluating and Enhancing the Theory of Mind in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bj/li25bj.pdf) (as "Perspective separation")**
> The model's internal ability to distinguish and represent cognitive information from different agents' points of view, separate from an omniscient perspective.

## Relationships

### Perspective taking →
- **Linear probing** (measurements) — *measured_by*
  > Using logistic regression, we performed binary classification on the representations of positive and negative samples to identify attention heads that are sensitive to perspective separation and belief representation.
  - [From Black Boxes to Transparent Minds: Evaluating and Enhancing the Theory of Mind in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bj/li25bj.pdf)

### Associated with
- **Theory of mind** (constructs)
  - [REVIVINGYOURMNEME: Predicting The Side Effects ofLLMUnlearning and Fine-Tuning via Sparse Model Diffing](https://aclanthology.org/2025.emnlp-main.1642.pdf)

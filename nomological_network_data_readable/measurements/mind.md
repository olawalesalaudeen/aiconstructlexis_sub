# MIND
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

MIND is presented in the provided literature as a method for hallucination detection. The most frequently described feature across sources is its capacity to automatically label data, which is contrasted with methods that rely on pre-annotated datasets. It is described as both a "classification-based" and an "unsupervised" method. One paper details its operationalization, stating that it "truncates Wikipedia articles and prompts an LLM to continue the next sentence," then automatically generates truth labels by matching named entities between the model's response and the original text. The method has been studied in relation to the construct of Generalization. One source reports that its "accuracy drops significantly when tested on other datasets," indicating an "inability to generalize well."

## Sources

**[Beyond Sequences: Two-dimensional Representation and Dependency Encoding for Code Generation](https://aclanthology.org/2025.acl-long.309.pdf)**
> A classification-based hallucination detection method that automatically labels data during detection to train its classifier.

## Relationships

### Associated with
- **Generalization** (constructs)
  > However, its accuracy drops significantly when tested on other datasets, indicating its inability to generalize well. (Section 4.1)
  - [One Planner To Guide Them All ! Learning Adaptive Conversational Planners for Goal-oriented Dialogues](https://aclanthology.org/2025.emnlp-main.1124.pdf)

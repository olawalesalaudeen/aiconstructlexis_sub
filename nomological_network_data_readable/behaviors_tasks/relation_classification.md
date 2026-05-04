# Relation classification
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Based on the available data, relation classification is defined as the observable task of assigning one or more relation labels to a pair of entities in a sentence according to their semantic relationship. The provided source material discusses two distinct ways this behavior is operationalized for large language models. One approach is multi-class classification, which requires a model to understand the semantics of all possible relation categories. However, one paper notes that this can be difficult for LLMs. An alternative operationalization frames the task as a binary classification problem, where a model must simply "determine whether this relation exists between the two queried entities" (AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity).

## Sources

**[AssoCiAm: A Benchmark for Evaluating Association Thinking while Circumventing Ambiguity](https://aclanthology.org/2025.emnlp-main.264.pdf)**
> The observable task of assigning one or more relation labels to a pair of entities in a sentence based on their semantic relationship.

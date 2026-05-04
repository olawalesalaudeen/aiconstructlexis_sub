# HANS
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

HANS is predominantly characterized as a dataset for Natural Language Inference (NLI), frequently described as a 'stress test' or 'adversarial' dataset. Across the provided papers, its main purpose is to evaluate a model's reliance on simple heuristics, with 'lexical overlap' being the most commonly cited heuristic it is designed to challenge. One paper elaborates that it manipulates features like subsequence and negation to expose reliance on 'syntactic heuristics rather than semantic understanding.' In practice, HANS is used to measure the behavior of `Natural language inference` and, in one instance, the construct of `Safety`. Researchers also use it for more specific assessments, such as evaluating 'minority generalization' and assessing 'length bias in binary classification.' The dataset, which one source notes contains 30K examples, is applied in both finetuning and in-context learning (ICL) evaluation settings. The consistent focus on testing against heuristics positions HANS as an instrument for evaluating whether models move beyond superficial cues for NLI tasks.

## Sources

**[CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.466.pdf)**
> Natural Language Inference dataset designed to evaluate models' sensitivity to lexical overlap and other artifacts, used here to assess length bias in binary classification.

## Relationships

### → HANS
- **Natural language inference** (behaviors tasks) — *measured_by*
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Generating Plausible Distractors for Multiple-Choice Questions via Student Choice Prediction](https://aclanthology.org/2025.acl-long.1155.pdf)

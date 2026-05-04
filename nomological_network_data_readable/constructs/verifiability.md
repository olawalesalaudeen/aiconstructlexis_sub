# Verifiability
**Type:** Construct  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, Verifiability is most frequently defined by the capacity to systematically check a model's reasoning process for correctness. This prevailing view, found in papers like "Fann or Flop" and "ImpliHateVid", emphasizes that a "structured decomposition" of reasoning enhances transparency and allows for the "systematic verification of each step." A different perspective, offered in "SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models", frames verifiability from a user-centric standpoint, defining it as the extent to which an LLM's output provides accurate citations that allow users to "double-check the answer." While the former focuses on the internal process, the latter centers on validating the final output. As a construct, Verifiability is operationalized through the task of Claim detection. One paper's evaluation process involves first determining if a comment contains a claim and then assessing how well that claim is substantiated. Ultimately, the concept is associated with improving transparency, trustworthiness, and facilitating error tracing in model outputs.

## Sources

**[ImpliHateVid: A Benchmark Dataset and Two-stage Contrastive Learning Framework for Implicit Hate Speech Detection in Videos](https://aclanthology.org/2025.acl-long.843.pdf)**
> The extent to which a model's reasoning process can be systematically checked for correctness due to its transparency and structured form.

## Relationships

### Associated with
- **Claim detection** (behaviors tasks)
  > This aspect [Verifiability] evaluates whether a review comment contains a claim (i.e., a subjective opinion) and how well it is substantiated. The first step is to determine whether the comment includes any claims. (Section 3.1)
  - [CLMTracing: Black-box User-level Watermarking for Code Language Model Tracing](https://aclanthology.org/2025.emnlp-main.1476.pdf)

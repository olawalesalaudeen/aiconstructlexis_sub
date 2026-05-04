# Prediction confidence
**Type:** Construct  
**Referenced in:** 3 papers  

## State of the Field

In the provided literature, prediction confidence is defined as the degree to which a model is certain about its predictions. The primary operationalization of this construct is through "the variance in perplexity scores across different choices for a given question," as stated in "Streamlining Redundant Layers to Compress Large Language Models." Further, the WikiText dataset is explicitly used as an instrument to assess the model's prediction confidence. One study also references a "stdi value" where a higher value indicates greater confidence. The concept is applied in the context of model compression to evaluate "stability," which measures the consistency of predictions before and after pruning. Additionally, prediction confidence is studied in relation to hallucination, with one paper describing knowledge hallucination as the act of "generating nonfactual responses with unwarranted confidence."

## Sources

**[Streamlining Redundant Layers to Compress Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4b00a351b41358965613c118e87dc28c-Paper-Conference.pdf)**
> The degree to which a model is certain about its predictions, operationally measured by the variance in perplexity scores across different choices for a given question.

## Relationships

### Prediction confidence →
- **WikiText** (measurements) — *measured_by*
  > "WikiText (Merity et al., 2022) to assess the model’s prediction confidence" (Section 5.1, Datasets)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  > "knowledge hallucination ... generating nonfactual responses with unwarranted confidence"
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)

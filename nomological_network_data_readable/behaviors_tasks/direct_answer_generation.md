# Direct answer generation
**Type:** Behavior  
**Referenced in:** 3 papers  

## State of the Field

Based on the provided data, direct answer generation is defined as an observable answering behavior where a model produces a final answer without showing intermediate reasoning steps. This behavior is framed as one of two typical approaches for question-answering systems, the other being "elaborate step-by-step reasoning" (AdaptThink: Reasoning Models Can Learn When to Think). It is studied in relation to Chain-of-thought reasoning (CoT), often as an alternative or more efficient mode of operation. For instance, one paper describes a framework to internalize CoT into a non-autoregressive "Silent Thought", which avoids the explicit output of reasoning steps (MIO: A Foundation Model on Multimodal Tokens). The provided materials characterize this as a mode of system operation rather than detailing specific benchmarks or datasets used for its evaluation.

## Sources

**[AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.185.pdf)**
> An observable answering behavior where the model produces a final answer without showing intermediate reasoning steps.

## Relationships

### Associated with
- **Chain-of-thought reasoning** (constructs)
  > DART (Distilling Autoregressive Reasoning to Silent Thought), a novel framework that enables the LLMs to internalize the autoregressive CoT into non-autoregressive Silent Thought (ST) with an excellent efficiency-efficacy trade-off. (Section 1)
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.256.pdf)

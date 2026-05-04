# Zero-shot evaluation
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Zero-Shot  

## State of the Field

Across the surveyed literature, Zero-shot evaluation is predominantly described as an evaluation setting or protocol designed to test a model's performance without any task-specific examples or demonstrations. The central operational characteristic, mentioned in nearly all sources, is that models are prompted to perform a task without any in-context examples, forcing them to rely on their pre-existing knowledge. As one paper puts it, "The models generate responses based solely on their pre-training" (Predicate-Guided Generation for Mathematical Reasoning). The most frequently stated purpose of this method is to assess a model's generalization ability and intrinsic knowledge. This is operationalized by measuring performance on tasks in "unseen domains without any fine-tuning" (FactCG: Enhancing Fact Checkers with Graph-Based Multi-Hop Data), through cross-lingual transfer, or by evaluating inherent capabilities such as temporal reasoning and Emotion analysis. A less common framing, from a single paper, treats it as a "prompting method where the model generates responses directly without additional guidance" (Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units). The approach is used across various tasks, including toxicity detection, ScreenQA, and query-focused summarization.

## Sources

**[DETQUS: Decomposition-Enhanced Transformers forQUery-focused Summarization](https://aclanthology.org/2025.naacl-long.139.pdf)**
> An evaluation setting in which models are prompted to answer questions without any prior examples, testing their intrinsic knowledge and generalization ability.

**[Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf) (as "Zero-Shot")**
> A prompting method where the model generates responses directly from a query without additional examples or structured guidance.

## Relationships

### Zero-shot evaluation →
- **Emotion analysis** (behaviors tasks) — *measured_by*
  - [Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf)

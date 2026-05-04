# Reasoning efficiency
**Type:** Construct  
**Referenced in:** 14 papers  

## State of the Field

Across the provided literature, reasoning efficiency is most commonly conceptualized as a model's ability to solve a problem using a minimal number of steps. This is often described in terms of minimizing 'reasoning steps or tool calls' to avoid 'unnecessary branch explorations' (Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees) or as a reflection of the model's capacity to 'quickly narrow down the candidate set' (Meta-rater: A Multi-dimensional Data Selection Method for Pre-training Language Models). A related but distinct framing, present in other work, defines reasoning efficiency in terms of computational cost. In this view, the construct is operationalized by measuring 'inference overhead, latency, or response length' (OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models) and is seen as the 'rational use of computational resources' (Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models). One paper extends this concept to include the appropriateness of the reasoning complexity relative to the problem's difficulty, suggesting that efficiency involves balancing performance against computational cost. Regardless of the specific metric, the underlying goal is consistently framed as achieving a correct outcome efficiently, with some papers noting the objective is to do so 'without sacrificing or even improving performance' (OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models).

## Sources

**[Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf)**
> The model's ability to solve a problem using a minimal number of reasoning steps or tool calls, avoiding unnecessary exploration.

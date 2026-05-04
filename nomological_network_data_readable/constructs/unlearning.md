# Unlearning
**Type:** Construct  
**Referenced in:** 12 papers  
**Also known as:** Forget efficacy, Removal, Knowledge removal, Knowledge unlearning  

## State of the Field

Across the surveyed literature, unlearning is most commonly defined as the process of removing specific information or knowledge from a model's weights so it can no longer perform related tasks. The primary goal is to "eliminate the influence of a specified target dataset" (Adaptive Localization of Knowledge Negation for Continual LLM Unlearning), preventing the model from reproducing or accurately responding to the targeted content. While this process-oriented view is prevalent, other work frames the concept with more specific terms like "Forget efficacy," "Removal," or "Knowledge removal," which describe it as a measurable degree of success, a latent property, or an observable performance reduction, respectively. To operationalize this construct, researchers measure the "observable reduction in the model's ability to recall or reproduce information" (GRU: Mitigating the Trade-off between Unlearning and Retention for LLMs), often demonstrated through decreased accuracy or likelihood on a "forget set." One paper also indicates that "LLM-as-a-judge" is used as a measurement instrument for unlearning. However, a dissenting view is present in the data, with one study suggesting that unlearning may not fully remove information, which can remain in "ways that are easy to recover" (On Evaluating the Durability of Safeguards for Open-Weight LLMs).

## Sources

**[A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf) (as "Forget efficacy")**
> The degree to which an unlearned model successfully removes specified information and does not reveal it in its outputs.

**[On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)**
> The process of removing specific information or knowledge from a model's weights, such that the model can no longer perform tasks related to that information.

**[Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a91841d2bcc0b13a3d0d5d60c9f0581-Paper-Conference.pdf) (as "Removal")**
> The latent property of an unlearned model having successfully deteriorated or erased the knowledge associated with a targeted unlearning dataset.

**[GRU: Mitigating the Trade-off between Unlearning and Retention for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25de/wang25de.pdf) (as "Knowledge removal")**
> The observable reduction in the model's ability to recall or reproduce information from a targeted dataset, demonstrated through decreased accuracy or likelihood on specific content.

**[Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wuerkaixi25a/wuerkaixi25a.pdf) (as "Knowledge unlearning")**
> Removing the influence of specified target data so the model cannot reproduce or accurately respond to it.

## Relationships

### Unlearning →
- **WMDP** (measurements) — *measured_by*
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **MUSE** (measurements) — *measured_by*
  - [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.444.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [HS-STaR: Hierarchical Sampling for Self-Taught Reasoners via Difficulty Estimation and Budget Reallocation](https://aclanthology.org/2025.emnlp-main.283.pdf)

### Associated with
- **Memorization** (constructs)
  - [Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a91841d2bcc0b13a3d0d5d60c9f0581-Paper-Conference.pdf)
- **Retention** (constructs)
  - [GRU: Mitigating the Trade-off between Unlearning and Retention for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25de/wang25de.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.444.pdf)

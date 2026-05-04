# Machine unlearning
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Forgetting, Knowledge unlearning  

## State of the Field

Across the provided literature, machine unlearning is predominantly defined as the latent ability of a model to selectively remove the influence of specific training data, making it behave as if those data points had never been observed. A recurring emphasis is on the dual nature of this process: the goal is not just to "forget" targeted information, such as private knowledge or memorized content, but to do so without degrading overall model utility or suffering from "catastrophic forgetting." Several papers frame this as a balance, where unlearning should be "precise, affecting only the Forget set without disturbing the Retain set" ("BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment"). To operationalize this construct, researchers use several measurement instruments; the provided data shows that machine unlearning is evaluated using benchmarks such as WMDP, TOFU, and MUSE, as well as through Membership inference attacks. The concept is studied alongside related constructs like Memorization, Faithfulness, and Adversarial robustness. One paper also posits a directional relationship, suggesting that machine unlearning causes Safety.

## Sources

**[Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf)**
> The latent ability of a model to remove the influence of selected training data so that those examples no longer shape its outputs as if they had never been observed.

**[Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf) (as "Forgetting")**
> The latent ability of a model to reduce its reliance on or association with specific training data, effectively treating those examples as if they were never observed.

**[KMMLU: Measuring Massive Multitask Language Understanding inKorean](https://aclanthology.org/2025.naacl-long.207.pdf) (as "Unlearning efficacy")**
> The degree to which a model removes targeted private knowledge about specified individuals from its parameters or outputs.

**[BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.444.pdf) (as "Unlearning")**
> The latent ability of a model to selectively forget specific knowledge or memorized content without degrading overall language performance or suffering catastrophic forgetting.

**[Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning](https://aclanthology.org/2025.emnlp-main.1109.pdf) (as "Knowledge unlearning")**
> The latent ability of a language model to remove targeted information while retaining unrelated knowledge after post-training.

## Relationships

### Machine unlearning →
- **TOFU** (measurements) — *measured_by*
  - [Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wuerkaixi25a/wuerkaixi25a.pdf)

### Associated with
- **Knowledge forgetting** (constructs)
  - [Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf)
- **Knowledge retention** (constructs)
  - [Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1348.pdf)
- **Interpretability and explainability** (constructs)
  - [Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1348.pdf)
- **Adversarial robustness** (constructs)
  - [Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1348.pdf)

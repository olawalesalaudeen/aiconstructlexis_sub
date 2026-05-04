# Jailbreak resistance
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Safety model evasion  

## State of the Field

Across the surveyed literature, jailbreak resistance is most commonly defined as the observable behavior of a model refusing to comply with prompts designed to bypass its safety filters and elicit harmful or prohibited content. A less frequent framing, termed "safety model evasion," characterizes the phenomenon as an outcome where a malicious prompt is misclassified by a dedicated, external safety model. To operationalize and assess this behavior, the field uses specific measurement instruments; for instance, jailbreak resistance is reported to be measured by LlamaGuard. The concept is frequently studied in relation to model training, with one paper noting that "fine-tuning significantly reduces the resistance of LLMs to jailbreaking" ("TAIA: Large Language Models are Out-of-Distribution Data Learners"). Conversely, other work discusses conducting "safety training on LLMs" to enhance this resistance. The term "jailbreak robustness" is also used to describe this behavior. One study notes that techniques like "adversarial tokenization" can increase the probability of bypassing safety layers, representing a failure of this resistance.

## Sources

**[TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)**
> The observable behavior of refusing to comply with prompts designed to bypass safety filters and elicit harmful or prohibited content.

**[Using Shapley interactions to understand how models use structure](https://aclanthology.org/2025.acl-long.1012.pdf) (as "Safety model evasion")**
> The observable outcome where a malicious prompt is misclassified as safe by a dedicated safety model, thereby bypassing an external layer of defense.

## Relationships

### Jailbreak resistance →
- **AdvBench** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **GCG attack** (measurements) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **PAIR** (measurements) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **AutoDAN** (measurements) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **LlamaGuard** (measurements) — *measured_by*
  - [Using Shapley interactions to understand how models use structure](https://aclanthology.org/2025.acl-long.1012.pdf)

### Associated with
- **Safety** (constructs)
  - [Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation andGaussian-Decayed Contrastive Learning](https://aclanthology.org/2025.acl-long.245.pdf)

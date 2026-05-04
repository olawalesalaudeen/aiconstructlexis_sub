# Multilingual reasoning
**Type:** Construct  
**Referenced in:** 9 papers  
**Also known as:** Multilingual Knowledge and Reasoning  

## State of the Field

The prevailing definition of multilingual reasoning across the provided literature is a model's ability to perform reasoning tasks effectively when presented with queries in multiple, non-English languages. A less frequent definition frames it more broadly as a latent ability to process and reason across both multiple languages and cultural contexts. This construct is primarily operationalized and measured through performance on specific benchmarks. The most commonly cited instrument for its assessment is MGSM, a benchmark of multilingual math word problems, with other papers also using MMMLU and MMLU for evaluation. The literature describes multilingual reasoning as a "significant challenge" for large language models, with research aiming to reduce performance differences among languages. As one study notes, LLMs have demonstrated "strong multilingual reasoning capabilities, even for low-resource languages" on the MGSM benchmark (Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models). Some approaches mentioned to facilitate this capability include translating test questions into English or using code as a "language-agnostic bridge".

## Sources

**[SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures](https://proceedings.neurips.cc/paper_files/paper/2024/file/e41efb03e20ca3c231940a3c6917ef6f-Paper-Conference.pdf) (as "Multilingual Knowledge and Reasoning")**
> The latent ability to process and reason across multiple languages and cultural contexts.

**[MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)**
> The ability of a model to perform reasoning tasks effectively when presented with queries in multiple, non-English languages.

## Relationships

### Multilingual reasoning →
- **MGSM** (measurements) — *measured_by*
  > “We conduct assessments on six benchmarks covering reasoning, understanding, and generation tasks that encapsulate various abilities of LLMs: MGSM”
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **X-CSQA** (measurements) — *measured_by*
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **Cross-lingual semantic alignment** (constructs) — *causes*
  - [Mufu:  Multilingual Fused Learning for Low-Resource Translation with LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/b44ae90136013a8d0e2d24f6015b6097-Paper-Conference.pdf)
- **MMMLU** (measurements) — *measured_by*
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-TurnLLMJailbreaks](https://aclanthology.org/2025.emnlp-main.1236.pdf)
- **MMLU** (measurements) — *measured_by*
  > Beyond English textual reasoning, we include two additional evaluation tracks: a multilingual experiment using MMLU and its professionally translated variant MMMLU (Hendrycks et al., 2021)...
  - [NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-TurnLLMJailbreaks](https://aclanthology.org/2025.emnlp-main.1236.pdf)

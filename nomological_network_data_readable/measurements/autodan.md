# AutoDAN
**Type:** Measurement  
**Referenced in:** 17 papers  

## State of the Field

AutoDAN is predominantly characterized in the provided literature as an automated attack method used to generate adversarial prompts. Its primary application is to measure the `Adversarial robustness` of large language models by attempting to bypass their safety alignments, a behavior referred to as `Jailbreaking`. The most common description of its underlying mechanism is a genetic algorithm, which one paper specifies as a "hierarchical genetic algorithm." However, there is some variation, with a smaller set of papers describing it as a "gradient-based" method or one that uses general "optimization techniques." The prompts it generates are described as both "high-perplexity" and "human-readable." Across the data, it is consistently classified as a "white-box" attack and is frequently studied alongside other methods like GCG and PAIR. A single source presents a distinct framing, describing AutoDAN as a "public dataset used for evaluating jailbreak detection," a less common usage in this collection of papers.

## Sources

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)**
> A genetic-algorithm jailbreak procedure that generates adversarial prompts intended to bypass LLM safety alignment.

## Relationships

### AutoDAN →
- **Jailbreaking** (behaviors tasks) — *causes*
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)

### → AutoDAN
- **Adversarial robustness** (constructs) — *measured_by*
  > Table 1: General model capability metrics and adversarial robustness (measured as ASR) of three LLMs trained using various safety fine-tuning methods. ... GCG ... PAIR ... AutoDAN ... HumanJailbreaks
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Jailbreak resistance** (behaviors tasks) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)

### Associated with
- **CSRT** (measurements)
  > We compare the CSRT to three non-multilingual red-teaming baselines (i.e., GCG (Zou et al., 2023), AutoDAN (Liu et al., 2024), and PAIR (Chao et al., 2025)). (Section 4.3)
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)

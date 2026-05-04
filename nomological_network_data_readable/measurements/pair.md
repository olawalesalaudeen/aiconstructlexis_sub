# PAIR
**Type:** Measurement  
**Referenced in:** 21 papers  

## State of the Field

PAIR, an acronym for Prompt Automatic Iterative Refinement, is consistently described across the provided literature as a black-box jailbreak attack procedure. The most common description of its mechanism involves using an attacker LLM to automatically and iteratively generate and refine prompts to make a target model produce harmful content. A few papers add further detail to this process, with one describing it as a "multi-turn conversation approach" and another noting it can frame harmful requests within "imaginary scenarios." A less frequent characterization describes it as a "population-based adversarial attack method that uses evolutionary algorithms." Across the surveyed work, PAIR is used as a measurement instrument to evaluate LLM safety and robustness. Specifically, papers use it to measure the constructs of `Jailbreaking` and `Harmlessness`. Researchers operationalize this by using PAIR to generate adversarial prompts and assess a model's vulnerability or the effectiveness of a defense mechanism. The method is frequently studied and compared alongside other attacks such as GCG, AutoDAN, and GPTFuzzer.

## Sources

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)**
> Prompt Automatic Iterative Refinement, a black-box jailbreak procedure in which an attacker LLM iteratively refines prompts until the target model is jailbroken.

## Relationships

### → PAIR
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Jailbreak resistance** (behaviors tasks) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)

### Associated with
- **Jailbreaking** (behaviors tasks)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **CSRT** (measurements)
  > We compare the CSRT to three non-multilingual red-teaming baselines (i.e., GCG (Zou et al., 2023), AutoDAN (Liu et al., 2024), and PAIR (Chao et al., 2025)). (Section 4.3)
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)

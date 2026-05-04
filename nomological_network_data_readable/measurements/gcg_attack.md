# GCG attack
**Type:** Measurement  
**Referenced in:** 36 papers  
**Also known as:** GCG, Greedy Coordinate Gradients (GCG), Greedy Coordinate Gradient Descent, nanoGCG, GCG Attack  

## State of the Field

The GCG attack is predominantly characterized in the provided literature as a white-box measurement procedure used to evaluate the safety and robustness of large language models. It operates as a gradient-based optimization method, often specified as "Greedy Coordinate Gradient" or "greedy projected coordinate descent," which requires access to the target model's gradients to function. The most common operationalization involves automatically generating an "adversarial suffix"—an often "unreadable" string of tokens, as one paper notes—that is appended to a harmful query to induce a jailbreak. While most sources describe generating suffixes, a few mention generating "attack strings" to be prepended or refer to GCG as a "dataset of jailbreak prompts." Across the surveyed work, the GCG attack is consistently used to measure constructs such as `Adversarial robustness`, `Jailbreaking`, `Safety`, and `Harmlessness`. Its primary function is to test a model's ability to resist attempts to "bypass model safety filters" and elicit "unsafe responses." One study adapts the algorithm beyond general safety to generate specific attacks on rule-based inference, including "rule suppression" and "state coercion." A lightweight version of the method, "nanoGCG," is also mentioned as a jailbreak evaluation procedure.

## Sources

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf) (as "GCG")**
> Greedy Coordinate Gradient, a white-box jailbreak attack procedure that searches for adversarial suffixes to elicit unsafe responses.

**[Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e2dd37e10bb18ed9d6d488f63094631-Paper-Conference.pdf) (as "Greedy Coordinate Gradients (GCG)")**
> An automated jailbreak algorithm that uses a greedy projected coordinate descent method to find an adversarial suffix of tokens that guides a model towards generating a specific, often undesirable, target output.

**[CROW: Eliminating Backdoors from Large Language Models via Internal Consistency Regularization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/min25b/min25b.pdf) (as "nanoGCG")**
> nanoGCG is a Greedy Coordinate Gradient method used here as a jailbreak evaluation procedure to generate adversarial prompts.

**[TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf) (as "Greedy Coordinate Gradient Descent")**
> Greedy Coordinate Gradient Descent (GCG), a white-box adversarial jailbreak procedure that generates attack strings prepended to harmful prompts.

**[Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf) (as "GCG Attack")**
> A specific implementation of an adversarial suffix attack from Zou et al. (2023b), used to evaluate model robustness.

**[SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)**
> An adversarial attack procedure generating universal suffixes to bypass model safety filters and test jailbreak resistance.

## Relationships

### → GCG attack
- **Adversarial robustness** (constructs) — *measured_by*
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Jailbreak resistance** (behaviors tasks) — *measured_by*
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Harmful content detection** (behaviors tasks) — *measured_by*
  - [Explaining the role of Intrinsic Dimensionality in Adversarial Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altinisik25a/altinisik25a.pdf)

### Associated with
- **CSRT** (measurements)
  - [MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark](https://aclanthology.org/2025.acl-long.657.pdf)

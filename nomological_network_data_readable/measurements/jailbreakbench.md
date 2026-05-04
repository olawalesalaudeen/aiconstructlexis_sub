# JailbreakBench
**Type:** Measurement  
**Referenced in:** 18 papers  
**Also known as:** Jailbreakbench  

## State of the Field

Across the provided literature, JailbreakBench is consistently defined as a standardized benchmark used to evaluate large language models. Its primary application is to measure a model's `Safety` and `Adversarial robustness` against jailbreak attacks, with papers also using it to assess `Harmlessness` and `Refusal behavior`. The benchmark is composed of harmful queries or instructions designed to test a model's resistance to generating disallowed content, and is listed in one paper among other "commonly used harmful query datasets" ("On the Role of Attention Heads in Large Language Model Safety"). In practice, researchers report using subsets of its data, such as sampling 100 harmful prompts for evaluation. A specific feature highlighted by one study is its evaluation protocol, which "recommends using LLM as a judge" to automatically assess whether a model produces a disallowed response ("FineReason: Evaluating and ImprovingLLMs’ Deliberate Reasoning through Reflective Puzzle Solving"). One paper also distinguishes between "template" and "direct" versions of the benchmark, though without further detail. The overall goal is to test "jailbreak resistance and safety degradation," particularly in response to what one paper calls "adversarial prompt injection."

## Sources

**[Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)**
> A standardized benchmark designed to evaluate a large language model's safety and robustness against a variety of jailbreak attacks.

**[On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf) (as "Jailbreakbench")**
> A harmful-query benchmark used to test jailbreak resistance and safety degradation after head ablation.

## Relationships

### → JailbreakBench
- **Adversarial robustness** (constructs) — *measured_by*
  > “We additionally evaluate on Adaptive Attack (Andriushchenko et al., 2024), a state-of-the-art adversarial attack method, on JailBreakBench (Chao et al., 2024).”
  - [Robust Prompt Optimization for Defending Language Models Against Jailbreaking Attacks](https://proceedings.neurips.cc/paper_files/paper/2024/file/46ed503889ab232c21c1162340ee17b2-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
- **Refusal behavior** (behaviors tasks) — *measured_by*
  > We evaluate the jailbreak Attack Success Rate (ASR) on JAILBREAKBENCH (Chao et al., 2024) using the STRONGREJECT fine–tuned judge (Souly et al., 2024).
  - [The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wollschlager25a/wollschlager25a.pdf)

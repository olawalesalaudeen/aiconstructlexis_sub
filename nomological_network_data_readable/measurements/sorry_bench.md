# SORRY-Bench
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** SORRY-bench, Sorry-Bench, SorryBench  

## State of the Field

Across the provided literature, SORRY-Bench is consistently described as a benchmark dataset composed of unsafe or harmful prompts. Its most common application is to evaluate a large language model's safety-related behaviors, specifically its ability to refuse or reject harmful instructions. Papers use it to operationalize and measure constructs such as `Safety`, `Refusal to answer`, and `Safety refusal`. A smaller body of work also positions it as a tool for evaluating `Adversarial attacks` or, more specifically, as a "jailbreak evaluation benchmark." Some sources specify that the benchmark contains 450 harmful instructions across 45 categories. Beyond evaluation, at least one paper notes its use as a source of unsafe prompts for training models, for instance, to "create a preference dataset" for safety alignment. The benchmark is used to quantify model performance through metrics like refusal rates, as one study observes a model's rate dropping "from 74.4% to 33.4% over the SORRY-Bench dataset" ("Unintentional Unalignment: Likelihood Displacement in Direct Preference Optimization").

## Sources

**[Unintentional Unalignment: Likelihood Displacement in Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)**
> A dataset of unsafe prompts used to evaluate and train models for safety alignment and refusal capabilities.

**[On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf) (as "SORRY-bench")**
> A benchmark for evaluating harmfulness in the HarmfulQA context using harmful instructions and model compliance.

**[Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf) (as "Sorry-Bench")**
> A benchmark dataset containing harmful prompts across 45 categories, used to evaluate a model's refusal capabilities for unsafe content.

**[OR-Bench: An Over-Refusal Benchmark for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cui25a/cui25a.pdf) (as "SorryBench")**
> A benchmark dataset used to assess an LLM's ability to reject questions with harmful intent.

## Relationships

### → SORRY-Bench
- **Safety** (constructs) — *measured_by*
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *measured_by*
  - [Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf)
- **Safety refusal** (constructs) — *measured_by*
  > “we address them with SORRY-Bench, our proposed benchmark” and “we evaluate over 50 proprietary and open-weight LLMs on SORRY-Bench, analyzing their distinctive safety refusal behaviors.”
  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf)
- **Adversarial attacks** (behaviors tasks) — *measured_by*
  > "We also consider two additional harmfulness evaluation datasets: HEx-PHI (Qi et al., 2023) and SORRY-bench (Xie et al., 2024)."
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)

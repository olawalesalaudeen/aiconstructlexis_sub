# SelfCheckGPT
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Self-CKGPT  

## State of the Field

Across the provided literature, SelfCheckGPT is predominantly characterized as a suite of methods for hallucination detection. Its operational principle is consistency-based; it analyzes multiple stochastically sampled responses from a model to assess the veracity of a given response, with one paper specifying this involves checking for "contradictions in its own generated text" (Self-Taught Agentic Long Context Understanding). A recurring feature is its application in "zero-resource" and "black-box or gray-box" settings. In practice, papers use SelfCheckGPT to measure the construct of Hallucination and, more broadly, for general Evaluation. Several sources also position it as a "baseline method" for performance comparison in fact-checking or hallucination detection tasks. While the core mechanism is consistently described, the specific goal is variously framed as assessing "self-consistency," "veracity," or performing "fact-checking." A single paper refers to it by the variant name "Self-CKGPT" while describing it similarly as a consistency-based method.

## Sources

**[LLM-Check: Investigating Detection of Hallucinations in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3c1e1fdf305195cd620c118aaa9717ad-Paper-Conference.pdf)**
> A suite of hallucination detection methods that analyzes multiple stochastically sampled responses from a model to assess the veracity of a given response, often in a black-box or gray-box setting.

**[Steer LLM Latents for Hallucination Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25a/park25a.pdf) (as "Self-CKGPT")**
> A consistency-based baseline method for hallucination detection that assesses the consistency of a model's own generated responses.

## Relationships

### → SelfCheckGPT
- **Evaluation** (behaviors tasks) — *measured_by*
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)

### Associated with
- **Hallucination detection** (behaviors tasks)
  - [ToW: Thoughts of Words Improve Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.158.pdf)

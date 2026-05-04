# BOLD
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, BOLD is consistently described as a benchmark dataset used to evaluate language models. Its primary application is to assess fairness, toxicity, and various forms of bias, with papers using it to measure constructs such as `Fairness`, `Societal bias`, `Social bias`, `Stereotyping`, and `Harmful content generation`. The analysis of gender bias is a recurring application, as noted in both its definition and in evidence showing its use "to analyze LM gender bias." Operationally, the benchmark is described as employing "web-based sentence prefixes to detect potential biases." In practice, BOLD is used in evaluations alongside other benchmarks like RealToxicityPrompts and AttaQ, and is also applied to test the consistency of model detoxification methods.

## Sources

**[Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf)**
> A benchmark dataset used to evaluate fairness and toxicity in language models, particularly for analyzing biases like gender bias.

## Relationships

### → BOLD
- **Fairness** (constructs) — *measured_by*
  - [DCR: Quantifying Data Contamination inLLMs Evaluation](https://aclanthology.org/2025.emnlp-main.1174.pdf)
- **Social bias** (constructs) — *measured_by*
  > Additionally, we further conducted an experiment where we use the BOLD dataset to analyze LM gender bias, results are shown in appendix Table 13. (Section 4.4)
  - [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf)
- **Stereotyping** (constructs) — *measured_by*
  - [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf)
- **Societal bias** (constructs) — *measured_by*
  - [Friend or Foe? A Computational Investigation of Semantic FalseFriends acrossRomance Languages](https://aclanthology.org/2025.emnlp-main.774.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  - [Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://aclanthology.org/2025.emnlp-main.804.pdf)

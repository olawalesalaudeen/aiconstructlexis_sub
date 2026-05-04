# WinoBias
**Type:** Measurement  
**Referenced in:** 14 papers  
**Also known as:** Winobias  

## State of the Field

Across the provided literature, WinoBias is consistently defined as a benchmark for measuring gender bias in language models, specifically through the task of coreference resolution. The instrument operationalizes this measurement using Winograd-style examples that pair gender-neutral professions with gendered pronouns, evaluating a model's ability to resolve them in both pro- and anti-stereotypical contexts. As one paper details, the task is to "identify the coreference link between the pronouns and the correct professional" ("Debiasing Algorithm through Model Adaptation"). Papers use WinoBias to assess several related constructs, most frequently `Social bias` and `Fairness`, with a specific focus on gender-occupation associations. It is described as a "widely studied" and "popular" benchmark for this purpose ("Are Models Biased on Text without Gender-related Language?", "ELABORATION..."). While the dominant framing is for measuring gender bias, a smaller number of papers characterize it as an "out-of-distribution bias benchmark" ("Enhancing Efficiency and Exploration in Reinforcement Learning forLLMs"). One source also notes that such conventional benchmarks may "pose challenges to reliably assessing modern LLMs" ("Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs").

## Sources

**[Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)**
> Coreference resolution benchmark designed to measure gender bias by evaluating model performance on pro- and anti-stereotypical Winograd-style examples involving professions and pronouns.

**[Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf) (as "Winobias")**
> A coreference resolution benchmark designed to evaluate gender-occupation bias in language models by testing pronoun resolution in gendered sentence pairs.

## Relationships

### → WinoBias
- **Social bias** (constructs) — *measured_by*
  > As typical examples, WinoBias (Zhao et al., 2018) measures the gender bias in language models by identifying the dependency between output words and social groups, where such bias is further mitigated with word-embedding debiasing techniques (Bolukbasi et al., 2016).
  - [Prompting Fairness: Integrating Causality to Debias Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9f26a2d143a227376dff99a279f93f99-Paper-Conference.pdf)
- **Coreference resolution** (behaviors tasks) — *measured_by*
  > WinoBias Zhao et al. (2018) present the dataset containing a WinoGrad scheme (Levesque et al., 2011) examples. ... The task is to identify the coreference link between the pronouns and the correct professional. (Section 2.3)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Fairness** (constructs) — *measured_by*
  > WinoBias Zhao et al. (2018) is an intra-sentence coreference resolution task designed to assess a system’s ability to correctly associate a gendered pronoun with an occupation in both pro-stereotypical and anti-stereotypical contexts. (Section 4.1.3)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Stereotyping** (constructs) — *measured_by*
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)

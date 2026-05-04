# Winogender
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** WinoGender  

## State of the Field

Across the provided literature, Winogender is most commonly described as a diagnostic dataset or benchmark for evaluating gender bias, specifically within the task of coreference resolution. Its primary function is to test whether models resolve pronouns in a gender-stereotyped manner, particularly in the context of occupations. One paper specifies its operationalization as "computing the Pearson correlation coefficient ρ between the probabilities assigned by the model to female-gendered pronouns... and the gender statistics of occupations" ("SHARE: AnSLM-based Hierarchical ActionCorREction Assistant for Text-to-SQL"). The benchmark is used to measure several constructs, including `Stereotyping`, `Social bias`, `Fairness`, and `Human preference alignment`. While this is the prevailing usage, a smaller line of work describes repurposing the benchmark for "non-stereotypical evaluation" by filtering sentences with strong gender co-occurrences. A critical perspective is also present, with one paper noting that WinoGrad Schema-based datasets like Winogender "are no longer adequate to evaluate recent LLMs" ("Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs").

## Sources

**[Are Models Biased on Text without Gender-related Language?](https://proceedings.iclr.cc/paper_files/paper/2024/file/37771cc0be272368102a37f202bb88d8-Paper-Conference.pdf)**
> Winogender (WG), a coreference-resolution gender-occupation bias benchmark repurposed here by filtering out sentences with strong gender co-occurrences.

**[Beyond Imitation: Leveraging Fine-grained Quality Signals for Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5c8236f62e33b5224634069e64cb271a-Paper-Conference.pdf) (as "WinoGender")**
> Diagnostic dataset evaluating gender bias in coreference resolution by testing whether models resolve pronouns in a gender-stereotyped manner.

## Relationships

### → Winogender
- **Stereotyping** (constructs) — *measured_by*
  - [SHARE: AnSLM-based Hierarchical ActionCorREction Assistant for Text-to-SQL](https://aclanthology.org/2025.acl-long.553.pdf)
- **Fairness** (constructs) — *measured_by*
  - [Enhancing Efficiency and Exploration in Reinforcement Learning forLLMs](https://aclanthology.org/2025.emnlp-main.76.pdf)
- **Social bias** (constructs) — *measured_by*
  - [Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cp/wang25cp.pdf)

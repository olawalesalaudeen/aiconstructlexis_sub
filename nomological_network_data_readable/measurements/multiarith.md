# MultiArith
**Type:** Measurement  
**Referenced in:** 32 papers  

## State of the Field

Across the provided literature, MultiArith is consistently used as a dataset to evaluate the mathematical and quantitative reasoning abilities of language models. It is uniformly defined as a collection of arithmetic word problems, with a prevailing emphasis in the definitions that these problems require multiple steps or operations to solve. Some sources add further detail, characterizing the problems as being at a 'grade-school' level or identifying MultiArith as a subset of the MAWPS dataset. In practice, it is frequently used for evaluation alongside other mathematical reasoning benchmarks, most commonly GSM8K, SVAMP, and AQuA. Beyond general performance measurement, a smaller set of studies employs MultiArith in more specific contexts, such as assessing the transferability of prompts optimized on other datasets. For instance, one paper notes its use to "evaluate the instructions optimized for GSM8K" on other datasets ("Large Language Models as Optimizers"). Other specific applications include using it to create evaluation scenarios with "distribution shift" or as an out-of-distribution benchmark to test model generalization.

## Sources

**[DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)**
> A dataset containing arithmetic word problems used to evaluate quantitative reasoning.

## Relationships

### → MultiArith
- **Mathematical reasoning** (constructs) — *measured_by*
  > We evaluate DTV on three quantitative reasoning datasets: GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021) and MultiArith (Roy & Roth, 2016).
  - [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a79ecda13603817de4cdfc68b417e89-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [MAC-Tuning:LLMMulti-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.36.pdf)

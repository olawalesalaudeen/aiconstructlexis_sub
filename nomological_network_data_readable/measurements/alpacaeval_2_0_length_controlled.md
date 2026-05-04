# AlpacaEval 2.0 Length Controlled
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Length-controlled AlpacaEval 2.0, Length-Controlled AlpacaEval  

## State of the Field

Across the provided sources, AlpacaEval 2.0 Length Controlled is consistently framed as an evaluation benchmark for chat models, with its defining feature being the control for response length. The instrument is used to measure the constructs of `Instruction following` and `Helpfulness`. The papers uniformly state that this length control is implemented to ensure fair comparisons, reduce stylistic bias, and mitigate what one source calls 'verbosity bias' ('Investigating Non-Transitivity in LLM-as-a-Judge'). The benchmark is described as a human preference-based evaluation that uses an LLM-as-a-judge. One paper specifies that it achieves length control by applying a 'generalized linear model... to derive length-controlled preferences' ('Investigating Non-Transitivity in LLM-as-a-Judge'). In addition to measuring specific constructs, it is also used for comparing model alignment and separability. Researchers are shown to use the benchmark to evaluate different model variants and report metrics such as win rates.

## Sources

**[Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf) (as "Length-controlled AlpacaEval 2.0")**
> A benchmark for evaluating chat model instruction-following capabilities where response length is controlled to provide a fair comparison.

**[From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf)**
> Human preference-based evaluation benchmark that uses LLM-as-a-judge with length control to reduce stylistic bias, used for comparing alignment and separability.

**[Investigating Non-Transitivity in LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25w/xu25w.pdf) (as "Length-Controlled AlpacaEval")**
> A modified version of the AlpacaEval framework that applies a generalized linear model to control for the influence of response length on evaluation scores.

## Relationships

### → AlpacaEval 2.0 Length Controlled
- **Helpfulness** (constructs) — *measured_by*
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  > We evaluate all variants on Length-controlled (LC) AlpacaEval 2.0 (Li et al., 2023) and MixEval (Ni et al., 2024). LC AlpacaEval 2.0 is a well-recognized benchmark for chat model evaluation.
  - [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf)

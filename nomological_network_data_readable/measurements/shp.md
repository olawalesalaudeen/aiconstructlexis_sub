# SHP
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the surveyed literature, SHP refers to the Stanford Human Preferences dataset, a measurement instrument used for both model training and evaluation. The prevailing description characterizes it as a dataset of prompts paired with two responses annotated for human preference. However, the source of this data is described differently across papers; some identify it as StackExchange questions, while another describes it as comprising Reddit posts where preference is indicated by likes. The most common application of SHP is for evaluation, where it is used to assess model alignment across diverse tasks. Specifically, some work employs it as an out-of-distribution benchmark to measure the generalization of reward models. Beyond evaluation, SHP is also used as a training set to "fine-tune base and reward models" (ARGS: Alignment as Reward-Guided Search).

## Sources

**[ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf)**
> Stanford Human Preferences dataset, consisting of prompts paired with two responses annotated for preference, used to evaluate alignment across diverse tasks.

## Relationships

### → SHP
- **Out-of-distribution generalization** (constructs) — *measured_by*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)

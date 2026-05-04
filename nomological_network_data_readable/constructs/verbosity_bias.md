# Verbosity bias
**Type:** Construct  
**Referenced in:** 21 papers  
**Also known as:** Length Bias  

## State of the Field

Across the surveyed literature, 'Verbosity bias', often termed 'Length bias', is predominantly characterized as a tendency for large language models, reward models, or LLM-based evaluators to prefer longer responses irrespective of their actual quality. This is commonly defined as a 'disposition of a reward model to favor outputs based on their sequence length rather than their true quality,' and is described as a 'prevalent' issue. A few papers frame this as a 'latent tendency' for a model or reward signal to prefer longer responses over more succinct ones of equal content. The concept is frequently discussed as a limitation of automated evaluation, with one source listing it alongside position and self-enhancement biases as a known issue for 'LLM-as-a-Judge' systems. While direct measurement instruments for the bias are not detailed, related concepts are used in human annotation. For instance, 'Verbosity' is treated as a rating dimension on a Likert-5 scale, defined as the extent to which a response is 'wordy or contains more text than necessary.' Conversely, 'Conciseness' is defined as the ability to convey information with minimal length. A minority perspective suggests the phenomenon 'may actually be mainly an artifact of bias in naive evaluations.'

## Sources

**[Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf) (as "Length bias")**
> A disposition of a reward model to favor outputs based on their sequence length rather than their true quality.

**[Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf) (as "Length Bias")**
> A latent tendency for the model or reward signal to prefer longer responses over more succinct ones of equal content.

**[HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf) (as "Verbosity")**
> The extent to which a model's response is wordy or contains more text than necessary.

**[Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)**
> The tendency of an LLM-based evaluator to prefer longer, more verbose responses, irrespective of their actual quality.

**[Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf) (as "Conciseness")**
> The ability to convey information clearly and effectively using as few words as necessary.

## Relationships

### Associated with
- **AlpacaEval 2.0** (measurements)
  - [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf)

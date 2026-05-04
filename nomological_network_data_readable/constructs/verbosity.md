# Verbosity
**Type:** Construct  
**Referenced in:** 34 papers  
**Also known as:** Length Bias, Response length generation, Overgeneration, Verbose response generation, Verbose generation, Overly verbose generation  

## State of the Field

The most prevalent framing of verbosity in the provided literature is as a negative bias, commonly termed "length bias" or "verbosity bias." This is widely defined as a disposition for models, reward models, or LLM-based evaluators to favor longer responses irrespective of their actual quality. Multiple papers describe this as a "prevalent" issue where models exploit spurious correlations, with one study noting it is a "known issue of length exploitation" where models generate long responses when the same content could be provided more succinctly ("Bootstrapping Language Models with DPO Implicit Rewards"). This bias is also identified as a limitation of using LLMs as evaluators. A smaller line of work treats verbosity more neutrally as a controllable attribute of a model's output, sometimes considered desirable, and is often included as a dimension for annotation alongside helpfulness and correctness. The construct is operationalized and measured using several methods, most commonly through `Human evaluation` and specifically with instruments like `HelpSteer`, `HelpSteer2`, and `MT-Bench`. Verbosity is studied in the context of tasks like `Question answering` and `Text summarization`, is related to `Human preference alignment`, and is reported to correlate with `Helpfulness`.

## Sources

**[Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)**
> The tendency of a model to produce outputs of a certain length, which can be controlled as a desirable attribute.

**[Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf) (as "Length bias")**
> A disposition of a reward model to favor outputs based on their sequence length rather than their true quality.

**[Bootstrapping Language Models with DPO Implicit Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4de96b9169aa869cc102afe31055e8-Paper-Conference.pdf) (as "Length Bias")**
> A latent tendency for the model or reward signal to prefer longer responses over more succinct ones of equal content.

**[Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://proceedings.iclr.cc/paper_files/paper/2025/file/9adc8ada9183f4b9a007a02773fd8114-Paper-Conference.pdf) (as "Verbosity bias")**
> The tendency of an LLM-based evaluator to prefer longer, more verbose responses, irrespective of their actual quality.

**[Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf) (as "Conciseness")**
> The ability to convey information clearly and effectively using as few words as necessary.

**[slow-reconvergence phase](https://aclanthology.org/2025.emnlp-main.1676.pdf) (as "Response length generation")**
> The observable production of text outputs with measurable word counts, varying in length based on model, prompt, and decoding settings.

**[Large Language Models Do Multi-Label Classification Differently](https://aclanthology.org/2025.emnlp-main.127.pdf) (as "Overgeneration")**
> Producing excessively long or verbose outputs, often continuing until the maximum generation length is reached, leading to incoherence.

**[Improving Reasoning Capabilities in Small Models through Mixture-of-layers Distillation with Stepwise Attention on Key Information](https://aclanthology.org/2025.emnlp-main.251.pdf) (as "Verbose response generation")**
> The observable tendency of a model to produce outputs that are excessively long or wordy relative to the complexity of the task.

**[CalibratingLLMConfidence by Probing Perturbed Representation Stability](https://aclanthology.org/2025.emnlp-main.531.pdf) (as "Verbose generation")**
> The tendency of a model to produce outputs that are unnecessarily long or contain redundant information.

**[NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf) (as "Overly verbose generation")**
> Producing responses that are excessively long, often including redundant or irrelevant content, beyond what is necessary to answer the prompt.

## Relationships

### Verbosity →
- **HelpSteer** (measurements) — *measured_by*
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HelpSteer2** (measurements) — *measured_by*
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf)

### → Verbosity
- **Helpfulness** (constructs) — *correlates*
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
- **In-context learning** (constructs) — *causes*
  - [Padding Tone: A Mechanistic Analysis of Padding Tokens inT2IModels](https://aclanthology.org/2025.naacl-long.390.pdf)

### Associated with
- **Question answering** (behaviors tasks)
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [L3Ms — Lagrange Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/92d3d2a9801211ca3693ccb2faa1316f-Paper-Conference.pdf)
- **Text summarization** (behaviors tasks)
  - [L3Ms — Lagrange Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/92d3d2a9801211ca3693ccb2faa1316f-Paper-Conference.pdf)
- **Reward hacking** (behaviors tasks)
  - [RRM:  Robust Reward Model Training Mitigates Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf)

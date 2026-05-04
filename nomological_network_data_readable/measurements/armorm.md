# ArmoRM
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** ArmoRM-Llama3-8B-v0.1, ArmoRM-8B, ArmoRM-Llama3-8B  

## State of the Field

Across the provided literature, ArmoRM is predominantly characterized as a multi-dimension reward model that functions as an automated judge to evaluate the alignment of large language model (LLM) responses. Its prevailing application is to score or rank model outputs, which is frequently done to create preference pairs for alignment training or to act as a proxy evaluator. As a measurement instrument, ArmoRM is used to assess a range of constructs, including `Helpfulness`, `Harmlessness`, and `Humor understanding`. One study specifically leverages its `instruction-following` dimension, while another selects five attributes for analysis: "complexity, instruction following, honesty, helpfulness, and intelligence depth." A less frequent but noted use is for filtering synthetic preference data, where one paper states it "effectively mitigates erroneous responses" ("Self-Boosting Large Language Models with  Synthetic Preference Data"). The instrument appears in several specific versions, such as the publicly-available `ArmoRM-Llama3-8B`, and is described as a "state-of-the-art" model whose performance is associated with the `Reward-Bench` benchmark. Some work also uses it to assign "ground truth labels" to responses for evaluation purposes.

## Sources

**[Self-Boosting Large Language Models with  Synthetic Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4352e2c9d93582898a2a20e1f514e8f-Paper-Conference.pdf) (as "ArmoRM-Llama3-8B-v0.1")**
> ArmoRM-Llama3-8B-v0.1, a scoring model used for filtering synthetic preference data in the Llama3 setting.

**[Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf) (as "ArmoRM-8B")**
> An 8-billion parameter reward model used as an automated evaluator, specifically leveraging its instruction-following dimension to score model outputs.

**[PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)**
> A state-of-the-art multi-dimension reward model used as an automated judge to evaluate the alignment of LLM responses from various perspectives.

**[Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf) (as "ArmoRM-Llama3-8B")**
> A specific, publicly-available reward model used as an external judge to score model-generated responses and create preference pairs for baseline training.

## Relationships

### → ArmoRM
- **Instruction following** (constructs) — *measured_by*
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  > For the evaluation of 'harmless', 'helpful', and 'humor' dimensions... Additionally, we employ the ArmoRM (Wang et al., 2024b), a multi-dimension reward model... For these reward models, we report their scores assessing LLM responses from various perspectives.
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [Harnessing and Evaluating the Intrinsic Extrapolation Ability of Large Language Models for Vehicle Trajectory Prediction](https://aclanthology.org/2025.naacl-long.224.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Humor understanding** (constructs) — *measured_by*
  > For the evaluation of 'harmless', 'helpful', and 'humor' dimensions... Additionally, we employ the ArmoRM (Wang et al., 2024b), a multi-dimension reward model... For these reward models, we report their scores assessing LLM responses from various perspectives.
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Preference ranking** (behaviors tasks) — *measured_by*
  - [Weighted-Reward Preference Optimization for Implicit Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/a49ca20266ea2d0d2dc1e3bb49196998-Paper-Conference.pdf)

### Associated with
- **Reward-Bench** (measurements)
  > Additionally, we employ the ArmoRM (Wang et al., 2024b), a multi-dimension reward model known for its state-of-the-art performance on the Reward-Bench benchmark (Lambert et al., 2024).
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)

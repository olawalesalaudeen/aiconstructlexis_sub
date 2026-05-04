# Anthropic HHH
**Type:** Measurement  
**Referenced in:** 22 papers  
**Also known as:** HH-RLHF, Anthropic-HH  

## State of the Field

Anthropic HHH, also referred to as HH-RLHF and Anthropic-HH, is consistently described across the provided literature as a dataset of human-assistant dialogues containing human preference labels. The instrument's most prevalent application is to measure the constructs of `Helpfulness` and `Harmlessness`, assessing how well models align with human values on these dimensions. Papers operationalize this measurement using the dataset's "binary preference labels based on response helpfulness in human-assistant conversations" ("MMDEND: Dendrite-Inspired Multi-Branch Multi-Compartment Parallel Spiking Neuron for Sequence Modeling"), where annotators select the "better" response. Beyond evaluation, the dataset is also frequently used for training, particularly for reinforcement learning from human feedback (RLHF) and to train reward models. While its primary focus is on helpfulness and harmlessness, some work also uses it to assess `Human preference alignment`, `Dialogue generation`, and, less commonly, `Humor understanding` and `Safety`. One analysis of the dataset, which calls it a "popular choice in the field," noted potential data quality issues, finding that "over 40% of the answers in the sampled dataset is incorrect" ("Jailbreak Large Vision-Language Models Through Multi-Modal Linkage"). Overall, it is presented as an instrument for both training and evaluating models on their alignment with human preferences.

## Sources

**[Jailbreak Large Vision-Language Models Through Multi-Modal Linkage](https://aclanthology.org/2025.acl-long.75.pdf) (as "HH-RLHF")**
> A human preference dataset used for reinforcement learning from human feedback, analyzed in this study for annotation errors that may propagate instruction-following biases into models.

**[Retrieve to Explain: Evidence-driven Predictions for Explainable Drug Target Identification](https://aclanthology.org/2025.acl-long.168.pdf)**
> A dialogue dataset with human inputs and assistant responses from real conversations, used to evaluate helpfulness, honesty, and harmlessness.

**[MMDEND: Dendrite-Inspired Multi-Branch Multi-Compartment Parallel Spiking Neuron for Sequence Modeling](https://aclanthology.org/2025.acl-long.1333.pdf) (as "Anthropic-HH")**
> A human feedback dataset containing binary preference labels on helpfulness in human-assistant conversations, used to train and evaluate reward models in RLHF.

## Relationships

### → Anthropic HHH
- **Helpfulness** (constructs) — *measured_by*
  > For HH-RLHF, we assess our model on helpfulness and harmlessness using GPT-4-1106-preview as an initial evaluator (Zheng et al., 2024), with human annotators providing a final verification for precise results, following (Chen et al., 2023b) and (Dai et al., 2023).
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  - [SimPER: A Minimalist Approach to Preference  Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
- **Humor understanding** (constructs) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
- **Safety alignment** (constructs) — *measured_by*
  - [SimPER: A Minimalist Approach to Preference  Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)

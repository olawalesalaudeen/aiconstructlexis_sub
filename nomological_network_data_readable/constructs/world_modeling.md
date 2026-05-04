# World modeling
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** Causal world model, World model  

## State of the Field

Across the provided literature, world modeling is most commonly characterized as a latent ability or capacity for an agent to build an internal representation of an environment's mechanics. This internal model is described as a structured understanding of underlying rules or a state space, which is used to understand observations and predict outcomes. A more specific framing from one paper introduces the concept of a "causal world model," which focuses on the representation of cause-effect relationships among tokens. The construct is frequently discussed in the context of large language models, which are described as having opportunities for "sophisticated world modeling" due to their extensive knowledge and reasoning abilities. Research applications mentioned in the sources include investigating the "biological alignment" of an LLM's internal world model and developing procedures to test whether a foundation model has learned a postulated world model. While the provided data does not specify how this construct is measured, one paper notes that learning to predict sequences may uncover a world model.

## Sources

**[Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/6f479ea488e0908ac8b1b37b27fd134c-Paper-Conference.pdf)**
> The latent ability of an agent to build an internal representation of an environment's mechanics to understand observations and predict outcomes.

**[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf) (as "World model")**
> A latent, structured understanding of the underlying mechanisms, rules, or state space that generates the observed data.

**[A Causal World Model Underlying Next Token Prediction: Exploring GPT in a Controlled Environment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yehezkel-rohekar25a/yehezkel-rohekar25a.pdf) (as "Causal world model")**
> A latent structural representation of cause-effect relationships among tokens in a sequence, which the model uses to generate outputs consistent with domain rules, even in out-of-distribution settings.

## Relationships

### World modeling →
- **Robotic manipulation** (behaviors tasks) — *causes*
  - [PIVOT-R: Primitive-Driven Waypoint-Aware World Model for Robotic Manipulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6164b6e5352c139e9ddc1a98c09e4e4a-Paper-Conference.pdf)
- **Planning** (constructs) — *causes*
  - [OZSpeech: One-step Zero-shot Speech Synthesis with Learned-Prior-Conditioned Flow Matching](https://aclanthology.org/2025.acl-long.1044.pdf)

### Associated with
- **State tracking** (constructs)
  - [Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf)
- **Action prediction** (behaviors tasks)
  - [Mastering Board Games by External and Internal Planning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schultz25a/schultz25a.pdf)

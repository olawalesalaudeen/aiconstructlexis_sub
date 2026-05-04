# Anthropic HH (RLHF)
**Type:** Measurement  
**Referenced in:** 77 papers  
**Also known as:** Anthropic-RLHF-HH, Anthropic/HH-RLHF, HH-RLHF, HH-RLHF*, hh-rlhf, Anthropic HH, ANTHROPIC HH, Anthropic-HH, HH-rlhf, HH-RLHF-harmless, HH-RLHF-helpful, Anthropic HH dataset, Anthropic harmless data, HH, HH-Golden dataset, Anthropic Harmlessness dataset, Anthropic Helpfulness dataset, Anthropic Helpfulness and Harmlessness (HH), Helpful & Harmless, Anthropic Helpfulness-Harmlessness dataset, Helpful-Harmless dataset  

## State of the Field

Across the surveyed literature, Anthropic HH (RLHF) is a dataset used for training and evaluating language models on alignment with human preferences. The dataset is consistently described as containing human-AI conversations, often in a multi-turn dialogue format, where two model-generated responses to a prompt are compared and one is labeled as preferred by human annotators. The primary criteria for these preference judgments are consistently cited as helpfulness and harmlessness. Papers in this set use the dataset to measure these two constructs directly, as well as related concepts like `Human preference alignment` and `Safety alignment`. The data is also used to assess behaviors such as `Dialogue generation` and phenomena like `Reward overoptimization`. While the core dataset focuses on helpfulness and harmlessness, some studies utilize distinct subsets like `HH-RLHF-helpful` and `HH-RLHF-harmless` to isolate these criteria. A few papers also mention other variations, including a version that adds "honesty" as a criterion (`Anthropic HHH`) and a modified version with higher-quality preferred responses (`HH-Golden dataset`). One paper notes that while the data can be multi-turn, it is "common to first convert from multi-turn into a single-turn format" ("Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLHF").

## Sources

**[Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf) (as "hh-rlhf")**
> The helpfulness and harmlessness dataset from Anthropic (Bai et al., 2022a), containing human preference comparisons between model responses, used here to analyze what behaviors are incentivized.

**[Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf) (as "Anthropic/HH-RLHF")**
> Dataset of human-AI conversation pairs used to train and evaluate helpful and harmless behavior in language models, containing preference-labeled responses for alignment evaluation.

**[ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf) (as "HH-RLHF")**
> The Helpful and Harmless dataset from Anthropic, a benchmark for alignment that consists of prompts each with two responses, where one is preferred by human annotators based on helpfulness and harmlessness.

**[Tool-Augmented Reward Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/4eb7f0abf16d08e50ed42beb1e22e782-Paper-Conference.pdf) (as "HH-RLHF*")**
> A 150-instance subset of the HH-RLHF dataset used for out-of-domain evaluation to test the model's ability to generalize its preference scoring to unseen prompts.

**[Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf) (as "Anthropic-RLHF-HH")**
> A large-scale dataset of human feedback on AI assistant responses, containing preference data for both helpful and harmless conversations.

**[Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf) (as "Anthropic-HH")**
> A preference dataset for evaluating helpfulness and harmlessness, consisting of prompts with two model-generated continuations ranked by human labelers.

**[Regressing the Relative Future: Efficient Policy Optimization for Multi-turn RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/186094ef879dcbd5ef6879782916c309-Paper-Conference.pdf) (as "Anthropic HH")**
> The Anthropic Helpful and Harmless dataset, a collection of multi-turn dialogues used to train and evaluate models on their ability to be helpful while avoiding harmful responses.

**[SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf) (as "ANTHROPIC HH")**
> The Anthropic Helpful and Harmless dataset, which contains pairs of multi-turn dialogues designed to evaluate a model's ability to be both helpful and safe.

**[3D-Properties: Identifying Challenges in DPO and Charting a Path Forward](https://proceedings.iclr.cc/paper_files/paper/2025/file/c080f9fb3658511bc4f063c5794ef706-Paper-Conference.pdf) (as "HH-rlhf")**
> A preference dataset used for training and evaluation in the comparison between DPO and reward-model training.

**[Interpreting Language Reward Models via Contrastive Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/3538a22cd3ceb8f009cc62b9e535c29f-Paper-Conference.pdf) (as "HH-RLHF-helpful")**
> A binary human-preference dataset of helpfulness-oriented response comparisons used to test reward-model explanations.

**[Interpreting Language Reward Models via Contrastive Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/3538a22cd3ceb8f009cc62b9e535c29f-Paper-Conference.pdf) (as "HH-RLHF-harmless")**
> A binary human-preference dataset of harmlessness-oriented response comparisons used to test reward-model explanations.

**[Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf) (as "Anthropic HH dataset")**
> The test split of the Anthropic Helpful and Harmless (HH) dataset, used to evaluate model alignment by assessing responses in single-step human-assistant interactions.

**[Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf) (as "Anthropic HHH")**
> A dataset of human preference comparisons over helpful, harmless, and honest AI responses, used here as a source of harmful prompts and responses.

**[MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf) (as "Anthropic harmless data")**
> A dataset of human-AI conversations used as a source of prompts for evaluating alignment on conversational tasks.

**[Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf) (as "HH")**
> The Anthropic Helpful and Harmless dataset, a collection of human preference data comparing model responses to evaluate and align language models.

**[Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf) (as "HH-Golden dataset")**
> A preference dataset, modified from HH-RLHF, used to evaluate a model's alignment with a broad spectrum of human preferences.

**[InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf) (as "Anthropic Helpfulness dataset")**
> A dataset consisting of multi-turn dialogues between a human and a digital assistant, with human preference labels indicating which of two responses is more helpful.

**[InfAlign: Inference-aware language model alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balashankar25a/balashankar25a.pdf) (as "Anthropic Harmlessness dataset")**
> A dataset of multi-turn dialogues with human preference labels, designed to train and evaluate a model's ability to avoid generating harmful or unsafe content.

**[Preference learning made easy: Everything should be understood through win rate](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bm/zhang25bm.pdf) (as "Anthropic Helpfulness and Harmlessness (HH)")**
> A dataset of human preference comparisons between model responses, focused on the criteria of being helpful and harmless.

**[Right Now, Wrong Then: Non-Stationary Direct Preference Optimization under Preference Drift](https://raw.githubusercontent.com/mlresearch/v267/main/assets/son25a/son25a.pdf) (as "Helpful & Harmless")**
> A preference dataset used to construct non-stationary preference data for LLM fine-tuning experiments.

**[Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf) (as "Anthropic Helpfulness-Harmlessness dataset")**
> A dataset containing conversations where human labelers compare two model responses based on helpfulness and harmlessness criteria.

**[Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf) (as "Helpful-Harmless dataset")**
> A large-scale dataset of human preference labels used for training and evaluating models on helpfulness and harmlessness.

## Relationships

### Anthropic HH (RLHF) →
- **Helpfulness** (constructs) — *measured_by*
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)

### → Anthropic HH (RLHF)
- **Helpfulness** (constructs) — *measured_by*
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
- **Dialogue generation** (behaviors tasks) — *measured_by*
  - [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf)
- **Reward overoptimization** (constructs) — *measured_by*
  - [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf)
- **Safety alignment** (constructs) — *measured_by*
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **Memorization** (constructs) — *measured_by*
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)

### Associated with
- **Conversational response generation** (behaviors tasks)
  - [MAP: Multi-Human-Value Alignment Palette](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca549a1547bc8e8ca2df968aeaf57715-Paper-Conference.pdf)

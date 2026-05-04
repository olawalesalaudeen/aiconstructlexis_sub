# Dialogue generation
**Type:** Behavior  
**Referenced in:** 27 papers  
**Also known as:** Dialogue response generation  

## State of the Field

Across the provided literature, dialogue generation is most commonly defined as the behavior of generating responses within a multi-turn conversational setting. A less frequent definition expands this to include single-turn interactions and explicitly adds the goal of balancing helpfulness and harmlessness. Operationally, the task is described as an agent receiving a "snippet of conversation" and predicting the "next utterance," often in the context of an AI assistant or chatbot interacting with a human. The field measures this behavior using a wide array of benchmarks and datasets, including Anthropic HHH, MT-Bench, Anthropic HH (RLHF), Wizard-of-Wikipedia, Databricks Dolly-15k, UltraFeedback, and ConvAI2. Evaluation is also conducted using methods such as LLM-as-a-judge. The provided materials connect this behavior to the RLHF training pipeline and note that it is sometimes used as a task to evaluate the broader construct of generalization. A recurring concern mentioned in the context of this behavior is the presence of hallucinations in model outputs.

## Sources

**[Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf)**
> Generating responses in a multi-turn conversational setting.

**[An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf) (as "Dialogue response generation")**
> Producing conversational responses in multi-turn or single-turn dialogue settings that address user queries while balancing helpfulness and harmlessness.

## Relationships

### Dialogue generation →
- **Anthropic HHH** (measurements) — *measured_by*
  - [SimPER: A Minimalist Approach to Preference  Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  > We evaluate its performance on dialogue (Zheng et al., 2023), math (Cobbe et al., 2021) and coding (Chen et al., 2021) following Wang et al. (2024d)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Chain of Hindsight aligns Language Models with Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/b4ccb915933443c86a588e45d77a5748-Paper-Conference.pdf)
- **Wizard-of-Wikipedia** (measurements) — *measured_by*
  > train a dialogue model on Wizard-of-Wikipedia (Dinan et al., 2019) which we then train further on synthetic data containing hallucinations
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **Databricks Dolly-15k** (measurements) — *measured_by*
  - [Beyond Interpretability: The Gains of Feature Monosemanticity on Model Robustness](https://proceedings.iclr.cc/paper_files/paper/2025/file/11822e84689e631615199db3b75cd0e4-Paper-Conference.pdf)
- **UltraFeedback** (measurements) — *measured_by*
  - [MallowsPO: Fine-Tune Your LLM with Preference Dispersions](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ddab70bf41ffe5d423840644d3357f4-Paper-Conference.pdf)
- **ConvAI2** (measurements) — *measured_by*
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)

### → Dialogue generation
- **Generalization** (constructs) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)

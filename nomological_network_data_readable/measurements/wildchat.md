# WildChat
**Type:** Measurement  
**Referenced in:** 12 papers  

## State of the Field

WildChat is consistently characterized across the provided literature as a dataset of real-world conversations between users and Large Language Models, specifically GPT models. One paper notes its collection method involved offering a free API in exchange for interaction logs, which allows the dataset to "more closely reflect real user needs" ("Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes"). This focus on authentic data is a recurring theme, with another study contrasting WildChat's capture of "real-world user interactions" with datasets containing primarily synthetic responses. As a measurement instrument, WildChat is used to assess several model attributes, including `Harmlessness`, `Refusal to answer`, and `Multilingual ability`. Researchers also employ it for more specific analyses, such as studying the overlap between model outputs and online text in "benign interactions," providing out-of-distribution prompts for testing generalization, and examining implicit feedback in naturalistic settings. The dataset is also generally studied in the context of `Dialogue`.

## Sources

**[Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf)**
> A dataset of real-world LLM conversations used here to analyze whether generated outputs overlap with online text in benign interactions.

## Relationships

### → WildChat
- **Refusal to answer** (behaviors tasks) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **Multilingual ability** (constructs) — *measured_by*
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)

### Associated with
- **Dialogue** (behaviors tasks)
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)

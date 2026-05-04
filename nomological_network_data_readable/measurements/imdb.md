# IMDb
**Type:** Measurement  
**Referenced in:** 45 papers  
**Also known as:** IMDB, Imdb, IMDB dataset, IMDb dataset  

## State of the Field

Across the surveyed literature, IMDb is consistently defined as a benchmark dataset of movie reviews used for binary sentiment classification. Its most frequent application is to measure and operationalize `Sentiment analysis` and general `Text classification`, where models must predict whether a review is positive or negative. Multiple sources describe it as a "large movie review dataset for binary classification". A distinct, recurring application uses IMDb to evaluate controlled text generation and what some papers term `sentiment alignment`. In these cases, the task is not classification but rather generating reviews with a specific sentiment, such as producing "positive comments on movies" to test alignment without human feedback. Less common uses found in the data include serving as an out-of-distribution target task and its use in recommendation system research. The dataset is also listed as a measure for `Adaptability`, `Generalization`, and `Sentiment control`, among other behaviors.

## Sources

**[IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)**
> A sentiment classification benchmark included in the expanded dataset pool for cascade evaluation.

**[Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf) (as "IMDB")**
> A sentiment-related dataset from GRUE used in the paper's reinforcement finetuning experiments.

**[Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf) (as "Imdb")**
> A dataset of movie reviews and ratings, widely used for sentiment analysis and recommendation system research.

**[Privately Aligning Language Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/477b39bfb9db99f60914dbfed5f23eb2-Paper-Conference.pdf) (as "IMDb dataset")**
> Sentiment classification benchmark used to evaluate controlled generation of positive movie reviews, serving as a testbed for alignment without human-in-the-loop.

**[RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf) (as "IMDB dataset")**
> A large movie review dataset used for evaluating controlled text generation, particularly sentiment alignment in generated reviews.

## Relationships

### → IMDb
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  > we train a CNN-LSTM model with 2.7 million parameters on the IMDB (Maas et al., 2011) for binary classification of positive or negative reviews.
  - [Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > Table 1 gives an overview of our experimental setup, including specifics for the task, datasets, encoders, LLMs, and task-specific prompts we use.
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)
- **Adaptability** (constructs) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [UQE: A Query Engine for Unstructured Databases](https://proceedings.neurips.cc/paper_files/paper/2024/file/34b3a40ec9752c1ae48fe85fef8fe8dc-Paper-Conference.pdf)
- **Sentiment control** (behaviors tasks) — *measured_by*
  - [Towards Robust Alignment of Language Models: Distributionally Robustifying Direct Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/294fd30f8cbb89ce328d5a01fef47fb4-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs) — *measured_by*
  - [Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.271.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)

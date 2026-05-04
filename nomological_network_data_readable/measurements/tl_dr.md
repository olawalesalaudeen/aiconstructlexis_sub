# TL;DR
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, TL;DR is characterized in two distinct ways: as a dataset and as an LM-based evaluation procedure. One framing describes it as a "curated collection of Reddit posts" for research, as noted in "Through the Valley: Path to Effective LongCoTTraining for Small Language Models". The other prevalent framing, found in works like "The Impossibility of FairLLMs", defines it as a benchmark where a model like GPT-4 evaluates the quality of summaries by judging the "win-rate between model’s generation and ground truth answer". The most common application of TL;DR is to measure the behavior of Text summarization, with papers operationalizing this by either evaluating on the dataset's test set or by employing the specific judge-model protocol. A smaller set of papers also reports using TL;DR as a measurement instrument for the construct of Human preference alignment.

## Sources

**[The Impossibility of FairLLMs](https://aclanthology.org/2025.acl-long.6.pdf)**
> A summarization benchmark where GPT-4 evaluates the quality of model-generated summaries against reference summaries using win-rate metrics.

## Relationships

### → TL;DR
- **Text summarization** (behaviors tasks) — *measured_by*
  > For the summarization task, we follow (Rafailov et al., 2024b) and evaluate the win rate against the base model, using GPT-4o as the judge model on 256 randomly sampled test cases from the TL;DR test set.
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)

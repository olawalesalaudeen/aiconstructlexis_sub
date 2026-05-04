# SLURP
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, SLURP is consistently described as a spoken language understanding dataset. Its most common application appears to be as a measurement instrument for evaluating model capabilities, specifically for tasks like `Information extraction` and `Intention recognition`. One paper highlights its use for "slot filling from reference transcriptions," drawing on the dataset's annotations for "scenarios, actions and entities." The dataset is composed of "single-turn user interactions with a home assistant," containing both audio recordings and text transcriptions, though at least one study reports using only the text for training. A different application is also noted, where SLURP serves as a "seed corpus for generating dialogues." In this context, it is used to construct new corpora by leveraging its "diverse intents and interwoven mode switches."

## Sources

**[Bayesian WeakS-to-Strong from Text Classification to Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/495e55f361708bedbab5d81f92048dcd-Paper-Conference.pdf)**
> SLURP is a spoken language understanding dataset used here for slot filling from reference transcriptions of single-turn user interactions.

## Relationships

### → SLURP
- **Information extraction** (behaviors tasks) — *measured_by*
  > SLURP dataset (Bastianelli et al., 2020) was used which contains 16.5k sentences and 72k audio recordings of single-turn user interactions with a home assistant, annotated with scenarios, actions and entities. (Section 5.1)
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
- **Intent classification** (behaviors tasks) — *measured_by*
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)

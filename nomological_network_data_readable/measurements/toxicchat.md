# ToxicChat
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, ToxicChat is consistently described as a benchmark dataset for assessing model safety. Its most prevalent application is for evaluating model performance on "query safety classification," as stated in multiple sources. Papers use this instrument to measure behaviors such as "Harmfulness detection" and "Harmful content detection." One definition elaborates on its structure, describing it as a prompt dataset with "multiple harmful categories" and "both simple and story-based templates." Another source specifies that it "contains both train and test splits with 5000 samples each" ("Language Models Largely Exhibit Human-like Constituent Ordering Preferences"). While its primary use is for evaluation, a smaller number of papers also identify it as a dataset suitable for training safety classifiers. The data shows it is frequently used alongside other safety benchmarks, including XSTest, WildJailBreak, and OpenAI Mod.

## Sources

**[BingoGuard: LLM Content Moderation Tools with Risk Levels](https://proceedings.iclr.cc/paper_files/paper/2025/file/782b6152c04e9948c2cb3833e9a288ef-Paper-Conference.pdf)**
> A benchmark dataset used for evaluating the performance of models on query safety classification.

## Relationships

### → ToxicChat
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **Harmful content detection** (behaviors tasks) — *measured_by*
  > We evaluate the guardrail models on six datasets including five standard safety datasets (OpenAI Mod (Markov et al., 2023),ToxicChat (Lin et al., 2023), XSTest (Röttger et al., 2023), Overkill (Shi et al., 2024), BeaverTails (Ji et al., 2024)) and (2) our novel safety dataset TwinSafety. (Section 5)
  - [$R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a07e87ecfa8a651d62257571669b0150-Paper-Conference.pdf)

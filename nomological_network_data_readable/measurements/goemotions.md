# GoEmotions
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** GoEmotion, Emotion  

## State of the Field

Across the provided literature, GoEmotions is most commonly described as a benchmark or dataset for evaluating emotion-related tasks, particularly emotion classification. The prevailing description characterizes it as a multilabel dataset of human-annotated Reddit comments, with one paper specifying it contains '58,000 Reddit comments' with '27 emotion labels plus neutral' (WarriorCoder: Learning from Expert Battles to Augment Code Large Language Models). Some work uses these 27 emotions in pooled clusters, such as admiration, anger, and joy. A distinct set of papers in this collection refers to an 'Emotion' dataset for the same purpose, but consistently defines it as having six classes like 'joy, sadness, anger, fear, love, and surprise'. While most papers use it for classification, a less frequent application is to 'train probes for positive and negative categories' (Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?). Overall, the instrument is used to measure behaviors such as `Text classification`, `Sentiment analysis`, and general `Classification`.

## Sources

**[Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)**
> Multilabel emotion recognition benchmark with 27 emotions, used here with pooled clusters (admiration, anger, fear, joy, optimism, sadness, surprise) to evaluate LLMs on emotion classification with individual and aggregate labels.

**[CCHall: A Novel Benchmark for Joint Cross-Lingual and Cross-Modal Hallucinations Detection in Large Language Models](https://aclanthology.org/2025.acl-long.1486.pdf) (as "GoEmotion")**
> Dataset of Reddit comments labeled with fine-grained emotions such as amusement, fear, and gratitude, used for emotion recognition evaluation.

**[Disentangling Biased Knowledge from Reasoning in Large Language Models via Machine Unlearning](https://aclanthology.org/2025.acl-long.306.pdf) (as "Emotion")**
> A dataset for fine-grained emotion classification, categorizing text into six classes: joy, sadness, anger, fear, love, and surprise.

## Relationships

### → GoEmotions
- **Text classification** (behaviors tasks) — *measured_by*
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  - [Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf)
- **Classification** (behaviors tasks) — *measured_by*
  - [Beyond the Score: Uncertainty-CalibratedLLMs for Automated Essay Assessment](https://aclanthology.org/2025.emnlp-main.993.pdf)

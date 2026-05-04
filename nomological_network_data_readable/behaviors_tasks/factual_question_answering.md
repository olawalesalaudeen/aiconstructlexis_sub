# Factual question answering
**Type:** Behavior  
**Referenced in:** 32 papers  
**Also known as:** Factual query answering, Single-fact question answering, Factual prediction, Truthful Answering, Truthful question answering, Honest response generation, Simple QA, Fact-based question answering  

## State of the Field

Across the surveyed literature, factual question answering is most commonly defined as the behavior of providing a precise, factually correct answer to a question that requires world knowledge. Alternative framings exist, including 'single-fact question answering' which requires only one supporting fact, and 'factual prediction,' which involves completing a prompt with a specific entity, often based on subject-relation-object triplets. A related cluster of definitions, such as 'truthful question answering' and 'honest response generation,' emphasizes not just correctness but also the avoidance of common misconceptions or the admission of prior misdeeds. This behavior is operationalized and measured using several benchmarks, with papers frequently citing Natural Questions (NQ), TruthfulQA, and TriviaQA. Performance is typically assessed via 'exact match' scoring, as one study reports for '32-shot Natural Questions (NQ)' (Sheared LLaMA), though F1 score and regular expression matching are also employed. The task is also examined in varied contexts, such as with visual assistance or following knowledge editing procedures. The behavior is studied alongside reasoning challenges and is explicitly related to the construct of Memorization, with one paper describing 'Simple QA' as evaluating the 'ability to recall and retrieve factual knowledge accurately' (From RAG to Memory).

## Sources

**[How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe79ae16496a0f5b57287873de072d1-Paper-Conference.pdf)**
> The observable behavior of providing a precise, factually correct answer to a question requiring world knowledge.

**[Does Reasoning Emerge? Examining the Probabilities of Causation in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a1f97d2b922da92e880d13b7d2bf02-Paper-Conference.pdf) (as "Factual query answering")**
> The observable behavior of responding to a direct query about a problem state based on provided facts.

**[BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Single-fact question answering")**
> The observable task of answering questions that require only one supporting fact.

**[Scalable Influence and Fact Tracing for Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/65798a76cc176c29b6bfefe84b0a03ff-Paper-Conference.pdf) (as "Factual prediction")**
> The task of completing a natural language prompt with a specific factual entity, such as filling in the object of a subject-relation pair.

**[Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf) (as "Truthful Answering")**
> The observable task of providing factually accurate answers as evaluated on benchmarks.

**[Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf) (as "Truthful question answering")**
> The observable behavior of providing answers that are factually correct and avoid common misconceptions.

**[Detecting Strategic Deception with Linear Probes](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goldowsky-dill25a/goldowsky-dill25a.pdf) (as "Honest response generation")**
> Producing a model output that truthfully communicates facts or admits to prior misdeeds without intent to mislead.

**[From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf) (as "Simple QA")**
> Generating answers to questions that require retrieving and recalling a single fact or entity from a knowledge source.

**[WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thede25a/thede25a.pdf) (as "Fact-based question answering")**
> Producing correct answers to factual questions based on updated knowledge, where each question is derived from a subject-relation-object triplet.

## Relationships

### Factual question answering →
- **TriviaQA** (measurements) — *measured_by*
  - [Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines](https://aclanthology.org/2025.naacl-long.168.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)
- **SQuAD v1.1** (measurements) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **NFCorpus** (measurements) — *measured_by*
  - [MCIP: ProtectingMCPSafety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.63.pdf)

### Associated with
- **Memorization** (constructs)
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)

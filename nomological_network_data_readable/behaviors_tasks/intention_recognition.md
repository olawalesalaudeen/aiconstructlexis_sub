# Intention recognition
**Type:** Behavior  
**Referenced in:** 20 papers  
**Also known as:** Intent detection, Post intent generation, Intent recognition, Multimodal intent recognition  

## State of the Field

Across the provided literature, "Intention recognition" is predominantly characterized as the task of identifying a user's goal or purpose from an utterance, frequently in the context of conversational AI and virtual assistants. Most definitions frame this as a classification problem, where an utterance is assigned to one of several predefined intents. A smaller set of studies expands this scope to include multimodal inputs, defining it as the classification of intent from text combined with video and audio cues, or inferring intentions from "subtle cues in a video." One paper presents a generative variant, "Post intent generation," where models must produce a description of an author's communicative purpose, such as "humor, complaint," for sharing content like a meme. This behavior is operationalized and measured using a variety of benchmarks, including SNIPS, MASSIVE, BANKING77, CLINC150, SLURP, and MIntRec2.0. The task is often studied alongside topic classification and sentiment analysis and is shown to be related to relational reasoning.

## Sources

**[Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing](https://aclanthology.org/2025.emnlp-main.1.pdf) (as "Intent detection")**
> The task of identifying the user's intent from an utterance, used in this paper to assess the generalizability of the error detection method.

**[A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.9.pdf) (as "Intent classification")**
> The task of identifying the user's intention or goal from a spoken or written utterance, typically in a conversational AI context.

**[WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation inThai](https://aclanthology.org/2025.emnlp-main.176.pdf) (as "Post intent generation")**
> Producing a description of the author's communicative purpose in sharing a meme, such as humor, complaint, or provocation, based on multimodal context.

**[TS-CLIP: Time Series Understanding byCLIP](https://aclanthology.org/2025.emnlp-main.232.pdf)**
> The observable task of identifying the underlying goal or intent of a user's utterances in a conversation.

**[AbsVis – Benchmarking How Humans and Vision-Language Models “See” Abstract Concepts in Images](https://aclanthology.org/2025.emnlp-main.418.pdf) (as "Intent recognition")**
> The task of classifying a user's utterance into one of several predefined intents, typically in the context of a virtual assistant.

**[Rank-Awareness and Angular Constraints: A New Perspective on Learning Sentence Embeddings fromNLIData](https://aclanthology.org/2025.emnlp-main.1130.pdf) (as "Multimodal intent recognition")**
> Classifying the intent expressed in a multimodal sample using text together with video and audio cues.

## Relationships

### Intention recognition →
- **CLINC** (measurements) — *measured_by*
  - [Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing](https://aclanthology.org/2025.emnlp-main.1.pdf)
- **Massive** (measurements) — *measured_by*
  - [AbsVis – Benchmarking How Humans and Vision-Language Models “See” Abstract Concepts in Images](https://aclanthology.org/2025.emnlp-main.418.pdf)
- **BANKING77** (measurements) — *measured_by*
  - [Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing](https://aclanthology.org/2025.emnlp-main.1.pdf)
- **MIntRec2.0** (measurements) — *measured_by*
  - [Rank-Awareness and Angular Constraints: A New Perspective on Learning Sentence Embeddings fromNLIData](https://aclanthology.org/2025.emnlp-main.1130.pdf)

### Associated with
- **Relational reasoning** (constructs)
  - [Rank-Awareness and Angular Constraints: A New Perspective on Learning Sentence Embeddings fromNLIData](https://aclanthology.org/2025.emnlp-main.1130.pdf)

# Massive
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** Massive(I)  

## State of the Field

The dataset Massive is used in the provided literature to measure a model's capacity for understanding user intent, with its application varying across papers. One described usage frames it as a multilingual dataset for "intent and slot detection" covering 15 low-resource languages, specifically to evaluate "zero-shot performance on unseen label schemas" ("AXIS: Efficient Human-Agent-Computer Interaction withAPI-FirstLLM-Based Agents"). Another paper presents a different application, denoted Massive(I), which is used for "intent discovery" and aims to identify "unknown intents in user utterances" ("QSpec: Speculative Decoding with Complementary Quantization Schemes"). Consistent with these applications, the dataset is explicitly used to measure the behavior of "Intention recognition". Thus, the data shows Massive being operationalized in at least two distinct ways: one focusing on zero-shot detection of predefined intents in a multilingual, low-resource context, and the other on discovering entirely new intents.

## Sources

**[AXIS: Efficient Human-Agent-Computer Interaction withAPI-FirstLLM-Based Agents](https://aclanthology.org/2025.acl-long.382.pdf)**
> Multilingual dataset for intent and slot detection covering 15 low-resource languages, used to evaluate zero-shot performance on unseen label schemas.

**[QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.241.pdf) (as "Massive(I)")**
> A dataset for intent discovery, aiming to identify unknown intents within user utterances.

## Relationships

### → Massive
- **Intention recognition** (behaviors tasks) — *measured_by*
  - [AbsVis – Benchmarking How Humans and Vision-Language Models “See” Abstract Concepts in Images](https://aclanthology.org/2025.emnlp-main.418.pdf)

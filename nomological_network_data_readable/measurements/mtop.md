# MTop
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** MTOP(I)  

## State of the Field

Across the provided literature, MTop is consistently presented as a benchmark dataset, though its specific application varies between papers. The prevailing usage, found across multiple sources, is to measure the behavior of semantic parsing. One paper elaborates on this, defining MTop as a tool for "evaluating multilingual task-oriented semantic parsing, specifically focusing on intent and slot filling" (Logits-Based Finetuning). This is reinforced by a source snippet which notes its use for tasks that "span from intent and slot filling." A different framing is presented in one paper which refers to a variant, "MTOP(I)," as a dataset for the behavior of intent discovery. In this context, the goal is to "discover unknown intents in user utterances" (QSpec: Speculative Decoding with Complementary Quantization Schemes). Thus, the data shows MTop being operationalized in two distinct ways: most commonly for evaluating semantic parsing, and in at least one case, for identifying novel user intents.

## Sources

**[Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.746.pdf)**
> A benchmark dataset for evaluating multilingual task-oriented semantic parsing, specifically focusing on intent and slot filling.

**[QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.241.pdf) (as "MTOP(I)")**
> A dataset for intent discovery, aiming to identify unknown intents within user utterances.

## Relationships

### → MTop
- **Semantic parsing** (behaviors tasks) — *measured_by*
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)

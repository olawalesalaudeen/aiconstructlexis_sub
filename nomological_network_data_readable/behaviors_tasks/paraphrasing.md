# Paraphrasing
**Type:** Behavior  
**Referenced in:** 38 papers  
**Also known as:** Text rephrasing, Reformulation, Rewriting, Text paraphrasing, Rephrasing, Query rephrasing, Profile diversification, Spoken-to-written transformation  

## State of the Field

Across the provided literature, paraphrasing is most commonly defined as the behavior of rewriting text to preserve its original semantic meaning while altering its wording or structure. This behavior is referred to by several names, including "text rephrasing," "rewriting," and "reformulation," with the core requirement of semantic equivalence being a consistent feature. The task is operationalized by prompting models to generate variations of an input, and its performance is evaluated using datasets like MRPC, which contains "human annotations for semantic equivalence" (Seq1F1B). A prevalent application of paraphrasing is in adversarial contexts, where it is used as an attack to evade detection or, as one paper notes, to create a "semantically similar but watermark-free form" of a text (PA-RAG). Paraphrasing is also frequently employed for data augmentation to generate "semantically equivalent text variants" (A Statistical Approach for Controlled Training Data Detection), diversify user profiles, or improve model generalization. A smaller set of studies frame it as a user behavior for restating a query after an unsatisfactory response, as a pretraining task, or as a method to resolve complex words to improve translation. More specific framings include "spoken-to-written transformation" and "query rephrasing" to test a model's reliance on semantic cues. Finally, this behavior is studied alongside `String manipulation` and is also used as a way to measure `Commonsense knowledge`.

## Sources

**[xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5cf13bfd3762821ef7607e63ee90075-Paper-Conference.pdf)**
> Reproducing the content of a document in different words, used here as a pretraining task to align retrieval features with text.

**[When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings](https://proceedings.iclr.cc/paper_files/paper/2025/file/dbdea7859f1d2fc10f2c9e79b8f5ae54-Paper-Conference.pdf) (as "Text rephrasing")**
> Producing a paraphrase of an input text while preserving its meaning.

**[Can Graph Descriptive Order Affect Solving Graph Problems withLLMs?](https://aclanthology.org/2025.acl-long.322.pdf) (as "Text rewriting")**
> The task of taking an input text and generating a modified version of it, often following a specific instruction like 'refine' or 'rephrase'.

**[Déjà Vu? Decoding Repeated Reading from Eye Movements](https://aclanthology.org/2025.acl-long.957.pdf) (as "Rewriting")**
> The task of rephrasing a given text to alter its structure or wording while preserving its original semantic meaning.

**[QQSUM: A Novel Task and Model of Quantitative Query-Focused Summarization for Review-based Product Question Answering](https://aclanthology.org/2025.acl-long.1016.pdf) (as "Reformulation")**
> The observable act of a participant repeating or rephrasing their query due to a failure to establish grounding, with the new utterance being semantically equivalent to the original.

**[Robust Multi-bit Text Watermark with LLM-based Paraphrasers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25k/xu25k.pdf) (as "Text paraphrasing")**
> The observable act of generating a new text that preserves the semantic meaning of an original text but uses different wording or structure.

**[Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes](https://aclanthology.org/2025.emnlp-main.133.pdf) (as "Rephrasing")**
> User behavior of restating their request in a different way to elicit a better model response after an unsatisfactory initial output.

**[Steering Language Models in Multi-Token Generation: A Case Study on Tense and Aspect](https://aclanthology.org/2025.emnlp-main.436.pdf) (as "Query rephrasing")**
> Modifying the phrasing of a query while preserving its original meaning to test for reliance on semantic rather than surface-level cues.

**[DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.894.pdf) (as "Profile diversification")**
> The observable behavior of an LLM rephrasing a given user or item profile to generate multiple semantically similar but textually distinct versions for data augmentation.

**[Retrieval-augmentedGUIAgents with Generative Guidelines](https://aclanthology.org/2025.emnlp-main.903.pdf) (as "Spoken-to-written transformation")**
> Producing a grammatically correct and semantically faithful written version of a spoken utterance, preserving all intended meaning while correcting structural deviations.

**[2025.emnlp-main.1250.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1250.checklist.pdf) (as "Paraphrase generation")**
> The model produces semantically equivalent variations of input sentences, used to expand diagnostic datasets while preserving meaning.

## Relationships

### → Paraphrasing
- **Instruction following** (constructs) — *measured_by*
  - [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/e4a46394ba5378b3f9a186a5b4c650d1-Paper-Conference.pdf)

### Associated with
- **String manipulation** (behaviors tasks)
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)

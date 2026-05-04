# MiniCheck
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** Minicheck  

## State of the Field

Across the provided literature, MiniCheck is most commonly characterized as an automatic metric used to evaluate the faithfulness of generated text. It is frequently defined as a trained, distilled Natural Language Inference (NLI) model that assesses summary-document entailment. Papers operationalize this by using MiniCheck to generate an entailment score between a claim and its evidence or to score the consistency of individual statements against source documents. The primary construct it is used to measure is Faithfulness, with some papers also describing it as a "hallucination detector" that classifies whether content is supported by context ("Curriculum Debiasing: Toward Robust Parameter-Efficient Fine-Tuning Against Dataset Biases"). The evaluation process is noted to sometimes involve internal document chunking, comparing generated summary sentences against these chunks. A less common framing describes it simply as a "verifier" model, used alongside other verifiers like AlignScore. Its application is noted in summarization tasks and long-context settings, where one study reports its efficacy is "comparable to GPT-4 performance" ("SLM-Mod: Small Language Models SurpassLLMs at Content Moderation").

## Sources

**[Rethinking the Role ofLLMs for Document-level Relation Extraction: a Refiner with Task Distribution and Probability Fusion](https://aclanthology.org/2025.naacl-long.320.pdf) (as "Minicheck")**
> A model used as a verifier to generate an entailment score between 0 and 1 for a claim and its corresponding evidence.

**[Palette of Language Models: A Solver for Controlled Text Generation](https://aclanthology.org/2025.naacl-long.498.pdf)**
> An automatic faithfulness metric based on a distilled NLI model that evaluates summary-document entailment, used here in long-context settings with document-level aggregation.

## Relationships

### → MiniCheck
- **Faithfulness** (constructs) — *measured_by*
  - [SLM-Mod: Small Language Models SurpassLLMs at Content Moderation](https://aclanthology.org/2025.naacl-long.442.pdf)

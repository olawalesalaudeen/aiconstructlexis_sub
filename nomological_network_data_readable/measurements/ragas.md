# RAGAS
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, RAGAS is consistently characterized as an evaluation framework for Retrieval-Augmented Generation (RAG) systems. The prevailing description is that of a "pointwise evaluation system" which leverages "prompted frontier models and embedding models" to generate scores. A related framing describes it as a general "LLM-based evaluation framework" capable of providing "scalable and automated assessments." The primary construct RAGAS is used to measure is `Faithfulness`, a connection explicitly stated across multiple sources. The framework is also reported to score system responses on other metrics, including "refusal" and "context relevance." In practice, it is used as a reference evaluator, sometimes alongside other tools like hallucination detectors, to assess the quality of RAG outputs.

## Sources

**[Curriculum Debiasing: Toward Robust Parameter-Efficient Fine-Tuning Against Dataset Biases](https://aclanthology.org/2025.acl-long.470.pdf)**
> A pointwise evaluation system for Retrieval-Augmented Generation that uses prompted frontier models and embedding models to score responses on metrics like refusal and faithfulness.

## Relationships

### → RAGAS
- **Faithfulness** (constructs) — *measured_by*
  - [Speech Discrete Tokens or Continuous Features? A Comparative Analysis for Spoken Language Understanding inSpeechLLMs](https://aclanthology.org/2025.emnlp-main.1267.pdf)

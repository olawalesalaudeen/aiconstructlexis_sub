# ParaDetox
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Based on the available data, ParaDetox is characterized as a dataset for evaluating language models. The single provided source defines it as containing pairs of "toxic" and "non-toxic" sentences generated through paraphrasing. This dataset is described as being used to identify toxicity-related features within a model's internal activations. In terms of its application as a measurement instrument, the data indicates ParaDetox is used to assess both `Conditional text generation` and `Semantic preservation`. In the context of measuring semantic preservation, the concept of semantic similarity is mentioned as a means to evaluate how well generated text preserves the meaning of the original input.

## Sources

**[EvaluatingLLM-Generated Diagrams as Graphs](https://aclanthology.org/2025.emnlp-main.641.pdf)**
> A dataset containing pairs of toxic and non-toxic paraphrased sentences, used to identify toxicity-related features in a model's activations.

## Relationships

### → ParaDetox
- **Semantic preservation** (constructs) — *measured_by*
  > Semantic Similarity (SIM) measures to what extent the generated text preserves the meaning of the original input. (Section 4.1.1)
  - [Measuring scalar constructs in social science withLLMs](https://aclanthology.org/2025.emnlp-main.1636.pdf)
- **Conditional text generation** (behaviors tasks) — *measured_by*
  - [Judging Quality Across Languages: A Multilingual Approach to Pretraining Data Filtering with Language Models](https://aclanthology.org/2025.emnlp-main.450.pdf)

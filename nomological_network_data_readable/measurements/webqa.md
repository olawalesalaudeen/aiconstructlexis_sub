# WebQA
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Based on the available data, WebQA is characterized as a retrieval-augmented question-answering (QA) dataset used to measure information retrieval capabilities. The instrument is specifically positioned to evaluate long-context retrieval performance. Operationally, it is set up with each question accompanied by 20 documents, which facilitates the assessment of position-dependent accuracy. The single source paper in this set leverages WebQA for evaluation alongside other datasets, including NaturalQuestions and TriviaQA, framing it as a tool for this purpose.

## Sources

**[MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)**
> Retrieval-augmented QA dataset used to evaluate long-context retrieval performance with 20 documents per question, assessing position-dependent accuracy.

## Relationships

### → WebQA
- **Information retrieval** (behaviors tasks) — *measured_by*
  > The evaluation leverages three datasets: NaturalQuestions (NQ) (Kwiatkowski et al., 2019), TriviaQA (TQA) (Joshi et al., 2017) and WebQA (WebQ) (Berant et al., 2013), and a specilized task KV Retrieval (Liu et al., 2024). (Section 5.1)
  - [MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering](https://aclanthology.org/2025.emnlp-main.78.pdf)

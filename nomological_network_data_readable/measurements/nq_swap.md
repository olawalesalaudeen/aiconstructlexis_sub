# NQ-Swap
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

NQ-Swap is characterized in the provided literature as a counterfactual question answering benchmark. It is used to measure model performance on `Question answering` and to assess constructs such as `Faithfulness` and `Context faithfulness`. The benchmark is defined as a modified version of the Natural Questions dataset where incorrect answers are deliberately swapped into the context. This design is intended to test a model's 'reliance on correct evidence.' One source describes it as offering a 'challenging and complementary evaluation of a model’s ability to identify and rely on the correct evidence,' positioning it as a tool for assessing a model's capacity to use valid information from a given context.

## Sources

**[Joint Modeling of Entities and Discourse Relations for Coherence Assessment](https://aclanthology.org/2025.emnlp-main.1114.pdf)**
> A counterfactual version of Natural Questions where incorrect answers are swapped into the context to test a model's reliance on correct evidence.

## Relationships

### → NQ-Swap
- **Faithfulness** (constructs) — *measured_by*
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Ethical Concern Identification inNLP: A Corpus ofACLAnthology Ethics Statements](https://aclanthology.org/2025.naacl-long.581.pdf)
- **Context faithfulness** (constructs) — *measured_by*
  > we also include two counter-factual QA benchmarks: NQ-Swap and ConfiQA, offering a more challenging and complementary evaluation of a model’s ability to identify and rely on the correct evidence. (Section 3.2)
  - [Joint Modeling of Entities and Discourse Relations for Coherence Assessment](https://aclanthology.org/2025.emnlp-main.1114.pdf)

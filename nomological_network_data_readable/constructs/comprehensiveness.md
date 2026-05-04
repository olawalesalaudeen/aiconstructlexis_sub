# Comprehensiveness
**Type:** Construct  
**Referenced in:** 16 papers  
**Also known as:** Answer comprehensiveness  

## State of the Field

Across the surveyed literature, Comprehensiveness is most commonly defined as the extent to which a generated output contains sufficient information to answer a query or support a downstream task. While this task-oriented framing is prevalent, other work defines the construct in terms of source coverage, such as incorporating perspectives from all available documents or including all relevant details from a source video. A related framing, termed "Answer comprehensiveness," focuses on the degree to which a response addresses the full set of facets needed for a complete answer. As a construct, Comprehensiveness is primarily operationalized and measured through `Human evaluation`, with papers reporting the use of human judges who rate outputs on Likert scales. A less common approach involves using `LLM-as-a-judge` for evaluation. One paper specifically operationalizes the concept as "sub-question coverage," noting this metric can "approximate human perception of answer quality well" (SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for ComplexQA). The construct is often studied alongside other subjective qualities like conciseness, clarity, and formality, and is explicitly likened to recall in at least one study.

## Sources

**[PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf)**
> The extent to which a summary contains enough information to answer the query or support the downstream task, regardless of whether every detail is directly copied from the source documents.

**[SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for ComplexQA](https://aclanthology.org/2025.naacl-long.301.pdf) (as "Answer comprehensiveness")**
> The extent to which a response addresses the full set of important facets needed for a complete answer to an open-ended question.

## Relationships

### Comprehensiveness →
- **Human evaluation** (measurements) — *measured_by*
  > We find the sub-question coverage as an answer quality metric can approximate human perception of answer quality well (section 4).
  - [VisDoM: Multi-DocumentQAwith Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.311.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [MemeArena: Automating Context-Aware Unbiased Evaluation of Harmfulness Understanding for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.891.pdf)

### → Comprehensiveness
- **Faithfulness** (constructs) — *measured_by*
  - [The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1769.pdf)

# QAMPARI
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided sources, QAMPARI is consistently defined as a benchmark dataset for attributable, factoid question-answering tasks. A common feature highlighted is that questions may have multiple answers, with one paper specifying that the answer to a question is "a list of entities drawn from different passages." While it is predominantly framed as a factoid QA dataset, one source also describes it as an "attributable factoid and long-form question-answering" task. The dataset is explicitly used for evaluation purposes. Based on the provided relationships, papers use QAMPARI to measure the constructs of `Faithfulness` and `Refusal` in language models. One definition also states it is used to evaluate "precision and recall in attributed generation." In evaluation settings, it is sometimes used alongside other benchmarks like ASQA and ELI5.

## Sources

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)**
> A benchmark dataset for attributable, factoid question-answering tasks where questions may have multiple answers, used for evaluation.

## Relationships

### → QAMPARI
- **Trustworthiness** (constructs) — *measured_by*
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **Refusal** (constructs) — *measured_by*
  > TRUST-ALIGN improves models' refusal capability. Across all 27 configurations, TRUST-ALIGN yields substantial improvements in F1GR. In LLaMA-3-8b, TRUST-ALIGN outperforms FRONT by 23.87% (ASQA), 47.95% (QAMPARI), and 45.72% (ELI5).
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)

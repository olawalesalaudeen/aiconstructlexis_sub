# ASQA
**Type:** Measurement  
**Referenced in:** 23 papers  

## State of the Field

Across the provided literature, ASQA is consistently described as a benchmark dataset for long-form question answering. The most prevalent feature highlighted is its focus on ambiguous questions, with several papers defining it as a tool to assess how well models generate answers that cover "multiple possible interpretations." This is further specified by one source stating that ASQA extends the AmbigQA dataset for this purpose. Another recurring theme is the dataset's utility for evaluating attributable generation, with some papers describing it as a benchmark for "attributable, long-form question-answering tasks" and for assessing "citation quality."

Based on its application in the surveyed papers, ASQA is used to measure a range of capabilities. It directly operationalizes the evaluation of `Question answering`, particularly `Conditional ambiguous question answering` and `Long-form text generation`. Beyond these core tasks, the dataset is also employed to assess broader model behaviors such as `Faithfulness` and `Refusal`. While widely used, one paper notes a potential limitation, suggesting its "annotation process leads to logical inconsistencies when linking different answer components."

## Sources

**[Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)**
> A benchmark dataset for attributable, long-form question-answering tasks used for evaluation.

## Relationships

### → ASQA
- **Trustworthiness** (constructs) — *measured_by*
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **Refusal** (constructs) — *measured_by*
  > TRUST-ALIGN improves models' refusal capability. Across all 27 configurations, TRUST-ALIGN yields substantial improvements in F1GR. In LLaMA-3-8b, TRUST-ALIGN outperforms FRONT by 23.87% (ASQA), 47.95% (QAMPARI), and 45.72% (ELI5).
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > The questions used for constructing our training data are sourced from the ASQA (Stelmakh et al., 2022), WebQuestions (Berant et al., 2013), and Natural Questions (Kwiatkowski et al., 2019) training splits. (Section 4.1.1)
  - [KS-Lottery: Finding Certified Lottery Tickets for Multilingual Transfer in Large Language Models](https://aclanthology.org/2025.naacl-long.459.pdf)
- **Conditional ambiguous question answering** (behaviors tasks) — *measured_by*
  - [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.56.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  > To the best of our knowledge, ASQA (Stelmakh et al., 2022) is the only dataset that falls into this category. (Section 4)
  - [Bitune: Leveraging Bidirectional Attention to Improve Decoder-OnlyLLMs](https://aclanthology.org/2025.emnlp-main.482.pdf)
- **Factual accuracy** (constructs) — *measured_by*
  - [Exploring Large Language Models for Detecting Mental Disorders](https://aclanthology.org/2025.emnlp-main.1753.pdf)

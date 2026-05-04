# ELI5
**Type:** Measurement  
**Referenced in:** 14 papers  
**Also known as:** ELI-5  

## State of the Field

Across the provided literature, ELI5 is consistently used as a benchmark for evaluating long-form question answering (LFQA). The dataset is composed of user-generated questions from the "Explain Like I’m Five" subreddit, focusing on topics like science, history, and everyday life. Models are evaluated on their ability to generate "paragraph-length responses" that are simple, comprehensive, and easy to understand, often requiring information from multiple sources. Its primary application is to measure question answering capabilities, with some studies also using it to assess model behaviors such as refusal. The prevailing definition describes it as an open-ended QA dataset for evaluating factual answering and helpfulness. A single paper presents a minority framing, referring to it as "ELI-5" and describing it as a collection of explanations adapted for personalized generation tasks. It is frequently described as a "challenging" dataset because the expected answers are "comprehensive and cover multiple aspects."

## Sources

**[An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)**
> Open-ended question-answering dataset of user-generated questions about science, history, and everyday life used to evaluate factual question answering and helpfulness.

**[2025.emnlp-main.475.checklist](https://aclanthology.org/attachments/2025.emnlp-main.475.checklist.pdf) (as "ELI-5")**
> Dataset of explanations for complex topics written at a fifth-grade level, adapted for personalized generation tasks.

## Relationships

### → ELI5
- **Long-form question answering** (behaviors tasks) — *measured_by*
  > We utilize two popular datasets for the task of long-form QA, including: ... 2) ELI5, which is a dataset for complex QA with paragraph-length responses... (Section 4)
  - [LLM4DistReconfig: A Fine-tuned Large Language Model for Power Distribution Network Reconfiguration](https://aclanthology.org/2025.naacl-long.209.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We run experiments on two question- answering datasets, namely NQ-Open and ELI5. (Section 3.1)
  - [Investigating Human Values in Online Communities](https://aclanthology.org/2025.naacl-long.78.pdf)
- **Trustworthiness** (constructs) — *measured_by*
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)
- **Refusal** (constructs) — *measured_by*
  > TRUST-ALIGN improves models' refusal capability. Across all 27 configurations, TRUST-ALIGN yields substantial improvements in F1GR. In LLaMA-3-8b, TRUST-ALIGN outperforms FRONT by 23.87% (ASQA), 47.95% (QAMPARI), and 45.72% (ELI5).
  - [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf)

# LoCoMo
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** LOCOMO  

## State of the Field

Across the provided literature, LoCoMo is consistently described as a benchmark designed to assess long-term conversational memory. It is characterized by its use of long dialogue histories, with one paper noting it is "the longest conversation dataset to date" ("SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents"). The benchmark operationalizes this assessment through a question-answering task, as it is explicitly used to measure this behavior. The questions are designed to test various reasoning types, with most sources agreeing on the inclusion of single-hop, multi-hop, and temporal reasoning. Different papers also mention additional categories, such as "commonsense, world knowledge, and adversarial reasoning" ("LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory") or "Open-domain" questions ("Corrupted but Not Broken: Understanding and Mitigating the Negative Impacts of Corrupted Data in Visual Instruction Tuning"). One source specifies that the benchmark includes 50 long-term chat histories. The prevailing usage of LoCoMo in this set of papers is as an instrument for evaluating a model's ability to retain and use information from very long conversations.

## Sources

**[LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)**
> A benchmark for long-term conversational memory that includes 50 long-term chat histories and questions testing various reasoning types like single-hop, multi-hop, and temporal reasoning.

**[SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf) (as "LOCOMO")**
> A long-term conversation benchmark designed to assess conversational memory over very long dialogue histories.

## Relationships

### → LoCoMo
- **Question answering** (behaviors tasks) — *measured_by*
  - [SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf)

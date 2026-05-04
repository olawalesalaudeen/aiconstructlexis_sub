# PrOntoQA
**Type:** Measurement  
**Referenced in:** 14 papers  
**Also known as:** ProntoQA  

## State of the Field

Across the provided literature, PrOntoQA is consistently characterized as a synthetic benchmark designed to evaluate logical reasoning in language models. It is most frequently used to measure `Logical reasoning` and, more specifically, `Logical deduction`, with some sources also connecting it to the measurement of `Commonsense knowledge`. The operationalization is described in two complementary ways: one common framing presents it as a dataset of hierarchical relationships where models must judge the correctness of a multi-step reasoning chain, while another describes it as a benchmark based on first-order logic, formal ontologies, and axioms. In practice, PrOntoQA is used for out-of-distribution (OOD) evaluation, and one paper notes the absence of a publicly available training set. The benchmark is also cited as corroborating the "content effect," a phenomenon where models' logical reasoning performance degrades as premises deviate from real-world knowledge. It is often studied alongside other formal reasoning instruments like ProofWriter.

## Sources

**[Initialization is Critical to Whether Transformers Fit Composite Functions by Reasoning or Memorizing](https://proceedings.neurips.cc/paper_files/paper/2024/file/19c145aaad40927c51f4d10eaa339c20-Paper-Conference.pdf)**
> A synthetic multi-step reasoning dataset where models must determine the correctness of a reasoning chain based on provided hierarchical relationships.

**[Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf) (as "ProntoQA")**
> A synthetic first-order logic reasoning benchmark used for comparison and out-of-distribution evaluation.

## Relationships

### → PrOntoQA
- **Logical reasoning** (constructs) — *measured_by*
  > For logical reasoning, we evaluate the PrOntoQA (Saparov & He, 2022) dataset for logical deduction in a 5-shot setting (Section 4).
  - [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf)
- **Logical deduction** (measurements) — *measured_by*
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)

### Associated with
- **ProofWriter** (measurements)
  - [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)

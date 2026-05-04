# FOLIO
**Type:** Measurement  
**Referenced in:** 21 papers  

## State of the Field

Across the provided literature, FOLIO is consistently characterized as a benchmark dataset for evaluating natural language reasoning grounded in first-order logic (FOL). The predominant use of FOLIO is to assess a model's ability to infer valid conclusions from a set of given premises, a task described as requiring `complex reasoning` or `multi-step reasoning`. A secondary, less common operationalization treats it as a natural language to first-order logic translation task, where evaluation focuses on logical form generation accuracy. The dataset is noted for its composition, containing "human annotations" and "expert-written natural language reasoning instances" paired with corresponding FOL representations. Papers almost universally employ FOLIO as a measurement instrument for the construct of `Logical reasoning`. As one study specifies, its validation split "comprises 203 expert-written natural language reasoning instances and corresponding first-order logic (FOL) annotations" (CRANE: Reasoning with constrained LLM generation).

## Sources

**[GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)**
> A benchmark dataset for evaluating natural language reasoning with first-order logic, requiring models to infer conclusions from given premises.

## Relationships

### → FOLIO
- **Logical reasoning** (constructs) — *measured_by*
  > To evaluate the efficacy of our approach, we use GSM8K (Cobbe et al., 2021), Big-Bench-Hard (BBH) (Suzgun et al., 2022), and FOLIO (Han et al., 2022) benchmark datasets for diverse reasoning tasks in mathematics, commonsense, and logical reasoning. (Section 5.1)
  - [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Morpheme Induction for Emergent Language](https://aclanthology.org/2025.emnlp-main.1285.pdf)

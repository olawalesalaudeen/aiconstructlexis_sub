# Arithmetic
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** ARITHMETIC  

## State of the Field

Across the provided literature, `Arithmetic` is predominantly characterized as a benchmark or dataset for evaluating language models on mathematical tasks. The most common operationalization involves problems with basic arithmetic operations, though the specifics vary between studies; some papers use natural language questions with "addition and subtraction of at most 5-digit numbers," while others employ mathematical expressions with "addition, multiplication, and subtraction" on two-digit numbers. A distinct framing, present in one paper, describes `ARITHMETIC` as a synthetic dataset designed to assess context sensitivity, using a wider range of operators where contexts provide "reassignments of subexpressions to another value resulting in a counterfactual answer." This instrument is explicitly used to measure constructs such as `Mathematical reasoning` and `Commonsense knowledge`. One specific application mentioned is the assessment of "generator-validator consistency," which is instantiated by "randomizing correctness" where a generator is prompted to be correct or incorrect and a validator checks the response.

## Sources

**[Benchmarking and Improving Generator-Validator Consistency of Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfcb583d225b1db8d3ca2331f6785774-Paper-Conference.pdf)**
> Benchmark task involving natural language arithmetic questions (addition and subtraction of up to 5-digit numbers) used to assess generator-validator consistency via correctness randomization.

**[Controllable Context Sensitivity and the Knob Behind It](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9d780d1e2d57d4b70e807608a72501b-Paper-Conference.pdf) (as "ARITHMETIC")**
> A synthetically generated dataset of simple arithmetic expressions where contexts provide reassignments of subexpressions to create counterfactual answers.

## Relationships

### → Arithmetic
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Pay More Attention to Images: Numerous Images-Oriented Multimodal Summarization](https://aclanthology.org/2025.naacl-long.475.pdf)

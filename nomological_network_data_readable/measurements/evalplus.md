# EvalPlus
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** Evalplus  

## State of the Field

Across the surveyed literature, EvalPlus is predominantly characterized as an augmented or upgraded version of the HumanEval and MBPP benchmarks, designed for a more rigorous evaluation of code generation. This enhanced rigor is achieved by substantially increasing the number of test cases for each problem; as one paper notes, "MBPP-Plus expands this by over 35 times the number of test cases." A less frequent framing describes it more broadly as an "evaluation framework" for assessing code generation models, with a specific focus on Python. The primary and most consistently reported use of EvalPlus is to measure the behavior of `Code generation`. It is also used to assess the constructs of `Self-correction` and `Self-reflection`. Operationally, papers use EvalPlus to add "plus test cases" to the base benchmarks, reporting scores for variants like "HumanEval+ (HE+)" and "MBPP+".

## Sources

**[$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf) (as "Evalplus")**
> An evaluation framework used for rigorous assessment of code generation models, particularly for Python.

**[GAPO: Learning Preferential Prompt through Generative Adversarial Policy Optimization](https://aclanthology.org/2025.acl-long.14.pdf)**
> An augmented version of the HumanEval and MBPP benchmarks that significantly increases the number of test cases per problem to provide a more rigorous evaluation.

## Relationships

### → EvalPlus
- **Code generation** (behaviors tasks) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Self-correction** (behaviors tasks) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *measured_by*
  - [SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf)

### Associated with
- **HumanEval** (measurements)
  - [IaC-Eval: A Code Generation Benchmark for Cloud Infrastructure-as-Code Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26b29298ae8acd94bd7e839688e329b-Paper-Datasets_and_Benchmarks_Track.pdf)

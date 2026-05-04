# BFCL
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, BFCL (Benchmark for Function Calling) is consistently described as a benchmark for evaluating the function-calling performance of large language models. Its most prevalent application is to measure Tool use, with multiple papers characterizing it as a "widely adopted" and "comprehensive" instrument for assessing an LLM's ability to invoke functions and tools. The benchmark operationalizes this evaluation through various categories, including "single-turn," "multi-turn," and tasks like "Simple Function, Multiple Function, Parallel Function, and Parallel Multiple Function." Some sources specify that evaluation is based on metrics such as "Abstract Syntax Tree (AST)" and "Executable Function Evaluation (Exec)." While primarily used for general tool use, BFCL is also reported to measure more specific constructs. For instance, one paper uses it to assess Hallucination, and another connects its 'multi-turn' component to the measurement of Memory management, particularly "sustained context management and dynamic decision-making."

## Sources

**[ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)**
> BFCL (Benchmark for Function Calling) is a benchmark used to evaluate LLM function-calling performance across single-turn, multi-turn, hallucination, and executable categories.

## Relationships

### → BFCL
- **Tool use** (behaviors tasks) — *measured_by*
  > The evaluation datasets employed are sourced from open-source collections as reported in the Llama3 paper, which include MMLU(Hendrycks et al., 2021a), IFEval(Zhou et al., 2023), HumanEval(Chen et al., 2021), MBPP(Austin et al., 2021), GSM8K(Cobbe et al., 2021), MATH(Hendrycks et al., 2021b), ARC Challenge (Clark et al., 2018), GPQA (Rein et al., 2023), BFCL(Yan et al., 2024), API-Bank(Li et al., 2023), and MGSM(Shi et al., 2022).
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *measured_by*
  > Accuracy performance comparison on BFCL-v3 leaderboard (updated on 09/20/2024). ... Hallucination (Table 2)
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **Memory management** (constructs) — *measured_by*
  > "the ‘multi-turn’ featuring eight curated API suites and 1000 queries, assessing sustained context management and dynamic decision-making"
  - [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)

### Associated with
- **Tool use** (behaviors tasks)
  - [PAPILLON: Privacy Preservation fromInternet-based and Local Language Model Ensembles](https://aclanthology.org/2025.naacl-long.174.pdf)

# API-Bank
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, API-Bank is consistently used as a benchmark to evaluate the ability of large language models to make tool calls. The most prevalent application of the instrument is to measure the construct of `Tool use`, with one paper also using it as an out-of-distribution benchmark to assess `Generalization`. Papers frequently describe it as a "dialogue-style tool call dataset" that covers both single- and multi-turn scenarios. The evaluation is operationalized by requiring a model to "call predefined local Python tools based on user requirements in the dialogue," with accuracy measured by comparing tool return values to a ground truth. Some sources provide specific details on its structure, noting it contains "314 tool-use dialogues and 753 API calls" and features two distinct levels of difficulty: one for invoking a known API and another for retrieving and then calling an API from multiple candidates. A less common application involves using its "benchmark loss" to monitor agent capabilities during pre-training.

## Sources

**[MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)**
> A benchmark for evaluating the ability of LLMs to make tool calls, covering single- and multi-turn scenarios.

## Relationships

### → API-Bank
- **Tool use** (behaviors tasks) — *measured_by*
  > The evaluation datasets employed are sourced from open-source collections as reported in the Llama3 paper, which include MMLU(Hendrycks et al., 2021a), IFEval(Zhou et al., 2023), HumanEval(Chen et al., 2021), MBPP(Austin et al., 2021), GSM8K(Cobbe et al., 2021), MATH(Hendrycks et al., 2021b), ARC Challenge (Clark et al., 2018), GPQA (Rein et al., 2023), BFCL(Yan et al., 2024), API-Bank(Li et al., 2023), and MGSM(Shi et al., 2022).
  - [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To evaluate the generality of MTU-LLaMA, we measure its performance on the OOD test split of MTU-Bench and two other OOD tool-use benchmarks, i.e., API-Bank (Li et al., 2023) and ToolTalk (Farn & Shin, 2023)... which show strong generalizability of MTU-LLaMA.
  - [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf)
- **Decision-making** (constructs) — *measured_by*
  - [AgentPro: EnhancingLLMAgents with Automated Process Supervision](https://aclanthology.org/2025.emnlp-main.507.pdf)

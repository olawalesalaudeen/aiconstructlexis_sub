# Multi-Agent Debate
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Multi-agent debate, Natural Language Debate  

## State of the Field

Across the surveyed literature, Multi-Agent Debate is most commonly described as a collaborative evaluation setting or reasoning method where multiple language model agents interact to solve a problem. The typical process involves agents engaging in a multi-round dialogue, proposing individual reasoning, and exchanging arguments to reach a consensus answer. While most definitions emphasize collaboration, one paper frames it as a framework where a judge determines the final solution after agents present arguments and counterarguments ("CFinBench: A ComprehensiveChinese Financial Benchmark for Large Language Models"). This procedure is used for several purposes, including measuring team performance, promoting "divergent thinking to overcome biases and rigid reasoning," and alleviating specific model failures. A smaller line of work treats it as a baseline protocol, referred to as "Natural Language Debate," where agents iteratively refine responses by considering peers' outputs to serve as a comparison for other methods. To operationalize this evaluation, papers in this set apply the Multi-Agent Debate procedure to assess model performance on benchmarks such as GSM8k and MMLU.

## Sources

**[CFinBench: A ComprehensiveChinese Financial Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.41.pdf)**
> Framework where multiple agents debate a problem, presenting arguments and counterarguments, with a judge determining the final solution.

**[Automatically Discovering How Misogyny is Framed on Social Media](https://aclanthology.org/2025.naacl-long.609.pdf) (as "Multi-agent debate")**
> Collaborative evaluation setting where two models engage in a dialogue to answer a question, used to measure team performance and order dependence.

**[Communicating Activations Between Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ramesh25a/ramesh25a.pdf) (as "Natural Language Debate")**
> Baseline protocol where multiple LLMs iteratively refine responses by considering peers' outputs in natural language, serving as a state-of-the-art comparison for activation communication.

## Relationships

### Multi-Agent Debate →
- **GSM8k** (measurements) — *measured_by*
  - [Communicating Activations Between Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ramesh25a/ramesh25a.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Communicating Activations Between Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ramesh25a/ramesh25a.pdf)

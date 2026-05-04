# CFBench
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

CFBench is consistently presented as a benchmark for evaluating language models on instruction following, with a prevalent focus on complex instructions containing multiple constraints. Across the provided sources, it is used to measure the behaviors of "Instruction following" and, more specifically, "Complex instruction following." The benchmark is designed to assess model performance across a "comprehensive range of constraint types," which are stated to include categories like format, content, style, and numerical dimensions. One paper characterizes it as a "Single-Instruction Multi-Constraint" benchmark. Another source provides a more specific description, defining it as a "large-scale Chinese Comprehensive Constraints Following Benchmark" with samples from numerous real-life scenarios and NLP tasks. The evaluation procedure is reported to use GPT-4 as a judge and can yield an "ISR score." CFBench is frequently mentioned alongside other complex instruction-following benchmarks such as FollowBench and ComplexBench.

## Sources

**[DAPEV2: Process Attention Score as Feature Map for Length Extrapolation](https://aclanthology.org/2025.acl-long.523.pdf)**
> Complex instruction-following benchmark assessing a model's ability to follow instructions with multiple constraints, evaluated using GPT-4 as a judge.

## Relationships

### → CFBench
- **Complex instruction following** (constructs) — *measured_by*
  > We mainly conduct evaluations on two complex instruction-following benchmarks, CFBench (Zhang et al., 2024) and FollowBench (Jiang et al., 2023), where instructions consist of multiple constraints.
  - [DAPEV2: Process Attention Score as Feature Map for Length Extrapolation](https://aclanthology.org/2025.acl-long.523.pdf)
- **Instruction following** (constructs) — *measured_by*
  > we propose CFBench, a large-scale Chinese Comprehensive Constraints Following Benchmark for LLMs, featuring 1,000 curated samples that cover more than 200 real-life scenarios and over 50 NLP tasks. (Abstract)
  - [NewsInterview: a Dataset and a Playground to EvaluateLLMs’ Grounding Gap via Informational Interviews](https://aclanthology.org/2025.acl-long.1581.pdf)

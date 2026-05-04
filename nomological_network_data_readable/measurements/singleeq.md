# SingleEq
**Type:** Measurement  
**Referenced in:** 15 papers  
**Also known as:** SingleEQ, Single Eq  

## State of the Field

Across the provided literature, SingleEq is consistently used as a benchmark to measure mathematical reasoning. It is most commonly defined as a dataset of math or arithmetic word problems that are solvable with a single equation, though one source describes them as algebraic word problems. A prevalent application of SingleEq is to assess model performance under distribution shift, with several papers explicitly identifying it as an out-of-distribution or out-of-domain test set. Other stated uses for the benchmark include evaluating "basic mathematical comprehension and formulation" and general equation-solving performance. The dataset is frequently employed alongside other arithmetic reasoning benchmarks such as GSM8k, SVAMP, and MultiArith to evaluate these capabilities.

## Sources

**[DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)**
> Dataset of math word problems solvable with a single equation, used to assess performance under distribution shift with simpler reasoning demands.

**[ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf) (as "SingleEQ")**
> Dataset of arithmetic word problems solvable with a single equation, used to evaluate basic mathematical comprehension and formulation.

**[OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf) (as "Single Eq")**
> A benchmark of algebraic word problems that are parsed into equations.

## Relationships

### → SingleEq
- **Mathematical reasoning** (constructs) — *measured_by*
  > we ... test on six different math reasoning datasets: MultiArith (Roy and Roth, 2016), GSM8K (Cobbe et al., 2021), AddSub (Hosseini et al., 2014), AQuA (Ling et al., 2017), SingleEq (Koncel-Kedziorski et al., 2015) and SVAMP (Patel et al., 2021). (Section 4.1)
  - [OccamLLM: Fast and Exact Language Model Arithmetic in a Single Step](https://proceedings.neurips.cc/paper_files/paper/2024/file/3eceb70f47690051d6769739fbf6294b-Paper-Conference.pdf)

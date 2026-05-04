# MAWPS
**Type:** Measurement  
**Referenced in:** 29 papers  
**Also known as:** mawps  

## State of the Field

Across the provided literature, MAWPS is predominantly characterized as a benchmark dataset composed of math word problems. Its most common application is to measure a model's mathematical and arithmetic reasoning abilities, and it is frequently evaluated alongside other arithmetic datasets such as GSM8K and SVAMP. Some papers also use it to assess in-context learning. A distinct operationalization appears in one study, which uses the term MAWPS to refer to the average performance across four separate datasets: SingleEQ, SingleOP, AddSub, and MultiArith. A smaller set of papers frames MAWPS specifically as an out-of-distribution or out-of-domain benchmark to test the generalization of reasoning skills. The problems within the benchmark are described as being at an elementary level and, as one paper notes, it serves to categorize and standardize problems from other datasets.

## Sources

**[Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](https://proceedings.iclr.cc/paper_files/paper/2024/file/b84b9d1fe05c5e74d8f9466f063327a5-Paper-Conference.pdf)**
> A benchmark dataset of math word problems designed to test a model's ability to solve arithmetic problems.

**[Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf) (as "mawps")**
> An out-of-distribution benchmark repository of math word problems.

## Relationships

### → MAWPS
- **Mathematical reasoning** (constructs) — *measured_by*
  > “we validate the efficacy and efficiency of Prompt-OIRL in offline prompt evaluation and optimization through experiments with 3 distinct LLMs, namely GPT-3.5-turbo, LLaMA-2-7B-Chat, and TigerBot-13B-Chat, across 3 arithmetic datasets: GSM8K (Cobbe et al., 2021a), MAWPS (Roy & Roth, 2016), and SVAMP(Patel et al., 2021)”
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  - [SocraticLM: Exploring Socratic Personalized Teaching with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9bae399d1f34b8650351c1bd3692aeae-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)

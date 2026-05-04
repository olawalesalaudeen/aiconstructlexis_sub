# Blocksworld
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** BlocksWorld  

## State of the Field

Across the provided literature, Blocksworld is consistently characterized as a classical planning benchmark used to evaluate the planning capabilities of language models. The task is most commonly defined as rearranging a stack of blocks on a table to achieve a target configuration, often with the constraint of moving only one unstacked block at a time, and is frequently formulated in PDDL. Its primary application is to operationalize and measure the construct of `Planning`, with papers referring to it as a "symbolic planning problem" and a standard benchmark where LLMs are reported to struggle. Some work also uses Blocksworld to specifically assess `Out-of-distribution generalization`, which is operationalized by testing models on problems requiring longer plan lengths than those seen during training. While the "classical planning" framing is prevalent, a smaller set of papers describe it as a "commonsense planning benchmark" for evaluating logical and procedural reasoning, or, less frequently, as an "embodied environment benchmark."

## Sources

**[System 1.x: Learning to Balance Fast and Slow Planning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/605e59e78284907aa4fce5280838def3-Paper-Conference.pdf)**
> A classical planning benchmark that involves rearranging a stack of blocks into a target configuration by moving one unstacked block at a time.

**[Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf) (as "BlocksWorld")**
> A classical planning benchmark task, formulated in PDDL, that involves rearranging blocks on a table to achieve a specified goal configuration.

## Relationships

### → Blocksworld
- **Planning** (constructs) — *measured_by*
  > We evaluate System-1.x Planner on two classical planning tasks that are challenging for LLMs (Valmeekam et al., 2023; Lehnert et al., 2024): (1) Maze Navigation and (2) Blocksworld. (Section 3)
  - [ALPINE: Unveiling The Planning Capability of Autoregressive Learning in Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d848cb2c84f0bba7f1f73cf232734c40-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs) — *measured_by*
  > reports our results on Blocksworld (BW) that studies out-of-distribution generalization to longer plan lengths. (Section 4.1)
  - [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf)

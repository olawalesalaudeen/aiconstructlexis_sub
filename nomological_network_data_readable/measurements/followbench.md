# FollowBench
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

FollowBench is consistently characterized as a benchmark for evaluating instruction-following performance in large language models. The prevailing usage is to assess **complex instruction following**, with papers noting its instructions often consist of "multiple constraints." The benchmark is defined as having "five levels of difficulty" and containing "diverse and open-ended instructions." A recurring feature is its evaluation methodology, which requires strong LLMs like GPT-4 for judgment because the tasks are not verifiable by simple code executions. One paper states this design allows it to "fully examine the generalization... to more general instructions" (Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models). Beyond complex instruction following and **generalization**, FollowBench is also used to measure **conversational ability** as part of a suite of human-preference benchmarks, and is listed as an instrument for assessing **commonsense knowledge**.

## Sources

**[Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)**
> A fine-grained constraint-following benchmark with five levels of difficulty, containing diverse and open-ended instructions that require evaluation by strong LLMs.

## Relationships

### → FollowBench
- **Instruction following** (constructs) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **Complex instruction following** (constructs) — *measured_by*
  > We mainly conduct evaluations on two complex instruction-following benchmarks, CFBench (Zhang et al., 2024) and FollowBench (Jiang et al., 2023), where instructions consist of multiple constraints.
  - [DAPEV2: Process Attention Score as Feature Map for Length Extrapolation](https://aclanthology.org/2025.acl-long.523.pdf)
- **Generalization** (constructs) — *measured_by*
  > FollowBench is a fine-grained constraint-following benchmark with five levels of difficulty. It contains diverse and open-ended instructions requiring evaluation by strong LLMs, such as GPT-4, which can fully examine the generalization of AUTOIF to more general instructions not verifiable by simple code executions. (Section 4).
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **Conversational ability** (constructs) — *measured_by*
  > We select 8 human-preference benchmarks for evaluation of the chat capabilities and reports the average normalized score at the percentage scale. Additionally, due to the high cost of conducting subjective evaluations with a paid API model, we use GPT4o as the Judge Model for main results only, and we judge with the open-source CompassJudger-1-32B (Cao et al., 2024) in ablation study and scaling experiments. (Section 4.1)
  - [TableLoRA: Low-rank Adaptation on Table Structure Understanding for Large Language Models](https://aclanthology.org/2025.acl-long.1091.pdf)

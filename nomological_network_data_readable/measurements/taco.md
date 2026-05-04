# TACO
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

TACO is consistently defined and used as a competitive programming benchmark to evaluate `Code generation`. The provided sources describe it as a dataset focused on "algorithmic code generation" and a tool to measure the generalization of model performance. A recurring feature is its difficulty-stratified test set, which is split into five levels from "easy" to "very-hard." This structure allows researchers to "examine the performance of different prompting strategies across difficulty levels," though some studies use a subset, such as just the "easy and hard split." The benchmark is a collection of problems sourced from other datasets like CodeContests and APPS, as well as various programming contest platforms. In practice, it is used for evaluation in zero-shot settings, and one paper notes the need for data decontamination to ensure valid measurement.

## Sources

**[What Makes Large Language Models Reason in (Multi-Turn) Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fef0802863f47775c3563e18cbba17-Paper-Conference.pdf)**
> A competitive programming benchmark with difficulty-stratified problems used to evaluate code generation across easy to very-hard splits.

## Relationships

### → TACO
- **Code generation** (behaviors tasks) — *measured_by*
  - [Learning How Hard to Think: Input-Adaptive Allocation of LM Computation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf)

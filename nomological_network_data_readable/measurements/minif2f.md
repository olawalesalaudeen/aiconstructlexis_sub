# miniF2F
**Type:** Measurement  
**Referenced in:** 26 papers  
**Also known as:** minif2f, MiniF2F, miniF2F-test  

## State of the Field

Across the provided literature, miniF2F is consistently defined as a benchmark for evaluating automated and formal theorem proving. It is most frequently used to measure the capabilities of `Theorem proving` and `Formal theorem proving`, and is also applied to assess `Autoformalization`, `Generalization`, and `Formal reasoning`. The benchmark is widely described as containing problems derived from high-school and Olympiad-level mathematics competitions like AIME and IMO, with several sources specifying a total of 488 problems split into validation and test sets. One paper characterizes these as "standalone competition problems that do not require external context" (miniCTX: Neural Theorem Proving with (Long-)Contexts). Operationally, models are evaluated on their ability to generate proofs that are verifiable within interactive theorem provers, and the data shows its use with multiple systems including Lean and Isabelle. Some papers refer specifically to a `miniF2F-test` variant for evaluation. While the prevailing usage is for formal-to-formal proving, one paper also mentions its application in "informal-to-formal" evaluation (Llemma: An Open Language Model for Mathematics).

## Sources

**[LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf)**
> Benchmark for formal theorem proving that evaluates models on their ability to generate proofs verifiable by a theorem prover.

**[Learning Formal Mathematics From Intrinsic Motivation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf) (as "minif2f")**
> A benchmark for formal theorem proving, containing problems from olympiad-level mathematics translated into multiple formal systems.

**[ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf) (as "MiniF2F")**
> A benchmark dataset of formal theorem proving problems derived from high-school mathematics competitions, used to evaluate neural theorem proving performance.

**[Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf) (as "miniF2F-test")**
> A benchmark dataset (mini Formal-to-Formal) used for evaluating language model-based theorem provers in the Lean interactive theorem prover.

## Relationships

### → miniF2F
- **Theorem proving** (behaviors tasks) — *measured_by*
  - [LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf)
- **Formal theorem proving** (behaviors tasks) — *measured_by*
  > benchmarks often focus on proving standalone competition problems (e.g., miniF2F (Zheng et al., 2022))
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Autoformalization** (behaviors tasks) — *measured_by*
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > The FORMALALIGN model exhibits consistent performance across four diverse datasets, demonstrating its ability to generalize its autoformalization evaluation capabilities. Particularly noteworthy are the model's AS scores of 66.39% and 64.61% on the challenging MiniF2F-Valid and MiniF2F-Test datasets, respectively.
  - [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Autoformalize Mathematical Statements by Symbolic Equivalence and Semantic Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/6034a661584af6c28fd97a6f23e56c0a-Paper-Conference.pdf)
- **Formal reasoning** (constructs) — *measured_by*
  - [MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)

### Associated with
- **PutnamBench** (measurements)
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)

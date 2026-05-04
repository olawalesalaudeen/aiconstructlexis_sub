# ProofNet
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** ProofNet-test  

## State of the Field

Across the provided literature, ProofNet is predominantly characterized as a benchmark for evaluating theorem proving capabilities, specifically within the Lean proof assistant. It is most commonly used to measure `Theorem proving` and `Formal theorem proving`, with some work also using it to assess `Information retrieval`, `Autoformalization`, and `Generalization` to out-of-domain theorems. The benchmark is consistently described as containing formalized mathematics problems at the college or undergraduate level, which distinguishes it from other instruments like miniF2F, noted to contain high-school level problems. Several sources characterize its problems as "isolated" or "less context-dependent." While its primary role is for evaluation, with papers reporting performance on its test set (`ProofNet-test`), a less common usage frames ProofNet as a "dataset of high-quality mathematical proofs" for collecting training data. One definition also states it is used to assess "advanced mathematical reasoning in LLMs."

## Sources

**[miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf)**
> ProofNet is a Lean theorem-proving benchmark used as a comparison benchmark for isolated or less context-dependent theorem proving.

**[STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf) (as "ProofNet-test")**
> Benchmark consisting of formalized college-level mathematics problems used to assess advanced mathematical reasoning in LLMs.

## Relationships

### → ProofNet
- **Theorem proving** (behaviors tasks) — *measured_by*
  > We conducted sufficient experiments on the widely recognized theorem-proving benchmarks, namely miniF2F (Zheng et al., 2022) and ProofNet (Azerbayev et al., 2023) in Lean. (Section 1)
  - [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf)
- **Autoformalization** (behaviors tasks) — *measured_by*
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > Table 2 demonstrates the results on the ProofNet benchmark.
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
- **Formal theorem proving** (behaviors tasks) — *measured_by*
  > Unlike popular benchmarks (e.g., miniF2F (Zheng et al., 2022), ProofNet (Azerbayev et al., 2023)...) that focus on isolated competition problems
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We also report the performance of the model trained only on LeanWorkbook for 24 iterations, excluding miniF2F-valid and proofnet-valid, demonstrating that the model trained with STP also generalizes to out-of-domain theorems. (Section 4.2)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)

### Associated with
- **PutnamBench** (measurements)
  - [PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf)

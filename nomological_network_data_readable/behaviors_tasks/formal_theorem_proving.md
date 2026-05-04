# Formal theorem proving
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Based on the provided literature, formal theorem proving is defined as the task of producing a correct formal proof for a theorem within an interactive theorem prover, such as Lean. It is frequently positioned as a "testbed for evaluating the reasoning capabilities of large language models (LLMs)," where models are tasked with proving a theorem given access to a repository's code. The field operationalizes and measures this behavior using specific benchmarks. The most commonly cited instruments are miniF2F, which includes "high-school level exercises and competition problems," and ProofNet, which pertains to "undergraduate-level theorems." Both of these benchmarks are characterized as focusing on "standalone" or "isolated" problems. Formal theorem proving is also studied alongside the broader concept of theorem proving, with papers discussing strategies such as "proof-step generation" and "whole-proof generation." Finally, it is associated with mathematical reasoning, though the provided sources do not detail the nature of this relationship.

## Sources

**[miniCTX: Neural Theorem Proving with (Long-)Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b5ef7bcc702a0232b4f1aea2523d0d2-Paper-Conference.pdf)**
> Producing a correct formal proof for a theorem in an interactive theorem prover such as Lean.

## Relationships

### Formal theorem proving →
- **miniF2F** (measurements) — *measured_by*
  > benchmarks often focus on proving standalone competition problems (e.g., miniF2F (Zheng et al., 2022))
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Isabelle** (measurements) — *measured_by*
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **ProofNet** (measurements) — *measured_by*
  > Unlike popular benchmarks (e.g., miniF2F (Zheng et al., 2022), ProofNet (Azerbayev et al., 2023)...) that focus on isolated competition problems
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [People who frequently useChatGPTfor writing tasks are accurate and robust detectors ofAI-generated text](https://aclanthology.org/2025.acl-long.268.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **Theorem proving** (behaviors tasks)
  > Language models in formal theorem proving typically employ two strategies: proof-step generation (Jiang et al., 2022a; Lample et al., 2022; Yang et al., 2023; Wu et al., 2024) and whole-proof generation (Zhao et al., 2023; Wang et al., 2023a). (Section 1)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)

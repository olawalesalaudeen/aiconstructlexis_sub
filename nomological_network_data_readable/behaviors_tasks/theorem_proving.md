# Theorem proving
**Type:** Behavior  
**Referenced in:** 35 papers  
**Also known as:** Proof generation, Algebraic inequality proving, Proof search, Theorem generation, Natural language proof generation, Formal proof generation, Tactic generation, Inequality proving, Proof tactic generation, Proof trajectory generation, Tactic prediction, Proof-step generation, Whole-proof generation, Premise selection, Theorem proof generation, Wordplay formalization, Constructive proof generation, Formal conjecture generation, Theorem proving ability, Theorem-proving ability, Out-of-distribution theorem-proving ability, Theorem-proving capability, Proof generation capability  

## State of the Field

Across the provided literature, theorem proving is most commonly characterized as the observable task of generating a valid, step-by-step proof for a given mathematical statement. This behavior is studied in two primary forms: generating human-readable proofs in natural language and, more frequently, producing proofs in a formal language like Lean that can be automatically verified. The performance of this behavior is operationalized and measured using several benchmarks, including miniF2F, ProofNet, LeanDojo, and PutnamBench. Researchers distinguish between different strategies for this task, such as 'whole-proof generation,' where a model produces the entire proof in a single pass, and interactive 'proof-step generation' or 'tactic generation,' where the model predicts one logical step at a time. The concept also encompasses more specific sub-tasks, including 'premise selection' (retrieving relevant lemmas), 'autoformalization' (translating from natural to formal language), and proving specific types of problems like algebraic inequalities. While the dominant framing is behavioral, a smaller set of papers conceptualizes theorem proving as a latent 'theorem-proving ability' or 'capability' of a model, which is then evidenced by performance on these tasks. Theorem proving is studied alongside related concepts such as mathematical reasoning, symbolic reasoning, and information retrieval. Some work also suggests that training models for proof generation can enhance capabilities in long-horizon planning.

## Sources

**[Proving Theorems Recursively](https://proceedings.neurips.cc/paper_files/paper/2024/file/9de7a49945898da86e062e7029baa284-Paper-Conference.pdf)**
> The observable task of generating a complete and formally verifiable sequence of proof steps that successfully proves a given theorem statement.

**[Lean Workbook: A large-scale Lean problem set formalized from natural language math problems](https://proceedings.neurips.cc/paper_files/paper/2024/file/bf236666a2cc5f3ae05d2e08485efc4c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Proof generation")**
> The observable task of searching for or generating proof tactics and trajectories to complete a formal theorem.

**[Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Algebraic inequality proving")**
> The observable task of generating a valid proof for a given algebraic inequality problem, typically at the Olympiad level.

**[PutnamBench: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition](https://proceedings.neurips.cc/paper_files/paper/2024/file/1582eaf9e0cf349e1e5a6ee453100aa1-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Proof search")**
> A search-based method where each proof attempt involves a distinct search process that can query a neural model multiple times.

**[Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Theorem generation")**
> The observable behavior of autonomously creating new, non-trivial mathematical theorems and their proofs.

**[Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Natural language proof generation")**
> The observable behavior of producing a human-readable, text-based proof for a mathematical problem.

**[Proving Olympiad Inequalities by Synergizing LLMs and Symbolic Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/06b35bf96174d97bae899d915a8b7210-Paper-Conference.pdf) (as "Tactic generation")**
> The observable behavior of producing a specific proof step or transformation (a 'tactic') to apply to a mathematical goal.

**[Proving Olympiad Inequalities by Synergizing LLMs and Symbolic Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/06b35bf96174d97bae899d915a8b7210-Paper-Conference.pdf) (as "Formal proof generation")**
> The behavior of producing a proof in a formal language, such as Lean, that can be automatically verified for correctness by a proof system.

**[Proving Olympiad Inequalities by Synergizing LLMs and Symbolic Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/06b35bf96174d97bae899d915a8b7210-Paper-Conference.pdf) (as "Inequality proving")**
> Deriving valid proofs for algebraic inequality statements, often by transforming the goal through scaling or rewriting.

**[CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf) (as "Proof tactic generation")**
> The observable action of a language model producing a single, one-step proof tactic (a command for a formal prover like Lean) given a current proof state.

**[Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf) (as "Tactic prediction")**
> The behavior of generating the next formal proof step, or "tactic," given the current proof state in an interactive theorem prover.

**[Lean-STaR: Learning to Interleave Thinking and Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5357781c204d4412e44ed9cbcdb08d5-Paper-Conference.pdf) (as "Proof trajectory generation")**
> Sampling sequences of proof states, thoughts, and tactics that form candidate theorem-proving attempts.

**[DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf) (as "Whole-proof generation")**
> A specific strategy for formal proof generation where the model generates the entire proof code from the theorem statement in a single pass, with verification performed only at the end.

**[DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf) (as "Proof-step generation")**
> An interactive strategy for formal proof generation where the model predicts a single subsequent tactic based on an intermediate tactic state, which is then verified before the next step is generated.

**[LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf) (as "Premise selection")**
> The behavior of identifying and retrieving relevant existing theorems, definitions, or lemmas (premises) from a large library to use in a new proof.

**[AI as Humanity’s Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text](https://proceedings.iclr.cc/paper_files/paper/2025/file/e304d374c85e385eb217ed4a025b6b63-Paper-Conference.pdf) (as "Theorem proof generation")**
> The task of generating mathematical proofs for given theorems.

**[A Reasoning-Based Approach to Cryptic Crossword Clue Solving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/andrews25a/andrews25a.pdf) (as "Wordplay formalization")**
> The process of translating a natural language wordplay explanation into a structured, executable format, such as Python code with assert statements.

**[MathConstruct: Challenging LLM Reasoning with Constructive Proofs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/balunovic25a/balunovic25a.pdf) (as "Constructive proof generation")**
> The observable task of generating a mathematical object, such as a set, matrix, or graph, that satisfies a set of specified constraints to prove a mathematical result.

**[STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf) (as "Formal conjecture generation")**
> The observable task of proposing new, related, and solvable mathematical statements (conjectures) based on existing seed theorems and proofs.

**[STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf) (as "Autoformalization")**
> The task of translating mathematical statements and proofs from natural language into a formal, machine-readable language.

**[Learning Formal Mathematics From Intrinsic Motivation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf) (as "Theorem proving ability")**
> The latent capacity of the model to successfully find valid proofs for mathematical statements within a formal system.

**[FVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving](https://proceedings.neurips.cc/paper_files/paper/2024/file/62c6d7893b13a13c659cb815852dd00d-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Theorem-proving ability")**
> A model's latent skill in generating valid, step-by-step proofs for formal statements or lemmas within a proof assistant environment.

**[Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf) (as "Theorem-proving capability")**
> The latent ability of an LLM to generate or complete formal proofs in a proof assistant across theorem-proving tasks and benchmarks.

**[Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf) (as "Out-of-distribution theorem-proving ability")**
> The model's capability to prove theorems that are distributionally distinct from its training data, such as competition-level problems.

**[Automated Proof Generation for Rust Code via Self-Evolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2e20d7402c9985eae4ba924c65370a8-Paper-Conference.pdf) (as "Proof generation capability")**
> The latent ability of an LLM to synthesize proofs that allow a Rust program and specification to be verified by Verus.

## Relationships

### Theorem proving →
- **miniF2F** (measurements) — *measured_by*
  - [LEGO-Prover: Neural Theorem Proving with Growing Libraries](https://proceedings.iclr.cc/paper_files/paper/2024/file/85dca46374dc0f27b4bb5f265b3d17f0-Paper-Conference.pdf)
- **ProofNet** (measurements) — *measured_by*
  > We conducted sufficient experiments on the widely recognized theorem-proving benchmarks, namely miniF2F (Zheng et al., 2022) and ProofNet (Azerbayev et al., 2023) in Lean. (Section 1)
  - [CARTS: Advancing Neural Theorem Proving with Diversified Tactic Calibration and Bias-Resistant Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/69dbaf03f7f37a7ccad9ccc92875a44d-Paper-Conference.pdf)
- **LeanDojo** (measurements) — *measured_by*
  - [Learning Formal Mathematics From Intrinsic Motivation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.pdf)
- **PutnamBench** (measurements) — *measured_by*
  - [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25h/dong25h.pdf)
- **Long-horizon planning** (constructs) — *causes*
  > We begin by training a whole-proof generation model, incorporating several auxiliary tasks to enhance its capabilities in mathematical reasoning and long-horizon planning
  - [DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf)

### → Theorem proving
- **Autoformalization** (behaviors tasks) — *causes*
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Sledgehammer** (measurements)
  - [Magnushammer: A Transformer-Based Approach to Premise Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5f5f22e3e09f4424592ffb06840ab0-Paper-Conference.pdf)
- **Formal theorem proving** (behaviors tasks)
  > Language models in formal theorem proving typically employ two strategies: proof-step generation (Jiang et al., 2022a; Lample et al., 2022; Yang et al., 2023; Wu et al., 2024) and whole-proof generation (Zhao et al., 2023; Wang et al., 2023a). (Section 1)
  - [LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks)
  - [Proving Olympiad Algebraic Inequalities without Human Demonstrations](https://proceedings.neurips.cc/paper_files/paper/2024/file/96f8c5e879c339dae55e6c2188b02a33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense knowledge** (constructs)
  - [Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf)
- **Mathlib** (measurements)
  > Most neural theorem provers based on Lean are primarily trained on Lean's mathematical library, Mathlib.
  - [Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation](https://proceedings.iclr.cc/paper_files/paper/2025/file/43f55776896a2e33239c2954519f605e-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks)
  > “The ability to search is fundamental in many important tasks, such as reasoning ... planning ... and navigation ... Recent work has demonstrated that transformer-based large language models (LLMs) struggle with proof search”
  - [Transformers Struggle to Learn to Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/28d43a64147bf94921041599efdf791d-Paper-Conference.pdf)
- **Abstraction** (constructs)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)
- **Autoformalization** (behaviors tasks)
  - [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf)

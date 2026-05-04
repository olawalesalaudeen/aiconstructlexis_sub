# ProofWriter
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

Across the provided literature, ProofWriter is consistently described as a benchmark or dataset used to evaluate logical and deductive reasoning in language models. It is widely used to operationalize and measure the construct of `logical reasoning`, and is also reported as a measure for `complex reasoning`. The benchmark's task involves logical inference over a set of provided natural language rules and facts to determine if a conclusion can be proven. Structurally, it is described as being composed of "small rule-bases" and, according to some sources, requires models to perform multi-step deduction and generate natural language proofs under a closed-world assumption. Some papers highlight its use in assessing performance on "moderately complex logical structures, such as conjunctions ('and') and disjunctions ('or')" in what one source calls a "knowledge-free setting." One paper notes that ProofWriter is part of a family of benchmarks that also includes Birds-Electricity and ParaRules, and it is frequently studied alongside other reasoning datasets like PrOntoQA and RuleTaker.

## Sources

**[Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf)**
> A deductive reasoning benchmark used to evaluate logical inference over written rules and facts.

## Relationships

### → ProofWriter
- **Logical reasoning** (constructs) — *measured_by*
  > We evaluate CLOVER on seven logical reasoning tasks: AR-LSAT (Zhong et al., 2022), ZebraLogic (Lin et al., 2025), Logic grid puzzle (Puzzle), Symbol interpretation (Symbol), and Logical deduction (Deduction) from the BigBench collaborative benchmark (Srivastava et al., 2022), FOLIO (Han et al., 2022), and ProofWriter (Tafjord et al., 2021). (Section 4.1)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Morpheme Induction for Emergent Language](https://aclanthology.org/2025.emnlp-main.1285.pdf)

### Associated with
- **PrOntoQA** (measurements)
  - [Large Language Models Meet Symbolic Provers for Logical Reasoning Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/862819c227b16f9af64dd6ad6cfdf275-Paper-Conference.pdf)

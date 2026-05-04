# Accuracy
**Type:** Construct  
**Referenced in:** 48 papers  
**Also known as:** Correctness, Task correctness, Prediction correctness, Plot quality, Proof correctness, Functional correctness, Response correctness, Syntactic correctness, Syntax correctness, Formal correctness, Formulation correctness, Synthetic data quality, Token quality, Mathematical rigor, Final Accuracy  

## State of the Field

Across the surveyed literature, the most prevalent usage of "Accuracy" defines it as the degree to which a model's response aligns with factual, logically valid, or expected outcomes for a given task. This general notion is often operationalized through evaluation by other LLMs, such as GPT-4, or by aligning with "human expectations of LLMs’ responses" ("AlpaGasus: Training a Better Alpaca with Fewer Data"). The concept is frequently specialized for particular domains, most notably in code generation, where a distinction is made between "syntactic correctness" (adherence to language grammar) and "functional correctness," which is typically measured by the generated program's ability to pass a set of test cases. Other domain-specific variants include "proof correctness" in theorem proving, "formulation correctness" for mathematical optimization, and "plot quality" in narrative generation. A few authors treat accuracy as a latent property of the model, such as "response correctness," which is described as being inferable from internal model states ("Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation"). A distinct but related line of work applies the concept to training data, defining "data quality" or "token quality" based on the relevance, clarity, and usefulness of examples for improving model performance. One paper introduces a specific evaluation metric called "Final Accuracy," which assesses the correctness of numerical results within a 5% error bound ("DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models").

## Sources

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf) (as "Correctness")**
> The degree to which a generated program is functionally accurate, meaning it produces the expected output for all given inputs as defined by a set of test cases.

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)**
> The degree to which a model's response correctly aligns with factual or logically valid outcomes for a given instruction and input.

**[Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf) (as "Task correctness")**
> The extent to which the model's predicted answer is right for the question after generating a rationale.

**[Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf) (as "Prediction correctness")**
> The latent ability of a model to produce accurate predictions, typically measured by task-specific accuracy metrics.

**[Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf) (as "Data quality")**
> The degree to which a synthetic or real example is relevant, unambiguous, and representative of the target real-world distribution.

**[Agents' Room:  Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf) (as "Plot quality")**
> The degree to which a story has a recognizable and coherent structure with events that move the narrative forward without logical or conceptual inconsistencies.

**[ImProver: Agent-Based Automated Proof Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/4864005cfdea7ebd07086ed1b9846825-Paper-Conference.pdf) (as "Proof correctness")**
> The property that a generated proof is valid and accepted by the proof assistant as establishing the theorem statement.

**[CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair](https://proceedings.iclr.cc/paper_files/paper/2025/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf) (as "Functional correctness")**
> The latent tendency for generated code to satisfy the intended specification and pass functional verification.

**[Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b1cfc8ede53f452cabf8b9cf4eef76-Paper-Conference.pdf) (as "Response correctness")**
> The latent property of a model's generated response being factually or logically correct for a given input, which can be inferred from internal model states.

**[Training Language Models on Synthetic Edit Sequences Improves Code Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43f900f571de6c96a70d5724a0fb565-Paper-Conference.pdf) (as "Syntactic correctness")**
> The degree to which generated code conforms to programming-language syntax and avoids linter-detected errors.

**[DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf) (as "Syntax correctness")**
> The model's capability to generate Verilog code that adheres to the language's grammatical and structural rules, allowing it to be successfully compiled.

**[Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf) (as "Formulation correctness")**
> The degree to which a generated mathematical optimization model accurately and faithfully represents the requirements and constraints of a real-world problem described in natural language.

**[WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf) (as "Synthetic data quality")**
> The latent property of synthetic model outputs that determines their effectiveness in improving downstream model performance during post-training, influenced by factors such as comprehensiveness, clarity, and stylistic coherence rather than raw model capability.

**[Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gulati25a/gulati25a.pdf) (as "Mathematical rigor")**
> The quality of a model's generated solution in terms of being logically airtight, providing justification for claims, and adhering to formal proof standards.

**[Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pang25a/pang25a.pdf) (as "Token quality")**
> The degree to which an individual token carries useful task-specific information for supervised fine-tuning rather than being redundant, uninformative, or harmful.

**[Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/petruzzellis25a/petruzzellis25a.pdf) (as "Formal correctness")**
> The extent to which a generated plan satisfies the formal preconditions and postconditions required for execution.

**[DSVD: Dynamic Self-Verify Decoding for Faithful Generation in Large Language Models](https://aclanthology.org/2025.emnlp-main.1051.pdf) (as "Final Accuracy")**
> Evaluation metric that measures the correctness of the final numerical result produced by the LLM, accepting values within a 5% error bound to account for floating-point precision.

## Relationships

### Accuracy →
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.290.pdf)

### Associated with
- **Helpfulness** (constructs)
  - [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs)
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)

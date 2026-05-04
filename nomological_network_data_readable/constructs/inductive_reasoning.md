# Inductive reasoning
**Type:** Construct  
**Referenced in:** 39 papers  
**Also known as:** Induction, Inductive generalization, Rule induction, Induction copying, Induction pattern matching  

## State of the Field

Across the provided literature, inductive reasoning is most commonly defined as the ability to infer general principles, underlying rules, or high-level abstractions from a limited set of specific observations and then generalize them to novel situations. Several papers describe this as a "core aspect of human intelligence" that allows for robust generalization to new scenarios from only a few examples ("Hypothesis Search: Inductive Reasoning with Language Models"). While this general framing is prevalent, a few papers offer more specific definitions, such as "inductive generalization," which is narrowly defined as reasoning about transitive causal relationships ("Reasoning Elicitation in Language Models via Counterfactual Feedback"). Other work treats induction in the context of specific tasks, like synthesizing information from multiple reasoning paths or identifying and continuing repeated subsequences of tokens. To operationalize and measure this construct, researchers employ a variety of benchmarks, including the visual reasoning task ARC, string and list transformation datasets like SyGuS and List functions, and the program synthesis dataset MBPP. Conceptually, inductive reasoning is frequently studied alongside other forms of logical reasoning, such as deductive and abductive reasoning, and is also associated with hypothesis formulation, rule-based reasoning, and compositionality. One paper also reports that inductive reasoning causes generalization.

## Sources

**[Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)**
> The ability to derive underlying principles or high-level abstractions from a limited set of observations and then generalize them to novel situations.

**[BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Induction")**
> The cognitive ability to infer general principles or patterns from specific instances or facts.

**[Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf) (as "Inductive generalization")**
> The ability to reason about a transitive causal relationship (A → C) after being shown examples of its constituent parts (A → B and B → C).

**[VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf) (as "Rule induction")**
> The ability to infer an underlying abstract rule, operation, or concept from a set of examples rather than being given an explicit instruction.

**[On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf) (as "Induction copying")**
> A synthetic task that requires identifying a subsequence of items within a longer sequence and predicting the item that immediately follows the subsequence.

**[Look Before You Leap: Universal Emergent Mechanism for Retrieval in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad36c2cfc423e75c6d68d751a955b22e-Paper-Conference.pdf) (as "Induction pattern matching")**
> The task of identifying and applying an abstract pattern from examples, such as copying previous tokens.

## Relationships

### Inductive reasoning →
- **List functions** (measurements) — *measured_by*
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
- **SyGuS** (measurements) — *measured_by*
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  > We verify our pipeline’s effectiveness on the ARC visual inductive reasoning benchmark, its variant 1D-ARC, string transformation dataset SyGuS, and list transformation dataset List Functions. (Section 1)
  - [Hypothesis Search: Inductive Reasoning with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a934282496e7b907f5d48d49bb4c9d7d-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **ACRE** (measurements) — *measured_by*
  - [LLMs Can Plan Only If We Tell Them](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf)
- **MBPP** (measurements) — *measured_by*
  > MBPP+ (Liu et al., 2023) expands a program synthesis dataset MBPP (Austin et al., 2021) with 35x more test cases. It covers basic Python programming tasks written by humans. The abundance of test cases avails utilizing MBPP+ as an inductive reasoning dataset (Section 4.1).
  - [CORG: Generating Answers from Complex, Interrelated Contexts](https://aclanthology.org/2025.naacl-long.429.pdf)

### Associated with
- **Logical reasoning** (constructs)
  > In this paper, we focus on four logical reasoning types: deductive, inductive, abductive, and analogical reasoning defined in (Nunes, 2012). (Section 3)
  - [TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks)
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
- **Hypothesis generation** (behaviors tasks)
  - [CORG: Generating Answers from Complex, Interrelated Contexts](https://aclanthology.org/2025.naacl-long.429.pdf)
- **Code generation** (behaviors tasks)
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Compositionality** (constructs)
  - [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf)
- **Rule-based reasoning** (constructs)
  - [MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b782a3462ee9d566291cff148333ea9b-Paper-Conference.pdf)
- **Graph reasoning** (constructs)
  > We combine the complementary strengths of a lightweight KG-specialized LLM with a powerful general LLM to enhance reasoning performance by leveraging their respective graph-based reasoning and inductive reasoning capabilities. (Section 1)
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)

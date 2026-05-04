# Pairwise comparison
**Type:** Behavior  
**Referenced in:** 21 papers  
**Also known as:** Pairwise rating, Pairwise Comparison  

## State of the Field

Across the provided literature, pairwise comparison is predominantly described as a behavior where two model-generated responses are compared to select a winner, loser, or tie. This is frequently operationalized by prompting a model to "judge which of rA and rB is better" for a given instruction, sometimes with the goal of selecting the answer that is "less wrong". This comparative approach is explicitly contrasted with "pointwise rating," where items are judged independently. A less common definition treats it as a task where a model judges a single item's correctness, with the output then compared against human annotations for accuracy. As an evaluation procedure, pairwise comparison is used to measure constructs like `Helpfulness`. The behavior is frequently situated within the `LLM-as-a-judge` paradigm, with one paper describing it as a "typical LLM-as-a-judge method". It is also studied in relation to `Knowledge forgetting`, and one paper reports that it can cause `Uncertainty estimation`. Beyond evaluation, one study notes its use as an inference strategy to "reduce the context size" by comparing all pairs of candidate generations.

## Sources

**[SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)**
> Comparing two model-generated responses and selecting a winner, loser, or tie.

**[From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.86.pdf) (as "Response ranking")**
> Selecting which of two candidate responses is better in a comparative judgment setting.

**[DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf) (as "Pairwise rating")**
> A comparison procedure in which documents are judged relative to one another rather than rated independently.

**[Correcting Negative Bias in Large Language Models through Negative Attention Score Alignment](https://aclanthology.org/2025.naacl-long.504.pdf) (as "Pairwise Comparison")**
> An evaluation task where MLLMs are asked to judge whether a given MCoT is correct or incorrect, with outputs compared to human annotations for accuracy.

## Relationships

### Pairwise comparison →
- **Uncertainty** (constructs) — *causes*
  - [An Empirical Analysis of Uncertainty in Large Language Model Evaluations](https://proceedings.iclr.cc/paper_files/paper/2025/file/82d3258eb58ceac31744a88005b7ddef-Paper-Conference.pdf)

### → Pairwise comparison
- **Helpfulness** (constructs) — *measured_by*
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Knowledge forgetting** (constructs)
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements)
  > We explore two typical LLM-as-a-judge methods: Pairwise comparison (Section 2.1)
  - [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf)

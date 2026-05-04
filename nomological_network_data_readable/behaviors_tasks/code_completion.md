# Code completion
**Type:** Behavior  
**Referenced in:** 12 papers  

## State of the Field

Across the provided literature, code completion is consistently defined as the behavior of generating code continuations from partial inputs, with an emphasis on producing syntactically and functionally correct output. This task is frequently situated within the context of long-context conditions. It is commonly grouped with other generative tasks, appearing alongside summarization, question-answering, creative writing, and translation in discussions of model capabilities. One paper notes that code completion and summarization are considered "more robust" than other tasks. While generally described abstractly, a specific operationalization is provided in one study where the task is used to generate structured output by having a model complete a Python script to add relation edges to a graph.

## Sources

**[CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)**
> Generating syntactically and functionally correct code continuations from partial code inputs, particularly under long-context conditions.

## Relationships

### Code completion →
- **LongBench** (measurements) — *measured_by*
  - [CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf)
- **RepoBench-P** (measurements) — *measured_by*
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a641b8ec86162fc875fb9f6456a542f-Paper-Conference.pdf)
- **TRACE** (measurements) — *measured_by*
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **MultiPL-E** (measurements) — *measured_by*
  - [ObscuraCoder: Powering Efficient Code LM Pre-Training Via Obfuscation Grounding](https://proceedings.iclr.cc/paper_files/paper/2025/file/23ff02034404b65776080cbf7148addd-Paper-Conference.pdf)

### Associated with
- **Text generation** (behaviors tasks)
  - [EvoCodeBench: An Evolving Code Generation Benchmark with Domain-Specific Evaluations](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a059625a6027aca18302803743abaa2-Paper-Datasets_and_Benchmarks_Track.pdf)

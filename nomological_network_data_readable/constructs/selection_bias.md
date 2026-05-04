# Selection bias
**Type:** Construct  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, selection bias is consistently defined as a model's latent tendency to favor certain options in multiple-choice tasks based on their identifiers or position, rather than their content. This phenomenon is described as an "inherent model preference" (Are Large Language Models Chronically Online Surfers?...) that leads models to "rely heavily on answer position, regardless of content" (Understanding Common Ground Misalignment...). The construct is operationalized by observing this systematic favoritism for specific option IDs, such as always picking 'A'. This behavior is framed as a methodological concern, as it can "compromise the robustness of the evaluation." While some work notes that this bias has received attention in LLMs, it is considered "largely unexplored for video-language models (VLMs)." Selection bias is studied alongside `Knowledge forgetting` and `Text generation`, and one paper suggests it has a causal influence on `Faithfulness`.

## Sources

**[PertEval: Unveiling Real Knowledge Capacity of LLMs with Knowledge-Invariant Perturbations](https://proceedings.neurips.cc/paper_files/paper/2024/file/149578235c90954e4f10e40fa181918f-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A latent tendency of a model to favor certain option identifiers (e.g., always picking 'A') regardless of content.

## Relationships

### Associated with
- **Knowledge forgetting** (constructs)
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [NESTFUL: A Benchmark for EvaluatingLLMs on Nested Sequences ofAPICalls](https://aclanthology.org/2025.emnlp-main.1703.pdf)

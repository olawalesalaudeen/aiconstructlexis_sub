# CodeContests
**Type:** Measurement  
**Referenced in:** 16 papers  
**Also known as:** CodeContests dataset, CodeContest  

## State of the Field

Across the provided literature, CodeContests is consistently described as a benchmark dataset used to measure code generation capabilities. The most common framing is that it features "challenging programming problems from code competitions," designed to evaluate the robustness and correctness of generated code. Several papers elaborate on its composition, with one noting it contains problems with "multiple human-written correct and incorrect solutions," and another stating that its test problems are divided into "basic and advanced levels according to their difficulty tags." The task format is specified as generating code from natural language descriptions, with solutions being evaluated against private test cases. The primary and most frequently documented use of CodeContests is to evaluate code generation, often alongside other benchmarks like HumanEval, MBPP, and APPS. A smaller line of work uses it to assess more specific constructs; for instance, one paper suggests that its competition-level problems provide an "ideal testbed to evaluate" algorithmic reasoning. Another paper lists it as a measure for faithfulness, though no specific evidence for this application is provided in the data.

## Sources

**[SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf)**
> A benchmark dataset featuring challenging programming problems from code competitions.

**[Generative Monoculture in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5178b2f2d7c44aa390c0777dc77b3f0c-Paper-Conference.pdf) (as "CodeContests dataset")**
> A competitive programming dataset containing problems with multiple human-written correct and incorrect solutions, used as the source distribution (Dsrc) for the code generation task.

**[Quantifying Semantic Emergence in Language Models](https://aclanthology.org/2025.acl-long.589.pdf) (as "CodeContest")**
> A benchmark dataset for code generation that includes test problems divided into basic and advanced levels based on their difficulty tags.

## Relationships

### → CodeContests
- **Code generation** (behaviors tasks) — *measured_by*
  - [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.189.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://proceedings.iclr.cc/paper_files/paper/2024/file/6111371a868af8dcfba0f96ad9e25ae3-Paper-Conference.pdf)
- **Algorithmic reasoning** (constructs) — *measured_by*
  > Competition-level benchmarks require algorithmic reasoning and thus provide an ideal testbed to evaluate whether CoT techniques can be extended beyond single-turn reasoning. (Section 1)
  - [What Makes Large Language Models Reason in (Multi-Turn) Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fef0802863f47775c3563e18cbba17-Paper-Conference.pdf)
- **Coding** (behaviors tasks) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)

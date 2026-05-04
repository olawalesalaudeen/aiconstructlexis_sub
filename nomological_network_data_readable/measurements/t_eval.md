# T-Eval
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, T-Eval is consistently characterized as a benchmark for evaluating how Large Language Models use external tools and APIs. The most frequently cited purpose is to assess the capabilities of "multi-step decision-making" and "API utilization." This is directly operationalized as a measure of a model's `Planning` ability. The benchmark is also reported to measure `Action execution` and `Commonsense knowledge`. A recurring theme is its design as an out-of-distribution (OOD) benchmark, which is used to test the generalization of these capabilities. As one paper notes, its OOD nature allows researchers to "evaluate the generalization capability of" a model in a zero-shot setting ("WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models").

## Sources

**[WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf)**
> An out-of-distribution benchmark designed to evaluate the multi-step decision-making and API utilization capabilities of LLMs.

## Relationships

### → T-Eval
- **Planning** (constructs) — *measured_by*
  > T-Eval, a widely-used benchmark to evaluate the multi-step decision-making capability of LLMs to utilize APIs... enhances the model's out-of-distribution planning ability.
  - [WorkflowLLM: Enhancing Workflow Orchestration Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d7259031023c5aa463187c4a31c95c8-Paper-Conference.pdf)
- **Action execution** (behaviors tasks) — *measured_by*
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf)

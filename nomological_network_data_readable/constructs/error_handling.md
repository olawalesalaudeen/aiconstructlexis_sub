# Error handling
**Type:** Construct  
**Referenced in:** 10 papers  
**Also known as:** Error correction, Failure recovery, Error tolerance, Error resilience, Error mitigation, Out-of-sync recovery, Performance recovery  

## State of the Field

Across the surveyed literature, error handling is most commonly framed as a latent capability of an agent or model to recover from mistakes and continue toward a goal. This prevailing usage encompasses detecting and rectifying errors in a sequence of thought, adjusting plans after invalid actions, or resynchronizing an internal state with an external environment. As one paper notes, this involves mechanisms like "error identification, recovery loops, self-correction, and fallback strategies" (SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION). Some work treats this as a distinct skill that can be taught, arguing that "error correction can be very different from the original error-free reasoning" (Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems). A few papers present more specialized definitions. One line of work treats it as "Error resilience," the stability of model outputs when computations are approximated (Progressive Mixed-Precision Decoding for Efficient LLM Inference). Another defines it as "Error mitigation," the reduction of incorrect predictions on supervised tasks (To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models). A third specific usage, "Performance recovery," operationalizes the construct by measuring a pruned model's ability to regain capabilities, using benchmarks such as WikiText-2, TruthfulQA, MMLU, ARC-Challenge, and GSM8k. The concept is also studied alongside other model properties like Hallucination, Fairness, and Harmlessness.

## Sources

**[PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3cf318fbeec1126da21e9185ae9908c-Paper-Conference.pdf) (as "Error recovery")**
> The ability to recover from mistakes in perception, skill execution, or partner actions and continue toward task completion.

**[Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/c239bac713017b0b2257b7622bf8aab3-Paper-Conference.pdf) (as "Error correction")**
> The latent skill of identifying and rectifying a mistake within a generated sequence of thought, which can be taught through pretraining.

**[Robotouille: An Asynchronous Planning Benchmark for LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d033407a1a4b7a75cd5f9e4575ad9fb5-Paper-Conference.pdf) (as "Failure recovery")**
> The ability of an agent to effectively adjust its plan and continue making progress toward a goal after encountering an invalid action or unexpected state change.

**[OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf) (as "Error tolerance")**
> The capability of a model to effectively handle and recover from errors, such as by revising its code or adjusting its reasoning based on execution feedback.

**[Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf) (as "Error resilience")**
> The degree to which an LLM's outputs remain stable when its computations are approximated or quantized.

**[SPA-BENCH: A COMPREHENSIVE BENCHMARK FOR SMARTPHONE AGENT EVALUATION](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a75f4dd9679aa4ff80a4e6f0a1dc700-Paper-Conference.pdf)**
> The latent capability of an agent to detect, recover from, and manage execution errors or unexpected situations during task performance.

**[SyncMind: Measuring Agent Out-of-Sync Recovery in Collaborative Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25l/guo25l.pdf) (as "Out-of-sync recovery")**
> The ability of an agent to detect that its internal understanding of a system state has diverged from the true state, diagnose the cause of the mismatch, and update its understanding to resynchronize.

**[To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf) (as "Error mitigation")**
> The ability of a model or intervention to reduce the frequency of incorrect predictions or outputs on supervised tasks.

**[Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf) (as "Performance recovery")**
> The latent ability of a pruned model to regain the functional capabilities of its original dense counterpart after compression, inferred from improvements in metrics like perplexity across tasks and sparsity levels.

## Relationships

### Error handling →
- **WikiText-2** (measurements) — *measured_by*
  > “Following pruning, we evaluate model perplexity on the WikiText-2 dataset”
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  > We evaluate our method on LLMs and show significant perplexity improvements over baselines. This is particularly noteworthy at high sparsity levels, maintaining robust improvements even as high as 70% sparsity. Benchmark results. In Table 3, we evaluate the performance of our method on several benchmark datasets.
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  > We evaluate our method on LLMs and show significant perplexity improvements over baselines. This is particularly noteworthy at high sparsity levels, maintaining robust improvements even as high as 70% sparsity. Benchmark results. In Table 3, we evaluate the performance of our method on several benchmark datasets.
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **MMLU** (measurements) — *measured_by*
  > We evaluate our method on LLMs and show significant perplexity improvements over baselines. This is particularly noteworthy at high sparsity levels, maintaining robust improvements even as high as 70% sparsity. Benchmark results. In Table 3, we evaluate the performance of our method on several benchmark datasets.
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)

### Associated with
- **Harmlessness** (constructs)
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)
- **Truthfulness** (constructs)
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)
- **Hallucination** (behaviors tasks)
  > An emerging line of research explores alternative steering techniques for error-related properties like truthfulness, and hallucination (Li et al., 2023; Qiu et al., 2024; Wang et al., 2025; Bhattacharjee et al., 2024). (Section 1).
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)
- **Fairness** (constructs)
  > While our current focus is error mitigation, by adapting the target signal with labeled inputs, MERA could steer LMs toward diverse specialised objectives (e.g., harmlessness, honesty, and fairness etc). (Section 1).
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)

# BIG-Bench Hard
**Type:** Measurement  
**Referenced in:** 115 papers  
**Also known as:** Big Bench Hard, Big-Bench Hard, Big-Bench-Hard, BigBench-Hard, BIG-Bench-Hard, BIG-Bench-Hard (BBH), BIG-Bench Hard (BBH), Big-bench-hard (BBH), BIG-bench Hard, BBH-Hard, BBH-Object-Count, BigBench-Hard (BBH), BigBenchHard  

## State of the Field

Across the provided literature, BIG-Bench Hard (BBH) is consistently characterized as a measurement instrument composed of a subset of tasks from the larger BIG-Bench suite, selected for being particularly challenging for contemporary language models. The benchmark's most prevalent application is the evaluation of `Reasoning`. Papers use it to assess various facets of this construct, including general, multi-step, logical, and `Symbolic reasoning`, with specific sub-tasks like 'Boolean Expression', 'DATE', and 'Navigate' often cited as examples. A smaller body of work also uses BIG-Bench Hard to measure `Commonsense knowledge`, and in isolated cases, it is used to evaluate `Catastrophic forgetting` and `Faithfulness`. The composition of the benchmark is described with some variation across papers, citing 21, 23, or 27 tasks in formats such as multiple-choice and free-form generation. One definition specifies these are tasks where 'pre-existing LLMs could not outperform human evaluators' ("$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning"). In practice, it is deployed in zero-shot, few-shot, and many-shot in-context learning settings, frequently alongside other common benchmarks like MMLU and GSM8K to provide a comprehensive assessment of model capabilities.

## Sources

**[Knowledge Fusion of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4fd5cfd2e31bebbccfa5ffa354c04bdc-Paper-Conference.pdf) (as "Big-Bench Hard")**
> Subset of challenging tasks from the Beyond the Imitation Game Benchmark (BIG-Bench) that require complex reasoning, used to assess advanced language model capabilities.

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf) (as "BBH")**
> The BIG-Bench Hard benchmark, a subset of challenging tasks from BIG-Bench that were identified as difficult for contemporary language models.

**[Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf)**
> Subset of the BIG-Bench suite focusing on challenging tasks requiring complex reasoning, including DATE and Navigate for symbolic reasoning.

**[Bias Runs Deep: Implicit Reasoning Biases in Persona-Assigned LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e1a87dbb7e954b8d9d6c91f6db771eb-Paper-Conference.pdf) (as "Big-Bench-Hard")**
> A subset of the Beyond the Imitation Game Benchmark (BIG-Bench) containing challenging tasks, used in this study to evaluate the knowledge and reasoning abilities of LLMs.

**[SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf) (as "Big Bench Hard")**
> Subset of the Beyond the Imitation Game benchmark focusing on challenging reasoning tasks requiring multi-step logic.

**[$\textit{Trans-LoRA}$: towards data-free Transferable Parameter Efficient Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/708fdc7911f11585ee7161518e509ae6-Paper-Conference.pdf) (as "BigBench-Hard")**
> A collection of 27 reasoning tasks where pre-existing LLMs could not outperform human evaluators, covering formats like multiple-choice and short response.

**[On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf) (as "BIG-Bench-Hard")**
> A benchmark suite consisting of 23 challenging tasks from the BIG-Bench benchmark that are identified as being difficult for prior language models.

**[CulturePark: Boosting Cross-cultural Understanding in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/77f089cd16dbc36ddd1caeb18446fbdd-Paper-Conference.pdf) (as "BIG-Bench-Hard (BBH)")**
> A benchmark suite comprising 21 challenging tasks designed to assess a model's semantic understanding and logical reasoning capabilities.

**[Self-playing Adversarial Language Game Enhances LLM Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4be7e9867ef163563f4a5e90cec478f-Paper-Conference.pdf) (as "BIG-Bench Hard (BBH)")**
> A benchmark consisting of 23 challenging tasks from the BIG-Bench suite that are difficult for current language models.

**[CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf) (as "Big-bench-hard (BBH)")**
> A suite of challenging benchmark tasks, from which specific symbolic reasoning tasks like Boolean Expression and Dyck Language are drawn.

**[Ensembles of Low-Rank Expert Adapters](https://proceedings.iclr.cc/paper_files/paper/2025/file/e8711daef520be07cb9852390c673de8-Paper-Conference.pdf) (as "BIG-bench Hard")**
> BIG-bench Hard (BBH), a benchmark used to test general language understanding and reasoning.

**[Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf) (as "BBH-Hard")**
> A subset of the BIG-Bench Hard benchmark used to evaluate a model's logical reasoning capabilities on challenging tasks.

**[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf) (as "BBH-Object-Count")**
> A benchmark task used here as one of the general evaluation tasks for zero-shot and in-context performance.

**[Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf) (as "BigBench-Hard (BBH)")**
> A general domain benchmark suite used to assess model capabilities on difficult tasks.

**[Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf) (as "BigBenchHard")**
> BigBenchHard is a challenging reasoning benchmark suite used here via boolean expressions and web of lies subsets.

## Relationships

### → BIG-Bench Hard
- **Reasoning** (constructs) — *measured_by*
  > "MMLU (Hendrycks et al., 2021a) to determine factuality, BBH (Suzgun et al., 2022) to check reasoning abilities"
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  > For out-domain evaluations, BIG-Bench-Hard (Suzgun et al., 2022) and MMLU-Pro (Wang et al., 2024b) are used. These benchmarks encompass challenging subsets of tasks across a wide range of domains and are widely employed for evaluating the capabilities of LLMs. Additionally, they include samples that are more complex than those in our training data, ensuring minimal overlap. We use lm-eval (Gao et al., 2024), available with MIT License, for reporting out-domain evaluation. (Section 5.1.1)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.940.pdf)
- **Symbolic reasoning** (constructs) — *measured_by*
  > Symbolic Reasoning. We use four benchmarks requiring multi-step logical deductions: (1) Boolean Expression from Big-bench-hard (BBH) (Suzgun et al., 2022)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)

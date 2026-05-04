# Hugging Face Open LLM Leaderboard
**Type:** Measurement  
**Referenced in:** 52 papers  
**Also known as:** Huggingface Open Leaderboard, Open LLM Leaderboards, HuggingFace open LLM leaderboard, OpenLLM LeaderBoard, OpenLLM leaderboard, Hugging Face Open LLM Leaderboard v1, Open VLM Leaderboard, OpenLM leaderboard, HuggingFace Open LLM Leaderboard, Open LLM Leaderboard v2, Open-LLM, Open LLM Leaderboard, Open LLM leaderboard, LLM Leaderboard, Open-LLM Leaderboard, Open LLM Benchmarks  

## State of the Field

The Hugging Face Open LLM Leaderboard is consistently characterized across the provided literature as a widely recognized public platform or evaluation suite for ranking and tracking the performance of open-source large language models. It is most commonly used to assess general reasoning and knowledge capabilities, with papers specifically employing it to measure constructs such as `commonsense knowledge`, `mathematical reasoning`, `faithfulness`, and `human preference alignment`. The leaderboard operationalizes these assessments by aggregating model performance across a standardized set of academic benchmarks, frequently including MMLU, ARC, HellaSwag, TruthfulQA, WinoGrande, and GSM8K. The evaluation methodology is often based on few-shot performance, and as one paper notes, it "primarily utiliz[es] accuracy as the evaluation metric" ("Benchmarking LLMs via Uncertainty Quantification"). Several sources state that the leaderboard is based upon the Eleuther AI Language Model Evaluation Harness. Beyond direct model evaluation, the platform also serves as a data source for secondary analyses, such as studying "similarity trends across capability levels" ("Great Models Think Alike and this Undermines AI Oversight") or for "IRT parameter estimation" ("MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs"). Described as a "proving ground for open LLMs" ("SKILL-MIX: a Flexible and Expandable Family of Evaluations for AI Models"), the leaderboard is shown to be an evolving tool, with papers citing different versions such as v1 and v2.

## Sources

**[SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf) (as "Huggingface Open Leaderboard")**
> A suite of benchmarks used to evaluate and rank open-source language models on a variety of downstream tasks.

**[Star-Agents: Automatic Data Optimization with LLM Agents for Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0852b88e96d973bd4e21b673f51621d0-Paper-Conference.pdf) (as "Open LLM Leaderboards")**
> A public platform that ranks and evaluates the performance of various large language models on a standardized set of benchmarks.

**[Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf) (as "HuggingFace open LLM leaderboard")**
> A widely recognized evaluation platform that compares LLM performance, primarily utilizing accuracy as the evaluation metric.

**[RocketEval: Efficient automated LLM evaluation via grading checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/937defc32e8ad2daba66a0e434177ae9-Paper-Conference.pdf) (as "OpenLLM LeaderBoard")**
> An evaluation suite that ranks and tracks the performance of open-source large language models on various benchmarks.

**[Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf) (as "OpenLLM leaderboard")**
> An evaluation suite that aggregates model performance across a standard set of academic benchmarks to measure general reasoning and knowledge capabilities.

**[Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf) (as "OpenLLM Leaderboard")**
> An evaluation suite comprising several standardized benchmarks used to assess the performance of large language models on various tasks.

**[PhyloLM: Inferring the Phylogeny of Large Language Models and Predicting their Performances in Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e28663712d5a3429a98918c3058f7b-Paper-Conference.pdf)**
> An evaluation suite that ranks and tracks the performance of open-access LLMs on a set of standard benchmarks.

**[Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf) (as "Hugging Face Open LLM Leaderboard v1")**
> A public leaderboard that evaluates and ranks open-source large language models on a suite of benchmarks.

**[TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf) (as "Open VLM Leaderboard")**
> An evaluation protocol and leaderboard for assessing the performance of vision-language models on a variety of tasks.

**[Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf) (as "OpenLM leaderboard")**
> A public platform for evaluating and ranking the performance of large language models across a standardized suite of benchmarks.

**[Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf) (as "HuggingFace Open LLM Leaderboard")**
> An evaluation framework that measures LLM performance across a standardized suite of diverse academic benchmarks.

**[Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf) (as "Open LLM Leaderboard v2")**
> An evaluation suite by Hugging Face that assesses LLM performance on a collection of challenging benchmark tasks.

**[Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb7baa005c239c1c7c4098c2a9e00450-Paper-Conference.pdf) (as "Open-LLM")**
> Open-LLM benchmark used to assess the impact of poisoning on benign model performance.

**[SimPER: A Minimalist Approach to Preference  Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf) (as "Open LLM Leaderboard")**
> A public leaderboard by HuggingFace that evaluates large language models on a suite of standardized benchmarks.

**[MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf) (as "Open LLM leaderboard")**
> A public platform that ranks and evaluates large language models on various benchmarks, used in this paper as a source of model evaluation data for IRT parameter estimation.

**[CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf) (as "LLM Leaderboard")**
> Benchmark suite assessing large language models on six key tasks: AI2 Reasoning Challenge, HellaSwag, MMLU, TruthfulQA, Winogrande, and GSM8K, using the Eleuther AI Language Model Evaluation Harness.

**[The Impossibility of FairLLMs](https://aclanthology.org/2025.acl-long.6.pdf) (as "Open-LLM Leaderboard")**
> An evaluation suite that ranks large language models based on their performance across a collection of standardized benchmarks.

**[Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels](https://aclanthology.org/2025.emnlp-main.26.pdf) (as "Open LLM Benchmarks")**
> A suite of standardized benchmarks used to evaluate the performance of large language models across a range of tasks.

## Relationships

### → Hugging Face Open LLM Leaderboard
- **Instruction following** (constructs) — *measured_by*
  - [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e128701ceca0ba03658a305faf39deb-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [On the Impact of Fine-Tuning on Chain-of-Thought Reasoning](https://aclanthology.org/2025.naacl-long.585.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Truthfulness** (constructs) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Language proficiency** (constructs) — *measured_by*
  - [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf)
- **Model merging** (behaviors tasks) — *measured_by*
  - [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf)

### Associated with
- **MMLU** (measurements)
  - [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **ARC** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **GSM8k** (measurements)
  - [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **HellaSwag** (measurements)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **TruthfulQA** (measurements)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **WinoGrande** (measurements)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Uncertainty** (constructs)
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MMLU-Pro** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **BBH** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)
- **MuSR** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)

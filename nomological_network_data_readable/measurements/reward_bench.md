# Reward-Bench
**Type:** Measurement  
**Referenced in:** 77 papers  
**Also known as:** Reward Bench, RewardBench, M-REWARDBENCH  

## State of the Field

Across the provided literature, Reward-Bench is consistently described as a benchmark for evaluating reward models (RMs), and in some cases, generative judges. The prevailing operationalization involves assessing model performance on preference-related tasks using a collection of human-validated data. Several papers specify that this data is structured as "prompt-chosen-rejected triplets," with one source noting it contains approximately 2,985 binary preference tasks. The benchmark is frequently used to measure a range of capabilities, including `Reward Modeling`, `Safety`, `Generalization`, `Commonsense knowledge`, `Mathematical reasoning`, and `LLM-as-a-judge` performance. The most commonly cited evaluation categories within the benchmark are Chat, Safety, and Reasoning. While most sources refer to an English-only version, one paper introduces M-REWARDBENCH, a multilingual variant designed to evaluate RMs across 23 languages. A smaller line of work also utilizes Reward-Bench specifically as an "out-of-distribution (OOD) benchmark" to assess model generalization. In practice, researchers use it to rank RMs by empirical performance and as a complement to other evaluation tools like JudgeBench for tasks requiring difficult reasoning.

## Sources

**[Learning LLM-as-a-Judge for Preference Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/09fd990b19b2e69cc4d20e9969e43f09-Paper-Conference.pdf)**
> A public benchmark for evaluating generative judges on preference-related sub-tasks.

**[RainbowPO: A Unified Framework for Combining Improvements in Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf) (as "Reward Bench")**
> A benchmark designed to evaluate the performance and quality of reward models used in preference optimization.

**[Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf) (as "RewardBench")**
> A benchmark for evaluating reward models on preference-related judgments and reasoning-oriented reward assessment.

**[GraphNarrator: Generating Textual Explanations for Graph Neural Networks](https://aclanthology.org/2025.acl-long.3.pdf) (as "M-REWARDBENCH")**
> A multilingual benchmark for evaluating reward models across 23 languages, assessing chat, safety, reasoning, and translation capabilities through human-validated preference triples.

## Relationships

### → Reward-Bench
- **Safety** (constructs) — *measured_by*
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We employ the primary dataset from RewardBench to evaluate the out-of-domain generalization capabilities of our reward models. (Section 4.3)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Reward prediction** (behaviors tasks) — *measured_by*
  > “We evaluate EURUS-RM-7B on three RM benchmarks, RewardBench (Lambert et al., 2024), AutoJ (Li et al., 2023a), and MT-Bench (Zheng et al., 2023).”
  - [MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1b248453bca182b6138b8c14a75340d-Paper-Conference.pdf)
- **Verbosity** (constructs) — *measured_by*
  - [Post-hoc Reward Calibration: A Case Study on Length Bias](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d50c76fdf75c24ece568fc84a7125fb-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.167.pdf)
- **Reward Modeling** (measurements) — *measured_by*
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **Programming** (behaviors tasks) — *measured_by*
  - [Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.167.pdf)

### Associated with
- **RM-Bench** (measurements)
  - [RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style](https://proceedings.iclr.cc/paper_files/paper/2025/file/6da1eec80095dc5937f7716db15aca4b-Paper-Conference.pdf)
- **JudgeBench** (measurements)
  > Thus, JudgeBench offers a valuable complement to RewardBench for evaluating reward models on difficult tasks requiring reasoning. (Section 4.3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **ArmoRM** (measurements)
  > Additionally, we employ the ArmoRM (Wang et al., 2024b), a multi-dimension reward model known for its state-of-the-art performance on the Reward-Bench benchmark (Lambert et al., 2024).
  - [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf)

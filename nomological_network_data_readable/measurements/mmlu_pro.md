# MMLU-Pro
**Type:** Measurement  
**Referenced in:** 81 papers  
**Also known as:** MMLU-PRO, MMLU Pro, MMLU PRO, MMLU-pro, MMLU Pro-MATH  

## State of the Field

Across the provided literature, MMLU-Pro is consistently characterized as a more robust, challenging, and enhanced version of the MMLU benchmark. One paper specifies that it "enhances its predecessor through more complex reasoning questions, expanded answer choices, and reduction of dataset noise" (POSITIONBIASMITIGATESPOSITIONBIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation). The benchmark is most frequently used to assess various forms of knowledge, including "general knowledge," "commonsense knowledge," "domain-specific knowledge," and "knowledge retention" across 14 domains such as Biology, Business, and Law. Alongside knowledge, it is also widely employed to evaluate "reasoning-oriented performance," "complex reasoning," and "multi-hop reasoning." A recurring application is to test model robustness, for instance, by using it for out-of-distribution "generalization ability" evaluation or to validate that performance on text tasks is not degraded after modifications like adding a vision modality. MMLU-Pro is also situated within larger evaluation frameworks, appearing as a task on the Hugging Face Open LLM Leaderboard and used for the "Knowledge" category in JudgeBench. A specialized subset, "MMLU Pro-MATH," is also noted for focusing specifically on professional-level mathematics problems.

## Sources

**[Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf) (as "MMLU-PRO")**
> A multi-task language understanding benchmark used here to evaluate reasoning-oriented performance on the UltraFeedback-finetuned models.

**[Can LLMs Understand Time Series Anomalies?](https://proceedings.iclr.cc/paper_files/paper/2025/file/05774fb74e863308c4b460c9f49f6918-Paper-Conference.pdf)**
> A benchmark used to validate that adding a vision modality to an LLM does not degrade its performance on text-based tasks.

**[How to Evaluate Reward Models for RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e01083b381b4865919b4915ef32e3d2-Paper-Conference.pdf) (as "MMLU Pro")**
> A verifiable benchmark used in PPE to assess a model's general knowledge.

**[Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf) (as "MMLU PRO")**
> A more robust and challenging version of the Massive Multitask Language Understanding (MMLU) benchmark.

**[DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf) (as "MMLU-pro")**
> A scientific benchmark used in the paper’s out-of-distribution evaluation.

**[ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf) (as "MMLU Pro-MATH")**
> A subset of the MMLU benchmark focused on professional-level mathematics problems.

## Relationships

### → MMLU-Pro
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > we evaluate unsupervised ICL on the GSM8K dataset that requires reasoning capabilities and on the MMLU(-Pro) dataset that covers broad knowledge of different disciplines. (Section 5.1)
  - [HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Q-Adapter: Customizing Pre-trained LLMs to New Preferences with Forgetting Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ebfb4ec1926fc6409df3bcf7ce957e8-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  > Additionally, we evaluate generative performance on complex reasoning tasks, such as GSM8K (Cobbe et al., 2021) with 5-shot prompting and MMLU-Pro Engineering/Law (Wang et al., 2024a) with zero-shot chain-of-thought.
  - [Lexico: Extreme KV Cache Compression via Sparse Coding over Universal Dictionaries](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25ae/kim25ae.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Condor: EnhanceLLMAlignment with Knowledge-Driven Data Synthesis and Refinement](https://aclanthology.org/2025.acl-long.1092.pdf)
- **Domain-specific knowledge** (constructs) — *measured_by*
  - [SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cb240de90aa20207db944c6c88a7cc0-Paper-Conference.pdf)
- **Multitask language understanding** (constructs) — *measured_by*
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Language Models Predict Empathy Gaps Between Social In-groups and Out-groups](https://aclanthology.org/2025.naacl-long.612.pdf)
- **Catastrophic forgetting** (behaviors tasks) — *measured_by*
  > On the knowledge-intensive benchmarks (i.e., WikiBench, MMLU, and MMLU-Pro), Genius can maintain the performances of the base LLMs, avoiding catastrophic forgetting after post-training (Section 3.2).
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.940.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Classification** (behaviors tasks) — *measured_by*
  > The classification benchmarks include ARC-Challenge (Clark et al., 2018), MMLU-Pro (Wang et al., 2024), and MixEval (Ni et al., 2024). (Section 5.2)
  - [A Unified Approach to Routing and Cascading for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dekoninck25a/dekoninck25a.pdf)
- **Task generalization** (constructs) — *measured_by*
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Multi-hop reasoning** (constructs) — *measured_by*
  - [POSITIONBIASMITIGATESPOSITIONBIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.79.pdf)

### Associated with
- **JudgeBench** (measurements)
  > We use MMLU-Pro for the Knowledge category. (Section 3)
  - [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements)
  - [On a Connection Between Imitation Learning and RLHF](https://proceedings.iclr.cc/paper_files/paper/2025/file/acf4a08f67724e9d2de34099f57a9c25-Paper-Conference.pdf)

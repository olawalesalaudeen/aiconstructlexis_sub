# Truthfulness
**Type:** Construct  
**Referenced in:** 26 papers  

## State of the Field

Based on the provided literature, Truthfulness is defined as the degree to which a model avoids producing false or misleading information. The definition places a particular emphasis on a model's performance when confronted with questions specifically designed to elicit misconceptions. This construct is operationalized through evaluation on specialized benchmarks. For instance, the TruthfulQA-DE dataset is explicitly cited as a tool to "evaluate model truthfulness." The design of this benchmark, which contains questions across numerous categories, is described as being tailored to assess how models handle misconceptions, directly reflecting the core focus of the construct's definition.

## Sources

**[Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking](https://aclanthology.org/2025.acl-long.111.pdf)**
> The degree to which the model avoids generating false or misleading information, particularly when faced with questions designed to elicit misconceptions.

## Relationships

### Truthfulness →
- **TruthfulQA** (measurements) — *measured_by*
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
- **OpenLLM Leaderboard** (measurements) — *measured_by*
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **UltraFeedback** (measurements) — *measured_by*
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
- **HaluEval** (measurements) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Human annotation study** (measurements) — *measured_by*
  - [Causally Modeling the Linguistic and Social Factors that Predict Email Response](https://aclanthology.org/2025.naacl-long.595.pdf)
- **SimpleQA** (measurements) — *measured_by*
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **BLEURT** (measurements) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **FINTRUST** (measurements) — *measured_by*
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **PLLuM-Align** (measurements) — *measured_by*
  - [REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Truthfulness
- **Alignment** (constructs) — *causes*
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  - [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://proceedings.neurips.cc/paper_files/paper/2024/file/5acd3c628aa1819fbf07c39ef73e7285-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Human preference alignment** (constructs) — *causes*
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Sycophancy** (constructs)
  - [Causally Motivated Sycophancy Mitigation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a52b0d191b619477cc798d544f4f0e4b-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Informativeness** (constructs)
  - [Subtle Errors in Reasoning: Preference Learning via Error-injected Self-editing](https://aclanthology.org/2025.acl-long.1507.pdf)
- **Open-ended question answering** (behaviors tasks)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Coherence** (constructs)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Human preference alignment** (constructs)
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Error handling** (constructs)
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)

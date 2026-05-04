# DROP
**Type:** Measurement  
**Referenced in:** 33 papers  

## State of the Field

Across the provided literature, DROP is consistently characterized as a reading comprehension benchmark designed to measure discrete reasoning over paragraphs. The required reasoning operations are frequently specified as numerical or logical tasks such as addition, counting, sorting, and arithmetic. Reflecting this focus, papers most commonly use DROP to evaluate the constructs of `Reasoning`, `Reading comprehension`, and `Commonsense knowledge`. It is also used to assess `Question answering` and, more specifically, `Discrete reasoning`. A smaller set of studies employs DROP to measure `Mathematical reasoning`, general `Understanding`, and a model's `Generalization` ability in out-of-distribution contexts. The data indicates that DROP is a "widely-used public" benchmark, often appearing in evaluation suites alongside other instruments. One paper also reports using a "decontextualized" version of the dataset for experimental evaluation.

## Sources

**[AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf)**
> A reading comprehension benchmark that requires discrete reasoning over paragraphs, such as addition, counting, or sorting.

## Relationships

### → DROP
- **Reading comprehension** (constructs) — *measured_by*
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  > DROP tests models’ abilities to perform complex reasoning over paragraphs, including approximately 96,000 questions containing numerical operations and logical inference.
  - [MMRC: A Large-Scale Benchmark for Understanding Multimodal Large Language Model in Real-World Conversation](https://aclanthology.org/2025.acl-long.1097.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Discrete reasoning** (constructs) — *measured_by*
  - [QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  > Besides, we also provide more experimental results on the decontextualized versions of a subset of DROP (Dua et al., 2019) and IIRC (Ferguson et al., 2020) in Appendix D.1. (Section 5.1)
  - [Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [LeTS: Learning to Think-and-Search via Process-and-Outcome Reward Hybridization](https://aclanthology.org/2025.emnlp-main.258.pdf)
- **Generalization** (constructs) — *measured_by*
  > For the OOD evaluation, we test each approach’s generalization ability on Deepmind Math (Saxton et al., 2019), MMLU-pro (Wang et al., 2024), strategyQA (Geva et al., 2021), and DROP (Dua et al., 2019). (Section 3.1)
  - [DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e5d6f9ac33ba9349ba7b2be9f21bad9-Paper-Conference.pdf)
- **Understanding** (constructs) — *measured_by*
  - [WET: Overcoming Paraphrasing Vulnerabilities in Embeddings-as-a-Service with Linear Transformation Watermarks](https://aclanthology.org/2025.acl-long.1123.pdf)
- **General reasoning** (constructs) — *measured_by*
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)

# AlpacaEval 2
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, AlpacaEval 2 is consistently characterized as a benchmark for evaluating instruction-following capabilities in language models, with some papers specifying it as a "general" or "open-ended" instruction-following benchmark. It is described as containing 805 questions or instructions, which are sourced from user interactions or other datasets. The evaluation procedure common to all descriptions involves using a GPT-based judge, such as GPT-4, to perform an automatic pairwise comparison between a model's output and a baseline response. The primary metrics reported from this evaluation are the "win rate" and the "length-controlled win rate (LC)". The most frequently stated application of AlpacaEval 2 is to measure `Instruction following`, and it is also described as one of the "widely accepted alignment benchmarks" used to assess `Human preference alignment`. The provided data also shows it is used to evaluate a broader set of constructs including `Commonsense knowledge`, `Conversational ability`, and `Faithfulness`.

## Sources

**[DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)**
> General instruction-following benchmark using 805 questions evaluated via length-controlled win rate with GPT-based judges.

## Relationships

### → AlpacaEval 2
- **Instruction following** (constructs) — *measured_by*
  > “AlpacaEval 2 (Li et al., 2023), Arena-Hard (Li et al., 2024b) and WildBench v2 (Lin et al., 2024) are general instruction-following benchmarks.”
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [Earlier Tokens Contribute More: Learning Direct Preference Optimization From Temporal Decay Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd9b4a28fb9eebe0430c3312a4898a41-Paper-Conference.pdf)
- **Conversational ability** (constructs) — *measured_by*
  - [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://proceedings.neurips.cc/paper_files/paper/2024/file/e099c1c9699814af0be873a175361713-Paper-Conference.pdf)
- **Alignment** (constructs) — *measured_by*
  - [DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Harnessing and Evaluating the Intrinsic Extrapolation Ability of Large Language Models for Vehicle Trajectory Prediction](https://aclanthology.org/2025.naacl-long.224.pdf)
- **Open-ended instruction following** (behaviors tasks) — *measured_by*
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Data Whisperer: Efficient Data Selection for Task-SpecificLLMFine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1136.pdf)

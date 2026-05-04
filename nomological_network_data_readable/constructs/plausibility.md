# Plausibility
**Type:** Construct  
**Referenced in:** 14 papers  

## State of the Field

Across the surveyed literature, plausibility is most commonly characterized as a quality of model-generated explanations or rationales. The prevailing definition describes it as an explanation's relevance to an input question and its support from established, language-based facts. A related line of work defines it as a rationale making "logical, common, or factual sense on its own" ("Tailoring Self-Rationalizers with Multi-Reward Distillation"), while other papers focus on user perception, framing it as how "intuitive, coherent, and convincing" an explanation is to an end user ("SenDetEX..."). A less frequent application of the term describes the "perceived credibility and reasonableness" of a generated hypothesis as judged by experts. To measure this construct, researchers employ `Human evaluation`, `LLM-based evaluation`, and the `BLiMP` benchmark. Plausibility is frequently studied in relation to `Faithfulness`, with one paper noting a "trade-off between plausibility and faithfulness." It is also associated with `Interpretability and explainability` and is sometimes used as a metric to evaluate it. Some work distinguishes implausibility from hallucination, where the former refers to a lack of informativeness and the latter to contradicting facts.

## Sources

**[RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)**
> The quality of a model's generated explanation being relevant to the input question and supported by established, language-based facts.

## Relationships

### Plausibility →
- **Human evaluation** (measurements) — *measured_by*
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1372.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **BLiMP** (measurements) — *measured_by*
  - [The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1769.pdf)

### → Plausibility
- **Interpretability and explainability** (constructs) — *measured_by*
  - [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.539.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [SenDetEX: Sentence-LevelAI-Generated Text Detection for Human-AIHybrid Content via Style and Context Fusion](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **Interpretability and explainability** (constructs)
  - [Is the MMI Criterion Necessary for Interpretability? Degenerating Non-causal Features to Plain Noise for Self-Rationalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d53d51e88d92d3723755f6d425bc513b-Paper-Conference.pdf)

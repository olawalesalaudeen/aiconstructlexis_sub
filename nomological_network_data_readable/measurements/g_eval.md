# G-Eval
**Type:** Measurement  
**Referenced in:** 17 papers  
**Also known as:** G-EVAL  

## State of the Field

Across the provided literature, G-Eval is predominantly characterized as an automated evaluation protocol that uses a large language model, frequently GPT-4, to assess the quality of generated text. The most common operationalization involves the evaluator LLM providing Likert-scale scores, typically from 1 to 5, based on a given prompt. Several sources specify that this process incorporates Chain-of-Thought (CoT) prompting, with one paper describing it as an "auto-CoT prompting framework" where the model evaluates claims step-by-step. A less common description, found in one paper, frames G-Eval as a method that "refines scoring granularity using a logit-weighted average of score tokens." The instrument is used to measure a wide array of constructs, including Faithfulness, Linguistic quality, Relevance, Completeness, and Naturalness. It is described as a "commonly used" framework, is studied alongside human evaluation, and has been adapted for specialized domains like chess commentary. One paper notes a potential limitation, stating that "the evaluation can be largely limited by the performance of the evaluator LLM itself."

## Sources

**[Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data](https://aclanthology.org/2025.naacl-long.38.pdf)**
> An automated evaluation protocol that uses a large language model (like GPT-4) to provide Likert-scale scores (1-5) for summary quality based on a given prompt.

**[Token-based Decision Criteria Are Suboptimal in In-context Learning](https://aclanthology.org/2025.naacl-long.279.pdf) (as "G-EVAL")**
> An auto-CoT prompting framework for natural language generation evaluation that uses chain-of-thought reasoning to generate evaluation steps, used here as a baseline for LLM-based assessment.

## Relationships

### → G-Eval
- **Fluency** (constructs) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Coherence** (constructs) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Relevance** (constructs) — *measured_by*
  - [Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation](https://aclanthology.org/2025.emnlp-main.1683.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **Completeness** (constructs) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **Ambiguity handling** (constructs) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **Naturalness** (constructs) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Empathy** (constructs) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Usability** (constructs) — *measured_by*
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Engagingness** (constructs) — *measured_by*
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1069.pdf)
- **Memorization** (constructs) — *measured_by*
  - [Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning](https://aclanthology.org/2025.emnlp-main.1069.pdf)

### Associated with
- **Human evaluation** (measurements)
  - [SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  > Furthermore, we report G-EVAL (Liu et al., 2023a), an auto-CoT prompting framework, and the current state-of-the-art in NLG evaluation. (Section 5.1)
  - [Token-based Decision Criteria Are Suboptimal in In-context Learning](https://aclanthology.org/2025.naacl-long.279.pdf)

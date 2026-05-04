# Verbalized confidence
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Verbal Confidence, Verbalization  

## State of the Field

Across the provided literature, verbalized confidence is consistently described as a measurement technique that involves directly prompting a large language model to self-report its confidence. This method, also referred to as 'Verbal Confidence' or 'Verbalization', is operationalized by asking the model to express its confidence in its own answer or judgment, sometimes as a scalar value, through what one paper calls 'well-designed prompts' (Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation). The definitions characterize it as a 'black-box self-evaluation procedure' and a 'baseline confidence measure'. The primary purpose of this procedure is to obtain a model's self-evaluated confidence level for a given output. In practice, verbalized confidence is used as a method to measure `Hallucination`. It is also studied in relation to `Instruction following`. The definitions and descriptions provided are in strong agreement, all centering on the direct elicitation of a confidence score from the model itself.

## Sources

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf)**
> A baseline confidence measure obtained by directly prompting an LLM judge to express its confidence in its own judgment as a scalar value.

**[Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b0b1cfc8ede53f452cabf8b9cf4eef76-Paper-Conference.pdf) (as "Verbal Confidence")**
> A black-box self-evaluation procedure that asks the model to express confidence in its own answer.

**[HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf) (as "Verbalization")**
> An evaluation protocol that measures a model's confidence by directly prompting it to self-report its confidence level.

## Relationships

### → Verbalized confidence
- **Hallucination** (behaviors tasks) — *measured_by*
  - [From Scores to Steps: Diagnosing and ImprovingLLMPerformance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.549.pdf)

### Associated with
- **Instruction following** (constructs)
  - [LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses](https://proceedings.iclr.cc/paper_files/paper/2024/file/3815d62554efad0878fad6c1c30ffda0-Paper-Conference.pdf)

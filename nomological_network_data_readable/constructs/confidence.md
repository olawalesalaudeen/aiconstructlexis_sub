# Confidence
**Type:** Construct  
**Referenced in:** 17 papers  
**Also known as:** Confidence capability  

## State of the Field

Across the surveyed literature, Confidence is most commonly framed as a model's internal assessment of its certainty regarding a generated output. This assessment is frequently used to determine a subsequent action, such as whether to provide a definitive answer, abstain from deciding, or seek more information. For instance, it is used to decide when a model should refrain from making diagnostic decisions or to assess whether an LLM judge's evaluation is likely to align with human preference. The construct is operationalized in varied ways; some work measures it by the consistency of model outputs, such as "the proportion of responses that affirm the correct causal relation" across multiple generations, while other approaches compute it from token probabilities. A distinct, less prevalent framing appears in the context of self-correction, where "confidence capability" is defined as the tendency to maintain already correct answers during the correction process. Confidence is also noted as being related to the construct of Self-reflection.

## Sources

**[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf)**
> The model's internal assessment of its certainty in providing a correct answer, used to decide whether to answer or seek more information.

**[Read it in Two Steps: Translating Extremely Low-Resource Languages with Code-Augmented Grammar Books](https://aclanthology.org/2025.acl-long.203.pdf) (as "Confidence capability")**
> The latent tendency of an LLM to maintain correct answers during self-correction, reflecting its internal certainty in initially generated correct responses.

## Relationships

### Associated with
- **Self-reflection** (behaviors tasks)
  - [BatchPrompt: Accomplish more with less](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d8c01de2dc698c54201c1c7d0b86974-Paper-Conference.pdf)

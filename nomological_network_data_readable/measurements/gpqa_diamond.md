# GPQA-Diamond
**Type:** Measurement  
**Referenced in:** 20 papers  
**Also known as:** GPQADiamond, GPQA Diamond  

## State of the Field

Across the provided literature, GPQA-Diamond is consistently characterized as an expert-level benchmark for evaluating advanced reasoning in STEM fields. It is defined as a set of 198 graduate-level, multiple-choice questions spanning biology, physics, and chemistry, and is sometimes identified as a challenging subset of the GPQA benchmark. The most common construct this instrument is used to measure is `Commonsense knowledge`, followed by `Mathematical reasoning`. A smaller set of studies uses GPQA-Diamond to operationalize other capabilities, including `Problem-solving`, `Complex reasoning`, and `Long Chain-of-Thought reasoning`. One paper specifically frames it as a tool for assessing zero-shot `Generalization`, describing it as an 'unseen task' to test model performance. The definitions reinforce its use for 'deep reasoning,' and evaluation is reported to be conducted using pass@1 accuracy.

## Sources

**[VisualWebInstruct: Scaling up Multimodal Instruction Data through Web Search](https://aclanthology.org/2025.emnlp-main.73.pdf)**
> Scientific reasoning benchmark containing 198 graduate-level multiple-choice questions across biology, physics, and chemistry.

**[Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence inLLMs](https://aclanthology.org/2025.emnlp-main.131.pdf) (as "GPQADiamond")**
> Challenging subset of GPQA used to assess zero-shot generalization on unseen, expert-level reasoning tasks.

**[Data Whisperer: Efficient Data Selection for Task-SpecificLLMFine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1136.pdf) (as "GPQA Diamond")**
> Expert-level question answering benchmark in STEM fields requiring deep reasoning, evaluated using pass@1 accuracy.

## Relationships

### → GPQA-Diamond
- **Reasoning** (constructs) — *measured_by*
  - [Data Whisperer: Efficient Data Selection for Task-SpecificLLMFine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1136.pdf)
- **Mathematical reasoning** (constructs) — *measured_by*
  - [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.375.pdf)
- **Problem-solving** (behaviors tasks) — *measured_by*
  - [La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cj/liu25cj.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [In-Context Learning Boosts Speech Recognition via Human-like Adaptation to Speakers and Language Varieties](https://aclanthology.org/2025.emnlp-main.220.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [Morpheme Induction for Emergent Language](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **Generalization** (constructs) — *measured_by*
  > we use GSM8K and MATH500, along with an additional dataset to assess how well our transferring-then-finetuning approach generalizes to the unseen task GPQADiamond (Rein et al., 2024). (Section 5.1).
  - [Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence inLLMs](https://aclanthology.org/2025.emnlp-main.131.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)

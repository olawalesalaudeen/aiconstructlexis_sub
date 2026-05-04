# Hypothesis formulation
**Type:** Behavior  
**Referenced in:** 6 papers  
**Also known as:** Zero-shot hypothesis generation, Hypothesis testing  

## State of the Field

Across the provided literature, hypothesis formulation is most commonly described as the behavior of generating testable scientific hypotheses or explanatory statements based on background knowledge, data patterns, or observations. This behavior is frequently operationalized by prompting language models to produce a set of hypotheses, sometimes using in-context demonstrations, as noted in one study (CIFLEX). A specific variant, "zero-shot hypothesis generation," is also explored, where the model generates hypotheses relying only on its internal knowledge without demonstrations. The field measures this capability using dedicated benchmarks like Researchbench, which covers "inspiration retrieval, hypothesis formulation, and ranking," and datasets for specific domains like chemistry and social science. A less common framing treats the concept as "hypothesis testing," a cyclical process where an agent formulates hypotheses about puzzle solutions, executes actions to validate them, and analyzes the outcomes. The generated outputs are sometimes expected to be "literature-grounded hypotheses with clear provenance" (EasyRec). Hypothesis formulation is studied alongside concepts such as inductive reasoning, causal inference, and self-correction. Additionally, commonsense understanding is reported to influence this behavior.

## Sources

**[FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.476.pdf) (as "Hypothesis generation")**
> The task of formulating and generating scientific hypotheses based on provided background knowledge or observations.

**[CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf) (as "Zero-shot hypothesis generation")**
> The observable behavior of generating hypotheses without any in-context demonstrations, relying solely on the model's internal knowledge.

**[EasyRec: Simple yet Effective Language Models for Recommendation](https://aclanthology.org/2025.emnlp-main.895.pdf)**
> Designing testable scientific hypotheses based on identified research ideas or data patterns.

**[ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming](https://aclanthology.org/2025.emnlp-main.810.pdf) (as "Hypothesis testing")**
> Executing actions to validate or invalidate generated hypotheses about puzzle solutions, followed by outcome analysis to refine future attempts.

# Representational stability
**Type:** Construct  
**Referenced in:** 3 papers  
**Also known as:** Representation stability, Instance-level stability  

## State of the Field

Across the provided literature, representational stability is most commonly defined as the robustness or consistency of a model's internal representations when subjected to perturbations in the input. A distinct framing, termed 'instance-level stability', focuses more on output consistency, defining it as the degree to which an accelerated model produces the same predictions as its original counterpart for the same inputs. The construct is typically operationalized by applying 'targeted, systematic perturbations' and then measuring the effect on a model's 'internal hidden state representations'. For example, one paper introduces a method, CCPS, that probes these internal states, hypothesizing that greater stability correlates with higher LLM confidence. This approach is presented as an 'efficient alternative to methods relying on multiple generation passes for consistency checking'. In the context of model acceleration, this stability is investigated to ensure accelerated models maintain 'behavioral fidelity'. The concept is also studied alongside `Faithfulness`.

## Sources

**[Towards Faithful Natural Language Explanations: A Study Using Activation Patching in Large Language Models](https://aclanthology.org/2025.emnlp-main.530.pdf)**
> The robustness of a model's internal hidden state representations against targeted, systematic perturbations.

**[2025.emnlp-main.530.checklist](https://aclanthology.org/attachments/2025.emnlp-main.530.checklist.pdf) (as "Representation stability")**
> The consistency of a model's internal representations when subjected to small perturbations in the input, reflecting the robustness of its semantic understanding.

**[ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.425.pdf) (as "Instance-level stability")**
> The degree to which an accelerated model produces the same predictions for the same inputs as its original, unaccelerated counterpart.

## Relationships

### Associated with
- **Reliability** (constructs)
  - [ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.425.pdf)
- **Behavioral fidelity** (constructs)
  > Low DR and NDR values signify that an accelerated VLM maintains behavioral fidelity and reliability. (Section 1)
  - [ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.425.pdf)

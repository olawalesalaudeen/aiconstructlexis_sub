# Multi-hop reasoning
**Type:** Construct  
**Referenced in:** 76 papers  
**Also known as:** Reasoning depth, Multihop reasoning  

## State of the Field

Across the provided literature, multi-hop reasoning is predominantly defined as a model's latent ability to connect, infer, and synthesize information from multiple, non-directly linked pieces of evidence. This process requires performing sequential logical steps or chains of inference to arrive at a conclusion. A smaller body of work frames this concept as "reasoning depth," focusing on the complexity and length of causal dependencies, or more specifically as the ability to trace logical relationships to detect inconsistencies. The field operationalizes this construct through tasks such as answering questions by integrating information across tables and text, performing visually grounded spatial reasoning via "block-placement tasks" (VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models), and reasoning across a sequence of charts. To measure this ability, researchers in this set use instruments including the MMLU-Pro benchmark and human evaluation. A recurring observation is that model performance tends to decrease as the number of reasoning steps increases, with one paper noting this exposes models’ "limitations in sequential inferencing and logical chaining" (Think Wider, Detect Sharper: Reinforced Reference Coverage for Document-Level Self-Contradiction Detection). This construct is also studied in the context of fact verification, where some work suggests that improving multi-hop inference may enhance a model's capacity for hallucination detection.

## Sources

**[AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios](https://aclanthology.org/2025.naacl-long.258.pdf)**
> The latent ability of a model to connect and infer information across multiple pieces of evidence that are not directly linked, requiring sequential logical steps to arrive at an answer.

**[POSITIONBIASMITIGATESPOSITIONBIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.79.pdf) (as "Reasoning depth")**
> The extent to which a model can engage with complex, multi-step reasoning problems that require more than surface-level understanding or pattern matching.

**[CanLLMs Ground when they (Don’t) Know: A Study on Direct and Loaded Political Questions](https://aclanthology.org/2025.acl-long.729.pdf) (as "Multihop reasoning")**
> The latent ability to trace and verify logical relationships across multiple entities and facts in a text, especially when indirect connections are required to detect inconsistencies.

## Relationships

### Multi-hop reasoning →
- **MMLU-Pro** (measurements) — *measured_by*
  - [POSITIONBIASMITIGATESPOSITIONBIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.79.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Conflict-Aware Soft Prompting for Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1372.pdf)

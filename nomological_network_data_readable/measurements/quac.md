# QuAC
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** QUAC, OR-QuAC  

## State of the Field

Across the provided literature, QuAC (Question Answering in Context) is consistently described as a benchmark for evaluating models on conversational question answering. Its most commonly cited feature is a conversational format involving "a series of interconnected questions" or "multi-turn dialogue structures with coreferences." As one paper notes, this structure challenges models "to track context across multiple turns" (Global Eye: Breaking the “Fixed Thinking Pattern” during the Instruction Expansion Process). Papers use QuAC to assess a model's ability to understand context and participate in dialogue, and one source reports it is used to measure "Commonsense knowledge". It is also employed to assess model generalization and is mentioned in the context of zero-shot evaluations. A variant, OR-QuAC, is also discussed, which is defined as a conversational QA dataset for "open-retrieval settings." This variant is distinguished by its inclusion of "context-independent rewrites of the dialogue questions," which allows for evaluation in single-turn scenarios in addition to dialogue-based ones.

## Sources

**[On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf)**
> The Question Answering in Context benchmark, which involves a series of interconnected questions in a conversational format.

**[BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf) (as "QUAC")**
> Question Answering in Context, a benchmark for evaluating a model's ability to understand context and participate in a dialogue about a text.

**[Dynamic Scaling of Unit Tests for Code Reward Modeling](https://aclanthology.org/2025.acl-long.344.pdf) (as "OR-QuAC")**
> Conversational question answering dataset focused on open-retrieval settings with multi-turn queries and associated passages.

## Relationships

### → QuAC
- **Reasoning** (constructs) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)

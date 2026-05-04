# Portability
**Type:** Construct  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, Portability is consistently defined as a model's ability to apply newly edited knowledge beyond the direct context of the edit. The prevailing usage frames this as applying knowledge to "related but distinct content or contexts" (MMKE-Bench). A more expansive view, offered by one paper, describes it as the extent to which an edit generalizes to more complex scenarios, such as "multi-hop reasoning or downstream tasks," which is seen as an indicator of deep knowledge integration (From Capabilities to Performance). The construct is operationalized by observing whether a model can successfully transfer an edit; for example, one paper notes that after editing the US president, "relevant knowledge such as the first lady of United States should be updated as well" (Unlocking Efficient...). Portability is frequently studied as a criterion within `Knowledge editing` and is also associated with `Complex reasoning`, with one study noting that portability "degrades in multi-hop reasoning settings" (From Capabilities to Performance). Additionally, one paper proposes that `Commonsense knowledge` influences Portability.

## Sources

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)**
> The ability of a model to successfully apply newly edited knowledge to related but distinct content or contexts.

## Relationships

### → Portability
- **Commonsense knowledge** (constructs) — *causes*
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)

### Associated with
- **Complex reasoning** (behaviors tasks)
  - [From Capabilities to Performance: Evaluating Key Functional Properties ofLLMArchitectures in Penetration Testing](https://aclanthology.org/2025.emnlp-main.803.pdf)
- **Knowledge editing** (behaviors tasks)
  > Knowledge editing seeks to maximize the chance of an LLM responding with y given x, while satisfying the following additional criteria at the same time...: (2) Portability: relevant knowledge such as the first lady of United States should be updated as well. (Section 2.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)

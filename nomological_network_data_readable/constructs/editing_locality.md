# Editing locality
**Type:** Construct  
**Referenced in:** 13 papers  
**Also known as:** Editing Locality, Semantic locality  

## State of the Field

The prevailing usage of "Editing locality" in the provided literature frames it as a property of knowledge editing methods, defined as the ability to modify targeted knowledge without affecting unrelated information. This dominant view is captured in definitions describing it as the extent to which "unrelated knowledge remains unchanged in the edited model" ("MMKE-Bench...") or the property of an edit to not influence "other unrelated knowledge" ("Precise Localization of Memories..."). This construct is operationalized by comparing a model's outputs before and after an edit to assess changes in unrelated knowledge. Poor locality is described as a limitation that can cause the "persistence of irrelevant or inaccurate facts" ("Precise Localization of Memories..."). A different line of work uses "locality" to refer to a constraint on token distance, where relevant tokens for a prediction are within a bounded range of each other ("The Role of Sparsity..."). Yet another paper introduces "semantic locality" to describe the shared semantics between consecutive tokens or user queries ("Oracle-MoE..."). Finally, editing locality is reported to influence both Faithfulness and Consistency.

## Sources

**[Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf) (as "Editing Locality")**
> The latent property of an editing method to modify targeted knowledge without influencing unrelated knowledge or model capabilities.

**[MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf) (as "Locality")**
> The extent to which unrelated knowledge remains unchanged in the edited model compared to its outputs before editing.

**[Oracle-MoE: Locality-preserving Routing in the Oracle Space for Memory-constrained Large Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25b/zhou25b.pdf) (as "Semantic locality")**
> The degree to which consecutive tokens or user interactions share similar high-level semantics, making their representations and routing decisions stable across nearby time steps.

## Relationships

### Editing locality →
- **Consistency** (constructs) — *causes*
  - [Oracle-MoE: Locality-preserving Routing in the Oracle Space for Memory-constrained Large Language Model Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25b/zhou25b.pdf)

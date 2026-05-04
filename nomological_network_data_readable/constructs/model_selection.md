# Model selection
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Algorithm selection, Model search  

## State of the Field

Across the surveyed literature, model selection is broadly defined as the process of choosing the most suitable model, function, or algorithm from a set of candidates for a given task. A primary distinction in its use is whether it is treated as a latent, internal mechanism of a model or as an observable, external process. Some papers frame it as an intrinsic ability, such as how transformers select between function classes or how in-context learning enables the selection of pre-trained capabilities for out-of-distribution tasks. In this view, it is operationalized by studying a model's internal mechanisms, with one paper identifying a "Low-test-error preference and the Similar-input-distribution preference" as drivers. A different line of work treats it as an observable task performed by an LLM agent, operationalized as a process of identifying, ranking, and selecting candidate models, sometimes under resource constraints. The construct is also studied in relation to decision-making, privacy, and commonsense knowledge.

## Sources

**[Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf) (as "Algorithm selection")**
> The latent mechanism by which a model, when faced with a new task, selects and implements the most suitable function or algorithm from its repertoire of pre-trained capabilities.

**[Selective induction Heads: How Transformers Select Causal Structures in Context](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf)**
> The ability of a model to choose the best-fitting model or function class from a set of candidates based on the provided data or context.

**[AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf) (as "Model search")**
> The observable process of an LLM agent identifying and selecting candidate machine learning models suitable for a given task.

## Relationships

### Associated with
- **Decision-making** (constructs)
  - [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)
- **Privacy** (constructs)
  > “we theoretically reveal the algorithm-selection mechanism for ICL. We find there simultaneously exist two parallel mechanisms: the Low-test-error preference and the Similar-input-distribution preference.”
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf)

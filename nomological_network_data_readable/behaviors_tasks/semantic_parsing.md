# Semantic parsing
**Type:** Behavior  
**Referenced in:** 13 papers  
**Also known as:** Query parsing, Prompt parsing, Intent and slot filling, Task-oriented dialogue parsing  

## State of the Field

Across the provided literature, semantic parsing is most commonly defined as the task of translating unstructured natural language inputs, such as user instructions or observations, into a structured, programmatic, or logical form. The target structured representation is frequently a JSON object with predefined keys, but is also described as machine-executable forms like logical queries or database commands. The general concept is specified in various contexts, appearing as "query parsing" or "prompt parsing" when converting user requests for downstream agents. A distinct application area is in dialogue systems, where the task is framed as "intent and slot filling" to identify user goals or as "task-oriented dialogue parsing" to update a conversational state. To operationalize and measure this behavior, papers use benchmarks such as MTop, with some work also citing SMCalFlow and TreeDST for dialogue-specific parsing. Semantic parsing is studied alongside code generation, and one paper presents a directional relationship where parsing user instructions is a preliminary step to ensure the quality of inputs prior to "actual code implementation" ("AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML").

## Sources

**[From an LLM Swarm to a PDDL-empowered Hive: Planning Self-executed Instructions in a Multi-modal Jungle](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a4215e2b23261056aeeba0f6f05371-Paper-Conference.pdf) (as "Query parsing")**
> The action of converting an unstructured natural language user query into a structured format with distinct components.

**[NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf)**
> The task of translating natural language inputs, such as observations or instructions, into a structured, programmatic, or logical form.

**[AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf) (as "Prompt parsing")**
> Converting unstructured user task descriptions into structured JSON format with standardized keys to extract requirements for downstream agents.

**[Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.746.pdf) (as "Intent and slot filling")**
> A semantic parsing task common in dialogue systems where the goal is to identify the user's overall goal (intent) and extract specific pieces of information (slots).

**[Logits-Based Finetuning](https://aclanthology.org/2025.emnlp-main.746.pdf) (as "Task-oriented dialogue parsing")**
> A semantic parsing task focused on interpreting user utterances within a goal-oriented conversation to update a dialogue state or execute an action.

## Relationships

### Semantic parsing →
- **MTop** (measurements) — *measured_by*
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://raw.githubusercontent.com/mlresearch/v267/main/assets/trirat25a/trirat25a.pdf)

### Associated with
- **Code generation** (behaviors tasks)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.289.pdf)

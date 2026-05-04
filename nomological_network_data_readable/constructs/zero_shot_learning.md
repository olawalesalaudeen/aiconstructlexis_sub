# Zero-shot learning
**Type:** Construct  
**Referenced in:** 23 papers  
**Also known as:** Zero-shot learning ability, Zero-shot capability, Zero-shot inference, Zero-shot prompting capability, Zero-shot adaptability, Zero-shot performance  

## State of the Field

Across the surveyed literature, Zero-shot learning is most commonly defined as a model's ability to perform a task without any task-specific training, fine-tuning, or prior examples. Some definitions elaborate on this, specifying that the model operates based on instructions or natural language descriptions alone, while one paper frames it as leveraging knowledge gained from other tasks to perform new ones. This construct is operationalized and measured using the LLM Evaluation Harness. The capability is demonstrated in a variety of applications, including image restoration, entity matching, and spoken language tasks. Zero-shot learning is frequently studied alongside related concepts such as In-context and few-shot learning, Multi-task capability, and Emergent abilities. Some work suggests that this ability is enabled by a model's Commonsense knowledge and its capacity for Speech-text alignment. In turn, zero-shot learning is reported to be used for Pseudo-label generation.

## Sources

**[Data-Driven Discovery of Dynamical Systems in Pharmacology using Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aea8bdc42d8ba3a67a69b3f18be93f69-Paper-Conference.pdf)**
> The ability to perform a task without any prior examples, such as estimating the value of acquiring a new data feature based only on its description.

**[From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf) (as "Zero-shot learning ability")**
> The capability of a model to perform a task given only a natural language description, without having seen any specific training examples for that task.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Zero-shot capability")**
> The ability to perform a task without any specific training examples for that task or condition.

**[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Zero-shot inference")**
> The ability of a model to perform tasks for which it has not been explicitly trained, by leveraging knowledge gained from other tasks.

**[Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf) (as "Zero-shot prompting capability")**
> The ability of a Large Language Model to perform tasks based on instructions alone, without any provided examples (shots).

**[Graceful Forgetting in Generative Language Models](https://aclanthology.org/2025.emnlp-main.667.pdf) (as "Zero-shot adaptability")**
> The model's ability to perform tasks, such as narrative recommendation, without any specific examples or fine-tuning for that task.

**[Generating Diverse Hypotheses for Inductive Reasoning](https://aclanthology.org/2025.naacl-long.430.pdf) (as "Zero-shot performance")**
> The ability of a model to perform tasks without any task-specific fine-tuning or examples provided in the context.

## Relationships

### Zero-shot learning →
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [MoDeGPT: Modular Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb7214d2fdfd84165b08539d59c92e07-Paper-Conference.pdf)
- **Pseudo-label generation** (behaviors tasks) — *causes*
  - [Entity Alignment with Noisy Annotations from Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1b57aaddf85ab01a2445a79c9edc1f4b-Paper-Conference.pdf)

### → Zero-shot learning
- **Instruction following** (constructs) — *causes*
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Speech-text alignment** (constructs) — *causes*
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.354.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Multi-task capability** (constructs)
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Image restoration** (behaviors tasks)
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Emergent abilities** (constructs)
  - [Knowledge Graph Guided Evaluation of Abstention Techniques](https://aclanthology.org/2025.naacl-long.354.pdf)

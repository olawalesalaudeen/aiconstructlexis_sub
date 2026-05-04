# Key-value retrieval
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Key-value retrieval is presented in the provided literature as a task for evaluating a model's ability to process long contexts. It is consistently defined as the task of "extracting the correct value corresponding to a given key from a context containing multiple key-value pairs" ("Mixture of In-Context Experts Enhance LLMs' Long Context Awareness"). This behavior is operationalized using prompts that contain numerous, sometimes randomly generated, key-value string pairs. The primary application of this task is to measure constructs such as "context awareness" and "context utilization". As one paper states, its purpose is to "evaluate the model’s ability to extract the correct value corresponding to a given query from the context" ("Mixture of In-Context Experts Enhance LLMs' Long Context Awareness"). Performance on the key-value retrieval task is measured using instruments like the InfiniteBench benchmark.

## Sources

**[Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)**
> The task of extracting the correct value corresponding to a given key from a context containing multiple key-value pairs.

## Relationships

### Key-value retrieval →
- **InfiniteBench** (measurements) — *measured_by*
  - [Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf)

### → Key-value retrieval
- **Context utilization** (constructs) — *measured_by*
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)

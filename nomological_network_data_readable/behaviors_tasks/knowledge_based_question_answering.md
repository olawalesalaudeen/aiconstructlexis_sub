# Knowledge-based question answering
**Type:** Behavior  
**Referenced in:** 7 papers  
**Also known as:** Knowledge grounded QA, Knowledge question answering  

## State of the Field

Across the surveyed literature, knowledge-based question answering is most commonly defined as the task of answering questions by making inferences over a body of general or domain-specific knowledge. Several papers specify that this often involves retrieving and synthesizing information from knowledge articles or recalling factual knowledge from short contexts. Applications are noted in specialized domains such as education, medicine, and code generation. A distinct, multimodal variant is also described as "Knowledge grounded QA," which involves answering questions about images that require external world knowledge in addition to visual evidence. This behavior is operationalized and measured using the MMLU benchmark. The task is studied alongside related concepts like `Commonsense knowledge` and, in its visual form, `Multi-image reasoning`.

## Sources

**[Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf)**
> The task of answering questions by making inferences over a body of domain-specific or general knowledge.

**[MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf) (as "Knowledge grounded QA")**
> Answering questions about images that require external or world knowledge in addition to visual evidence.

**[ACCORD: Closing the Commonsense Measurability Gap](https://aclanthology.org/2025.naacl-long.194.pdf) (as "Knowledge question answering")**
> Answering domain-specific factual or conceptual questions from short contexts, often requiring retrieval of specialized knowledge.

## Relationships

### Knowledge-based question answering →
- **MMLU** (measurements) — *measured_by*
  - [CanLLMs Convert Graphs to Text-Attributed Graphs?](https://aclanthology.org/2025.naacl-long.66.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Cost-efficient Knowledge-based Question Answering with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0aafec03d59db29a92fa683bd783374-Paper-Conference.pdf)
- **Multi-image reasoning** (constructs)
  - [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf)

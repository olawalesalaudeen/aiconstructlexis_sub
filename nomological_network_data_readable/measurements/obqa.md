# OBQA
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, OBQA is consistently characterized as a question-answering dataset modeled after open book exams. The task requires models to answer questions using a provided set of facts, which are variously described as 'common knowledge facts,' 'broad common knowledge,' or 'elementary science facts.' The predominant application of OBQA in this set of papers is to measure `Commonsense understanding`, with one paper explicitly including it in a list of 'Eight commonsense reasoning datasets' used for evaluation. The concept of `Reasoning` is also a recurring theme in its description, with definitions stating it is designed to 'assess reasoning with broad common knowledge' and test 'science knowledge and reasoning.' A smaller number of papers also use it to specifically measure `Complex reasoning`. Less frequently, OBQA is employed to evaluate other capabilities, including `Text generation`, `Generalization`, `Reading comprehension`, and `Zero-shot question answering`.

## Sources

**[CRMArena: Understanding the Capacity ofLLMAgents to Perform ProfessionalCRMTasks in Realistic Environments](https://aclanthology.org/2025.naacl-long.195.pdf)**
> The Open Book Question Answering dataset, which requires models to answer questions using a provided set of common knowledge facts.

## Relationships

### → OBQA
- **Commonsense reasoning** (constructs) — *measured_by*
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [P](https://aclanthology.org/2025.acl-long.722.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)
- **Zero-shot question answering** (behaviors tasks) — *measured_by*
  - [ARB-LLM: Alternating Refined Binarizations for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea5ffdf7da91256ecd2770f9fd2dade9-Paper-Conference.pdf)
- **Complex reasoning** (behaviors tasks) — *measured_by*
  - [HiRA: Parameter-Efficient Hadamard High-Rank Adaptation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)

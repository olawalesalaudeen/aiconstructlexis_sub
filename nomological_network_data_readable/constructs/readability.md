# Readability
**Type:** Construct  
**Referenced in:** 20 papers  
**Also known as:** Human-readability, Cognitive effort during reading  

## State of the Field

Across the surveyed literature, Readability is most commonly defined as the quality of a text being easy for a human to read and understand. This construct is frequently operationalized through two primary methods: direct human judgment, where evaluators rate texts, and automated metrics. Specific metrics cited include the Flesch Reading-Ease Score (FRES), Gunning Fog index, and, in the specialized context of subtitles, constraints like characters per line (CPL) and characters per second (CPS). While the 'ease of understanding' framing is prevalent, a smaller set of studies applies the concept to specific domains, defining it as stylistic consistency in code or as the semantic coherence of adversarial prompts that mimic human writing. A distinct line of work treats it as a measure of 'Cognitive effort during reading,' inferred from eye movement patterns. One study on patent claims presents a contrasting view where higher-quality revisions can become less readable, an outcome described as "inherently different from normal text revision tasks" (From Redundancy to Relevance: Information Flow inLVLMs Across Reasoning Tasks). Readability is reported to be improved by text simplification and is studied alongside concepts like text quality and human preference alignment.

## Sources

**[A Systematic Examination of Preference Learning through the Lens of Instruction-Following](https://aclanthology.org/2025.naacl-long.553.pdf)**
> The quality of generated text being easy to read and understand, as judged by human evaluators.

**[AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf) (as "Human-readability")**
> The quality of a generated text, such as an adversarial prompt, being semantically coherent and appearing as if written by a human, making it difficult to distinguish from benign inputs.

**[NO-VER](https://aclanthology.org/2025.emnlp-main.379.pdf) (as "Cognitive effort during reading")**
> The latent level of mental processing load a reader experiences while comprehending a text, inferred from eye movement patterns and modulated by text type, word-level features, and decoding strategies.

## Relationships

### Readability →
- **Human evaluation** (measurements) — *measured_by*
  > users rate Readability (Ribeiro et al., 2023) to ensure the extra perspectives do not harm comprehension. (Section 6.3)
  - [tRAG: Term-level Retrieval-Augmented Generation for Domain-Adaptive Retrieval](https://aclanthology.org/2025.naacl-long.335.pdf)

### → Readability
- **Human preference alignment** (constructs) — *causes*
  - [Towards Federated RLHF with Aggregated Client Preference for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124dde499d62b58e97e42a45b26d7369-Paper-Conference.pdf)
- **Text simplification** (behaviors tasks) — *causes*
  > This refinement greatly improves the readability of documents, making them more accessible to diverse audiences... (Section 1)
  - [KMI: A Dataset ofKorean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.542.pdf)

### Associated with
- **Human preference alignment** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Text quality** (constructs)
  - [Multi-Modal Framing Analysis of News](https://aclanthology.org/2025.emnlp-main.1607.pdf)

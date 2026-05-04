# Linguistic capability
**Type:** Construct  
**Referenced in:** 7 papers  
**Also known as:** Language capability, Linguistic ability, Language skills  

## State of the Field

Across the provided literature, "Linguistic capability" is predominantly defined as a model's fundamental, underlying proficiency in understanding and generating human language, often described as a latent capacity derived from pre-training. The definitions are largely consistent, using related terms like "language proficiency" and "linguistic ability" to refer to a general competence covering syntax, semantics, and pragmatics. This construct is frequently discussed in the context of trade-offs; some research emphasizes that this capability must be retained when a model acquires specialized skills, while other work frames it as a performance objective to be optimized alongside routing efficiency. As one study notes, a training objective can be "decomposed into optimizing linguistic capabilities and minimizing the average number of activated experts" ("Ada-K Routing: Boosting the Efficiency of MoE-based LLMs"). A smaller line of work conceptualizes it as a set of "general cognitive abilities" that are stably represented and can be probed through neuron behavior ("THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation"). In terms of measurement, this construct is operationalized through performance on benchmark tasks. The provided data shows that the MMLU benchmark is used to assess what papers refer to as "language ability." One paper also states that an average score across multiple tasks is "commonly used as an indicator of overall language proficiency" ("TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models").

## Sources

**[Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf) (as "Language capability")**
> The model's underlying proficiency in understanding and generating human language, which should be retained even after specialized skill training.

**[TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e664650506f1cf2b4696df892147c06e-Paper-Conference.pdf) (as "Language proficiency")**
> The overall ability of a model to understand and generate human language across a diverse set of tasks.

**[Ada-K Routing: Boosting the Efficiency of MoE-based LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/df22a19686a558e74f038e6277a51f68-Paper-Conference.pdf)**
> The model's underlying ability to maintain language modeling performance while being optimized for routing efficiency.

**[Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention](https://aclanthology.org/2025.acl-long.271.pdf) (as "Linguistic ability")**
> The latent capacity of a model to understand and produce language effectively, including syntax, semantics, and pragmatics, derived from pre-training on diverse textual data.

**[THOR-MoE: Hierarchical Task-Guided and Context-Responsive Routing for Neural Machine Translation](https://aclanthology.org/2025.acl-long.1041.pdf) (as "Language skills")**
> General cognitive abilities of a language model to perform diverse language understanding tasks, such as sentiment classification or factual reasoning, which are stably represented across contexts and can be probed through neuron behavior.

## Relationships

### Linguistic capability →
- **MMLU** (measurements) — *measured_by*
  > However, the high-quality data used in SFT significantly improved the language ability, effectively mitigating the disadvantages introduced during the pre-training phase. (Section 5.2)
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)

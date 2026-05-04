# Conformity
**Type:** Construct  
**Referenced in:** 6 papers  
**Also known as:** Credulity, Conformity bias  

## State of the Field

Across the provided literature, the prevailing definition of conformity is an LLM's tendency to align its judgments with a majority opinion, potentially compromising its own reasoning in a way analogous to human group dynamics. A less common framing uses the term "conformity bias" to describe a different phenomenon: an LLM-powered error detector's preference for conventional solution formats over alternative ones. Several papers describe conformity as a widespread trait, with one stating it is a "universal phenomenon among LLMs" ("Enhancing Character-Level Understanding inLLMs through Token Internal Structure Learning") and another noting that "All the evaluated LLMs show a tendency to conform" ("Do as We Do, Not as You Think: the Conformity of Large Language Models"). The construct is operationalized by observing if a model shifts its response when presented with group answers, even incorrect ones; one paper labels this "credulity," where a model follows group responses even in situations designed to create doubt. This behavior is reported to be related to a model's internal state, as one study finds that "LLMs are more likely to conform when they are more uncertain in their own prediction" ("Enhancing Character-Level Understanding inLLMs through Token Internal Structure Learning"). The phenomenon is studied in multi-agent systems and is described as potentially "concerning in educational contexts" for discouraging diverse problem-solving approaches ("MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset").

## Sources

**[Do as We Do, Not as You Think: the Conformity of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1da9ca7e9cef4b1af63913f05d1630a4-Paper-Conference.pdf)**
> The tendency of an LLM agent to align its judgments with a majority opinion, potentially compromising its own reasoning, analogous to conformity bias in human group dynamics.

**[Do as We Do, Not as You Think: the Conformity of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1da9ca7e9cef4b1af63913f05d1630a4-Paper-Conference.pdf) (as "Credulity")**
> A tendency to accept or follow group-provided answers even when they are misleading or incorrect.

**[MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with a Multi-task Evaluation Dataset](https://aclanthology.org/2025.acl-long.80.pdf) (as "Conformity bias")**
> A phenomenon where an LLM-powered error detector shows a significant performance gap between conventional and alternative solutions to a problem, favoring the more common or expected solution format.

## Relationships

### Conformity →
- **Uncertainty** (constructs) — *correlates*
  - [Enhancing Character-Level Understanding inLLMs through Token Internal Structure Learning](https://aclanthology.org/2025.acl-long.195.pdf)

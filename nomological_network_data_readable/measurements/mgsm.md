# MGSM
**Type:** Measurement  
**Referenced in:** 38 papers  

## State of the Field

Across the surveyed literature, MGSM is consistently characterized as a benchmark for evaluating reasoning in large language models, with a specific focus on multilingual contexts. The prevailing usage is to measure mathematical reasoning, a purpose cited by a large number of studies. A closely related and also frequent application is the assessment of multilingual reasoning more broadly. The benchmark is uniformly described as being derived from the GSM8K dataset, consisting of grade-school level math word problems translated into multiple non-English languages, with sources variously citing nine, ten, or eleven languages. As one paper specifies, its creation involved "manually translating 250 samples from the GSM8K test set into multiple languages" ("Learning to Substitute Words with Model-based Score Ranking"). While the dominant application is for mathematical and multilingual reasoning, a few papers employ it to evaluate other capabilities, such as "sequential instruction-following" or "generalization to template-compatible domains". Overall, MGSM is operationalized as a tool to test a model's non-English quantitative and problem-solving abilities.

## Sources

**[AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)**
> Multilingual Grade School Math benchmark evaluating mathematical reasoning across languages, used to test non-English quantitative reasoning ability.

## Relationships

### → MGSM
- **Mathematical reasoning** (constructs) — *measured_by*
  > ...the latter two focus on examining the agents’ reasoning abilities, including mathematical and logical reasoning. (Section 3.1)
  - [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf)
- **Multilingual reasoning** (constructs) — *measured_by*
  > “We conduct assessments on six benchmarks covering reasoning, understanding, and generation tasks that encapsulate various abilities of LLMs: MGSM”
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [AFRIDOC-MT: Document-levelMTCorpus forAfrican Languages](https://aclanthology.org/2025.emnlp-main.1414.pdf)
- **Generalization** (constructs) — *measured_by*
  > we include (6) MGSM (Shi et al., 2022), a structured math reasoning task where predefined logic may suffice, to evaluate generalization to template-compatible domains. (Section 5.1)
  - [Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.93.pdf)

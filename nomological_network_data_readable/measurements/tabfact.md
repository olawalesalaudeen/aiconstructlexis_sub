# TabFact
**Type:** Measurement  
**Referenced in:** 7 papers  

## State of the Field

Across the provided literature, TabFact is consistently defined as a benchmark dataset for table-based fact verification. The core task requires a model to determine if a given statement is supported by an accompanying Wikipedia table, a process frequently described as assessing whether the statement is 'entailed or refuted' by the table's content. One paper specifies that the labels for this task are 'Entailed' ('True') or 'Refuted' ('False'), while two sources mention a test set containing 2,024 statements and 298 tables. As a measurement instrument, TabFact is used to evaluate several model capabilities. The provided data shows it is used to assess `Table understanding` and `Table and chart reasoning`, in addition to being used for more general `Evaluation`. Its role as a tool for table-based reasoning is a recurring theme, with one paper referring to it as a 'widely-used table-based reasoning benchmark'.

## Sources

**[DAWN-ICL: Strategic Planning of Problem-solving Trajectories for Zero-Shot In-Context Learning](https://aclanthology.org/2025.naacl-long.97.pdf)**
> A benchmark dataset for table-based fact verification, containing statements paired with Wikipedia tables, where the task is to determine if the statement is supported by the table.

## Relationships

### → TabFact
- **Evaluation** (behaviors tasks) — *measured_by*
  - [Mitigating Lost-in-Retrieval Problems in Retrieval Augmented Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1090.pdf)
- **Table question answering** (behaviors tasks) — *measured_by*
  - [TableRAG: Million-Token Table Understanding with Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/88dd7aa6979e352fda7c4952ca8eac59-Paper-Conference.pdf)
- **Table reasoning** (constructs) — *measured_by*
  - [Instantly Learning Preference Alignment via In-contextDPO](https://aclanthology.org/2025.naacl-long.9.pdf)

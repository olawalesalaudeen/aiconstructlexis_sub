# FLORES-200
**Type:** Measurement  
**Referenced in:** 32 papers  
**Also known as:** Flores-200, Flores200  

## State of the Field

Across the provided literature, FLORES-200 is predominantly characterized as a multilingual benchmark dataset used to evaluate machine translation. Its most frequent application is assessing translation performance across a wide range of languages, with a recurring emphasis on its coverage of low-resource languages, such as in Assamese-to-English translation. Papers operationalize translation quality on this benchmark using several metrics; while one common definition specifies the chrF1 metric, other studies report using spBLEU and COMET. While primarily an evaluation tool, a few papers also repurpose its development and test sets as a source of high-quality parallel training data. A smaller body of work employs the dataset for other purposes, such as evaluating cross-lingual retrieval, identifying expert neurons, or as the source material for other benchmarks like Belebele for reading comprehension. Most definitions state it covers 200 languages, though one source specifies 204. The snippets show it is often used to evaluate models in few-shot in-context learning settings.

## Sources

**[LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf)**
> A multilingual benchmark dataset for evaluating machine translation quality across 200 languages, including many low-resource ones, using the chrF1 metric.

**[A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b9536e186a77feff516893a5f393f7a-Paper-Conference.pdf) (as "Flores-200")**
> Massive multilingual benchmark dataset used for evaluating low-resource and high-resource language translation, including development and test sets used here as high-quality parallel training data.

**[Inference Compute-Optimal Video Vision Language Models](https://aclanthology.org/2025.acl-long.118.pdf) (as "Flores200")**
> A machine translation dataset containing parallel text for 204 languages, used for identifying expert neurons and evaluating cross-lingual retrieval.

## Relationships

### → FLORES-200
- **Machine translation** (behaviors tasks) — *measured_by*
  > We utilize the Flores-200 (Team, 2022) Assamese-to-English translation dataset for low-resource translation. (Section 4.1)
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2ad28981782bb62f025d2893791b629-Paper-Conference.pdf)

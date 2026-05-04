# DBPedia
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** DBpedia, Dbpedia, DB Pedia  

## State of the Field

Across the provided literature, DBPedia is consistently characterized as a benchmark dataset derived from Wikipedia used to evaluate models. The prevailing usage of DBPedia is to measure `Text classification`, with most papers defining it as a topic or ontology classification task. This common operationalization involves categorizing text into one of 14 classes, as multiple sources specify it is for "14-way topic classification". For instance, one paper describes it as a task of "multi-class classification of Wikipedia articles". A distinct, less common framing is presented by one paper which describes DBPedia as having a "three-layer taxonomy tree, with 9/70/219 classes" and uses it to measure `Hierarchical text classification`. The dataset is also reported in this collection of papers as a tool for assessing `In-context and few-shot learning` and `Sensitivity`.

## Sources

**[Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)**
> A benchmark dataset for 14-way topic classification derived from Wikipedia, used to evaluate a model's ability to categorize text into one of fourteen ontological classes.

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf) (as "Dbpedia")**
> The DBpedia ontology classification dataset, a benchmark for topic classification.

**[IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf) (as "DBpedia")**
> A dataset for ontology classification derived from Wikipedia, used to evaluate text categorization.

**[A Systematic Analysis of Base Model Choice for Reward Modeling](https://aclanthology.org/2025.emnlp-main.9.pdf) (as "DB Pedia")**
> A topic classification dataset derived from Wikipedia, with 14 classes corresponding to DBpedia ontology types.

## Relationships

### → DBPedia
- **Text classification** (behaviors tasks) — *measured_by*
  > We study text classification on three datasets: 4-way news classification AGNews (Zhang et al., 2015), 6-way question classification TREC (Voorhees and Tice, 2000), and 14-way topic classification DBPedia (Zhang et al., 2015).
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Sensitivity** (constructs) — *measured_by*
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.73.pdf)
- **Hierarchical text classification** (behaviors tasks) — *measured_by*
  - [Evaluating and Aligning Human Economic Risk Preferences inLLMs](https://aclanthology.org/2025.emnlp-main.918.pdf)

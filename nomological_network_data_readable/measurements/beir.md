# BEIR
**Type:** Measurement  
**Referenced in:** 21 papers  
**Also known as:** BEIR benchmark  

## State of the Field

Across the provided literature, BEIR is consistently characterized as a benchmark composed of a diverse collection of datasets from various domains. Its prevailing use is to evaluate information retrieval capabilities, with a recurring emphasis on measuring a model's out-of-domain and zero-shot performance. Papers frequently use BEIR to operationalize and measure constructs such as `Generalization`, `Ranking`, and `Retrieval effectiveness`. The evaluation is typically conducted in a zero-shot setting, which, as one paper notes, allows researchers to “evaluate the generalization capabilities of IR models across various scenarios without task-specific fine-tuning.” While the acronym BEIR is stable, its expansion varies slightly across papers, including “Benchmark for Evaluation of Information Retrieval,” “Broad Evaluation of Information Retrieval,” and “Benchmarking IR.” The benchmark is described as containing between 14 and 18 datasets, and is often used in conjunction with other instruments like TREC DL and MS MARCO. A connection to the MTEB benchmark is also noted, with one paper stating that the retrieval tasks within MTEB are “commonly referred to as BEIR”.

## Sources

**[Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2cefdb2c4c3274b78cd450bac35228df-Paper-Conference.pdf)**
> The Benchmark for Evaluation of Information Retrieval (BEIR) is a collection of diverse datasets used to measure a model's out-of-domain retrieval performance.

**[From perception to production: how acoustic invariance facilitates articulatory learning in a self-supervised vocal imitation model](https://aclanthology.org/2025.emnlp-main.1218.pdf) (as "BEIR benchmark")**
> Broad Evaluation of Information Retrieval benchmark, a diverse collection of datasets including Covid, SciFact, DBpedia, and NFCorpus, used to evaluate zero-shot retrieval and re-ranking performance across domains.

## Relationships

### → BEIR
- **Information retrieval** (behaviors tasks) — *measured_by*
  > Using the Qwen-2.5-32B model, we annotate utility on the MS MARCO dataset and conduct retrieval experiments on MS MARCO and BEIR... (Abstract)
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We conducted experiments on DL19, DL20, and BEIR, and show the results in Table 2. (Section 4.4)
  - [VISA: Retrieval Augmented Generation with Visual Source Attribution](https://aclanthology.org/2025.acl-long.1457.pdf)
- **Ranking** (behaviors tasks) — *measured_by*
  > We further evaluate QRRETRIEVER as a re-ranker on the standard BEIR benchmark (Thakur et al., 2021). (Section 1)
  - [Easy asPIE? Identifying Multi-Word Expressions withLLMs](https://aclanthology.org/2025.emnlp-main.1214.pdf)
- **Retrieval effectiveness** (constructs) — *measured_by*
  > "We evaluate retrieval effectiveness using two retrieval benchmarks: MS MARCO (Bajaj et al., 2016) and BEIR (Thakur et al., 2021)."
  - [SAFE-SQL: Self-Augmented In-Context Learning with Fine-grained Example Selection for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.963.pdf)

### Associated with
- **MTEB** (measurements)
  > Note that our model also attains
the highest scores in 15 retrieval tasks (commonly referred to as BEIR (Thakur et al., 2021)), 11
clustering tasks, and 12 classification tasks in the MTEB benchmark.
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)

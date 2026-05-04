# TyDiQA
**Type:** Measurement  
**Referenced in:** 19 papers  
**Also known as:** TydiQA, TYDIQA, Tydi QA  

## State of the Field

Across the provided sources, TyDiQA is consistently characterized as a benchmark for multilingual question answering. Its prevailing use is to evaluate a model's capabilities across a diverse set of "typologically different languages," as noted in several definitions. Papers use TyDiQA to operationalize and measure several abilities, most commonly "Multilingual ability" and "Multilingual question answering," but also general "Question answering," "Commonsense knowledge," and "Faithfulness." The task format is described by some sources as "single-hop question answering" where models must answer questions given a context from a "Wikipedia datastore" or article. While most definitions emphasize its multilingual nature, there is a slight variation in the number of languages mentioned, with some papers citing nine and others eleven. The benchmark is also used in language-specific subsets, as one paper notes with "TyDiQA { ID, SW, FI }". TyDiQA is frequently included in evaluation suites alongside other benchmarks like MMLU, GSM8K, and BBH to assess general model performance, particularly for instruction-tuned LLMs.

## Sources

**[Language Model Cascades: Token-Level Uncertainty And Beyond](https://proceedings.iclr.cc/paper_files/paper/2024/file/11f5520daf9132775e8604e89f53925a-Paper-Conference.pdf)**
> A multilingual question answering benchmark included in the expanded evaluation set, with language-specific subsets used in evaluation.

**[SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf) (as "TydiQA")**
> A benchmark for evaluating multilingual question answering capabilities across a diverse set of typologically different languages.

**[Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf) (as "TYDIQA")**
> TyDi QA, a multilingual question-answering benchmark used here to evaluate instruction-tuned LLMs.

**[Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf) (as "TyDi QA")**
> A single-hop question answering benchmark evaluated with Wikipedia datastore contexts.

**[Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf) (as "Tydi QA")**
> A question answering dataset covering 11 typologically diverse languages, requiring models to answer questions given a Wikipedia article.

## Relationships

### → TyDiQA
- **Multilingual ability** (constructs) — *measured_by*
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [TSDS: Data Selection for Task-Specific Model Finetuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/13848b5893119ff772b69812c95914fa-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Multilingual question answering** (behaviors tasks) — *measured_by*
  - [Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness](https://aclanthology.org/2025.emnlp-main.1466.pdf)

### Associated with
- **OpenLLM Leaderboard** (measurements)
  - [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/faa6144674bce872365874c576b4f56f-Paper-Conference.pdf)

# QNLI
**Type:** Measurement  
**Referenced in:** 27 papers  

## State of the Field

Across the surveyed literature, QNLI is consistently characterized as a benchmark for evaluating Natural Language Inference (NLI), specifically in a question-answering context. The task, which multiple sources state is derived from the SQuAD dataset, is most commonly defined as determining whether a given sentence contains the answer to a question, operationalized as an entailment or binary classification problem. A recurring theme is its inclusion as a standard task within the GLUE benchmark, where it is used to assess general model capabilities for Natural Language Understanding. Papers frequently employ QNLI to evaluate the performance of models after procedures like fine-tuning, privacy-preserving learning, and compression, as noted in one study that compares the "accuracy of the compressed models... on MNLI and QNLI datasets" ("Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models"). Beyond general performance measurement, a smaller set of studies uses QNLI to investigate specific model behaviors, such as analyzing length bias or, as one paper observes, a tendency for models to default to an "'entailment'" prediction with certain content-free prompts ("Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering").

## Sources

**[Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf)**
> A question-answering natural language inference benchmark used to evaluate entailment classification for question-sentence pairs.

## Relationships

### → QNLI
- **Natural language inference** (behaviors tasks) — *measured_by*
  > natural language inference and entailment: ANLI-R{1,2,3} (Nie et al., 2020), CB (De Marneffe et al., 2019), RTE, QNLI (QA/NLI), MNLI (Williams et al., 2018). (Section 5.1)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > These datasets encompass various typical language understanding tasks such as natural language inference. (Section 5.1)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > 2) QNLI: This is a dataset containing sentence pairs for binary classification (entailment/not entailment). We use accuracy as the metric. (Section 5)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1769.pdf)

### Associated with
- **GLUE** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): ... and Natural Language Inference (MNLI, RTE, QNLI).
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)

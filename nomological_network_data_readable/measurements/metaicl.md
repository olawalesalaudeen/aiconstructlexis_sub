# MetaICL
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, MetaICL is predominantly described as a benchmark dataset designed to evaluate in-context learning. It is consistently used to measure the construct of "In-context and few-shot learning" by assessing a model's ability to generalize to new tasks and domains. The benchmark is composed of a large number of unique NLP tasks—specified as 142 in several sources—which span text classification, question answering (QA), natural language inference (NLI), and paraphrase detection. These tasks are structured into distinct meta-training and meta-testing partitions, with one paper describing a "high-to-low resources setting" with 61 training and 26 unseen test tasks. The evaluation metric is specified in one source as accuracy on multiple-choice questions. While most papers treat it as a dataset, a less common framing describes MetaICL as a broader "evaluation framework" that also involves a "short finetuning" procedure. In all cases, its application is to validate methodologies for in-context learning scenarios.

## Sources

**[Compressed Context Memory for Online Language Model Interaction](https://proceedings.iclr.cc/paper_files/paper/2024/file/97dc07f1253ab33ee514f395a82fa7cc-Paper-Conference.pdf)**
> A benchmark dataset designed for evaluating in-context learning, composed of 142 unique NLP tasks divided into distinct meta-training and meta-testing partitions.

## Relationships

### → MetaICL
- **In-context learning** (constructs) — *measured_by*
  - [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf)

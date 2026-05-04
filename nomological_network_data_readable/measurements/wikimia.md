# WikiMIA
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** WIKIMIA  

## State of the Field

Across the provided literature, WikiMIA is consistently described as a benchmark dataset for evaluating pre-training data detection algorithms on large language models. The prevailing operationalization of the benchmark is temporal; it contains excerpts from Wikipedia articles that are classified as either "seen" or "unseen" based on whether their publication date precedes a model's training cutoff. This temporal separation based on the model's release timeline is its defining feature. Papers use WikiMIA to compare the performance of different detection methods, with one study noting its use to show accuracy gains over methods like "Min-K%" and "Min-K%++". However, this temporal design is also a point of contention. At least one paper criticizes the benchmark, arguing that separating data by publication date introduces "artificial distribution shifts." This critique is substantiated by the finding that a "blind baseline—which predicts membership solely from text content without any model access—already achieves 98.7% AUC," questioning the validity of the task as framed by the dataset.

## Sources

**[TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf) (as "WIKIMIA")**
> A dataset specifically designed to evaluate training data detection algorithms on large language models.

**[Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)**
> A temporal benchmark dataset for evaluating pretraining data detection methods, containing excerpts from Wikipedia articles classified as "seen" or "unseen" based on their publication date relative to a model's training cutoff.

## Relationships

### → WikiMIA
- **Pre-training data detection** (behaviors tasks) — *measured_by*
  > WIKIMIA is a dataset specifically designed to evaluate TDD algorithms on large language models.
  - [Detecting Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf)

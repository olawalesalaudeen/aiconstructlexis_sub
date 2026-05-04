# TQA
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, TQA is a benchmark dataset, though its specific identity is inconsistent. The prevailing usage refers to "Textbook Question Answering," which is described as a reading comprehension benchmark consisting of scientific textbooks. In this capacity, it is used to evaluate models' abilities in reading comprehension, with performance often measured by F1 scores. Some work also uses this version of TQA to evaluate "knowledge-based reasoning" or for fine-tuning models. One study operationalizes it to measure "Out-of-distribution detection" by translating its content into a different language. A less common usage, found in one paper, uses the acronym TQA to refer to the "TriviaQA dataset," which is characterized as a challenging dataset for closed-book question answering.

## Sources

**[Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce806d8b4bf38cd92d483e5a0490d983-Paper-Conference.pdf)**
> Textbook Question Answering (TQA), a reading-comprehension benchmark used here in generative format to assess reading comprehension.

## Relationships

### → TQA
- **Out-of-distribution detection** (behaviors tasks) — *measured_by*
  > We then repeat the experiment with the statements translated into Samoan, an out-of-distribution language for TQA (Kembhavi et al., 2017).
  - [Scalable Bayesian Learning with posteriors](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f9f4ff2ebebb298d88e3fe0e10162db-Paper-Conference.pdf)

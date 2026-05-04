# BookMIA
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

BookMIA is most commonly described as a membership inference benchmark designed to evaluate large language models. Across the provided literature, it is used to measure the construct of `Memorization` and to perform the task of `Pre-training data detection`. The benchmark is composed of text excerpts and paragraphs from books, with some sources specifying they are copyrighted. Its operational design frequently relies on a temporal distinction, contrasting passages from popular books, treated as potentially memorized content, with excerpts from books published after a model's knowledge cutoff, which are labeled as 'unseen'. Some studies use only these 'unseen' data points to assess model responses to novel content. One paper notes a potential limitation, stating that benchmarks like BookMIA "cannot be reliably used for Llama-3 because the model was trained more recently."

## Sources

**[Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)**
> A membership inference benchmark for book excerpts used as a prior temporal detection dataset.

## Relationships

### BookMIA →
- **Memorization** (constructs) — *measured_by*
  > We use the BookMIA dataset (Shi et al., 2023), which consists of text excerpts from books published in 2023 (after the knowledge cutoff of the models we study) as examples of unseen text, and passages from popular books as memorized examples (Chang et al., 2023). (Section 4.1)
  - [Towards Efficient and Multifaceted Computer-assisted Pronunciation Training Leveraging Hierarchical Selective State Space Model and Decoupled Cross-entropy Loss](https://aclanthology.org/2025.naacl-long.99.pdf)

### → BookMIA
- **Pre-training data detection** (behaviors tasks) — *measured_by*
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)

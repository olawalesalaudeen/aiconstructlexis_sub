# RedPajama V2
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** RedPajama-V2, RedpajamaV2  

## State of the Field

Across the provided literature, RedPajama V2 is consistently characterized as a large-scale, preprocessed web-corpus dataset designed for pretraining language models. It is described as being compiled from "diverse Internet sources" and containing up to "30 trillion tokens" (Programming Every Example: Lifting Pre-training Data Quality Like Experts at Scale). The most prevalent application of RedPajama V2 is as a pretraining set, with one study explicitly noting it is "designed for training language models" in the context of language modeling (No Need to Talk: Asynchronous Mixture of Language Models). Some research utilizes specific subsets of the data, such as the "'sample-100B' subset" for experiments (Improving Pretraining Data Using Perplexity Correlations). Beyond its primary use for pretraining, the dataset also serves other measurement purposes. For instance, one paper uses it as a source of text domains for measuring model losses to inform data selection, while another employs its validation set as a benchmark to measure forgetting by tracking changes in pretraining loss.

## Sources

**[Improving Pretraining Data Using Perplexity Correlations](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c625366ae28066fcb1827b44517d674-Paper-Conference.pdf)**
> A web-corpus dataset used as the source of pretraining text domains on which model losses were measured for data selection.

**[No Need to Talk: Asynchronous Mixture of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ae2d3297891cad0c56dd12d60ff7dde-Paper-Conference.pdf) (as "RedPajama-V2")**
> A large-scale web-text corpus used to train the language models in the paper.

**[Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf) (as "RedpajamaV2")**
> A large and diverse corpus (Weber et al., 2024) used for pretraining models, with its validation set also used as a benchmark to measure forgetting by tracking changes in pretraining loss.

## Relationships

### → RedPajama V2
- **Language modeling** (behaviors tasks) — *measured_by*
  > “We use the RedPajama-V2 dataset (Computer, 2023), which is a large-scale collection of text data designed for training language models.”
  - [No Need to Talk: Asynchronous Mixture of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ae2d3297891cad0c56dd12d60ff7dde-Paper-Conference.pdf)

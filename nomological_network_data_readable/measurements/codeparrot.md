# CodeParrot
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

CodeParrot is consistently described as a benchmark or dataset for evaluating language models on programming language sequences. The provided literature uses it to measure two related capabilities. One prevalent application is for assessing general language modeling performance, where it is defined as a "code modeling dataset" and performance is measured using perplexity, as shown in one study ("MorphMark"). A more specific framing, found in other work, presents CodeParrot as a "code-oriented long-context benchmark" explicitly used for "length extrapolation evaluation" ("Gated Delta Networks"). In this context, it is used to assess a model's "capacity to extrapolate to sequences of up to 20K tokens." Thus, across the available data, CodeParrot serves as an instrument to evaluate how well models handle code, both in terms of standard language modeling and their ability to generalize to long sequences.

## Sources

**[Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)**
> A code-oriented long-context benchmark used in the length extrapolation evaluation.

## Relationships

### → CodeParrot
- **Length generalization** (constructs) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > Language modeling, for which we evaluate perplexity on PG19 (Rae et al., 2020), Proof-Pile (Zhangir Azerbayev), and CodeParrot (CodeParrot) (Section 3.1)
  - [MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.241.pdf)

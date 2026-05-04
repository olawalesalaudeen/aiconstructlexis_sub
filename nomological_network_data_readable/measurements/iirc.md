# IIRC
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided sources, IIRC (Iterative Information Retrieval and Comprehension) is consistently characterized as a benchmark dataset for reading comprehension used for evaluation. The dataset is described as focusing on information integration, requiring models to answer questions by "linking information across document sections" to test both retrieval and contextual understanding. In practice, papers use IIRC to measure both `Question answering` and `Mathematical reasoning`. The measurement of mathematical reasoning is specifically associated with using "decontextualized versions of a subset of ... IIRC," as noted in one study. Its general application is for evaluation, with one paper reporting that a model "demonstrates a consistent advantage across metrics" on the dataset.

## Sources

**[Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf)**
> A reading comprehension benchmark dataset (Iterative Information Retrieval and Comprehension) used for evaluation.

## Relationships

### → IIRC
- **Mathematical reasoning** (constructs) — *measured_by*
  > Besides, we also provide more experimental results on the decontextualized versions of a subset of DROP (Dua et al., 2019) and IIRC (Ferguson et al., 2020) in Appendix D.1. (Section 5.1)
  - [Agent-Oriented Planning in Multi-Agent Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/31610e68fe41a62e460e044216a10766-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Take the essence and discard the dross: A Rethinking on Data Selection for Fine-Tuning Large Language Models](https://aclanthology.org/2025.naacl-long.337.pdf)

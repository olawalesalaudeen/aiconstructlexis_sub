# XNLI
**Type:** Measurement  
**Referenced in:** 40 papers  

## State of the Field

Across the surveyed literature, XNLI is a frequently used benchmark for evaluating models on cross-lingual natural language inference (NLI). The task is consistently defined as classifying the relationship between sentence pairs as one of entailment, contradiction, or neutrality across multiple languages, with sources citing either 14 or 15 languages. The most prevalent use of XNLI is to directly measure the behavior of "Natural language inference." Papers also commonly employ it to assess a broader set of related constructs, including "language understanding," "semantic understanding," "textual reasoning," and "cross-lingual alignment." Less frequently, it is used to evaluate "knowledge transferability" and "zero-shot cross-lingual transfer." The instrument's application extends beyond direct model evaluation, serving as a source for new datasets or as a form of "indirect supervision for translation evaluation." As one study notes, it is "commonly utilized for evaluating the general capabilities of multilingual models," often in conjunction with other cross-lingual benchmarks.

## Sources

**[Are Bert Family Good Instruction Followers?  A Study on Their Potential And Limitations](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a13eb0c08247364066e8d86551c3090-Paper-Conference.pdf)**
> Cross-lingual Natural Language Inference dataset that assesses a model's ability to determine entailment, contradiction, or neutrality between sentence pairs in multiple languages.

## Relationships

### → XNLI
- **Natural language inference** (behaviors tasks) — *measured_by*
  > For NLI and reasoning, we use XNLI (Conneau et al., 2018) and XCOPA (Ponti et al., 2020) with zero-shot prompting. (Section 5.4)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **Textual reasoning** (behaviors tasks) — *measured_by*
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Cross-lingual alignment** (constructs) — *measured_by*
  > In this section, we pretrain small multilingual MLMs and evaluate their performance on the XNLI dataset (Conneau et al., 2018). (Section 5)
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Machine translation** (behaviors tasks) — *measured_by*
  - [Heads up! Large Language Models Can Perform Tasks Without Your Instruction via Selective Attention Head Masking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25l/han25l.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **Semantic understanding** (constructs) — *measured_by*
  > The two multilingual tasks evaluate MrT5's ability to understand high-level semantics... specifically, two cross-lingual benchmarks (XNLI and TyDi QA)
  - [MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e9dd32cb9f9bff397f1a7ebd07010f2-Paper-Conference.pdf)
- **Zero-shot cross-lingual transfer** (behaviors tasks) — *measured_by*
  - [SEAL: Scaling to Emphasize Attention for Long-Context Retrieval](https://aclanthology.org/2025.acl-long.1406.pdf)

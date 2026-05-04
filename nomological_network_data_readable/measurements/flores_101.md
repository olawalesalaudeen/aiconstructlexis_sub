# Flores-101
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** FLORES-101  

## State of the Field

Flores-101 is consistently characterized across the provided literature as a benchmark dataset for evaluating multilingual capabilities, with a primary focus on machine translation. The dataset is described as containing professionally or human-written sentences with "aligned translations across 101 languages" ("VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models"). Its most prevalent application is to measure the performance of machine translation, with evidence showing its use for evaluating bidirectional translation tasks. A smaller body of work frames its use more broadly for assessing "multilingual general and cross-lingual generation capabilities" ("LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing"). The methods for evaluation on this benchmark are described in slightly different ways; some sources mention its use for qualitative evaluation, while another specifies the use of quantitative metrics like BLEU and COMET to assess translation quality. Overall, Flores-101 is operationalized as a common instrument for testing model performance on translation across a large number of languages.

## Sources

**[CRScore: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](https://aclanthology.org/2025.naacl-long.458.pdf)**
> A benchmark dataset consisting of sentences professionally translated across 101 languages, used for qualitative evaluation of interventions in a machine translation context.

**[LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.328.pdf) (as "FLORES-101")**
> Benchmark for evaluating machine translation and cross-lingual generation across 101 languages, using BLEU and COMET metrics to assess translation quality.

## Relationships

### → Flores-101
- **Machine translation** (behaviors tasks) — *measured_by*
  > We perform the same interventions on the Flores-101 dataset (Goyal et al., 2022), which provides aligned translations across 101 languages. We present a selection of qualitative examples in Figure 7. (Section 4.3)
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)

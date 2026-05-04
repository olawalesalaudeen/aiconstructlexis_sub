# MKQA
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided literature, MKQA is consistently described as a benchmark dataset for multilingual and cross-lingual question answering. Its most frequent application is to measure the `Multilingual question answering` capabilities of models, with sources specifying it represents open-domain and open-ended QA tasks. One paper notes the dataset is comprised of "10k knowledge question-answer pairs aligned across 26 languages" ("Causal Representation Learning..."). A related use frames MKQA as a tool for assessing `Knowledge retrieval`, with one study selecting it as a "representative" dataset for this purpose in the context of interpretability analysis ("CompAct..."). Additionally, strong performance on the benchmark is reported as evidence of a model's `Cross-lingual alignment` capability. Some papers also include MKQA within a broader suite of benchmarks to assess general LLM abilities covering reasoning and understanding.

## Sources

**[Behavior-SD: Behaviorally Aware Spoken Dialogue Generation with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)**
> Multilingual Knowledge Questions and Answers, a cross-lingual question answering dataset used as a knowledge retrieval benchmark in interpretability analysis.

## Relationships

### → MKQA
- **Multilingual question answering** (behaviors tasks) — *measured_by*
  > We use the following question-answering (QA) tasks: (i) MLQA (Lewis et al., 2020a), (ii) MKQA (Longpre et al., 2021) and (iii) XOR-TyDi QA (Asai et al., 2021) as they best represent multilingual open-ended question-answering tasks. (Section 3.1)
  - [Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness](https://aclanthology.org/2025.emnlp-main.1466.pdf)
- **Knowledge retrieval** (behaviors tasks) — *measured_by*
  > We selected MKQA (Longpre et al., 2021), BoolQ (Clark et al., 2019), and AmbigQA (Min et al., 2020) as representative datasets of knowledge retrieval tasks for the interpretability analysis. (Section 5.3)
  - [CompAct: Compressed Activations for Memory-EfficientLLMTraining](https://aclanthology.org/2025.naacl-long.72.pdf)
- **Cross-lingual alignment** (constructs) — *measured_by*
  > Notably, it achieves significant improvements of +3.6% R@20 and +5.7% nDCG@10 over the strongest baseline (M3-Embedding), demonstrating superior cross-lingual alignment capability. (Section 4.4)
  - [CoEvo: Coevolution ofLLMand Retrieval Model for Domain-Specific Information Retrieval](https://aclanthology.org/2025.emnlp-main.758.pdf)

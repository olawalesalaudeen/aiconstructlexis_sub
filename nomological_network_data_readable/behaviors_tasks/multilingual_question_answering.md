# Multilingual question answering
**Type:** Behavior  
**Referenced in:** 11 papers  

## State of the Field

Across the surveyed literature, multilingual question answering is most commonly defined as the task of answering questions in multiple languages, typically evaluated on a dedicated benchmark. Several papers specify that this behavior involves answering a question based on a provided context or passage, with one study describing it as finding "relevant information (the needle) from the input context (the haystack)". While most definitions center on cross-language capabilities, one paper notes that the task can encompass "both monolingual and cross-lingual retrieval." The behavior is operationalized and measured using several specific instruments. The most frequently cited benchmarks are MLQA, MKQA, and XQuAD, which are used to facilitate the "cross-lingual evaluation of QA systems." MLQA and MKQA are specifically mentioned as representing "multilingual open-ended question-answering tasks." TyDiQA is also identified as a measurement instrument for this behavior. In some contexts, the task is extended to evaluate related abilities, such as truthfulness using "multilingual TruthfulQA" or inference using "XNLI".

## Sources

**[Data Pruning by Information Maximization](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d848891e365ca623dc8352db9782585-Paper-Conference.pdf)**
> Answering questions in multiple languages as evaluated on a multilingual QA benchmark.

## Relationships

### Multilingual question answering →
- **MLQA** (measurements) — *measured_by*
  > However, efforts such as MLQA (Lewis et al., 2020) and XQuAD (Artetxe et al., 2019) have introduced datasets supporting multiple languages, facilitating cross-lingual evaluation of QA systems. (Section 5)
  - [On the Vulnerability of Text Sanitization](https://aclanthology.org/2025.naacl-long.267.pdf)
- **XQuAD** (measurements) — *measured_by*
  > However, efforts such as MLQA (Lewis et al., 2020) and XQuAD (Artetxe et al., 2019) have introduced datasets supporting multiple languages, facilitating cross-lingual evaluation of QA systems. (Section 5)
  - [GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)
- **MKQA** (measurements) — *measured_by*
  > We use the following question-answering (QA) tasks: (i) MLQA (Lewis et al., 2020a), (ii) MKQA (Longpre et al., 2021) and (iii) XOR-TyDi QA (Asai et al., 2021) as they best represent multilingual open-ended question-answering tasks. (Section 3.1)
  - [Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness](https://aclanthology.org/2025.emnlp-main.1466.pdf)
- **TyDiQA** (measurements) — *measured_by*
  - [Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness](https://aclanthology.org/2025.emnlp-main.1466.pdf)

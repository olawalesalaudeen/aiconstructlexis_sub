# XQuAD
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** XQUAD  

## State of the Field

Across the provided literature, XQuAD is consistently characterized as a benchmark dataset for evaluating question answering capabilities in multiple languages. It is most frequently used to measure the constructs of "Multilingual question answering" and "Question answering," with one paper also linking it to "Language understanding." The task is commonly specified as "extractive" question answering, where models answer questions from a provided context, which one source identifies as paragraphs from Wikipedia. A few papers provide more detail on its origin, describing XQuAD as a translation of the SQuAD v1.1 development set. In terms of operationalization, one paper reports using the F1-score for assessment, while another notes using the "whole testset" for evaluation. XQuAD is often studied alongside other multilingual benchmarks such as MLQA and TyDiQA. A less common application mentioned by one study is its use, in conjunction with MGSM, to measure "sequential instruction-following capabilities."

## Sources

**[GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)**
> A benchmark dataset for evaluating multilingual extractive question answering across several languages.

**[Beyond Logit Lens: Contextual Embeddings for Robust Hallucination Detection & Grounding inVLMs](https://aclanthology.org/2025.naacl-long.489.pdf) (as "XQUAD")**
> Cross-lingual question answering benchmark assessing reading comprehension in multiple languages using F1-score.

## Relationships

### → XQuAD
- **Multilingual question answering** (behaviors tasks) — *measured_by*
  > However, efforts such as MLQA (Lewis et al., 2020) and XQuAD (Artetxe et al., 2019) have introduced datasets supporting multiple languages, facilitating cross-lingual evaluation of QA systems. (Section 5)
  - [GuideLLM: ExploringLLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.288.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > “Question Answering: We focus on 3 QA datasets 1) XQUAD (Artetxe et al., 2019)” (Section 4.1)
  - [Has this Fact been Edited? Detecting Knowledge Edits in Language Models](https://aclanthology.org/2025.naacl-long.493.pdf)

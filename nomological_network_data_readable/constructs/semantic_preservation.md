# Semantic preservation
**Type:** Construct  
**Referenced in:** 11 papers  
**Also known as:** Content preservation  

## State of the Field

Across the provided literature, semantic preservation is most commonly defined as the degree to which a transformed or stylized text retains the meaning of the original input. This concept is frequently applied in text generation tasks where, as one paper notes, "generating stylized responses must not compromise the original semantics" ("DRESSing Up LLM: Efficient Stylized Question-Answering via Style Subspace Editing"), and also in the context of adversarial attacks on watermarking, where modifications should maintain the original content. A less common application treats semantic preservation as the extent to which a subset of a dataset retains the semantic information of the full set. The construct is operationalized and measured in several ways; some papers use BERTScore to evaluate semantic similarity with contextual embeddings, while others employ the Semantic Similarity (SIM) measure from the ParaDetox benchmark. In the context of dataset subsetting, one paper quantifies it using the Wasserstein distance between text embeddings. The concept is studied in relation to Style transfer and Text quality.

## Sources

**[DRESSing Up LLM: Efficient Stylized Question-Answering via Style Subspace Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/09425891e393e64b0535194a81ba15b7-Paper-Conference.pdf)**
> The degree to which a stylized response retains the meaning of the original response rather than drifting in content.

**[Pareto Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf) (as "Content preservation")**
> The degree to which the semantic meaning of an input text is maintained in a transformed output text.

## Relationships

### Semantic preservation →
- **BERTScore** (measurements) — *measured_by*
  > "Evaluation metrics Our evaluation spans detection performance (AUC and accuracy), text quality (PPL and BLEU), semantic alignment (STS and BertScore)"
  - [Are Language Models Consequentialist or Deontological Moral Reasoners?](https://aclanthology.org/2025.emnlp-main.1564.pdf)
- **ParaDetox** (measurements) — *measured_by*
  > Semantic Similarity (SIM) measures to what extent the generated text preserves the meaning of the original input. (Section 4.1.1)
  - [Measuring scalar constructs in social science withLLMs](https://aclanthology.org/2025.emnlp-main.1636.pdf)

### Associated with
- **Style transfer** (behaviors tasks)
  - [Pareto Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf)
- **Text quality** (constructs)
  - [Multi-Modal Framing Analysis of News](https://aclanthology.org/2025.emnlp-main.1607.pdf)

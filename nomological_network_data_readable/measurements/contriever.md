# Contriever
**Type:** Measurement  
**Referenced in:** 8 papers  

## State of the Field

Across the provided literature, Contriever is consistently characterized as a dense retrieval model used for information retrieval and feature extraction. The most common framing describes it as a "text feature extractor" used to produce embeddings or feature representations from text samples. Several papers elaborate on this, defining it as a "general-purpose dense retriever" trained on web documents, with one study specifying it is an "unsupervised dense retrieval model trained using contrastive learning on text data without annotated pairs" (AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence). This unsupervised training is noted to enable the generation of "high-quality embeddings by learning directly from the structure of the corpus." In practice, it is used to retrieve top-k documents, sometimes as a component in a RAG pipeline or as a first-pass retriever whose outputs are subsequently reranked. The model is frequently mentioned alongside other retrievers like DPR and BM25. A specific variant, Contriever-MS MARCO, is also mentioned in one paper.

## Sources

**[Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf)**
> A text feature extractor used to produce embeddings for selected text samples in the file-selection procedure.

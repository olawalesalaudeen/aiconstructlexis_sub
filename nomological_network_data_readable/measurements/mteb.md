# MTEB
**Type:** Measurement  
**Referenced in:** 30 papers  

## State of the Field

Across the provided literature, MTEB (Massive Text Embedding Benchmark) is consistently defined as a comprehensive evaluation suite used to assess the performance of text embedding models. The most prevalent description characterizes it as a collection of 56 English tasks across seven or eight categories, though some papers focus on a subset, such as its ten semantic textual similarity (STS) tasks. Papers widely use MTEB to measure behaviors like information retrieval, semantic textual similarity, clustering, and classification, as well as reranking and summarization. It is also employed to operationalize and evaluate broader constructs such as representation quality, expressive power, and model generalization. Positioned as a "general-purpose" framework, it is sometimes contrasted with domain-specific alternatives or studied alongside other benchmarks like BEIR. While its use is widespread, one paper offers a note of caution, stating that "higher MTEB performance does not guarantee better downstream performance" ("PaSa: AnLLMAgent for Comprehensive Academic Paper Search"). Another source specifies that the benchmark's tasks "do not contain instructions" ("Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset").

## Sources

**[Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf)**
> The Massive Text Embedding Benchmark (MTEB) is a comprehensive evaluation suite used to assess the performance of text embedding models.

## Relationships

### → MTEB
- **Information retrieval** (behaviors tasks) — *measured_by*
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Semantic textual similarity** (behaviors tasks) — *measured_by*
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Text embedding** (behaviors tasks) — *measured_by*
  - [Layer by Layer: Uncovering Hidden Representations in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/skean25a/skean25a.pdf)
- **Reranking** (behaviors tasks) — *measured_by*
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Clustering** (behaviors tasks) — *measured_by*
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Expressive power** (constructs) — *measured_by*
  > For embedding performance we evaluate using the 56 main datasets from MTEB (Muennighoff et al., 2023c). (Section 3.1)
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > To validate the effectiveness and generalization ability of our proposed method, we followed the data selection strategy of e5-mistral-7b-instruct (Wang et al., 2023) and used only a small portion of the MTEB training dataset for zero-shot training. (Section 4.3)
  - [CoEvo: Coevolution ofLLMand Retrieval Model for Domain-Specific Information Retrieval](https://aclanthology.org/2025.emnlp-main.758.pdf)
- **Representation quality** (constructs) — *measured_by*
  > we conduct experiments on ten text similarity (STS) tasks in MTEB (Muennighoff et al., 2022) (Section 5.1)
  - [Layer by Layer: Uncovering Hidden Representations in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/skean25a/skean25a.pdf)

### Associated with
- **BEIR** (measurements)
  > Note that our model also attains
the highest scores in 15 retrieval tasks (commonly referred to as BEIR (Thakur et al., 2021)), 11
clustering tasks, and 12 classification tasks in the MTEB benchmark.
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)

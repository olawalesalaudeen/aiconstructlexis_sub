# Semantic textual similarity
**Type:** Behavior  
**Referenced in:** 21 papers  
**Also known as:** Semantic equivalence detection, Text similarity prediction, Text pair classification, Semantic similarity, Sentence similarity estimation, Sentence similarity, Sentence alignment, Text similarity computation, Semantic similarity judgment, Semantic text similarity  

## State of the Field

Across the provided literature, semantic textual similarity is predominantly characterized as the task of assessing the degree to which two pieces of text are similar in meaning. The most common framing involves predicting a continuous similarity score, as seen in definitions like "quantifying the degree of semantic similarity between two sentences, often on a continuous scale." A smaller body of work treats it as a classification or judgment task, such as determining whether two sentences are paraphrases, convey the same meaning, or are semantically related. Specific applications mentioned include "sentence alignment" between abstracts and summaries and "text pair classification" in the financial domain. The behavior is most frequently operationalized and measured using the Massive Text Embedding Benchmark (MTEB), with specific datasets like STS-Benchmark, STS12, QQP, and MRPC also cited. Alternative measurement approaches are also described, including the use of algorithms like BM25, prompting models like GPT-4o for judgment, and human evaluation. This behavior is frequently evaluated alongside other embedding tasks like classification, clustering, and retrieval, and is also documented as being related to the construct of Consistency.

## Sources

**[SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Semantic equivalence detection")**
> The task of determining whether two sentences convey the same meaning, potentially despite differences in their lexical and syntactic structure.

**[PiSSA: Principal Singular Values and Singular Vectors Adaptation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/db36f4d603cc9e3a2a5e10b93e6428f2-Paper-Conference.pdf) (as "Text similarity prediction")**
> Predicting the semantic similarity score between two text sentences.

**[LiteASR: Efficient Automatic Speech Recognition with Low-Rank Approximation](https://aclanthology.org/2025.emnlp-main.170.pdf) (as "Semantic similarity")**
> The observable task of assessing the degree to which two pieces of text are similar in meaning.

**[Dialect-SQL: An Adaptive Framework for Bridging the Dialect Gap in Text-to-SQL](https://aclanthology.org/2025.emnlp-main.179.pdf) (as "Text pair classification")**
> The observable behavior of determining whether two financial texts are semantically related, such as assessing if a headline matches a news article or if a query matches user intent.

**[DIDS: Domain Impact-aware Data Sampling for Large Language Model Training](https://aclanthology.org/2025.emnlp-main.216.pdf) (as "Sentence similarity estimation")**
> The task of quantifying the degree of semantic similarity between two sentences, often on a continuous scale.

**[CoVoGER: A Multilingual Multitask Benchmark for Speech-to-text Generative Error Correction with Large Language Models](https://aclanthology.org/2025.emnlp-main.321.pdf) (as "Sentence similarity")**
> Judging whether two sentences are semantically similar or paraphrases.

**[Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.697.pdf) (as "Sentence alignment")**
> Matching a sentence in a plain language summary to one or zero semantically similar sentences in the parallel abstract.

**[Analyzing values about gendered language reform inLLMs’ revisions](https://aclanthology.org/2025.emnlp-main.1278.pdf) (as "Text similarity computation")**
> The use of algorithms like BM25 or Sentence-BERT to compute similarity scores between text segments for retrieval and sampling decisions.

**[EmoAgent: Assessing and Safeguarding Human-AIInteraction for Mental Health Safety](https://aclanthology.org/2025.emnlp-main.595.pdf) (as "Semantic similarity judgment")**
> The observable behavior of comparing two text responses to determine whether their meaning is preserved, used here to detect changes in model output after neuron dropout.

**[Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)**
> The task of measuring the degree of semantic equivalence between two texts, typically on a continuous scale.

**[MMTEB: Massive Multilingual Text Embedding Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc0e3f908a2116ba529ad0a1530a3675-Paper-Conference.pdf) (as "Semantic text similarity")**
> The task of determining how similar two pieces of text are in meaning, typically by assigning a continuous score.

## Relationships

### Semantic textual similarity →
- **MTEB** (measurements) — *measured_by*
  > It includes data for various tasks including Retrieval, Reranking, Clustering, Classification, and STS. (Section 4.1)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **STS12** (measurements) — *measured_by*
  > Semantic Textual Similarity (STS): Directly measures the ability of embeddings to capture fine-grained semantic similarity. We use STSB, STS12 (both from MTEB (Muennighoff et al., 2023)) and SICK (from (Marelli et al., 2014)). (Section 4.1)
  - [Your Mixture-of-Experts LLM Is Secretly an Embedding Model for Free](https://proceedings.iclr.cc/paper_files/paper/2025/file/aed2049f68827943dda5a63b7c4ba0a2-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [SUGARCREPE++ Dataset: Vision-Language Model Sensitivity to Semantic and Lexical Alterations](https://proceedings.neurips.cc/paper_files/paper/2024/file/200661bf8f4993b7828a45a2a90f2ecf-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Consistency** (constructs)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)

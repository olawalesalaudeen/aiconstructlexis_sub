# Ranking
**Type:** Behavior  
**Referenced in:** 43 papers  
**Also known as:** Response re-ranking, Image reranking, Code reranking, Website reranking, Document reranking, Document relevance assessment, Zero-shot reranking, Zero-shot re-ranking, Passage re-ranking, Document re-ranking, Listwise reranking, Passage reranking, Re-ranking, Information reranking, Candidate re-ranking  

## State of the Field

Across the surveyed literature, the most prevalent framing of Ranking is as a 'reranking' process, where an initial list of retrieved candidates is re-evaluated and re-ordered to improve the final result. This behavior is applied to a wide variety of candidates, including documents, passages, images, code snippets, and even model-generated responses. The primary goal is consistently defined as improving the precision or relevance of the top-ranked results, or to "enhance top passage relevance" as one paper puts it ("Easy asPIE? Identifying Multi-Word Expressions withLLMs"). The performance of this behavior is commonly operationalized and measured using benchmarks such as MSMARCO, BEIR, and CodeSearchNet. While most definitions describe a two-stage retrieval-then-rerank pipeline, some work also explores variations like `zero-shot reranking`, which uses prompting without task-specific fine-tuning, and `listwise reranking`, which reorders items by considering their relative positions simultaneously. Beyond standard information retrieval, this behavior is also applied to mitigate hallucinations through "response re-ranking" ("ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models"). Some studies report that applying reranking can improve performance on downstream tasks, with one paper finding it "significantly improves mAP@5" in cross-modal retrieval ("MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS").

## Sources

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf)**
> Ranking a list of items according to their relevance to a query, one of the five task types included in Shopping MMLU.

**[STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Reranking")**
> The process of re-evaluating and re-ordering an initial set of retrieved candidates to improve the precision of the top-ranked results.

**[ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf) (as "Response re-ranking")**
> An observable procedure for hallucination mitigation where multiple candidate responses are generated, evaluated by an annotator model, and the one with the lowest predicted hallucination rate is selected.

**[INQUIRE: A Natural World Text-to-Image Retrieval Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4ad9c75f0d60ed75700f020adb3f705-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Image reranking")**
> The process of re-ordering an initial set of retrieved images using a more sophisticated model to improve the final ranking's relevance to a query.

**[CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf) (as "Code reranking")**
> The process of re-ordering an initial list of retrieved code snippets to improve the relevance of the final ranking.

**[MMSearch: Unveiling the Potential of Large Models as Multi-modal Search Engines](https://proceedings.iclr.cc/paper_files/paper/2025/file/04e6525463afaa460b5a2e6868b18f18-Paper-Conference.pdf) (as "Website reranking")**
> Selecting the most informative website from retrieved search results for downstream answer extraction.

**[BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e48f562a2c8f64c7404a6c3a518af74-Paper-Conference.pdf) (as "Document reranking")**
> Ranking retrieved documents so that the most relevant document is placed first.

**[MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf) (as "Zero-shot reranking")**
> The observable behavior of performing a reranking task using a model that has not been specifically fine-tuned for that task, relying instead on its pre-trained capabilities activated through prompting.

**[Training Large Language Models for Retrieval-Augmented Question Answering through Backtracking Correction](https://proceedings.iclr.cc/paper_files/paper/2025/file/80790082a3b0e4fa9061730ee876f5ba-Paper-Conference.pdf) (as "Document relevance assessment")**
> The observable task of evaluating one or more retrieved documents and making an explicit judgment about their relevance to a given query.

**[Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf) (as "Zero-shot re-ranking")**
> Ranking a set of retrieved documents by their relevance to a query without task-specific fine-tuning.

**[HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf) (as "Passage re-ranking")**
> Ranking a set of retrieved passages by relevance to a query and outputting an ordered list of document IDs.

**[From perception to production: how acoustic invariance facilitates articulatory learning in a self-supervised vocal imitation model](https://aclanthology.org/2025.emnlp-main.1218.pdf) (as "Document re-ranking")**
> The process of reordering a list of candidate documents based on their estimated relevance to a query, typically following an initial retrieval stage.

**[LLMs Behind the Scenes: Enabling Narrative Scene Illustration](https://aclanthology.org/2025.emnlp-main.125.pdf) (as "Listwise reranking")**
> The model reorders a list of passages by considering their relative positions and relevance simultaneously, producing a full ranking rather than pairwise or pointwise scores.

**[Detecting Knowledge Boundary of Vision Large Language Models by Sampling-Based Inference](https://aclanthology.org/2025.emnlp-main.1459.pdf) (as "Passage reranking")**
> The task of assigning fine-grained relevance scores to a list of candidate passages for a given query to produce a re-ordered, more relevant list.

**[R-TOFU: Unlearning in Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.266.pdf) (as "Re-ranking")**
> The process of re-ordering an initial list of retrieved candidates based on additional information or a refined query to improve the final ranking.

**[Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1041.pdf) (as "Information reranking")**
> Reordering a list of retrieved documents based on their relevance to a query, particularly in scenarios requiring reasoning beyond surface-level matching.

**[ComicScene154: A Scene Dataset for Comic Analysis](https://aclanthology.org/2025.emnlp-main.1609.pdf) (as "Candidate re-ranking")**
> The process of reordering an initial list of candidate entities to place the most accurate or relevant entity at the top.

## Relationships

### Ranking →
- **Cross-modal retrieval** (behaviors tasks) — *causes*
  > We find that MLLMs can be used as zero-shot rerankers to further boost retrieval accuracy in challenging tasks that require the understanding of multimodal queries, such as ... composed image retrieval. (Section 6)
  - [MM-EMBED: UNIVERSAL MULTIMODAL RETRIEVAL WITH MULTIMODAL LLMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/6d5d6afa9957cfc9142ba60e78a467e9-Paper-Conference.pdf)
- **CodeSearchNet** (measurements) — *measured_by*
  > For evaluation, we employ the CodeSearchNet and AdvTest text-to-code retrieval benchmarks... the top 100 results from our code retriever are passed to the reranker, with evaluation conducted using MRR@100.
  - [CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking](https://proceedings.iclr.cc/paper_files/paper/2025/file/285b0e63256699c04dbf2c8d4163fba4-Paper-Conference.pdf)
- **HELMET** (measurements) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **MS MARCO** (measurements) — *measured_by*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **Retrieval-augmented generation** (behaviors tasks) — *correlates*
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
- **BEIR** (measurements) — *measured_by*
  > We further evaluate QRRETRIEVER as a re-ranker on the standard BEIR benchmark (Thakur et al., 2021). (Section 1)
  - [Easy asPIE? Identifying Multi-Word Expressions withLLMs](https://aclanthology.org/2025.emnlp-main.1214.pdf)

### Associated with
- **Question answering** (behaviors tasks)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)

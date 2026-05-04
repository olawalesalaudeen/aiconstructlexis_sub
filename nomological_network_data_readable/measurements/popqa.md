# PopQA
**Type:** Measurement  
**Referenced in:** 54 papers  
**Also known as:** POPQA  

## State of the Field

Across the provided literature, PopQA is consistently characterized as an open-domain question answering (ODQA) dataset used to evaluate factual knowledge. Its most prevalent feature, mentioned in nearly all sources, is a focus on "long-tail knowledge" concerning rare or low-popularity entities. This emphasis is intended to test models on facts they are unlikely to have memorized, with one paper noting its questions are "difficult for LLMs to answer from parametric memory alone" (C-3PO: Compact Plug-and-Play Proxy Optimization to Achieve Human-like Retrieval-Augmented Generation). A smaller set of papers adds descriptive details, framing it as an "entity-centric" dataset derived from Wikidata triples and composed of "single-hop" queries. Primarily, PopQA is used to measure the behaviors of `Open-domain question answering` and `Question answering`. It is also frequently employed to evaluate a model's `Generalization` ability, particularly in out-of-domain evaluation settings.

## Sources

**[Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)**
> Open-domain question answering dataset focusing on rare entities, evaluating factual knowledge retrieval in long-tail scenarios.

**[Adaptive Chameleon  or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts](https://proceedings.iclr.cc/paper_files/paper/2024/file/99261adc8a6356b38bcf999bba9a26dc-Paper-Conference.pdf) (as "POPQA")**
> An entity-centric question answering dataset derived from Wikidata triples, used to evaluate LLMs on factual knowledge and memory consistency.

## Relationships

### → PopQA
- **Open-domain question answering** (behaviors tasks) — *measured_by*
  > Short-form generations tasks include two open-domain question answering (QA) datasets, PopQA (Mallen et al., 2023) and TriviaQA-unfiltered (Joshi et al., 2017)... (Section 4.1)
  - [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We demonstrate ADACAD’s effectiveness on a diverse range of tasks, covering question-answering (QA) and summarization, with six QA datasets (Natural Question (NQ; Kwiatkowski et al., 2019), NQ-SWAP (Longpre et al., 2021), TriviaQA (Joshi et al., 2017), PopQA (Mallen et al., 2023), HotpotQA (Yang et al., 2018), TabMWP (Lu et al., 2023)) (Section 1).
  - [Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting](https://proceedings.iclr.cc/paper_files/paper/2025/file/2ea06b52f613716e67458f5ab3fb7558-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [To Trust or Not to Trust? Enhancing Large Language Models' Situated Faithfulness to External Contexts](https://proceedings.iclr.cc/paper_files/paper/2025/file/186a213d720568b31f9b59c085a23e5a-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **Memorization** (constructs) — *measured_by*
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Factual knowledge** (constructs) — *measured_by*
  - [On Synthetic Data Strategies for Domain-Specific Generative Retrieval](https://aclanthology.org/2025.acl-long.393.pdf)

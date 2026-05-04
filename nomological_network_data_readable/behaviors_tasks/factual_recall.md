# Factual recall
**Type:** Behavior  
**Referenced in:** 9 papers  
**Also known as:** Multi-hop factual recall, Single-hop factual recall  

## State of the Field

In the provided literature, factual recall is characterized as the observable task of answering factual questions, with a common distinction made between single-hop and multi-hop variants. Single-hop recall is defined as answering a direct question where only one fact needs to be retrieved, such as "What is the capital city of Spain?". In contrast, multi-hop factual recall is a more complex task requiring the model to chain together two or more pieces of information. This multi-hop variant is specifically discussed in the context of knowledge editing, where it assesses if a model can "leverage the updated knowledge for reasoning". One paper notes that models often "struggle with multi-hop factual recall tasks involving newly edited knowledge" even while they "perform well on single-hop fact recall tasks". To operationalize and evaluate this behavior, researchers employ a range of question-answering benchmarks. The provided sources indicate that factual recall is measured using datasets such as TriviaQA, Natural Questions, WebQuestions, CounterFact, MMLU, and ARC. The concept is also studied in relation to the construct of factuality and the topics of in-context reasoning and language modeling.

## Sources

**[Locate-then-edit for Multi-hop Factual Recall under Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aq/zhang25aq.pdf) (as "Multi-hop factual recall")**
> The observable task of answering a question that requires chaining together two or more pieces of factual information, particularly after one of the facts in the chain has been edited.

**[Locate-then-edit for Multi-hop Factual Recall under Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aq/zhang25aq.pdf) (as "Single-hop factual recall")**
> Correctly answering a direct factual question where the subject is explicitly stated and only one fact needs to be retrieved.

## Relationships

### Factual recall →
- **CounterFact** (measurements) — *measured_by*
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)
- **TriviaQA** (measurements) — *measured_by*
  > “We plot the accuracy versus sparsity for the OPT-13B, OPT-30B, LLaMA-13B, and LLaMA-33B models on TriviaQA dataset for fact recall evaluation (left)”
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  > We consider nine varied downstream tasks: ... (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019))
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)
- **ARC** (measurements) — *measured_by*
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)
- **WebQuestions** (measurements) — *measured_by*
  > We consider nine varied downstream tasks: ... (f) fact recall (WebQuestions (Berant et al., 2013), Natural Questions (Kwiatkowski et al., 2019))
  - [Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks](https://aclanthology.org/2025.naacl-long.618.pdf)

### Associated with
- **Factuality** (constructs)
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **In-context reasoning** (constructs)
  - [Distributional Associations vs In-Context Reasoning: A Study of Feed-forward and Attention Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/533a89d7c2980218d82dbe3ea85f77ae-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  - [Understanding Factual Recall in Transformers via Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bf9f909c24c8879d1b7f86fa50a9e49-Paper-Conference.pdf)

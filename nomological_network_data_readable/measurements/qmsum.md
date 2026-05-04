# QMSum
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

QMSum is consistently characterized across the provided literature as a query-based, multi-domain meeting summarization dataset, and is frequently identified as part of the SCROLL benchmark. The dataset is composed of meeting transcripts from various domains, such as academic and industrial settings, which are paired with questions and their corresponding summaries. One paper provides an example of a query: “What did the group discuss about budget balancing?”. The transcripts are described as being from "realistic multi-party meetings". In terms of its application, QMSum is most commonly used to measure different facets of summarization, including `Text summarization`, `Dialogue summarization`, and what one study terms "global summarization" by using the dataset's "general queries". Beyond this primary function, it is also employed to assess broader capabilities like `Generalization`, `Length generalization` for long sequences, and overall `Text generation quality`. The ROUGE-1 score is mentioned as a metric used for evaluation on this benchmark. Additionally, QMSum serves as a source of data for constructing other benchmarks.

## Sources

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)**
> A query-based multi-domain meeting summarization dataset from the SCROLL benchmark.

## Relationships

### → QMSum
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Moreover, the choice of the four datasets, which include short- and long-form generation, question answering, summarization, and multi-hop reasoning, demonstrates the generalizability of the Sparse RAG approach. (Section 1)
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [Accelerating Inference of Retrieval-Augmented Generation via Sparse Context Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/411fa9d368b5485be4c6bb62615b365e-Paper-Conference.pdf)
- **Dialogue summarization** (behaviors tasks) — *measured_by*
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)

### Associated with
- **SCROLLS** (measurements)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)

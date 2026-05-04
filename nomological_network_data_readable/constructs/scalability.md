# Scalability
**Type:** Construct  
**Referenced in:** 84 papers  
**Also known as:** Scaling ability, Context-aware scaling, Inference scaling, Scaling with inference-time compute, Test-time compute scaling  

## State of the Field

Across the surveyed literature, 'Scalability' is a multifaceted construct most commonly referring to either a system's performance improvement with increased resources or its capacity to handle large-scale inputs and systems efficiently. One prevalent line of work frames scalability as the predictable improvement in model performance as model capacity, sparse parameters, or training dataset size increases, a concept closely related to `Scaling laws`. Another frequently discussed variant is 'inference scaling' or 'test-time scaling,' where performance is enhanced by allocating more computational resources at inference, such as through additional search steps, which is reported to improve outcomes in behaviors like `Code debugging`. A separate but also common usage defines scalability as the ability to handle large inputs, such as 'large table corpora' ('OpenTab'), or to extend a system to more languages or models without a proportional increase in computational cost. Less common definitions describe scalability as an internal 'context-aware scaling' mechanism within attention, or as the maintained effectiveness of an attack method on a growing knowledge base. The construct is operationalized and measured using various instruments; for instance, the `MUSE` benchmark is used to evaluate scalability with respect to the size of removal requests, and performance on `GSM8k` is also used as a measure. Scalability is studied alongside constructs like `Generalization` and `Memorization`, and some work suggests that behaviors like `Chain-of-thought reasoning` can improve it. Furthermore, scalability is sometimes positioned as a driver of `Emergent abilities`.

## Sources

**[Magnushammer: A Transformer-Based Approach to Premise Selection](https://proceedings.iclr.cc/paper_files/paper/2024/file/ab5f5f22e3e09f4424592ffb06840ab0-Paper-Conference.pdf)**
> The capacity to handle large table corpora and large tables while staying within token and computational limits.

**[Ultra-Sparse Memory Network](https://proceedings.iclr.cc/paper_files/paper/2025/file/d78d68cae595fabadd187b583ee8708e-Paper-Conference.pdf) (as "Scaling ability")**
> The extent to which model performance improves predictably as model capacity or sparse parameters increase.

**[Systematic Outliers in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e23bee2df5fc72018d9d74d875d7cf3-Paper-Conference.pdf) (as "Context-aware scaling")**
> The tendency for internal mechanisms to dynamically adjust attention magnitude based on input context, reducing unnecessary updates for some tokens while emphasizing others.

**[SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf) (as "Inference scaling")**
> The degree to which a model's performance on a task improves as more computational resources are allocated at inference time, for instance by generating and evaluating more candidate solutions.

**[Large Language Models to Diffusion Finetuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cetin25a/cetin25a.pdf) (as "Test-time compute scaling")**
> The latent ability of a model to improve its performance by allocating more computational resources during inference, with accuracy increasing monotonically as more steps are taken.

**[AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf) (as "Scaling with inference-time compute")**
> The ability of the model to improve performance proportionally as more inference-time compute (LLM calls) is allocated, without diminishing returns.

**[Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf) (as "Scaling behavior")**
> The tendency for performance gains to change systematically as dataset size, compute, or model size increases.

**[TurboRAG: Accelerating Retrieval-Augmented Generation with PrecomputedKVCaches for Chunked Text](https://aclanthology.org/2025.emnlp-main.335.pdf) (as "Test-time scaling")**
> The phenomenon where model performance improves as a function of increased computational effort during inference, such as through more search steps or deeper exploration.

## Relationships

### Scalability →
- **Emergent abilities** (constructs) — *causes*
  - [Neural Residual Diffusion Models for Deep Scalable Vision Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d51ceadaf09a4699f18986702df24987-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Neuro-Symbolic Data Generation for Math Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/29d319f7c1513c9ecd81d3a6e9632a6e-Paper-Conference.pdf)
- **MUSE** (measurements) — *measured_by*
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Utility preservation** (constructs) — *measured_by*
  > The performance of GA, NPO, and their regularized variants, measured by utility preservation, degrades with larger forget set sizes (a) and sequential unlearning requests (b). (Figure 6)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Code debugging** (behaviors tasks) — *causes*
  > Our algorithm yields a significant boost in performance compared to best-of-N and self-repair, and also exhibits strong generalisation across datasets and models. Moreover, our approach shows stronger scaling with inference-time compute budget compared to baselines.
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)

### → Scalability
- **Chain-of-thought reasoning** (constructs) — *causes*
  > Our analysis shows that CoT reasoning is crucial for unlocking DPO’s potential, as it mitigates reward hacking, strengthens discriminative capabilities, and improves scalability. (Section 5.1)
  - [KatFishNet: DetectingLLM-GeneratedKorean Text through Linguistic Feature Analysis](https://aclanthology.org/2025.acl-long.1031.pdf)
- **In-context learning** (constructs) — *causes*
  - [Iterative Vectors: In-Context Gradient Steering without Backpropagation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25j/liu25j.pdf)
- **Noise robustness** (constructs) — *causes*
  - [RAGGED: Towards Informed Design of Scalable and Stable RAG Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsia25a/hsia25a.pdf)

### Associated with
- **Scaling laws** (measurements)
  - [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf)
- **Generalization** (constructs)
  > This paper aims to evaluate and rethink the generalization capability of the SKP paradigm from four perspectives including Granularity, Transferability, Scalability, and Universality. (Abstract)
  - [Multimodal Transformers are Hierarchical Modal-wise Heterogeneous Graphs](https://aclanthology.org/2025.acl-long.110.pdf)
- **Memorization** (constructs)
  > we propose a simple statistical ansatz based on memorization to study scaling laws in the context of inference. (Abstract)
  - [A Simple Model of Inference Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/levi25a/levi25a.pdf)

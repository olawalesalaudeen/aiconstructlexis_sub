# MNLI
**Type:** Measurement  
**Referenced in:** 52 papers  
**Also known as:** SMNLI  

## State of the Field

Across the provided literature, MNLI (Multi-Genre Natural Language Inference) is consistently characterized as a benchmark for measuring Natural Language Inference (NLI). The task it operationalizes is most commonly described as a multi-class classification problem where a model must determine if a "premise" sentence entails, contradicts, or is neutral with respect to a "hypothesis" sentence. Papers frequently use MNLI to evaluate a model's language understanding capabilities, and its results are sometimes treated as a general indicator of downstream task performance, as one study notes, "we use the results on MNLI... to indicate the performance on downstream tasks" (Fast-ELECTRA for Efficient Pre-training). The benchmark is very often situated within the broader GLUE benchmark, studied alongside other NLI datasets like QNLI and RTE.

While its primary use is for general NLI evaluation, a smaller set of studies employ specific versions of the dataset for more targeted analysis. For instance, some papers use its "hard-match" and "hard-mismatch" versions to assess model generalization and robustness to out-of-distribution data. A distinct, synthetic variant named SMNLI is also described in one paper, created by subsampling MNLI to intentionally induce spurious correlations for evaluation purposes. The benchmark is applied in diverse evaluation contexts, including assessing the accuracy of compressed models after pruning and the performance of models in privacy-preserving federated learning settings.

## Sources

**[Accurate Retraining-free Pruning for Pretrained Encoder-based Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/45fc8e1c55df116b23488f3cdb2fc642-Paper-Conference.pdf)**
> A natural language inference benchmark used to evaluate entailment classification across sentence pairs.

**[Focus On This, Not That! Steering LLMs with Adaptive Feature Specification](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lamb25a/lamb25a.pdf) (as "SMNLI")**
> A synthetic Natural Language Inference (NLI) dataset created by subsampling the MNLI dataset to induce specific spurious correlations between text genres and labels for evaluation purposes.

## Relationships

### → MNLI
- **Natural language inference** (behaviors tasks) — *measured_by*
  > natural language inference and entailment: ANLI-R{1,2,3} (Nie et al., 2020), CB (De Marneffe et al., 2019), RTE, QNLI (QA/NLI), MNLI (Williams et al., 2018). (Section 5.1)
  - [Linear Log-Normal Attention with Unbiased Concentration](https://proceedings.iclr.cc/paper_files/paper/2024/file/b57939005a3cbe40f49b66a0efd6fc8c-Paper-Conference.pdf)
- **Natural language understanding** (constructs) — *measured_by*
  > These datasets encompass various typical language understanding tasks such as natural language inference. (Section 5.1)
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **Zero-shot task performance** (behaviors tasks) — *measured_by*
  - [Plug-and-Play: An Efficient Post-training Pruning Method for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/db6ccc979860d7a233ecaf588bb23512-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > “we assess its performance on paraphrase detection using the QQP dev set, natural language inference (NLI) using both the MNLI matched and mismatched dev sets, and commonsense reasoning using the SWAG dev set.”
  - [MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval](https://aclanthology.org/2025.emnlp-main.1583.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): ... and Natural Language Inference (MNLI, RTE, QNLI).
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks)
  > Paraphrasing datasets like PAWS (Zhang et al., 2019) are common pretraining datasets, and standard NLI datasets like MNLI (Williams et al., 2018) contain many similar samples due to their construction through edits, so NLI predictions are expected to be more reliable on these pairs. (Section 4.3)
  - [Auto-GDA: Automatic Domain Adaptation for Efficient Grounding Verification in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/7eb6233e02f7d9efbb84acd839a996fb-Paper-Conference.pdf)

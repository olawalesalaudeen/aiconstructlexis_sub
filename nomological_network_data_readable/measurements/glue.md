# GLUE
**Type:** Measurement  
**Referenced in:** 146 papers  
**Also known as:** GLUE benchmark  

## State of the Field

Across the surveyed literature, GLUE (General Language Understanding Evaluation) is consistently defined as a benchmark suite or collection of diverse tasks used to evaluate model performance. Its most prevalent application is to measure the construct of "Natural language understanding," a purpose supported by a vast number of papers. A smaller body of work also uses GLUE to assess other capabilities such as "Text classification," "Generalization," "Adversarial robustness," and "Parameter efficiency." The benchmark is operationalized through a set of sub-tasks that papers frequently identify, including sentiment analysis (SST-2), paraphrasing (MRPC, QQP), natural language inference (MNLI, QNLI, RTE), and linguistic acceptability (CoLA). While most commonly employed in a fine-tuning context, as one study notes, "Our fine-tuning set-up for each GLUE task matches that of the original paper" ("Sudden Drops in the Loss..."), some research also uses it for zero-shot or few-shot evaluations. For instance, one paper specifies that "GLUE tasks are tested with 2-shot examples in context" ("HIGGS..."). The benchmark is used to evaluate a wide range of models and methods, with performance often reported as an average score across its constituent tasks.

## Sources

**[A Good Learner can Teach Better: Teacher-Student Collaborative Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a781ff9cfb267277937db1818284739f-Paper-Conference.pdf)**
> A collection of natural language understanding tasks including sentiment analysis, textual entailment, and paraphrasing, used to evaluate model performance across diverse NLP benchmarks.

**[Encryption-Friendly LLM Architecture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6715b4e97be055687c1ecaf33913d358-Paper-Conference.pdf) (as "GLUE benchmark")**
> The General Language Understanding Evaluation (GLUE) benchmark is a collection of diverse natural language understanding tasks used to evaluate model performance.

## Relationships

### → GLUE
- **Natural language understanding** (constructs) — *measured_by*
  > We compare our approach with LoRA and other parameter-efficient adaptation methods on the natural language understanding (GLUE) and natural language generation (E2E) benchmarks... (Section 1)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  > We first evaluate the language understanding tasks from the GLUE benchmark(Wang et al., 2018) including MNLI, SST2, QNLI and QQP using the RoBERTa model.
  - [Representation Deficiency in Masked Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfde7fb279709eff53faa074b45840d8-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [On the Optimization Landscape of Low Rank Adaptation Methods for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c34262c35aa5f8c1a091822cbb2020c2-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  > We evaluate on the GLUE benchmark, where we exclude the RTE dataset due to high standard deviations in the obtained scores. (Section 4.1)
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > "Additional evaluation of SMAAT on language understanding benchmarks, including GLUE and advGLUE are reported in Appendix E."
  - [Soft Syntactic Reinforcement for Neural Event Extraction](https://aclanthology.org/2025.naacl-long.480.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  > To further assess preservation of language modeling capability, we also evaluated on downstream tasks: MLMs on GLUE tasks... (Section 3.3).
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > “Existing research evaluates adversarial robustness of LLMs on the GLUE dataset (Wang et al., 2018)”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **Masked language modeling** (behaviors tasks) — *measured_by*
  - [Headless Language Models: Learning without Predicting with Contrastive Weight Tying](https://proceedings.iclr.cc/paper_files/paper/2024/file/92864e1191ed272deb0914b3bb50f97c-Paper-Conference.pdf)
- **Parameter efficiency** (constructs) — *measured_by*
  > Our method achieves comparable performance to LoRA on the General Language Understanding Evaluation (GLUE) benchmark while using only half the parameters. (Section 1)
  - [AID: Adaptive Integration of Detectors for SafeAIwith Language Models](https://aclanthology.org/2025.naacl-long.230.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  > We finetune the pretrained RoBERTa-base model (Liu et al., 2019) on the GLUE benchmark, a widely used suite for evaluating NLP models across various tasks, including sentiment analysis and question answering (Wang et al., 2019). (Section 4.2)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.71.pdf)
- **Sentiment analysis** (behaviors tasks) — *measured_by*
  > We finetune the pretrained RoBERTa-base model (Liu et al., 2019) on the GLUE benchmark, a widely used suite for evaluating NLP models across various tasks, including sentiment analysis and question answering (Wang et al., 2019). (Section 4.2)
  - [Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models](https://aclanthology.org/2025.naacl-long.71.pdf)
- **Few-shot learning** (measurements) — *measured_by*
  - [On the Crucial Role of Initialization for Matrix Factorization](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d67ec04032cccf4a21d04c0ae4ab268-Paper-Conference.pdf)
- **Model merging** (behaviors tasks) — *measured_by*
  - [CABS: Conflict-Aware and Balanced Sparsification for Enhancing Model Merging](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25x/yang25x.pdf)
- **Language proficiency** (constructs) — *measured_by*
  > To assess the significance of the localized units on the models’ linguistic abilities, we utilize three widely used benchmarks that measure formal linguistic competence (Mahowald et al., 2024). ... Third, GLUE...
  - [HIGGS: Pushing the Limits of Large Language Model Quantization via the Linearity Theorem](https://aclanthology.org/2025.naacl-long.544.pdf)
- **Language processing** (constructs) — *measured_by*
  - [HIGGS: Pushing the Limits of Large Language Model Quantization via the Linearity Theorem](https://aclanthology.org/2025.naacl-long.544.pdf)
- **Sequence classification** (behaviors tasks) — *measured_by*
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
- **Utility preservation** (constructs) — *measured_by*
  > For General Capability, we measure that using the average of six GLUE metrics in Section 4.5. (Figure 3 caption)
  - [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf)
- **Memory efficiency** (constructs) — *measured_by*
  > The control approach demonstrates the lowest GPU memory usage, requiring only 12.634 GB, which is 1.396 GB less than LoRA and 3.652 GB less than DoRA. (Section 5.2)
  - [From Weight-Based to State-Based Fine-Tuning: Further Memory Reduction on LoRA with Parallel Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25au/zhang25au.pdf)
- **Conceptual understanding** (constructs) — *measured_by*
  - [Bridging the Gap Between Molecule and Textual Descriptions via Substructure-aware Alignment](https://aclanthology.org/2025.emnlp-main.1198.pdf)

### Associated with
- **SST-2** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): Sentiment Analysis (SST-2)...
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
- **MRPC** (measurements)
  > ...we omit the time-intensive MNLI and QQP tasks, thus forgoing the use of the MNLI trick3 for tasks MRPC, RTE, and STS-B. (Section 4.1)
  - [Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy](https://proceedings.iclr.cc/paper_files/paper/2024/file/3d09a88c3372cdb79401fde592ca4db8-Paper-Conference.pdf)
- **QQP** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): Sentiment Analysis (SST-2), Duplicate Question Detection (QQP)...
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
- **RTE** (measurements)
  > Table 1: DeBERTaV3-base fine-tuning on GLUE benchmark. ... RTE ... (Acc)
  - [Prompt Tuning Strikes Back: Customizing Foundation Models with Low-Rank Prompt Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/548551c07a68c8f0a87d67c6167cedb1-Paper-Conference.pdf)
- **QNLI** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): ... and Natural Language Inference (MNLI, RTE, QNLI).
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
- **MNLI** (measurements)
  > we consider the following five challenging tasks in GLUE dataset (Wang et al., 2018): ... and Natural Language Inference (MNLI, RTE, QNLI).
  - [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf)
- **CoLA** (measurements)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)
- **WNLI** (measurements)
  > RTE and WNLI (both from GLUE)
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)

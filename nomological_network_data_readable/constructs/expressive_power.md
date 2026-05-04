# Expressive power
**Type:** Construct  
**Referenced in:** 78 papers  
**Also known as:** Representation capability, Representation capacity, Representational capability, Representational capacity, Expressiveness, Expressivity, Representation power, Expressive capacity, Model expressiveness, Semantic representational power, Computational power, Robust predictive power, Low-rank expressiveness, Preference expressiveness, Computational expressivity, Discriminative power, Function approximation power, Simulation power, Representation capabilities  

## State of the Field

Across the surveyed literature, "Expressive power" is most commonly defined as the range and complexity of functions or tasks a model architecture is capable of representing or solving. A closely related and frequent framing describes it as the latent ability of a model to form high-quality internal representations or embeddings that capture complex patterns and semantic relationships. A recurring line of inquiry operationalizes this concept theoretically, characterizing it as the set of formal languages or computational problems a model can solve, often in terms of circuit complexity classes like TC0 or PTIME; for instance, one paper shows that "prompting is Turing-complete," while others link Chain-of-Thought reasoning to an expansion of expressiveness. In the context of parameter-efficient fine-tuning, expressive power is frequently discussed as a capability constrained by low-rank adaptation methods, with many studies noting that the "low-rank constraint limits the expressive capacity of LoRA," creating a trade-off with parameter efficiency. The construct is operationalized and measured through performance on downstream tasks, with its "representational capability" for text embeddings evaluated using the MTEB benchmark and other work using LLM-as-a-judge procedures. Enhanced expressive power is reported to influence performance on several downstream behaviors, with some studies arguing it boosts capabilities in mathematical reasoning, code generation, and personalization. While the focus is often on general function approximation, a smaller set of papers defines more specific variants, such as "semantic representational power" for capturing word relationships, "simulation power" for generating synthetic data, or "preference expressiveness" for modeling complex human preferences.

## Sources

**[Efficient Learning with Sine-Activated Low-Rank Matrices](https://proceedings.iclr.cc/paper_files/paper/2025/file/112d8e0c7563de6e3408b49a09b4d8a3-Paper-Conference.pdf) (as "Representational capacity")**
> The degree to which a model's parameterization can encode complex signals or functions while maintaining compactness.

**[Ask, and it shall be given: On the Turing completeness of prompting](https://proceedings.iclr.cc/paper_files/paper/2025/file/123d3e814e257e0781e5d328232ead9b-Paper-Conference.pdf)**
> The range and complexity of functions or tasks that a model is capable of performing or representing.

**[Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf) (as "Representational capability")**
> The latent ability of a model to produce high-quality numerical vector representations (embeddings) of text for tasks like retrieval, clustering, and semantic similarity.

**[Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf) (as "Representation capability")**
> The ability of a model architecture to capture and store information, such as global context, within its token representations.

**[MoS: Unleashing Parameter Efficiency of Low-Rank Adaptation with Mixture of Shards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e574db41163e700545ff4114f96b3d7a-Paper-Conference.pdf) (as "Representation capacity")**
> The model's latent ability to form internal representations sufficient for solving a range of tasks, which can be constrained by parameter sharing or rank.

**[Language Models Need Inductive Biases to Count Inductively](https://proceedings.iclr.cc/paper_files/paper/2025/file/378226e5df7eded3e401de5c9493143c-Paper-Conference.pdf) (as "Expressivity")**
> The range of functions or computational problems that a model architecture is theoretically capable of representing or solving.

**[RandLoRA: Full rank parameter-efficient fine-tuning of large models](https://proceedings.iclr.cc/paper_files/paper/2025/file/382b95a6580cfb0b5ca33c74b4e0e770-Paper-Conference.pdf) (as "Representation power")**
> The inherent capacity of a model's parameterization to capture complex functions and patterns required for downstream tasks.

**[Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf) (as "Expressiveness")**
> The capacity of a model's parameter space, such as a prompt, to represent complex functions and capture fine-grained, client-specific patterns.

**[RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf) (as "Expressive capacity")**
> The ability of a model or adaptation method to represent or approximate complex functions, often related to the effective rank of its parameter updates.

**[ComLoRA: A Competitive Learning Approach for Enhancing LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/e993102e60e4484686f0bafe7ba8b8f2-Paper-Conference.pdf) (as "Model expressiveness")**
> The degree to which a fine-tuned model can represent complex patterns and tasks with limited adaptation capacity.

**[Rethinking Evaluation of Sparse Autoencoders through the Representation of Polysemous Words](https://proceedings.iclr.cc/paper_files/paper/2025/file/380a0b16a7e6f8c5010f798c9f2d3c61-Paper-Conference.pdf) (as "Semantic representational power")**
> The capacity of a model's internal representations to accurately capture and preserve the semantic relationships between words or concepts.

**[Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf) (as "Computational power")**
> The set of problems or formal languages that a given neural network architecture is theoretically capable of solving, defining the upper and lower bounds on its reasoning capabilities.

**[Filtered not Mixed: Filtering-Based Online Gating for Mixture of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d4c2f25bf0c33065b7d4fb9be2a9add1-Paper-Conference.pdf) (as "Robust predictive power")**
> The latent ability of an ensemble model to maintain high predictive performance by optimally and adaptively aggregating the predictions of its constituent expert models.

**[Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ab/huang25ab.pdf) (as "Function approximation power")**
> The latent ability of a model to represent complex or discontinuous functions by projecting onto appropriate basis functions, such as wavelets, enabling effective modeling of non-smooth signals.

**[Uncertainty Quantification for LLM-Based Survey Simulations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25am/huang25am.pdf) (as "Simulation power")**
> The capacity of an LLM to generate a large number of diverse and representative synthetic samples before its simulated distribution deviates significantly from the target population, as quantified by the selected sample size bk.

**[From Low Rank Gradient Subspace Stabilization to Low-Rank Weights: Observations, Theories, and Applications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jaiswal25a/jaiswal25a.pdf) (as "Low-rank expressiveness")**
> The degree to which a model's weight matrix can be accurately approximated by a low-rank decomposition, reflecting underlying structural efficiency and convergence during training.

**[AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf) (as "Discriminative power")**
> The ability of a PRM to accurately distinguish between correct and incorrect reasoning steps, especially at fine-grained (e.g., token) levels.

**[Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf) (as "Computational expressivity")**
> The capacity of a model to represent complex computational functions, particularly those beyond the circuit complexity of transformers and linear SSMs, such as non-linear and non-diagonal state transitions.

**[Beyond Bradley-Terry Models: A General Preference Model for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25de/zhang25de.pdf) (as "Preference expressiveness")**
> The extent to which a model can represent rich, complex preference relations rather than only simple scalar-ordering assumptions.

**[A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Representation capabilities")**
> The degree to which a model's learned embeddings of antibody sequences effectively capture the biological information necessary for downstream tasks like binding prediction.

## Relationships

### Expressive power →
- **MTEB** (measurements) — *measured_by*
  > For embedding performance we evaluate using the 56 main datasets from MTEB (Muennighoff et al., 2023c). (Section 3.1)
  - [Generative Representational Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/70cf215430492f7d34830a24e744b3f1-Paper-Conference.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  > The proposed method increases expressivity by redesigning two primary attention modules to improve categorical and numerical reasoning capabilities.
  - [RaSA: Rank-Sharing Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4fd162d3e2d015233486a2e313828a7-Paper-Conference.pdf)
- **Personalization** (constructs) — *causes*
  > The residual term is crucial for retaining the expressiveness lost during the factorization process, thereby preserving the client-specific learning and improving personalization (Section 1).
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *causes*
  - [Over-Tokenized Transformer: Vocabulary is Generally Worth Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25bb/huang25bb.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [TACO: Enhancing Multimodal In-context Learning via Task Mapping-Guided Sequence Configuration](https://aclanthology.org/2025.emnlp-main.40.pdf)

### → Expressive power
- **Information retrieval** (behaviors tasks) — *causes*
  > Our positive results showing that enhancing in-context retrieval can improve RNNs’ representation power hold for vanilla Linear RNNs, and can be easily extended to more complex architectures. (Section 1)
  - [RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *causes*
  - [RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/79dc391a2c1067e9ac2b764e31a60377-Paper-Conference.pdf)
- **Reward hacking** (behaviors tasks) — *causes*
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf)

### Associated with
- **Parameter efficiency** (constructs)
  > frequency-domain decomposition with carefully selected frequency components can surpass the expressivity of traditional low-rank-based methods
  - [SLTrain: a sparse plus low rank approach for parameter and memory efficient pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/d63cf0622eed012a17fe88fced64dcb8-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
- **Learnability** (constructs)
  - [How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf)
- **Molecule understanding** (behaviors tasks)
  - [A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf)
- **In-context learning** (constructs)
  - [Why In-Context Learning Models are Good Few-Shot Learners?](https://proceedings.iclr.cc/paper_files/paper/2025/file/6c7ca1889f01a9b767c631686fb5fd24-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks)
  > In this paper, we propose a kernel interpretation for the autoregressive setting. We introduce a framework to rigorously analyze the expressivity of deep Transformers in next-token prediction. (Section 1)
  - [Towards Understanding the Universality of Transformers for Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/d846c59be138a704e800f36e7fcb696a-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs)
  > traditional performance metrics like Mean Squared Error and L0 sparsity ignore the evaluation of the semantic representational power of SAEs — whether they can acquire interpretable monosemantic features while preserving the semantic relationship of words
  - [Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **Uniformity** (constructs)
  - [QualiSpeech: A Speech Quality Assessment Dataset with Natural Language Reasoning and Descriptions](https://aclanthology.org/2025.acl-long.1151.pdf)

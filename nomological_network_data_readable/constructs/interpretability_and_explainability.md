# Interpretability and explainability
**Type:** Construct  
**Referenced in:** 290 papers  
**Also known as:** Explainability, Interpretability, Manner, Interpretive ability, Weight-based interpretability, Interpretable learning, Intrinsic interpretability, Feature interpretability, Model interpretability, Mechanistic interpretability, Explanation, Human auditability, Transparency and interpretability, Output transparency, System transparency, Algorithmic understanding  

## State of the Field

Across the surveyed literature, interpretability and explainability are widely discussed constructs referring to the degree to which a model's internal processes and outputs can be understood by humans. The most prevalent definition of interpretability centers on assigning concise, human-understandable meaning to learned features or representations, a focus common in work on sparse autoencoders. In contrast, explainability is more frequently defined as the system's ability to provide a rationale or justification for its predictions. A distinct line of work also investigates "mechanistic interpretability," which aims to reverse-engineer a model's internal computations into understandable circuits, while related concepts like "transparency" and "human auditability" are also explored. The field operationalizes these constructs through several methods, with automated evaluation frequently performed using an LLM-as-a-judge to rate feature comprehensibility, alongside specialized instruments like SAE Bench. Human evaluation is also a common approach, where experts or crowdworkers assess the quality of explanations or the clarity of learned features, sometimes aided by interfaces like Neuronpedia. Several model capabilities are reported to enhance interpretability, with chain-of-thought reasoning and retrieval-augmented systems being frequently mentioned for their ability to generate traceable rationales. These constructs are often studied alongside `Faithfulness` and `Steerability`, and one paper notes a potential trade-off with `Expressive power`, while `Polysemanticity` is identified as a central obstacle.

## Sources

**[An interpretable error correction method for enhancing code-to-code translation](https://proceedings.iclr.cc/paper_files/paper/2024/file/5e01f4ef7ffeedf3317a44461d18df9d-Paper-Conference.pdf) (as "Interpretability")**
> The degree to which a learned feature or representation can be given a concise, human-understandable explanation that predicts its activations.

**[Beam Enumeration: Probabilistic Explainability For Sample Efficient Self-conditioned Molecular Design](https://proceedings.iclr.cc/paper_files/paper/2024/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf) (as "Explainability")**
> The extent to which the system provides a rationale that helps users understand why a prediction was made.

**[StrucText-Eval: Evaluating Large Language Model’s Reasoning Ability in Structure-Rich Text](https://aclanthology.org/2025.acl-long.12.pdf) (as "Clarity")**
> The degree to which a hypothesis is understandable and clearly articulated, enabling effective use by humans or models.

**[Capture the Key in Reasoning to EnhanceCoTDistillation Generalization](https://aclanthology.org/2025.acl-long.22.pdf) (as "Manner")**
> The latent ability of a model to express its contributions clearly and with appropriate complexity for the task at hand.

**[KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.930.pdf) (as "Transparency")**
> The degree to which the embedding dimensions correspond to human-interpretable lexical units, allowing inspection of model decisions through cluster weights.

**[Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.188.pdf) (as "Interpretive ability")**
> The capacity to apply hierarchical legal interpretation methods—literal, systematic, purposive, sociological, and historical—to clarify the meaning and application of legal texts in context.

**[Bilinear MLPs enable weight-based mechanistic interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7504142a20a3e1fe9dd7de42f475828c-Paper-Conference.pdf) (as "Weight-based interpretability")**
> The property of a model where its computational mechanisms can be understood by directly analyzing its weight parameters, rather than relying on activation patterns over a dataset.

**[Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf) (as "Interpretable learning")**
> The ability to extract compact, human-understandable predictive rules from labeled data and apply them consistently across examples.

**[Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf) (as "Intrinsic interpretability")**
> The degree to which an LLM’s internal representations and predictions can be directly understood through human-interpretable concepts rather than post-hoc explanations.

**[NNsight and NDIF: Democratizing Access to Open-Weight Foundation Model Internals](https://proceedings.iclr.cc/paper_files/paper/2025/file/e6c65eb9b56719c1aa45ff73874de317-Paper-Conference.pdf) (as "Model interpretability")**
> The extent to which a model's internal states can be inspected, manipulated, and studied in a transparent way.

**[Efficient Dictionary Learning with Switch Sparse Autoencoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc4fbc2c77d2150c4e61e0fca6c2e95a-Paper-Conference.pdf) (as "Feature interpretability")**
> The degree to which the features learned by a sparse autoencoder correspond to distinct, human-understandable concepts.

**[Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf) (as "Mechanistic interpretability")**
> The degree to which a model's internal computations can be dissected and understood in terms of human-interpretable components.

**[MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf) (as "Explanation")**
> The ability to infer and articulate the underlying logic, purpose, or mechanism behind what is happening in a video.

**[DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf) (as "Human auditability")**
> The property of a model's decision-making process that allows a human to understand, verify, and trust the rationale behind a given decision.

**[Free Process Rewards without Process Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25c/yuan25c.pdf) (as "Transparency and interpretability")**
> The quality of a reward model that allows for a clear understanding of its evaluation process by providing scores for each intermediate reasoning step.

**[Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf) (as "System transparency")**
> The degree to which a model's inherent biases and their sources are clearly identified and communicated to users at the system level.

**[Position: Political Neutrality in AI Is Impossible — But Here Is How to Approximate It](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fisher25a/fisher25a.pdf) (as "Output transparency")**
> The latent trait of acknowledging and labeling political bias in model outputs, allowing users to interpret responses with awareness of potential slant.

**[Position: We Need An Algorithmic Understanding of Generative AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eberle25a/eberle25a.pdf) (as "Algorithmic understanding")**
> The degree to which the internal step-by-step procedures used by a model to solve tasks are known and explainable.

## Relationships

### Interpretability and explainability →
- **LLM-as-a-judge** (measurements) — *measured_by*
  > We evaluate feature interpretability using gpt4o-mini as an LLM judge.
  - [Efficient Dictionary Learning with Switch Sparse Autoencoders](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc4fbc2c77d2150c4e61e0fca6c2e95a-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > For Pythia SAEs, we asked human crowdworkers to rate the interpretability of random features, random neurons, features from our feature circuits, and neurons from our neuron circuits.
  - [Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ba4d47a83e498c2b1a0868cba20f6de-Paper-Conference.pdf)
- **Trustworthiness** (constructs) — *causes*
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **SAE Bench** (measurements) — *measured_by*
  > To address the core challenge of measuring how effectively a model and SAE work together, Karvonen et al. (2024) introduce SAEBench, a benchmark of SAE metrics that are faithful to possible real world use cases. (Section 5.1)
  - [Inference-Time Decomposition of Activations (ITDA): A Scalable Approach to Interpreting Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/leask25a/leask25a.pdf)
- **Steerability** (constructs) — *causes*
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **VQA-X** (measurements) — *measured_by*
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Attention rollout** (measurements) — *measured_by*
  > “We explore the attention matrices with three explanation methods: raw attention, attention rollout (Abnar & Zuidema, 2020), and attribution”
  - [OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f2fc4053a66edfa430bcdf9a6ff3b17-Paper-Conference.pdf)
- **Safety** (constructs) — *causes*
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **Neuronpedia** (measurements) — *measured_by*
  > We manually interpret each feature using the Neuronpedia interface (Lin & Bloom, 2023), which displays maximally activating dataset exemplars on a large text corpus, as the features’ direct effects on output logits.
  - [Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ba4d47a83e498c2b1a0868cba20f6de-Paper-Conference.pdf)
- **Plausibility** (constructs) — *measured_by*
  - [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Alignment** (constructs) — *causes*
  - [SAE-V: Interpreting Multimodal Models for Enhanced Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lou25b/lou25b.pdf)
- **G-Eval** (measurements) — *measured_by*
  - [Same evaluation, more tokens: On the effect of input length for machine translation evaluation using Large Language Models](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **e-SNLI** (measurements) — *measured_by*
  - [HookMoE: A learnable performance compensation strategy of Mixture-of-Experts forLLMinference acceleration](https://aclanthology.org/2025.emnlp-main.1611.pdf)

### → Interpretability and explainability
- **Chain-of-thought reasoning** (constructs) — *causes*
  > Con-J ensures natural interpretability through the generated rationales supporting the judgments (Abstract).
  - [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks) — *causes*
  - [SocialGPT: Prompting LLMs for Social Relation Reasoning via Greedy Segment Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/047682108c3b053c61ad2da5a6057b4e-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *causes*
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Commonsense understanding** (constructs) — *causes*
  - [A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual grounding** (constructs) — *causes*
  - [A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf)
- **Dialogue** (behaviors tasks) — *causes*
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **Structural reasoning** (constructs) — *causes*
  - [Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction](https://aclanthology.org/2025.naacl-long.124.pdf)
- **Disentanglement** (constructs) — *causes*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **Causal inference** (behaviors tasks) — *causes*
  > "ADAM constructs a nearly perfect causal graph from scratch, enabling efficient task decomposition and execution with strong interpretability."
  - [ADAM: An Embodied Causal Agent in Open-World Environments](https://proceedings.iclr.cc/paper_files/paper/2025/file/392aae924264f2c56d1895b232bb46b6-Paper-Conference.pdf)
- **Prompt engineering** (behaviors tasks) — *causes*
  > Additionally, we add the perplexity regularization term Lperpl to promote the interpretability of the optimized prompt
  - [Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd61329e2c14b93a89d617c914140f64-Paper-Conference.pdf)
- **Reasoning** (constructs) — *causes*
  - [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wen25g/wen25g.pdf)
- **Attribution** (constructs) — *causes*
  - [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.513.pdf)
- **Activation sparsity** (constructs) — *causes*
  > Besides acceleration, activation sparsity also helps improve interpretability, which is important for reliable and well-performing LLMs. (Section 2.1)
  - [Mixture of Experts Made Intrinsically Interpretable](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ag/yang25ag.pdf)
- **Neuronpedia** (measurements) — *measured_by*
  - [Analyze Feature Flow to Enhance Interpretation and Steering in Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/laptev25a/laptev25a.pdf)
- **Intent understanding** (constructs) — *causes*
  - [Follow the Flow: Fine-grained Flowchart Attribution with Neurosymbolic Agents](https://aclanthology.org/2025.emnlp-main.1145.pdf)
- **Backtracking** (behaviors tasks) — *causes*
  - [End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.202.pdf)

### Associated with
- **Trustworthiness** (constructs)
  - [A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf)
- **Medical reasoning** (constructs)
  - [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination** (behaviors tasks)
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.508.pdf)
- **Polysemanticity** (constructs)
  > A central obstacle to mechanistic interpretability is polysemanticity, where individual neurons encode multiple, unrelated concepts (Olah et al., 2020). Specifically, we refer to the hidden neurons from the multi-layer perceptron (MLPs) in Transformers. Such polysemantic neurons lack clear, singular roles, making it difficult to identify disentangled features or factors in neural networks.
  - [Mixture of Experts Made Intrinsically Interpretable](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ag/yang25ag.pdf)
- **Explanation generation** (behaviors tasks)
  > Human readability and explainability are essential to effective fact-checking. ... This final, post-prediction stage addresses that need by generating a concise summary that distills the key findings and critical evidence, including hyperlinks. (Section 3)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Reasoning** (constructs)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
- **Transparency** (constructs)
  - [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf)
- **Plausibility** (constructs)
  - [Is the MMI Criterion Necessary for Interpretability? Degenerating Non-causal Features to Plain Noise for Self-Rationalization](https://proceedings.neurips.cc/paper_files/paper/2024/file/d53d51e88d92d3723755f6d425bc513b-Paper-Conference.pdf)
- **Controllability** (constructs)
  > our findings indicate that precise behavior control offers valuable insights into the transparency and interpretability of PEFT methods, a topic that has been largely underexplored. (Section 1)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **Disentanglement** (constructs)
  - [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf)
- **Expressive power** (constructs)
  > traditional performance metrics like Mean Squared Error and L0 sparsity ignore the evaluation of the semantic representational power of SAEs — whether they can acquire interpretable monosemantic features while preserving the semantic relationship of words
  - [Large Language Models are Interpretable Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/887932131fddf943e8fe3310b62c0147-Paper-Conference.pdf)
- **Code generation** (behaviors tasks)
  - [RAG-SR: Retrieval-Augmented Generation for Neural Symbolic Regression](https://proceedings.iclr.cc/paper_files/paper/2025/file/19a8e70828c01059631f913442ae31e6-Paper-Conference.pdf)
- **Claim verification** (behaviors tasks)
  - [Multilingual Needle in a Haystack: Investigating Long-Context Behavior of Multilingual Large Language Models](https://aclanthology.org/2025.naacl-long.268.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [SATER: A Self-Aware and Token-Efficient Approach to Routing and Cascading](https://aclanthology.org/2025.emnlp-main.532.pdf)
- **Activation steering** (measurements)
  > Since steering may enable lightweight and interpretable control over model outputs, it has emerged as a potential alternative to finetuning and prompting
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Machine unlearning** (constructs)
  - [Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1348.pdf)
- **Usability** (constructs)
  - [A Training-Free Length Extrapolation Approach forLLMs: Greedy Attention Logit Interpolation](https://aclanthology.org/2025.emnlp-main.444.pdf)

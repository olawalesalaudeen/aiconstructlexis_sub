# Commonsense understanding
**Type:** Construct  
**Referenced in:** 248 papers  
**Also known as:** Commonsense grounding, Commonsense awareness, General world knowledge, World model, Common sense knowledge, Physical commonsense knowledge, Temporal commonsense knowledge, World knowledge priors, World knowledge reasoning, Common sense reasoning, Common-sense reasoning, Commonsense inference, Physical commonsense, Common sense inference, Common sense understanding  

## State of the Field

Across the surveyed literature, commonsense understanding is most frequently conceptualized as 'commonsense reasoning'—the ability to make inferences, judgments, and presumptions about ordinary situations using implicit world knowledge. This general framing encompasses various related terms like 'world knowledge,' 'commonsense grounding,' and 'world model,' which collectively describe a model's internalized representation of the physical and social world. While most definitions are broad, a few papers offer more specific framings, such as 'physical commonsense' for object interactions or 'temporal commonsense' for event orderings, and one study notes its boundaries are 'vague and ill-defined' (VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models). The field predominantly operationalizes this latent construct by measuring model performance on question-answering and sentence-completion tasks. The most common measurement instruments cited are benchmarks like HellaSwag, WinoGrande, PIQA, ARC, BoolQ, and CommonsenseQA. Some of these instruments are used to assess specific facets of the construct, as when PIQA is described as being 'focused on physical commonsense knowledge' (Latent Inter-User Difference Modeling forLLMPersonalization). This construct is also reported to influence a range of downstream behaviors, with some papers suggesting it drives task planning, generalization, and reward function generation, and it is frequently studied alongside mathematical reasoning and natural language inference.

## Sources

**[AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf) (as "Commonsense grounding")**
> The latent ability to apply everyday knowledge and intuitive understanding of the physical and social world to interpret and act in realistic scenarios.

**[FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)**
> The ability to provide accurate and contextually relevant responses to instructions that require commonsense knowledge.

**[Self-Augmented Preference Alignment for Sycophancy Reduction inLLMs](https://aclanthology.org/2025.emnlp-main.626.pdf) (as "Commonsense awareness")**
> The tendency to produce travel plans that satisfy basic validity constraints such as including real POIs and avoiding hallucinated or repetitive items.

**[EnhancingLLM-Based Social Bot via an Adversarial Learning Framework](https://aclanthology.org/2025.emnlp-main.1186.pdf) (as "Commonsense knowledge")**
> The implicit background knowledge about the world that allows for resolving ambiguities and making informed judgments, such as recognizing brand abbreviations or variations in addresses.

**[Bridging the Gap Between Molecule and Textual Descriptions via Substructure-aware Alignment](https://aclanthology.org/2025.emnlp-main.1198.pdf) (as "General world knowledge")**
> The model's stored knowledge about facts and concepts from the world that can be applied in evaluation tasks.

**[Continuously SteeringLLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.234.pdf) (as "World model")**
> A latent representation of real-world knowledge and causal relationships that enables the model to reason about physical and abstract quantities, even in the absence of direct training data.

**[Continuously SteeringLLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.234.pdf) (as "World knowledge")**
> The body of factual and conceptual information about the real world encoded within a model, used for reasoning about novel scenarios.

**[ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering](https://aclanthology.org/2025.emnlp-main.227.pdf) (as "Common sense knowledge")**
> The implicit knowledge about the world that humans use to make inferences and decisions.

**[Latent Inter-User Difference Modeling forLLMPersonalization](https://aclanthology.org/2025.emnlp-main.537.pdf) (as "Physical commonsense knowledge")**
> The ability to reason about everyday physical situations and object interactions using intuitive world knowledge.

**[Towards Language-AgnosticSTIPA: Universal Phonetic Transcription to Support Language Documentation at Scale](https://aclanthology.org/2025.emnlp-main.1601.pdf) (as "Temporal commonsense knowledge")**
> The model's internalized understanding of typical temporal sequences and event orderings derived from real-world experience or training data.

**[Subjective Behaviors and Preferences inLLM: Language of Browsing](https://aclanthology.org/2025.emnlp-main.1262.pdf) (as "World knowledge priors")**
> Memorized linguistic associations about typical visual attributes of objects that the model can retrieve from pretraining rather than from the current image.

**[Breaking the Noise Barrier:LLM-Guided Semantic Filtering and Enhancement for Multi-Modal Entity Alignment](https://aclanthology.org/2025.emnlp-main.1685.pdf) (as "World knowledge reasoning")**
> The ability to connect textual mentions to external factual knowledge (e.g., that Big Ben is in the UK) to infer implicit geographic, cultural, or encyclopedic facts necessary for determining relevance.

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf) (as "Commonsense reasoning")**
> The ability to make presumptions about the ordinary world, reflecting a shared understanding of everyday situations.

**[Eureka: Human-Level Reward Design via Coding Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf) (as "Common sense reasoning")**
> The ability to make sound practical judgments concerning everyday situations or events, such as identifying which state variables are relevant for a physical task.

**[WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf) (as "Commonsense inference")**
> The ability to make plausible inferences about everyday situations and concepts that are not explicitly stated.

**[Grounding Language Plans in Demonstrations Through Counterfactual Perturbations](https://proceedings.iclr.cc/paper_files/paper/2024/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf) (as "Common-sense reasoning")**
> The latent ability to infer plausible task structure and physical interactions from language and demonstrations in embodied settings.

**[Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf) (as "Physical commonsense")**
> The latent ability to reason about everyday physical interactions and plausible physical outcomes.

**[SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/693ce820ea7e0f0c70a2a833cbdf7ccc-Paper-Conference.pdf) (as "Common sense inference")**
> The ability to apply general world knowledge to interpret video content and provide a logical framework for understanding events.

**[Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf) (as "Common sense understanding")**
> The model's ability to comprehend and reason about situations in a way that aligns with general human knowledge and intuition.

## Relationships

### Commonsense understanding →
- **HellaSwag** (measurements) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Divergences between Language Models and Human Brains](https://proceedings.neurips.cc/paper_files/paper/2024/file/f96839fc751b67492e17e70f5c9730e4-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **MathQA** (measurements) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **AgentBench** (measurements) — *measured_by*
  - [AgentBench: Evaluating LLMs as Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [MoE-SVD: Structured Mixture-of-Experts LLMs Compression via Singular Value Decomposition](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25az/li25az.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [A Hitchhiker's Guide to Fine-Grained Face Forgery Detection Using Common Sense Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/059d2b9188cdb7ae00f4d78cc9469704-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)
- **SciQ** (measurements) — *measured_by*
  - [R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf)
- **Action selection** (behaviors tasks) — *causes*
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **Reward function generation** (behaviors tasks) — *causes*
  - [REvolve: Reward Evolution with Large Language Models using Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc8ee7c7ab5b5f6b1615045dfb617ed6-Paper-Conference.pdf)
- **Task planning** (constructs) — *causes*
  - [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/8ec46cecdae5407662899c5f6698cd8b-Paper-Conference.pdf)
- **Hypothesis generation** (behaviors tasks) — *causes*
  - [NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf)

### Associated with
- **Commonsense knowledge** (constructs)
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
- **Future prediction** (behaviors tasks)
  - [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a00548031e4647b13042c97c922fadf1-Paper-Conference.pdf)
- **Analytical reasoning** (constructs)
  - [Self-DC: When to Reason and When to Act? Self Divide-and-Conquer for Compositional Unknown Questions](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Inductive bias** (constructs)
  - [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf)

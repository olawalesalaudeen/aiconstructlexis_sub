# In-context learning
**Type:** Construct  
**Referenced in:** 304 papers  
**Also known as:** Few-shot learning, Few-shot learning ability, In-context improvement, Leveraging natural language feedback, In-context learning capability, In-context learning ability, In-Context Learning ability, In-context learnability, In-context causal structure selection, Test-time learning, Few-shot capability, Few-shot learning capability, Few-shot ability, Few-shot baseline, Few-shot Chain-of-Thought prompting, Zero-shot instruction prompting, Few-shot prompting, Zero-shot prompting, Zero-shot evaluation, Few-shot evaluation, In-Context Learning, FEW-SHOT, In-context few-shot demonstration, Few-shot benchmarking protocols, Zero-shot, In-Context Prompting, In-context learning evaluation, Few-shot prediction, Many-shot in-context learning, Zero-shot prediction, Few-shot forecasting, Few-shot reasoning, Context-based prediction, Zero-shot Evaluation, Zero-shot forecasting, One-shot adaptation, Few-shot adaptation, Few-shot inference, Few-shot range estimation  

## State of the Field

Across the provided literature, In-context learning (ICL) is overwhelmingly defined as a model's ability to adapt to a new task by conditioning on a few input-output examples, or demonstrations, provided in the prompt. A near-universal characteristic is that this adaptation occurs at inference time without any parameter updates, distinguishing it from conventional fine-tuning. While this core definition is consistent, some papers offer more specific framings, such as "task learning" to emphasize inferring new input-label mappings, or "in-context improvement" which focuses on iterative refinement based on feedback. The underlying mechanism is described as a subject of debate, with some papers viewing it as a form of meta-learning or implicit Bayesian inference. The construct is operationalized and measured through model performance on various downstream tasks, including question-answering, summarization, and time series forecasting, using benchmarks such as MINT, MATH, and HELMET. In-context learning is reported to be related to a model's "prompt steerability" and is sometimes contrasted with instruction following, with one study noting that instruction tuning can suppress it. Some studies propose that this ability enables other behaviors; for instance, one paper reports that few-shot Chain-of-Thought prompting, a form of ICL, facilitates compositional reasoning.

## Sources

**[A Benchmark for Learning to Translate a New Language from One Grammar Book](https://proceedings.iclr.cc/paper_files/paper/2024/file/52d63f9e4b81f866bf69fb3c834aad47-Paper-Conference.pdf)**
> The ability of a language model to adapt to a new task by conditioning on a few input-label demonstrations provided in the prompt, without parameter updates.

**[CLEX: Continuous  Length Extrapolation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3df38ca67befaed9c03b95ffee07d9f8-Paper-Conference.pdf) (as "Few-shot learning")**
> Performing tasks based on a small number of in-context examples provided in the input, requiring generalization and pattern recognition within long contexts.

**[Eureka: Human-Level Reward Design via Coding Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf) (as "In-context improvement")**
> The ability of the LLM to refine and enhance previously generated outputs based on feedback or reflection provided within the context window, enabling iterative optimization without parameter updates.

**[MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf) (as "Leveraging natural language feedback")**
> The latent ability of an LLM to adapt and improve its outputs in response to natural language feedback from a user or simulated user across multiple interaction turns.

**[Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c7793beb7f32b559df55d48370f2b8ae-Paper-Conference.pdf) (as "Few-shot learning ability")**
> The latent capacity to learn effective policies from very small amounts of task-specific data, leveraging prior knowledge from language model pre-training.

**[LogiCity: Advancing Neuro-Symbolic AI with Abstract Urban Simulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/8196be81e68289d7a9ece21ed7f5750a-Paper-Datasets_and_Benchmarks_Track.pdf) (as "In-context learning capability")**
> The ability to infer task rules and answer new questions from a small set of demonstrations provided in the prompt.

**[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf) (as "In-context learning ability")**
> The model's capacity to perform evaluation tasks when conditioned on example input-output pairs in the prompt.

**[Training Nonlinear Transformers for Chain-of-Thought Inference:  A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf) (as "In-Context Learning ability")**
> The latent capability of a model to perform a task by conditioning on a few input-output examples provided in the prompt, without explicit intermediate reasoning steps.

**[Selective induction Heads: How Transformers Select Causal Structures in Context](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf) (as "In-context causal structure selection")**
> The ability of a model to dynamically identify the correct underlying causal relationship between tokens, such as the lag in a Markov chain, from the context and use it for prediction.

**[Chain-of-Thought Provably Enables Learning the (Otherwise) Unlearnable](https://proceedings.iclr.cc/paper_files/paper/2025/file/da535999561b932f56efdd559498282e-Paper-Conference.pdf) (as "In-context learnability")**
> A formal property of a task, indicating whether a model can successfully learn to solve it with high probability given a sufficient number of in-context examples.

**[Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1304.pdf) (as "Test-time learning")**
> The latent ability of a model to improve its performance through interaction, feedback, and reflection during test time by discovering and applying generalizable strategies beyond memorization.

**[Enhanced Noun-Noun Compound Interpretation through Textual Enrichment](https://aclanthology.org/2025.emnlp-main.1316.pdf) (as "Task learning")**
> The latent ability of a model to infer and apply new input-label mappings from in-context demonstrations that were not encountered during pre-training, reflecting on-the-fly generalization rather than retrieval of memorized patterns.

**[Weight-Aware Activation Sparsity with ConstrainedBayesian Optimization Scheduling for Large Language Models](https://aclanthology.org/2025.emnlp-main.58.pdf) (as "In-context reasoning")**
> The model's capacity to reason and solve problems based on the information provided within the current context or prompt.

**[From News to Forecast: Integrating Event Analysis in LLM-Based Time Series Forecasting with Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/6aef8bffb372096ee73d98da30119f89-Paper-Conference.pdf) (as "Few-shot capability")**
> The ability of a pre-trained model to perform tasks effectively with only a small number of examples, without requiring extensive fine-tuning.

**[Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1453.pdf) (as "Few-shot learning capability")**
> The model's ability to learn and perform a task based on a small number of examples provided within the prompt's context.

**[GeoEdit: Geometric Knowledge Editing for Large Language Models](https://aclanthology.org/2025.emnlp-main.677.pdf) (as "Few-shot ability")**
> The model's capability to adapt to new prediction tasks with minimal fine-tuning samples, indicating efficient learning from limited data.

**[RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning](https://aclanthology.org/2025.emnlp-main.1631.pdf) (as "Systematic generalization")**
> The capacity to apply learned knowledge about a new word consistently and flexibly across structurally different but semantically related contexts.

**[Logical Consistency of Large Language Models in Fact-Checking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3209cf3312b2cbb68e33644362ddc2bd-Paper-Conference.pdf) (as "Zero-shot instruction prompting")**
> An evaluation procedure where an LLM is given a prompt with explicit instructions on how to perform a task, without any task-specific examples, to assess its performance as a baseline against fine-tuning.

**[Are Transformers Able to Reason by Connecting Separated Knowledge in Training Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/476c9ac41c967332dd28fb844e166b34-Paper-Conference.pdf) (as "Few-shot Chain-of-Thought prompting")**
> An evaluation procedure where a model's input prompt is augmented with a small number of example problems that include explicit, intermediate step-by-step reasoning to guide the model's own reasoning process.

**[TypedThinker: Diversify Large Language Model Reasoning with Typed Thinking](https://proceedings.iclr.cc/paper_files/paper/2025/file/494ad6d9b36d9a1528dbf3baeb4e8a72-Paper-Conference.pdf) (as "Few-shot baseline")**
> A few-shot prompting evaluation procedure using three in-context examples to solve benchmark problems.

**[Can LLMs Understand Time Series Anomalies?](https://proceedings.iclr.cc/paper_files/paper/2025/file/05774fb74e863308c4b460c9f49f6918-Paper-Conference.pdf) (as "Zero-shot prompting")**
> An evaluation procedure in which the model must detect anomalies without any labeled examples in the prompt.

**[Can LLMs Understand Time Series Anomalies?](https://proceedings.iclr.cc/paper_files/paper/2025/file/05774fb74e863308c4b460c9f49f6918-Paper-Conference.pdf) (as "Few-shot prompting")**
> An evaluation procedure in which the model detects anomalies after being shown a small number of labeled examples.

**[CREMA: Generalizable and Efficient Video-Language Reasoning via Multimodal Modular Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9079234614422c036c5a92bb8ec04c4-Paper-Conference.pdf) (as "Zero-shot evaluation")**
> Evaluation protocol assessing model performance on tasks without fine-tuning, measuring generalization capability.

**[Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3064f7a0ca2328ecb41a3aef6177d68-Paper-Conference.pdf) (as "Few-shot evaluation")**
> An evaluation procedure where a model is prompted with a small number of task examples (e.g., 5-shot) in its context before being asked to solve a new problem instance.

**[Entity Decomposition with Filtering: A Zero-Shot Clinical Named Entity Recognition Framework](https://aclanthology.org/2025.naacl-long.151.pdf) (as "In-Context Learning")**
> A prompting technique that provides examples within the input to guide the LLM in performing knowledge checking tasks, used here as a baseline for comparison with representation methods.

**[FunBO: Discovering Acquisition Functions for Bayesian Optimization with FunSearch](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aglietti25a/aglietti25a.pdf) (as "FEW-SHOT")**
> Evaluation setup for fast adaptation of acquisition functions using only a small number (e.g., 5) of examples from a target function class.

**[Iterative Vectors: In-Context Gradient Steering without Backpropagation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25j/liu25j.pdf) (as "Few-shot benchmarking protocols")**
> A standard evaluation procedure for few-shot classification in which episodes are formed from support examples and a query, then used to assess model predictions.

**[EVOLvE: Evaluating and Optimizing LLMs For In-Context Exploration](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nie25b/nie25b.pdf) (as "In-context few-shot demonstration")**
> An inference-time evaluation method where optimal exploration trajectories from an oracle algorithm are provided as few-shot examples to guide the LLM’s decision-making.

**[Catch Your Emotion: Sharpening Emotion Perception in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/fang25h/fang25h.pdf) (as "Zero-shot")**
> A direct inference evaluation procedure in which the model answers emotion classification prompts without additional training.

**[PhantomWiki: On-Demand Datasets for Reasoning and Retrieval Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25d/gong25d.pdf) (as "In-Context Prompting")**
> Evaluation method where the full document corpus is included in the model's prompt, either directly (ZEROSHOT) or with chain-of-thought examples (COT), to test reasoning within context limits.

**[Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation](https://aclanthology.org/2025.naacl-long.482.pdf) (as "In-context learning evaluation")**
> An evaluation setup where a model's performance is tested by providing it with a few examples (2 or 4) of the moderation task within the prompt.

**[Not All LLM-Generated Data Are Equal: Rethinking Data Weighting in Text Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/03dfa2a7755635f756b160e9f4c6b789-Paper-Conference.pdf) (as "Few-shot prediction")**
> The task of making predictions based on a small number of examples (shots) provided in the context or prompt.

**[Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf) (as "Zero-shot prediction")**
> Making fitness predictions without any support-set examples for the target task.

**[SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf) (as "Many-shot in-context learning")**
> The observable task of learning a new task from a large number of examples provided within the context and then applying that learned skill to a new query.

**[Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/ded26b348d55953a4863d41540b7d5c4-Paper-Conference.pdf) (as "Few-shot reasoning")**
> The observable behavior of performing reasoning tasks when provided with only a small number of examples (e.g., 5-shot) in the prompt.

**[Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf) (as "Few-shot forecasting")**
> The task of performing time series forecasting using only a small fraction of the available training data.

**[Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf) (as "Context-based prediction")**
> Producing the correct output by using labels or information present in the surrounding context rather than relying on stored associations.

**[Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf) (as "Zero-shot Evaluation")**
> The observable behavior of performing tasks without any task-specific fine-tuning or examples provided in the prompt.

**[Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf) (as "Zero-shot forecasting")**
> The task of performing time series forecasting on a target dataset without having been trained on any of its data, typically by training on a different source dataset.

**[Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf) (as "Zero-shot learning")**
> Performing a task without any task-specific fine-tuning, relying solely on the model's pre-existing knowledge.

**[Zebra: In-Context Generative Pretraining for Solving Parametric PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/serrano25a/serrano25a.pdf) (as "One-shot adaptation")**
> The observable behavior of inferring the dynamics of a system and making predictions for a new query after being provided with only a single example trajectory from that system.

**[TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf) (as "Few-shot adaptation")**
> Learning contextually from demonstrations in a few-shot setting to improve performance on new tasks.

**[Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Few-shot inference")**
> Making predictions on downstream tasks using only a small number of labeled examples per class.

**[Combining Observational Data and Language for Species Range Estimation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f96b24df4b06f5d68389845a9a13ed9-Paper-Conference.pdf) (as "Few-shot range estimation")**
> The behavior of estimating species range maps using a small number of location observations combined with textual priors.

## Relationships

### In-context learning →
- **Generalization** (constructs) — *causes*
  > In standard ICL (which we will refer to as prequential ICL), the query xq is a novel input that does not appear in the context. In the alternative form of ICL (which we will call train-risk ICL), the query xq is a randomly-selected input that appeared previously in the context x1:j.
  - [Probing the Decision Boundaries of In-context Learning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb5dd4476448c44e55a759a985b3bbec-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [Understanding In-Context Learning from Repetitions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d88f6f81e1aaf606776ffdd06fdf24ef-Paper-Conference.pdf)
- **MetaICL** (measurements) — *measured_by*
  - [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf)
- **Instruction following** (constructs) — *causes*
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.582.pdf)
- **Code generation** (behaviors tasks) — *causes*
  - [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf)
- **Task planning** (constructs) — *causes*
  - [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)
- **MINT** (measurements) — *measured_by*
  > It is a benchmark for LLMs that measures their performance during multi-turn interaction, focusing on two particular capabilities (§2.1): ... (2) leveraging natural language feedback. (Section 1)
  - [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)
- **DBPedia** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **SST-5** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **MNLI** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Factuality** (constructs) — *causes*
  - [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
- **Out-of-distribution generalization** (constructs) — *causes*
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *causes*
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Weather** (measurements) — *measured_by*
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **MRPC** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **RTE** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **XSum** (measurements) — *measured_by*
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks) — *measured_by*
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **VQA-v2** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VizWiz** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Tool use** (behaviors tasks) — *causes*
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *causes*
  - [Linking In-context Learning in Transformers to Human Episodic Memory](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ba385c3ea3bb417ac6d6a33e24411bc-Paper-Conference.pdf)
- **COCO** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OK-VQA** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TextVQA** (measurements) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Mathematical reasoning** (constructs) — *causes*
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
- **Logical reasoning** (constructs) — *causes*
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **M4** (measurements) — *measured_by*
  - [AutoTimes: Autoregressive Time Series Forecasters via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **MATH** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Verbosity** (constructs) — *causes*
  - [Padding Tone: A Mechanistic Analysis of Padding Tokens inT2IModels](https://aclanthology.org/2025.naacl-long.390.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurements) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurements) — *measured_by*
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Compositional generalization** (constructs) — *causes*
  - [Attention as a Hypernetwork](https://proceedings.iclr.cc/paper_files/paper/2025/file/abfa542f546df3c6c35695ec8d5bf4b9-Paper-Conference.pdf)
- **MAWPS** (measurements) — *measured_by*
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
- **HELMET** (measurements) — *measured_by*
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **Adaptability** (constructs) — *causes*
  - [Zebra: In-Context Generative Pretraining for Solving Parametric PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/serrano25a/serrano25a.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **Zero-shot inference** (behaviors tasks) — *causes*
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Compositional reasoning** (constructs) — *causes*
  > Our findings demonstrate that few-shot Chain-of-Thought prompting enables Transformers to perform compositional reasoning on FTCT by revealing correct combinations of fragments, even if such combinations were absent in training data. (ABSTRACT)
  - [Are Transformers Able to Reason by Connecting Separated Knowledge in Training Data?](https://proceedings.iclr.cc/paper_files/paper/2025/file/476c9ac41c967332dd28fb844e166b34-Paper-Conference.pdf)
- **WSC** (measurements) — *measured_by*
  - [Improving Dialogue State Tracking through Combinatorial Search for In-Context Examples](https://aclanthology.org/2025.acl-long.1394.pdf)
- **Scalability** (constructs) — *causes*
  - [Iterative Vectors: In-Context Gradient Steering without Backpropagation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25j/liu25j.pdf)
- **Code debugging** (behaviors tasks) — *causes*
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **AIME 2025** (measurements) — *measured_by*
  > “AIME 2025 ... We leverage this most recent mathematics benchmark to examine the test-time learning capabilities of large language models in solving high-level mathematical problems.”
  - [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1304.pdf)
- **Information retrieval** (behaviors tasks) — *causes*
  - [AISees YourLocation—But With A Bias Toward The Wealthy World](https://aclanthology.org/2025.emnlp-main.911.pdf)

### → In-context learning
- **Instruction following** (constructs) — *causes*
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Representation learning** (constructs) — *causes*
  - [Transformers are Minimax Optimal Nonparametric In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/c11daad0a48ea5f3c5c6390c7b060720-Paper-Conference.pdf)
- **Knowledge transferability** (constructs) — *causes*
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *causes*
  - [What is Wrong with Perplexity for Long-context Language Modeling?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebd6641c32ed633c2a3addc689d39896-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf)
- **Contextual understanding** (constructs) — *causes*
  - [Context-Alignment: Activating and Enhancing LLMs Capabilities in Time Series](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1de63ec74f40d3234c4e053f3528e18-Paper-Conference.pdf)
- **Memorization** (constructs) — *causes*
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Length generalization** (constructs) — *causes*
  - [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf)

### Associated with
- **Generalization** (constructs)
  - [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf)
- **Tool use** (behaviors tasks)
  - [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf)
- **Parametric knowledge** (constructs)
  - [The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://proceedings.iclr.cc/paper_files/paper/2024/file/540a3bf4863672cdaebfed69fa2ce335-Paper-Conference.pdf)
- **Knowledge recall** (behaviors tasks)
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
- **Reasoning** (constructs)
  - [Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25at/yang25at.pdf)
- **Text classification** (behaviors tasks)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Emergent abilities** (constructs)
  - [Lines of Thought in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/649f080d8891ab4d4b262cb9cd52e69a-Paper-Conference.pdf)
- **Zero-shot learning** (constructs)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
- **Representation learning** (constructs)
  - [How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
- **Out-of-distribution generalization** (constructs)
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
- **Problem-solving** (behaviors tasks)
  - [Looped Transformers are Better at Learning Learning Algorithms](https://proceedings.iclr.cc/paper_files/paper/2024/file/b8402301e7f06bdc97a31bfaa653dc32-Paper-Conference.pdf)
- **In-context classification** (behaviors tasks)
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Privacy** (constructs)
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Zero-shot inference** (behaviors tasks)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Abstract reasoning** (constructs)
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Synthetic Socratic Debates: Examining Persona Effects on Moral Decision and Persuasion Dynamics](https://aclanthology.org/2025.emnlp-main.832.pdf)
- **Image classification** (behaviors tasks)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
- **Selectivity** (constructs)
  - [Theoretical Foundations of Deep Selective State-Space Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6231c5f46598cfd09ff1970524e0436-Paper-Conference.pdf)
- **Logical reasoning** (constructs)
  - [From Unstructured Data to In-Context Learning: Exploring What Tasks Can Be Learned and When](https://proceedings.neurips.cc/paper_files/paper/2024/file/1da38b872e19f1f4a3c2846720e8f64a-Paper-Conference.pdf)
- **Knowledge transferability** (constructs)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **Understanding** (constructs)
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Long-context understanding** (constructs)
  - [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf)
- **Information retrieval** (behaviors tasks)
  - [Look Before You Leap: Universal Emergent Mechanism for Retrieval in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad36c2cfc423e75c6d68d751a955b22e-Paper-Conference.pdf)
- **Question answering** (behaviors tasks)
  - [Federated In-Context Learning: Iterative Refinement for Improved Answer Quality](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25db/wang25db.pdf)
- **Expressive power** (constructs)
  - [Why In-Context Learning Models are Good Few-Shot Learners?](https://proceedings.iclr.cc/paper_files/paper/2025/file/6c7ca1889f01a9b767c631686fb5fd24-Paper-Conference.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Long-context processing** (constructs)
  - [CAMIEval: EnhancingNLGEvaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.439.pdf)
- **Memorization** (constructs)
  - [Zero-shot forecasting of chaotic systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea4d65c59073e8faf79222654d25fbe2-Paper-Conference.pdf)
- **Tabular classification** (behaviors tasks)
  - [TabFlex: Scaling Tabular Learning to Millions with Linear Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25b/zeng25b.pdf)
- **Multi-image reasoning** (constructs)
  - [MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2c3c86679300047c740c9900f19ddac-Paper-Conference.pdf)
- **Grammatical error correction** (behaviors tasks)
  - [Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Controllability** (constructs)
  > The prompt steerability of a model is related to how well a model can learn from in-context examples (Brown, 2020; Wies et al., 2024). (Section 1.1)
  - [Getting More Juice Out of Your Data: Hard Pair Refinement Enhances Visual-Language Models Without Extra Data](https://aclanthology.org/2025.naacl-long.400.pdf)
- **Knowledge retrieval** (behaviors tasks)
  - [Towards Operationalizing Right to Data Protection](https://aclanthology.org/2025.naacl-long.417.pdf)
- **Semantic understanding** (constructs)
  - [Benchmarking and Building Zero-ShotHindi Retrieval Model withHindi-BEIRandNLLB-E5](https://aclanthology.org/2025.naacl-long.221.pdf)
- **Text summarization** (behaviors tasks)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Stability** (constructs)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
- **Previous-token attention** (behaviors tasks)
  - [Strategy Coopetition Explains the Emergence and Transience of In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/singh25c/singh25c.pdf)
- **Task alignment** (constructs)
  - [Lemmatization ofPolish Multi-word Expressions](https://aclanthology.org/2025.emnlp-main.1127.pdf)

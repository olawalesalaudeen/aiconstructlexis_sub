# General capabilities
**Type:** Construct  
**Referenced in:** 147 papers  
**Also known as:** Downstream Performance, Downstream performance, General abilities, General ability, General capability, General performance, Generic performance, Model Capability, Model capability, Model performance, General purpose performance, General-purpose ability, General-purpose capabilities, Model utility, Model Utility, Model competence, Effectiveness, General task performance, Task performance, Downstream benchmark performance, Foundational capabilities, LLM capability, Benign capabilities, Generalist abilities, General problem-solving, Capability, General model utility, Utility, Skill, Cross capabilities, Worst-case performance, Ability, AI R&D capability, ML R&D capability, Research engineering skill, Latent abilities, Latent capability, Action-level ability, Decision-level ability, General language model capability, General model capability, Capabilities set, Benchmark utility, Value, Capabilities, All-round capability, Intrinsic capacity, Model capacity, Policy performance, Prompt performance, Relative performance, Domain-specific performance, Benign utility  

## State of the Field

Across the surveyed literature, "General capabilities" is a widely used construct referring to a model's overall performance across a broad range of tasks and domains, as opposed to its performance on a specific or specialized task. The construct is frequently invoked to assess whether an intervention—such as model editing, safety alignment, or fine-tuning—degrades a model's pre-existing or foundational abilities, with some studies noting that such interventions may "compromise the model’s general capabilities" ("ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time"). The most prevalent method for operationalizing this construct is through performance on multitask benchmarks; MMLU is the most frequently cited instrument used to measure general capabilities, general ability, and model utility. A smaller body of work also uses open-ended evaluation systems like the LMSYS Chatbot Arena. While the core idea is consistent, the terminology varies, with authors using terms like "model utility," "downstream performance," and "benign utility" to refer to this concept of broad, non-specialized performance. Some research connects this construct to other phenomena, with one study observing that higher general capabilities correlate with stronger performance on potentially harmful tasks, while another links its degradation to catastrophic forgetting. Several definitions also frame it as a latent, unobservable trait inferred from benchmark scores, representing the model's underlying proficiency in areas like reasoning and knowledge application.

## Sources

**[Private Attribute Inference from Images with Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb97e9a7c811904c9b01f51fde66edcf-Paper-Conference.pdf)**
> A model's overall proficiency and performance across a wide range of tasks, which is shown to correlate with its performance on specific, potentially harmful tasks like private attribute inference.

**[Everything is Editable: Extend Knowledge Editing to Unstructured Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/02763667a5761ff92bb15d8751bcd223-Paper-Conference.pdf) (as "General ability")**
> The model's broader performance on unrelated tasks or knowledge after editing, reflecting whether edits degrade overall capability.

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf) (as "General capability")**
> The model's overall performance on a wide range of standard, non-adversarial tasks, such as question answering and instruction following.

**[Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf) (as "Generic performance")**
> The overall downstream effectiveness of a pre-trained LLM across diverse evaluation tasks rather than a single target domain.

**[Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf) (as "General abilities")**
> The broad set of capabilities of a large language model, such as reasoning and summarization, that are not directly targeted by a specific model edit but can be negatively affected by it.

**[Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf) (as "General performance")**
> The overall capability of a model across a wide range of tasks and domains, as opposed to performance on a specific, narrow task.

**[Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf) (as "General-purpose capabilities")**
> Broad task competence of an LLM across heterogeneous chat and reasoning tasks rather than a single narrow domain.

**[Optimized Multi-Token Joint Decoding With Auxiliary Model for LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/438c34f45d7b5d82aef1b6016e695d5a-Paper-Conference.pdf) (as "Downstream Performance")**
> The latent capability of the model to successfully complete tasks, inferred from accuracy or scores on benchmarks.

**[RegMix: Data Mixture as Regression for Language Model Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf) (as "Downstream performance")**
> The overall capability of a pre-trained model to perform effectively on a wide range of evaluation tasks it was not explicitly trained on.

**[LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf) (as "Model utility")**
> The overall performance and general knowledge of a model on tasks and data that are unaffected by the unlearning process.

**[Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf) (as "Model Capability")**
> The general ability of the model to perform desired tasks, such as language modeling or question answering, without degradation.

**[Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf) (as "Model capability")**
> The overall level of a model's general cognitive abilities, such as reasoning and knowledge, which often correlates with its scale and performance on standard benchmarks.

**[Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf) (as "General-purpose ability")**
> A model's broad capability across a wide range of tasks and domains, as opposed to specialized performance on a narrow domain.

**[Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf) (as "Model Utility")**
> The latent general capability of a model to perform diverse tasks effectively without degradation from interventions.

**[Determine-Then-Ensemble: Necessity of Top-k Union for Large Language Model Ensembling](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbb10d319d44f8c3b4720873e4177c65-Paper-Conference.pdf) (as "Model performance")**
> The overall effectiveness of a model on a given set of tasks, which is a key determinant for successful ensembling.

**[Scaling Long Context Training Data by Long-Distance Referrals](https://proceedings.iclr.cc/paper_files/paper/2025/file/fbf49f35b6dd2bef1ad12768c0509daa-Paper-Conference.pdf) (as "General purpose performance")**
> The overall capability of a model across a wide range of domains and tasks, as opposed to specialized performance in a narrow domain.

**[Balancing Act: Diversity and Consistency in Large Language Model Ensembles](https://proceedings.iclr.cc/paper_files/paper/2025/file/a5554e55d7a21e62d0d7a028ec0ea1c7-Paper-Conference.pdf) (as "Task performance")**
> The overall quality of an ensemble's outputs on a downstream benchmark or task, as reflected by how well it solves the target evaluation problems.

**[Scaling Instruction-tuned LLMs to Million-token Contexts via Hierarchical Synthetic Data Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/bb36593e5e438aac5dd07907e757e087-Paper-Conference.pdf) (as "General task performance")**
> The overall capability of the model to perform standard NLP tasks without regression when optimized for specific constraints like long context.

**[TC-MoE: Augmenting Mixture of Experts with Ternary Expert Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/bda8f7ac4c3ccc494b5206ee3fd92771-Paper-Conference.pdf) (as "Effectiveness")**
> The overall quality or performance of the model in achieving its objectives, as measured by accuracy on evaluation benchmarks, distinct from its computational cost.

**[Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf) (as "Model competence")**
> The overall capability and effectiveness of a language model that results from its pretraining regimen, which is crucially impacted by data mixture proportions.

**[Improving Pretraining Data Using Perplexity Correlations](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c625366ae28066fcb1827b44517d674-Paper-Conference.pdf) (as "Downstream benchmark performance")**
> The latent capability of a language model that enables it to score highly on a diverse set of evaluation benchmarks.

**[PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf) (as "LLM capability")**
> The overall latent ability level of a language model across evaluation tasks, inferred from how well it performs and is ranked relative to other models.

**[StringLLM: Understanding the String Processing Capability of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e4013f157410cb7612701b318fb4ac2-Paper-Conference.pdf) (as "Foundational capabilities")**
> The general, pre-existing knowledge and skills of a large language model, which are evaluated to ensure they are not degraded by specialized fine-tuning.

**[HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf) (as "General problem-solving")**
> A broad capability to handle a variety of tasks and input formats, acquired through training on a diverse multi-task dataset.

**[Self-Play Preference Optimization for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/e48fa1c4f08fd1ae35d5df8352c3106d-Paper-Conference.pdf) (as "Generalist abilities")**
> The model's capacity to perform well across a wide and diverse range of tasks and domains without task-specific fine-tuning.

**[Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf) (as "Benign capabilities")**
> The extent to which a safeguarded model retains general-purpose performance on non-target tasks after safety training and tampering.

**[Capability Localization: Capabilities Can be Localized rather than Individual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/648a5a590ca6f2bb5de53f938e230160-Paper-Conference.pdf) (as "Capability")**
> A general, transferable ability of a model, reflected as a commonality across a dataset, that can be localized to a specific set of neurons and enhances performance on related tasks.

**[Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf) (as "General model utility")**
> The model's broad task performance across general-purpose evaluations, used here as an overall indicator of whether interventions preserve usefulness.

**[Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf) (as "Utility")**
> The overall quality and usefulness of the model's generated output for a given task, considered as a trade-off against safety measures.

**[Unearthing Skill-level Insights for Understanding Trade-offs of Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5526c73e3ff4f2a34009e13d15f52fcb-Paper-Conference.pdf) (as "Skill")**
> A latent underlying competency that a model must apply to solve an evaluation instance, often spanning multiple benchmarks and surfacing only through solution steps.

**[MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf) (as "Usefulness")**
> The extent to which a model's response provides practical value or utility to the user for their specific task.

**[Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf) (as "Cross capabilities")**
> The ability to integrate multiple distinct capabilities across different types of expertise to address complex, real-world tasks.

**[Estimating the Probabilities of Rare Outputs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cdaac2a02c4fdcae77ba083b110efcc3-Paper-Conference.pdf) (as "Worst-case performance")**
> The extent to which a model avoids highly undesirable outputs on rare or adversarially shifted inputs rather than only performing well on average.

**[A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf) (as "Decision-level ability")**
> The latent cognitive capacity for problem-solving, diagnosis, and planning required to determine a course of action for a given skill.

**[A Mathematical Framework for AI-Human Integration in Work](https://raw.githubusercontent.com/mlresearch/v267/main/assets/celis25a/celis25a.pdf) (as "Action-level ability")**
> The latent capacity for executing a pre-determined solution, such as implementing a fix or carrying out a planned procedure for a given skill.

**[Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf) (as "General language model capability")**
> The overall proficiency of a model across a wide range of standard language understanding and generation benchmarks.

**[Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf) (as "General model capability")**
> The overall performance and competence of a model across a wide range of standard tasks, distinct from its specialized safety behaviors.

**[MAGELLAN: Metacognitive predictions of learning progress guide autotelic LLM agents in large goal spaces](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gaven25a/gaven25a.pdf) (as "Competence")**
> The underlying ability of an agent to successfully achieve a given goal, often operationalized as the probability of success.

**[The Elicitation Game: Evaluating Capability Elicitation Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hofstatter25a/hofstatter25a.pdf) (as "Latent capability")**
> A capability that a model possesses but exhibits with low probability by default, which can be revealed through specific elicitation techniques.

**[MERGE$^3$: Efficient Evolutionary Merging on Consumer-grade GPUs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mencattini25a/mencattini25a.pdf) (as "Latent abilities")**
> The underlying, unobservable capabilities of a model, such as problem-solving or linguistic skills, which are estimated using statistical methods rather than being directly measured.

**[PaperBench: Evaluating AI’s Ability to Replicate AI Research](https://raw.githubusercontent.com/mlresearch/v267/main/assets/starace25a/starace25a.pdf) (as "ML R&D capability")**
> The latent ability of an AI agent to perform tasks associated with machine learning research and development, such as understanding, implementing, and experimentally validating novel concepts from academic papers.

**[Reliable and Efficient Amortized Model-based Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25c/truong25c.pdf) (as "Ability")**
> The unobservable, unidimensional latent trait of a language model that determines its probability of correctly answering a question, independent of the question's difficulty.

**[RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf) (as "AI R&D capability")**
> The latent ability of an AI agent to autonomously perform the complex, open-ended tasks involved in advancing artificial intelligence research and development.

**[RE-Bench: Evaluating Frontier AI R&D Capabilities of Language Model Agents against Human Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wijk25a/wijk25a.pdf) (as "Research engineering skill")**
> The underlying competence to make progress on open-ended machine learning research engineering problems through experimentation, implementation, and compute-efficient problem solving.

**[Position: Scaling LLM Agents Requires Asymptotic Analysis with LLM Primitives](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meyerson25a/meyerson25a.pdf) (as "Capabilities set")**
> The latent trait representing the scope of tasks an LLM can reliably perform, which determines its suitability for specific agent roles within a system.

**[STAMP Your Content: Proving Dataset Membership via Watermarked Rephrasings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rastogi25a/rastogi25a.pdf) (as "Benchmark utility")**
> The extent to which a watermarked or modified benchmark continues to function as a reliable and valid measure of model performance, preserving both absolute scores and relative model rankings.

**[Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf) (as "Value")**
> The usefulness or functional benefit of a creative artifact to the user, assessed based on task-specific criteria such as persuasiveness, clarity, or appropriateness.

**[A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Capabilities")**
> The general ability of a model to perform tasks correctly and generate high-quality, useful, and coherent information.

**[MemoryFormer : Minimize Transformer Computation by Removing Fully-Connected Layers](https://proceedings.neurips.cc/paper_files/paper/2024/file/24143e25a82f856aeed58b2f497d623b-Paper-Conference.pdf) (as "All-round capability")**
> Broad general task competence across diverse benchmark types, including knowledge and reasoning tasks.

**[CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases](https://aclanthology.org/2025.naacl-long.8.pdf) (as "Intrinsic capacity")**
> The underlying, general-purpose capabilities of a base model, independent of specific fine-tuning or prompting techniques, which influences its performance on downstream tasks.

**[Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf) (as "Model capacity")**
> The finite ability of a model, parameterized by the embedding dimension 'd', to store associations without performance degradation from interference.

**[AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf) (as "Relative performance")**
> A model's capability or quality assessed through direct comparison with other models, rather than against an absolute standard.

**[TAROT: Targeted Data Selection via Optimal Transport](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25l/feng25l.pdf) (as "Domain-specific performance")**
> The model's effectiveness on a specific, targeted set of tasks or data distribution, as opposed to general-purpose performance.

**[Hyperband-based Bayesian Optimization for Black-box Prompt Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schneider25b/schneider25b.pdf) (as "Prompt performance")**
> The latent trait reflecting how well a given prompt enables an LLM to produce correct outputs on a downstream task, inferred from validation error patterns across prompts.

**[Free Process Rewards without Process Labels](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25c/yuan25c.pdf) (as "Policy performance")**
> The ability of the model to directly solve downstream tasks when used as a policy model rather than as a reward model.

**[Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf) (as "Benign utility")**
> The model's ability to maintain its performance and helpfulness on legitimate, non-malicious tasks and prompts.

## Relationships

### General capabilities →
- **MMLU** (measurements) — *measured_by*
  > To assess general ability, we evaluate both the MMLU score of the edited model and the Loc-FactScore for unrelated questions. (Section 5.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GPQA** (measurements) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BBH** (measurements) — *measured_by*
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **TyDiQA** (measurements) — *measured_by*
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MATH** (measurements) — *measured_by*
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TextVQA** (measurements) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)
- **VQA-v2** (measurements) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **MMMU-Pro** (measurements) — *measured_by*
  - [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)
- **WikiText** (measurements) — *measured_by*
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **LMSYS Chatbot Arena** (measurements) — *measured_by*
  > “An emerging trend in LLM evaluation is therefore to rely on open-ended evaluation systems, a notable example being the LMSYS Chatbot Arena”
  - [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf)
- **C-Eval** (measurements) — *measured_by*
  - [Enhancing Automated Interpretability with Output-Centric Feature Descriptions](https://aclanthology.org/2025.acl-long.289.pdf)
- **CMMLU** (measurements) — *measured_by*
  - [Enhancing Automated Interpretability with Output-Centric Feature Descriptions](https://aclanthology.org/2025.acl-long.289.pdf)
- **RACE** (measurements) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **AG News** (measurements) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)
- **IMDb** (measurements) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)

### Associated with
- **Commonsense knowledge** (constructs)
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Reasoning** (constructs)
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  > Validated across multiple datasets and models, this method significantly alleviates forgetting in both general and in-context learning abilities, confirming the correlation between FV dynamics and forgetting. (Section 1)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.940.pdf)
- **Question difficulty** (constructs)
  - [Principled Data Selection for Alignment: The Hidden Risks of Difficult Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25f/gao25f.pdf)

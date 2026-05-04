# Knowledge transfer
**Type:** Construct  
**Referenced in:** 90 papers  
**Also known as:** Transferability, Attack transferability, Ability transfer, Transfer learning, Skill transfer, Generalization to unseen tasks, Transfer, Cross-task generalization, Class-knowledge transfer, Task transfer, Cross-task transfer, In-context transferability, Strategy transferability, Task transferability, Backward transfer, Forward transfer, Hyperparameter transfer, Multilingual transfer, Cross-lingual transferability  

## State of the Field

Across the provided literature, "Knowledge transfer" is predominantly framed as a model's ability to apply learned knowledge, skills, or representations from one context—such as a task, domain, language, or model—to a different one. A substantial line of work focuses specifically on adversarial contexts, defining the concept as "attack transferability" or "strategy transferability," which measures the extent to which jailbreak prompts or data poisoning attacks developed for one model remain effective against others. As one paper states, this is evaluated by the level to which "prompts produced to jailbreak one LLM can successfully jailbreak another model" (AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models). More general applications include the transfer of learned skills to new tasks, the application of knowledge across languages, and the reuse of optimal hyperparameters across model sizes. The construct is also discussed in terms of its directionality, with `forward transfer` referring to improved learning on new tasks and `backward transfer` to improved performance on previously learned ones. Operationally, knowledge transfer is most frequently measured by evaluating a model's performance on unseen tasks or out-of-domain datasets, using benchmarks such as MMLU, HellaSwag, ARC-Challenge, and the adversarial-focused Harmbench. The concept is studied alongside `systematic generalization` and `complex reasoning`. Some work suggests that knowledge transfer is influenced by `abstraction` and `chain-of-thought reasoning`, and in turn, it is reported to improve downstream behaviors like `sign language translation`.

## Sources

**[AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f83cb637e159e789f5576ff6848874de-Paper-Conference.pdf) (as "Transferability")**
> The degree to which continuous prompts learned on one language model can be effectively applied to another, reflecting the generalizability of task semantics across model architectures and embedding spaces.

**[Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf) (as "Attack transferability")**
> The extent to which attacks, either at the prompt or embedding level, developed for one model are effective against other models, suggesting shared vulnerabilities in their safety mechanisms.

**[Finite State Automata Inside Transformers with Chain-of-Thought: A Mechanistic Study on State Tracking](https://aclanthology.org/2025.acl-long.669.pdf)**
> The latent ability of domain-specific experts to share and apply their learned knowledge to relevant downstream tasks within a multi-expert system.

**[CLLMate: A Multimodal Benchmark for Weather and Climate Events Forecasting](https://aclanthology.org/2025.emnlp-main.887.pdf) (as "Ability transfer")**
> The latent capacity to transfer learned capabilities from one language or domain to another without retraining, preserving the core knowledge while adapting to new linguistic contexts.

**[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf) (as "Transfer learning")**
> The ability of a model to leverage knowledge gained from training on one task or objective to improve its performance on a different but related task or objective.

**[Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf) (as "Skill transfer")**
> The degree to which a capability or mechanism learned on one task can be successfully applied or adapted to improve performance on a different task.

**[Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf) (as "Knowledge transferability")**
> The model's ability to effectively transfer learned patterns and knowledge from source domains to improve performance on different target domains.

**[HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/e43a33994a28f746dcfd53eb51ed3c2d-Paper-Conference.pdf) (as "Generalization to unseen tasks")**
> The ability of a model to perform effectively on tasks that were not included in its fine-tuning data.

**[Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf) (as "Transfer")**
> The ability to apply learned knowledge, such as abstract variables, from a training context to a new, related context.

**[dEBORA: Efficient Bilevel Optimization-based low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f0c4f3d83c58df58380af3b0729354c-Paper-Conference.pdf) (as "Cross-task generalization")**
> The model's ability to apply knowledge learned from one set of tasks to perform well on different, unseen tasks.

**[Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf) (as "Task generalization")**
> The extent to which a compressed model preserves performance across in-domain and out-of-domain evaluation settings.

**[Task-Adaptive Pretrained Language Models via Clustered-Importance Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/688006b3d1df8be5bb2a2a31a407180c-Paper-Conference.pdf) (as "Task transfer")**
> The ability of a model trained for one task to perform well on a different, unevaluated task.

**[Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf) (as "Class-knowledge transfer")**
> The ability of an LLM to transfer learned properties from higher-level classes to subordinate entities.

**[LLaVA-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c9f95e9ec39fa5ad3d0a562b993b92aa-Paper-Conference.pdf) (as "Cross-task transfer")**
> The ability to apply knowledge or skills learned from one set of tasks to perform new, untrained tasks, often by composing existing capabilities.

**[BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf) (as "In-context transferability")**
> A task-level latent property estimated from how much exemplars from one task improve performance on another task when used as in-context examples.

**[AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf) (as "Strategy transferability")**
> The extent to which discovered jailbreak strategies remain effective across different target models, attacker models, or datasets.

**[BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf) (as "Task transferability")**
> The degree to which knowledge or skill learned from one task improves performance on another task, reflecting overlap or generalization across tasks.

**[LeanAgent: Lifelong Learning for Formal Theorem Proving](https://proceedings.iclr.cc/paper_files/paper/2025/file/b67c77f8db8b991d73d6f2e16f491840-Paper-Conference.pdf) (as "Backward transfer")**
> The extent to which learning new tasks improves performance on previously learned tasks.

**[Adapt-$\infty$: Scalable Continual Multimodal Instruction Tuning via Dynamic Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6610efd6c767f63343a4ab28505212e-Paper-Conference.pdf) (as "Forward transfer")**
> The phenomenon where knowledge gained from previous tasks improves the learning of new, subsequent tasks.

**[u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e3130a164f5c724e37271b93bc76dd28-Paper-Conference.pdf) (as "Hyperparameter transfer")**
> The degree to which optimal hyperparameter values found on a small proxy model successfully apply to a larger target model, maintaining performance.

**[YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf) (as "Multilingual transfer")**
> The phenomenon where training a model on multiple languages, including high-resource ones, improves its performance on low-resource languages.

**[McEval: Massively Multilingual Code Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/dad66bb085bab14fbca07cfa4271f00b-Paper-Conference.pdf) (as "Cross-lingual transferability")**
> The model's ability to apply knowledge and skills learned from one programming language to tasks in another programming language.

## Relationships

### Knowledge transfer →
- **Generalization** (constructs) — *causes*
  - [Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)
- **Sign language translation** (behaviors tasks) — *causes*
  > We see that on both translation and lang id, sign language pretraining is substantially better than none (as in Uthus et al. [35]) and multilingual transfer helps both the higher-resource sign language (ASL) and the lower-resource sign languages within YouTube-SL-25.
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
- **Sign language recognition** (behaviors tasks) — *causes*
  > We see that on both translation and lang id, sign language pretraining is substantially better than none (as in Uthus et al. [35]) and multilingual transfer helps both the higher-resource sign language (ASL) and the lower-resource sign languages within YouTube-SL-25.
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)

### → Knowledge transfer
- **Abstraction** (constructs) — *causes*
  - [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf)
- **Cross-lingual alignment** (constructs) — *causes*
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.328.pdf)

### Associated with
- **Complex reasoning** (behaviors tasks)
  - [Iteration Head: A Mechanistic Study of Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/c50f8180ef34060ec59b75d6e1220f7a-Paper-Conference.pdf)
- **Continual learning** (constructs)
  - [Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf)
- **Knowledge manipulation** (constructs)
  - [Knowledge Graph Finetuning Enhances Knowledge Manipulation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e44337573fcac83f219c8effa4ebf90d-Paper-Conference.pdf)
- **Expert specialization** (constructs)
  - [Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d24b7366d714b09a977946ef0d9bf3ad-Paper-Conference.pdf)

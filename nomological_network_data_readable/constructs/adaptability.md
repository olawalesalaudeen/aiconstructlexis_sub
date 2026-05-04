# Adaptability
**Type:** Construct  
**Referenced in:** 113 papers  
**Also known as:** Adaptation, Continual learning efficiency, Adaptivity, Self-adaptation, Adaptive capabilities, Cross-domain transfer, Domain adaptation, Cross-table generalizability, Cross-platform generalization, Task-specific adaptation, Task-adaptiveness, Task adaptivity, Adaptation to feedback, Cognitive flexibility, Distributional flexibility, Domain knowledge adaptation, Rapid domain adaptation  

## State of the Field

Across the surveyed literature, "Adaptability" is a broad construct, often used interchangeably with terms like "domain adaptation" and "flexibility," that predominantly refers to a model's capacity to adjust its behavior and performance to new tasks, domains, or data distributions without requiring full retraining. The prevailing usage frames this as aligning a model with specific downstream tasks based on their distributional characteristics or maintaining performance when faced with a domain shift. A smaller subset of work defines adaptability more specifically, for instance as "self-adaptation," where a model modifies its own behavior in real-time without external intervention, or as "adaptivity," which refers to an optimizer's use of parameter-specific update rules. The literature also contains discussion on whether adaptation represents true new learning or, as one paper asks, if it "simply draw[s] out capabilities that the model had already learned" (A Benchmark for Learning to Translate a New Language from One Grammar Book). The construct is operationalized and measured through model performance on a wide array of benchmarks. Papers in this set use instruments such as AndroidWorld and OSWORLD to evaluate adaptability in dynamic agent tasks, while others like Mind2Web, ScreenSpot, AG News, and ChemProt are used to assess performance on new tasks and domains. Adaptability is frequently studied alongside and considered related to Generalization, and some work reports that planning and compositionality can influence a model's adaptive capabilities.

## Sources

**[A Benchmark for Learning to Translate a New Language from One Grammar Book](https://proceedings.iclr.cc/paper_files/paper/2024/file/52d63f9e4b81f866bf69fb3c834aad47-Paper-Conference.pdf) (as "Adaptation")**
> The capacity of a model to acquire new capabilities or knowledge from limited, task-specific reference materials rather than relying on pre-existing training data.

**[DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf)**
> The ability of a model to adjust its behavior and performance to align with specific downstream tasks based on their distributional characteristics.

**[Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf) (as "Continual learning efficiency")**
> The ability of a model to rapidly adapt to new downstream tasks beyond its initial training set, indicating how well it builds on existing knowledge for future learning.

**[GITA: Graph to Visual and Textual Integration for Vision-Language Graph Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/00295cede6e1600d344b5cd6d9fd4640-Paper-Conference.pdf) (as "Flexibility")**
> The model's capacity to handle diverse tasks using the same architecture without requiring specialized, task-specific designs.

**[Deconstructing What Makes a Good Optimizer for Autoregressive Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/07ea874e9e4f71ec6680a3574a485a36-Paper-Conference.pdf) (as "Adaptivity")**
> The extent to which an optimizer uses parameter-specific or layer-specific preconditioning rather than a single global update rule.

**[Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf) (as "Self-adaptation")**
> The ability of a large language model to evaluate and modify its own behavior in real-time in response to the specific demands of a given task or prompt, without external intervention.

**[ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf) (as "Adaptive capabilities")**
> The latent capacity of a language model to flexibly adjust its behavior to new tasks or scenarios without retraining.

**[Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf) (as "Cross-domain generalization")**
> The model's ability to maintain performance when evaluated on data from a different domain or distribution than its training data.

**[NatureLM-audio: an Audio-Language Foundation Model for Bioacoustics](https://proceedings.iclr.cc/paper_files/paper/2025/file/36c20807317ae6cb3817acd554da2d32-Paper-Conference.pdf) (as "Cross-domain transfer")**
> The capacity to reuse representations learned from speech and music for bioacoustic tasks.

**[Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf) (as "Domain adaptation")**
> The model's ability to adjust its output distribution to better suit a specific domain, such as medicine or law, without undergoing additional training.

**[Bridging the Semantic Gap Between Text and Table: A Case Study on NL2SQL](https://proceedings.iclr.cc/paper_files/paper/2025/file/283f1354f1de1c53a14afe0a6740e889-Paper-Conference.pdf) (as "Cross-table generalizability")**
> The extent to which learned table representations transfer across different tables and schemas rather than overfitting to a specific table or prompt context.

**[Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf) (as "Cross-platform generalization")**
> The degree to which a model's performance transfers across different operating systems and environments (web, desktop, mobile) without specific training on all platforms.

**[Text-to-LoRA: Instant Transformer Adaption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/charakorn25a/charakorn25a.pdf) (as "Task-specific adaptation")**
> The latent capacity of a model to adjust its behavior to meet the requirements of a particular downstream task through parameter modification.

**[Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ge25d/ge25d.pdf) (as "Task adaptation")**
> The latent ability of the model to effectively learn and perform on new tasks in a sequential setting without access to prior data.

**[Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cu/li25cu.pdf) (as "Cognitive flexibility")**
> The ability to shift behavior when rules or contingencies change, rather than persisting with a previously successful strategy.

**[Can Transformers Learn Full Bayesian Inference in Context?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/reuter25a/reuter25a.pdf) (as "Distributional flexibility")**
> The latent ability to adapt to complex, non-Gaussian, and multimodal posterior shapes without being constrained by parametric variational families.

**[Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25d/shi25d.pdf) (as "Adaptation to feedback")**
> The ability to dynamically modify behavior in response to real-time user corrections, constraints, or changes in task goals during execution.

**[Generalization Principles for Inference over Text-Attributed Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bq/wang25bq.pdf) (as "Task adaptivity")**
> The capacity of a model to adjust its internal representations or reasoning based on the specific task context, such as class definitions or labeling goals, without fine-tuning.

**[G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cu/zhang25cu.pdf) (as "Task-adaptiveness")**
> The latent ability of a multi-agent system to dynamically adjust its communication topology complexity based on the difficulty and nature of the given task, optimizing efficiency and performance.

**[Test-Time Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25z/hu25z.pdf) (as "Domain knowledge adaptation")**
> The latent ability of an LLM to adjust to specialized subject-matter content in vertical domains such as medicine, agriculture, geography, and finance.

**[HICode: Hierarchical Inductive Coding withLLMs](https://aclanthology.org/2025.emnlp-main.1581.pdf) (as "Rapid domain adaptation")**
> The capacity of a speculative decoding method to quickly adjust its draft generation to new or low-resource domains without retraining, by leveraging generalizable patterns from cached n-grams.

## Relationships

### Adaptability →
- **AndroidWorld** (measurements) — *measured_by*
  > This approach enables ﬁner-grained analyses of agent adaptability, essential for real-world deployment. (Section 3.3)
  - [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/01a83bc2f2732a58e6aa731e659e7101-Paper-Conference.pdf)
- **RCT** (measurements) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **ChemProt** (measurements) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **AG News** (measurements) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **IMDb** (measurements) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **ScreenSpot** (measurements) — *measured_by*
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **MiniWoB++** (measurements) — *measured_by*
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **AitW** (measurements) — *measured_by*
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **Mind2Web** (measurements) — *measured_by*
  > Our approach demonstrates superior performance in task accuracy and adaptability, as validated by benchmarks such as ScreenSpot, MiniWob, AITW, and Mind2Web.
  - [Grounding Multimodal Large Language Model in GUI World](https://proceedings.iclr.cc/paper_files/paper/2025/file/31fc85f7461ce71eadf27fb7281973bd-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **OSWORLD** (measurements) — *measured_by*
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **Compositionality** (constructs) — *causes*
  > By focusing on this principled parameterization, our approach mitigates the risk of overfitting, drastically reduces computational demands, and allows for inherent compositionality. (Section 1)
  - [Transformer-Squared: Self-adaptive LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/244da015b91e64f2d9362703fa2a902b-Paper-Conference.pdf)

### → Adaptability
- **In-context learning** (constructs) — *causes*
  - [Zebra: In-Context Generative Pretraining for Solving Parametric PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/serrano25a/serrano25a.pdf)
- **Planning** (constructs) — *causes*
  > "Additionally, unlike previous methods that relied on linear action sequences and re-planning from scratch... OSCAR’s state machine integrates real-time verification feedback for fine-grained, task-driven re-planning, significantly improving efficiency and adaptability."
  - [OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)

### Associated with
- **Generalization** (constructs)
  > "we investigate whether ASPRM demonstrates model transferability and rating position, in-domain, and cross-domain generalization capability"
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
- **Catastrophic forgetting** (behaviors tasks)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.932.pdf)
- **Multimodal understanding** (constructs)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
- **Masked language modeling** (behaviors tasks)
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [ComLoRA: A Competitive Learning Approach for Enhancing LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/e993102e60e4484686f0bafe7ba8b8f2-Paper-Conference.pdf)
- **Consistency** (constructs)
  - [Effective Skill Unlearning through Intervention and Abstention](https://aclanthology.org/2025.naacl-long.323.pdf)
- **Machine translation** (behaviors tasks)
  - [HICode: Hierarchical Inductive Coding withLLMs](https://aclanthology.org/2025.emnlp-main.1581.pdf)
- **Text summarization** (behaviors tasks)
  - [AesBiasBench: Evaluating Bias and Alignment in Multimodal Language Models for Personalized Image Aesthetic Assessment](https://aclanthology.org/2025.emnlp-main.387.pdf)

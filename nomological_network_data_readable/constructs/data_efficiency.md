# Data efficiency
**Type:** Construct  
**Referenced in:** 88 papers  
**Also known as:** Sample efficiency, Sample-efficiency, Data Efficiency, Data utilization  

## State of the Field

Across the surveyed literature, the most prevalent framing of data efficiency is a model's ability to achieve strong performance with limited training data. This is broadly defined as either requiring a smaller absolute amount of data to reach a performance target or learning effectively from few examples, demonstrations, or feedback. While this core idea is consistent, its specific manifestation varies by context; for instance, in policy learning it is described as improving from few demonstrations, while in generative or embodied settings it can refer to minimizing oracle calls, candidate solutions, or environmental interactions. The construct is operationalized and measured through model performance in data-scarce scenarios on benchmarks including ALFWorld, VirtualHome, GrailQA, and FGVC. Data efficiency is also studied in relation to Reward Modeling. Several papers propose mechanisms that are reported to improve data efficiency, including a model's capacity for Relational reasoning, Self-reflection, and Task decomposition. Other reported drivers are algorithmic, such as In-context reinforcement learning and Attention sparsity, with one study noting that sparsity is a "key factor of the improvement induced by CoT" ("From Sparse Dependence to Sparse Attention..."). The ability to leverage pre-trained knowledge is also frequently cited as a source of data efficiency, as noted in papers like "Vision-Language Foundation Models as Effective Robot Imitators".

## Sources

**[$\mathcal{B}$-Coder: Value-Based Deep Reinforcement Learning for Program Synthesis](https://proceedings.iclr.cc/paper_files/paper/2024/file/7e9c2053258b1bdd32ff2654802cd594-Paper-Conference.pdf) (as "Sample efficiency")**
> The ability of a model to achieve strong performance with limited training data by leveraging shared skills and effective parameter usage across tasks.

**[Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)**
> The amount of training data required for a model to achieve a certain level of performance on a task, with higher efficiency meaning less data is needed.

**[Policy Improvement using Language Feedback Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/4d4f7cf206bb00f9a38a5b6ae92cf79a-Paper-Conference.pdf) (as "Sample-efficiency")**
> The degree to which a policy-learning approach can improve from few demonstrations or limited feedback rather than requiring many expert examples.

**[Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (as "Data Efficiency")**
> The latent property describing how effectively a model utilizes training data to achieve performance, often measured by epochs or tokens required.

**[Data Selection via Optimal Control for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf) (as "Data utilization")**
> The efficiency with which a model learns from a given amount of pre-training data, where higher utilization means achieving a target performance level with less data.

## Relationships

### Data efficiency →
- **VirtualHome** (measurements) — *measured_by*
  - [True Knowledge Comes from Practice: Aligning Large Language Models with Embodied Environments via Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ee60f53717bd9c2abdcca66dfbec65da-Paper-Conference.pdf)
- **ALFWorld** (measurements) — *measured_by*
  > "We conduct experiments on major benchmarks like ALFWorld and Overcooked, demonstrating that the sample efficiency of traditional RL algorithms... can largely benefit from integrating LLM action priors."
  - [Efficient Reinforcement Learning with Large Language Model Priors](https://proceedings.iclr.cc/paper_files/paper/2025/file/797be96e4481c3fe5d675c1ba5352969-Paper-Conference.pdf)
- **GrailQA** (measurements) — *measured_by*
  - [Context-Aware Sentiment Forecasting viaLLM-based Multi-Perspective Role-Playing Agents](https://aclanthology.org/2025.acl-long.137.pdf)
- **FGVC** (measurements) — *measured_by*
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)

### → Data efficiency
- **Self-reflection** (behaviors tasks) — *causes*
  - [ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ced59d480e07d290b6f29fc8798f195-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks) — *causes*
  - [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf)
- **Attention sparsity** (constructs) — *causes*
  > Using a parity-learning setup, we demonstrate that CoT can substantially improve sample efficiency... confirming that sparsity in attention layers is a key factor of the improvement induced by CoT.
  - [From Sparse Dependence to Sparse Attention: Unveiling How Chain-of-Thought Enhances Transformer Sample Efficiency](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa6d4d2020aac4bd8f7cdb2771fc1ae2-Paper-Conference.pdf)
- **In-context reinforcement learning** (constructs) — *causes*
  > Recent studies have shown that Transformers can perform in-context reinforcement learning (RL) by imitating existing RL algorithms, enabling sample-efficient adaptation to unseen tasks without parameter updates.
  - [Distilling Reinforcement Learning Algorithms for In-Context Model-Based Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5c4a7643ab90cd62320df95c873a1c6f-Paper-Conference.pdf)
- **Relational reasoning** (constructs) — *causes*
  > Our results demonstrate that integrating explicit relational computational mechanisms into the Transformer architecture leads to significant performance gains in terms of data efficiency and parameter efficiency. (Section 1)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
- **Knowledge transferability** (constructs) — *causes*
  - [Can RLHF be More Efficient with Imperfect Reward Models? A Policy Coverage Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25o/huang25o.pdf)
- **General reasoning** (constructs) — *causes*
  - [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.727.pdf)

### Associated with
- **Reward Modeling** (measurements)
  - [Are explicit belief representations necessary? A comparison between Large Language Models andBayesian probabilistic models](https://aclanthology.org/2025.naacl-long.573.pdf)

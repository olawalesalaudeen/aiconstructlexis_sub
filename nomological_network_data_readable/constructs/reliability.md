# Reliability
**Type:** Construct  
**Referenced in:** 42 papers  
**Also known as:** Model reliability, Prediction reliability, Reasoning reliability, Reward model reliability, Tool reliability, Verifier reliability  

## State of the Field

Across the surveyed literature, Reliability is predominantly characterized as a latent property of a model concerning its ability to consistently perform correctly and safely. Multiple definitions converge on the related concepts of dependability and trustworthiness, with one paper defining it as the "overall dependability and consistency of a model's performance and outputs across different situations" ("CODE..."). A recurring framing is that reliability entails freedom from errors, such as outputs containing "outdated or incorrect information" or "undesirable biases" ("A Cognitive Evaluation Benchmark..."). The absence of this property is described as a factor that "hinders the adoption of LMMs in real-world applications" ("CODE..."), and it is a particular focus in high-stakes domains like biomedicine. Since the provided data does not specify measurement instruments, the operational focus is on methods to improve this construct. One commonly cited approach is uncertainty quantification, described as a "promising direction to improve the reliability of LLMs" ("Kernel Language Entropy..."). Another perspective suggests reliability can be enhanced when models provide "explicit reasoning processes and attribution" and acknowledge their own limitations ("mPLUG-DocOwl2...").

## Sources

**[Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities](https://proceedings.neurips.cc/paper_files/paper/2024/file/10c456d2160517581a234dfde15a7505-Paper-Conference.pdf)**
> The latent property of a model consistently performing correctly and safely, which uncertainty quantification aims to improve.

**[CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf) (as "Model reliability")**
> The overall dependability and consistency of a model's performance and outputs across different situations.

**[A Hitchhiker’s Guide to Scaling Law Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/choshen25a/choshen25a.pdf) (as "Prediction reliability")**
> The degree to which estimated scaling laws consistently and accurately forecast the performance of target models, accounting for variability across seeds and training dynamics.

**[BRiTE: Bootstrapping Reinforced Thinking Process to Enhance Language Model Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhong25e/zhong25e.pdf) (as "Reasoning reliability")**
> The consistency and trustworthiness of a model's reasoning outputs, such that generated rationales are valid and lead to correct conclusions across diverse problems.

**[Policy Filtration for RLHF to Mitigate Noise in Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bq/zhang25bq.pdf) (as "Reward model reliability")**
> The degree to which a reward model's assigned rewards align with the actual performance of model responses, varying across reward ranges.

**[Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf) (as "Tool reliability")**
> The ability of a large language model to accurately and effectively interact with external tools throughout a task, maximizing successful outcomes while minimizing errors and hallucinations.

**[From Passive to Active Reasoning: Can Large Language Models Ask the Right Questions under Incomplete Information?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25e/zhou25e.pdf) (as "Verifier reliability")**
> The consistency and accuracy with which a model component evaluates and selects promising reasoning paths during search-based active reasoning, affecting the overall effectiveness of strategies like tree-of-thought.

## Relationships

### Reliability →
- **TruthfulQA** (measurements) — *measured_by*
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf)
- **zs-RE** (measurements) — *measured_by*
  - [Investigating Pedagogical Teacher and StudentLLMAgents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.676.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Commonsense Reasoning inArab Culture](https://aclanthology.org/2025.acl-long.381.pdf)
- **CounterFact** (measurements) — *measured_by*
  - [Investigating Pedagogical Teacher and StudentLLMAgents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.676.pdf)

### → Reliability
- **Hallucination** (behaviors tasks) — *causes*
  - [Seeing More, Saying More: Lightweight Language Experts are Dynamic Video Token Compressors](https://aclanthology.org/2025.emnlp-main.29.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *causes*
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **Adversarial robustness** (constructs)
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Locality** (constructs)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Confidence calibration** (constructs)
  - [On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf)
- **Preference consistency** (constructs)
  - [Aligning with Logic: Measuring, Evaluating and Improving Logical Preference Consistency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25u/liu25u.pdf)
- **Validity** (constructs)
  - [Position: Human Baselines in Model Evaluations Need Rigor and Transparency (With Recommendations & Reporting Checklist)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25s/wei25s.pdf)
- **Representational stability** (constructs)
  - [ConsistentChat: Building Skeleton-Guided Consistent Multi-Turn Dialogues for Large Language Models from Scratch](https://aclanthology.org/2025.emnlp-main.425.pdf)

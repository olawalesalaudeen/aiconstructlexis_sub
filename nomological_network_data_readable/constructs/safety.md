# Safety
**Type:** Construct  
**Referenced in:** 832 papers  
**Also known as:** Security alignment, LLM security, Safety capability, Thread-safety, Safety performance, Safety-aware reasoning, Model robustness, Bias resistance, Hidden representation stability, Molecular stability, Unlearning Stability, Training instability, Routing stability, Feature learning stability, Multi-turn stability, Policy stability, Vision feature stability, Attention entropy stability, Recursive stability, Content safety, Temporal generalizability, Error tolerance, Response consistency, Stylistic self-consistency, Instruction sensitivity, Typo-fixing  

## State of the Field

The prevailing usage of "Safety" across the provided literature centers on a model's disposition to avoid generating harmful, unethical, unsafe, or toxic content, a concept frequently labeled as "Harmlessness." This construct is most often discussed in the context of a model's response to adversarial or malicious prompts, with several papers defining it as the ability to resist such "jailbreak" attempts. A recurring theme is the tension between safety and helpfulness, often described as competing objectives; as one paper notes, "the use of instruction finetuning without safety considerations introduces a rather critical trade-off between helpfulness and harmfulness" (Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions). A smaller set of papers frames the concept more broadly as "Trustworthiness," a quality encompassing reliability and fairness, while a distinct, outlier usage of "Thread-safety" refers to processing multiple information streams simultaneously. The field operationalizes safety by evaluating model outputs on a wide array of benchmarks designed to elicit unsafe behavior, including `AdvBench`, `Harmbench`, `JailbreakBench`, and `ToxiGen`. A primary behavior used as an indicator of safety is the model's "Refusal to answer" harmful queries, and evaluation is also commonly performed using `LLM-as-a-judge` setups. Several constructs are positioned as influencing safety, with `Human preference alignment` and `Logical reasoning` reported to improve it, while phenomena like `Knowledge forgetting` are seen as detrimental. The concept is also studied alongside "Robustness," though robustness is typically defined more broadly as performance stability under various perturbations rather than exclusively avoiding harmful content.

## Sources

**[ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf) (as "Harmlessness")**
> The property of a model to avoid producing unsafe, unethical, or toxic content.

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)**
> The model's disposition to avoid generating harmful, unethical, or dangerous content, particularly in response to adversarial prompts.

**[Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf) (as "Security alignment")**
> The extent to which an LLM has been aligned to distinguish malicious from normal inputs and keep its behavior within safe boundaries.

**[Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf) (as "LLM security")**
> The model-level property of resisting harmful or malicious prompts by refusing unsafe requests and avoiding harmful outputs.

**[On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf) (as "Safety capability")**
> The latent property of a large language model that enables it to align with human values by avoiding the generation of unsafe, toxic, or harmful content in response to queries.

**[Needle Threading: Can LLMs Follow Threads Through Near-Million-Scale Haystacks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/acfcb9e8f066f14cab7368e07cfab5be-Paper-Conference.pdf) (as "Thread-safety")**
> The ability of a model to simultaneously track and process multiple independent threads of information or queries without a significant degradation in performance.

**[CoE: A Clue of Emotion Framework for Emotion Recognition in Conversations](https://aclanthology.org/2025.acl-long.1149.pdf) (as "Safety performance")**
> The underlying trait reflecting how effectively a model resists generating unsafe content, inferred from patterns of refusal across diverse linguistic and cultural contexts.

**[PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1493.pdf) (as "Safety-aware reasoning")**
> The latent ability of a model to integrate safety evaluation into its reasoning process, enabling self-monitoring and dynamic adjustment of responses based on safety status at each step.

**[Gandalf the Red: Adaptive Security for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pfister25a/pfister25a.pdf) (as "Security")**
> The degree to which a defense prevents attackers from successfully exploiting an LLM application.

**[AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f83cb637e159e789f5576ff6848874de-Paper-Conference.pdf) (as "Robustness")**
> The stability of model performance under variations in prompt engineering choices, including in-context example selection, order, template design, and verbalizer format.

**[Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf) (as "Model robustness")**
> The stability of an LLM's reasoning performance across similar problems, tasks, or perturbations in task conditions.

**[FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf) (as "Bias resistance")**
> The tendency to resist being led into biased outputs when confronted with misleading guidance, biased context, or conflicting instructions.

**[Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf) (as "Stability")**
> The property of a decoding algorithm where small perturbations to the model's logits result in only small, bounded changes to the output token probabilities.

**[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf) (as "Hidden representation stability")**
> The degree to which the internal distribution of hidden states remains invariant after parameter editing.

**[NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/3fb6c52aeb11e09053c16eabee74dd7b-Paper-Conference.pdf) (as "Molecular stability")**
> The degree to which generated molecular structures remain chemically stable and adhere to valency constraints.

**[Towards Robust and Parameter-Efficient Knowledge Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3076133f08b40607d00a8f48f6acd71c-Paper-Conference.pdf) (as "Unlearning Stability")**
> The degree to which the optimization process during unlearning avoids divergence or catastrophic forgetting of retained knowledge.

**[A Multi-Power Law for Loss Curve Prediction Across Learning Rate Schedules](https://proceedings.iclr.cc/paper_files/paper/2025/file/63e88a6ebfb1f68808a058a32b947e71-Paper-Conference.pdf) (as "Training stability")**
> The property of the training process characterized by the absence of overshooting and oscillation in the loss landscape.

**[SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf) (as "Training instability")**
> A latent property of the LLM training process characterized by disruptions to learning, which can lead to performance degradation or catastrophic divergence.

**[u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e3130a164f5c724e37271b93bc76dd28-Paper-Conference.pdf) (as "Numerical stability")**
> The property of a model's training process where the floating-point representations of tensors stay within the valid range of a given numerical format, avoiding overflow or underflow.

**[MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7efe88bb4138d602e56637cfcf713654-Paper-Conference.pdf) (as "Routing stability")**
> The consistency and reliability of the expert selection mechanism across different layers and inputs.

**[u-$\mu$P: The Unit-Scaled Maximal Update Parametrization](https://proceedings.iclr.cc/paper_files/paper/2025/file/e3130a164f5c724e37271b93bc76dd28-Paper-Conference.pdf) (as "Feature learning stability")**
> The property of a model's training dynamics where different components learn at balanced rates, avoiding situations where some parts learn too quickly or slowly relative to others.

**[SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf) (as "Multi-turn stability")**
> The degree to which an LLM maintains adherence to system-message constraints over successive dialogue turns.

**[WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c66e1fcc9691aae706250638f36f681b-Paper-Conference.pdf) (as "Policy stability")**
> The degree to which the agent's policy avoids excessive drift across training phases while still improving on new tasks.

**[PolyPythias: Stability and Outliers across Fifty Language Model Pre-Training Runs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d611d06e3207330555fbc10810e70163-Paper-Conference.pdf) (as "Representational stability")**
> The consistency of token representations across seeds and training checkpoints, indicating how similar internal states remain under varying initial conditions.

**[Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf) (as "Vision feature stability")**
> The property of a vision encoder to produce consistent and unvarying feature representations when the semantic content of an input image remains unchanged despite mild perturbations.

**[ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf) (as "Attention entropy stability")**
> The tendency for the model's attention distribution to remain from becoming overly diffuse as context length increases.

**[A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf) (as "Recursive stability")**
> A property of a generative model in a self-consuming training loop that quantifies how much its output distribution changes in response to small perturbations in the initial real dataset across multiple generations.

**[A Survey ofQUDModels for Discourse Processing](https://aclanthology.org/2025.naacl-long.85.pdf) (as "Trustworthiness")**
> The broader latent quality of being reliable and safe across multiple risk dimensions, including harmfulness, bias, and other safety concerns.

**[Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.306.pdf) (as "Content safety")**
> The latent tendency of an LLM to avoid unsafe, harmful, or policy-violating content in human interactions.

**[Large Language Models Share Representations of Latent Grammatical Concepts Across Typologically Diverse Languages](https://aclanthology.org/2025.naacl-long.313.pdf) (as "Temporal generalizability")**
> The ability of a classification model to maintain performance when applied to future data that may exhibit distributional shifts over time.

**[DS2-ABSA: Dual-Stream Data Synthesis with Label Refinement for Few-Shot Aspect-Based Sentiment Analysis](https://aclanthology.org/2025.acl-long.753.pdf) (as "Error tolerance")**
> The latent ability of a model to maintain performance quality despite input errors or noise, such as producing coherent summaries from imperfect transcriptions.

**[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.290.pdf) (as "Response consistency")**
> The degree to which a model produces structurally, lexically, and logically stable outputs across different instruction styles for the same underlying task.

**[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.290.pdf) (as "Stylistic self-consistency")**
> A model's ability to generate outputs that are stylistically similar to each other when responding to the same problem presented with varied instructions.

**[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.290.pdf) (as "Instruction sensitivity")**
> The degree to which a model's outputs and performance change when the same task is phrased with different instruction styles.

**[VisCRA: A Visual Chain Reasoning Attack for Jailbreaking Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.313.pdf) (as "Typo-fixing")**
> The latent ability of an LLM to recognize and correct typographical errors in input text by leveraging local and global contextual information to recover the intended meaning.

## Relationships

### Safety →
- **AdvBench** (measurements) — *measured_by*
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **ToxiGen** (measurements) — *measured_by*
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
- **Reward-Bench** (measurements) — *measured_by*
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
- **XSTEST** (measurements) — *measured_by*
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://aclanthology.org/2025.naacl-long.281.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Llama Guard 2** (measurements) — *measured_by*
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
- **MM-SafetyBench** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **RealToxicityPrompts** (measurements) — *measured_by*
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **MaliciousInstruct** (measurements) — *measured_by*
  - [Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **StrongReject** (measurements) — *measured_by*
  - [REFFLY: Melody-Constrained Lyrics Editing Model](https://aclanthology.org/2025.naacl-long.565.pdf)
- **Beavertails** (measurements) — *measured_by*
  - [Powerformer: Efficient and High-Accuracy Privacy-Preserving Language Model with Homomorphic Encryption](https://aclanthology.org/2025.acl-long.544.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3b18d368150474ac6fc9bb665d3eb3da-Paper-Conference.pdf)
- **OpenAI moderation API** (measurements) — *measured_by*
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **JailbreakBench** (measurements) — *measured_by*
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
- **ALERT** (measurements) — *measured_by*
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **Privacy** (constructs) — *measured_by*
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *causes*
  - [Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf)
- **SORRY-Bench** (measurements) — *measured_by*
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **SIUO** (measurements) — *measured_by*
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **FigStep** (measurements) — *measured_by*
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Model collapse** (constructs) — *causes*
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Anthropic HHH** (measurements) — *measured_by*
  - [Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **t-SNE visualization** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **HEX-PHI** (measurements) — *measured_by*
  - [Powerformer: Efficient and High-Accuracy Privacy-Preserving Language Model with Homomorphic Encryption](https://aclanthology.org/2025.acl-long.544.pdf)
- **DoAnythingNow** (measurements) — *measured_by*
  - [Neuron-Level Sequential Editing for Large Language Models](https://aclanthology.org/2025.acl-long.816.pdf)
- **TRACE** (measurements) — *measured_by*
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **POSE** (measurements) — *measured_by*
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
- **FINTRUST** (measurements) — *measured_by*
  - [Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **VoiceBench** (measurements) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **PLLuM-Align** (measurements) — *measured_by*
  - [REALM: Recursive Relevance Modeling forLLM-based Document Re-Ranking](https://aclanthology.org/2025.emnlp-main.1219.pdf)

### → Safety
- **Alignment** (constructs) — *causes*
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **Text editing** (behaviors tasks) — *causes*
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *correlates*
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)

### Associated with
- **Harmlessness** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Refusal to answer** (behaviors tasks)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [Functional Homotopy: Smoothing Discrete Optimization via Continuous Parameters for LLM Jailbreak Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed212957dbe503283c577a94202cb8c-Paper-Conference.pdf)
- **Trustworthiness** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (constructs)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Usefulness** (constructs)
  - [Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats](https://proceedings.iclr.cc/paper_files/paper/2025/file/699c5a2bb87a8aa32c4ad541d9997361-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Backdoor vulnerability** (constructs)
  - [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf)
- **Jailbreak resistance** (behaviors tasks)
  - [Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation andGaussian-Decayed Contrastive Learning](https://aclanthology.org/2025.acl-long.245.pdf)
- **Generation quality** (constructs)
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
- **Personalization** (constructs)
  - [Retrospective Learning from Interactions](https://aclanthology.org/2025.acl-long.1201.pdf)
- **Ethical reasoning** (constructs)
  - [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)

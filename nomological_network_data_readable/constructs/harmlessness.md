# Harmlessness
**Type:** Construct  
**Referenced in:** 207 papers  
**Also known as:** Harmfulness, Toxicity, Hatefulness, Exaggerated safety behaviors, Harm, Non-toxicity, Oversafety, Anti-toxicity  

## State of the Field

Across the surveyed literature, Harmlessness is predominantly framed as a latent construct representing a model's disposition to avoid generating unsafe, unethical, or toxic content, often in response to malicious prompts. This concept is frequently discussed under the related names "Toxicity" and "Harmfulness," encompassing a wide range of undesirable outputs from rude language and hateful sentiment to the promotion of dangerous activities. The field operationalizes this construct through a diverse set of measurement instruments, with the most common methods including automated classifiers like Perspective API and Detoxify, evaluation using an LLM-as-a-judge, and performance on datasets such as Anthropic HHH and Real-Toxicity-Prompts. Direct human evaluation is also a frequently used measurement approach. Harmlessness is consistently studied alongside "Helpfulness" as a pair of core objectives for "Human preference alignment," a process which some papers state is intended to cause harmlessness. A smaller line of work also characterizes the related phenomenon of "Oversafety" or "Exaggerated safety behaviors," where models overgeneralize safety rules and refuse to answer benign queries. While most definitions are broad, a few papers adopt narrower framings, such as focusing specifically on hateful content or language promoting unhealthy dieting.

## Sources

**[ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf)**
> The degree to which a model avoids producing unsafe or harmful responses when given potentially malicious multimodal inputs.

**[Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf) (as "Toxicity")**
> The latent property or risk of a model generating harmful, offensive, or inappropriate content.

**[SoftMatcha: A Soft and Fast Pattern Matcher for Billion-Scale Corpus Searches](https://proceedings.iclr.cc/paper_files/paper/2025/file/159511050630689045bf5593e74b13cc-Paper-Conference.pdf) (as "Harmfulness")**
> The latent disposition of a model to generate ethically problematic content, such as private information or information that could facilitate dangerous activities.

**[Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf) (as "Hatefulness")**
> The degree to which a text expresses or promotes hateful sentiment toward a target group.

**[CogLM: Tracking Cognitive Development of Large Language Models](https://aclanthology.org/2025.naacl-long.5.pdf) (as "Harm")**
> The extent to which language promotes or glorifies unhealthy dieting, body objectification, or other harmful eating-disorder-related content.

**[Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf) (as "Non-toxicity")**
> The latent trait of a language model to avoid generating harmful or offensive content, especially in response to malicious or provocative prompts.

**[AI-LieDar : Examine the Trade-off Between Utility and Truthfulness inLLMAgents](https://aclanthology.org/2025.naacl-long.596.pdf) (as "Exaggerated safety behaviors")**
> A latent tendency for models to overgeneralize safety constraints, leading to unwarranted refusals to respond to safe or benign queries, especially those involving identity terms.

**[Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation](https://aclanthology.org/2025.naacl-long.604.pdf) (as "Oversafety")**
> A latent tendency of an MLLM to inappropriately refuse or avoid responding to safe or benign inputs due to overgeneralization of safety rules or misperception of risk.

**[StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1501.pdf) (as "Anti-toxicity")**
> The latent tendency of a language model to suppress or counteract toxic content generation, manifested through increased activation of neural components geometrically opposed to toxic representations.

## Relationships

### Harmlessness →
- **Anthropic HHH** (measurements) — *measured_by*
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
- **RealToxicityPrompts** (measurements) — *measured_by*
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
- **Perspective API** (measurements) — *measured_by*
  - [Unveiling and Manipulating Prompt Influence in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/77c6ccacfd9962e2307fc64680fc5ace-Paper-Conference.pdf)
- **Detoxify** (measurements) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **ToxiGen** (measurements) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **PKU-SafeRLHF** (measurements) — *measured_by*
  - [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf)
- **Beavertails** (measurements) — *measured_by*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **AdvBench** (measurements) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **StrongReject** (measurements) — *measured_by*
  - [The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25f/pan25f.pdf)
- **Llama-Guard** (measurements) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **OpenAI moderation API** (measurements) — *measured_by*
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **XSTEST** (measurements) — *measured_by*
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness inLLMAgents](https://aclanthology.org/2025.naacl-long.596.pdf)
- **JailbreakBench** (measurements) — *measured_by*
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **PKU-SafeRLHF-10K** (measurements) — *measured_by*
  - [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf)
- **HEX-PHI** (measurements) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Safe-RLHF** (measurements) — *measured_by*
  - [PromptRefine: Enhancing Few-Shot Performance on Low-ResourceIndic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.18.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **CrowS-Pairs** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Anthropic Red Team** (measurements) — *measured_by*
  - [Unmasking and Improving Data Credibility: A Study with Datasets for Training Harmless Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c3837ae3d17a91b08bf5cc19280e7fd2-Paper-Conference.pdf)
- **GPT-4 Head-to-head Comparison** (measurements) — *measured_by*
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **Hateful Memes** (measurements) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmful content generation** (behaviors tasks) — *causes*
  - [A](https://aclanthology.org/2025.acl-long.185.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **BBQ** (measurements) — *measured_by*
  - [Surprising Effectiveness of pretraining Ternary  Language Model at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/6499f26637f74f7c0fbfb46668434973-Paper-Conference.pdf)
- **Harmful instructions** (measurements) — *measured_by*
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **AgentHarm** (measurements) — *measured_by*
  - [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf)
- **ArmoRM** (measurements) — *measured_by*
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *correlates*
  - [PromptRefine: Enhancing Few-Shot Performance on Low-ResourceIndic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.18.pdf)
- **LlamaGuard 3** (measurements) — *measured_by*
  - [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.239.pdf)
- **GCG attack** (measurements) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **PAIR** (measurements) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **DeepInception** (measurements) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Human preference alignment** (constructs) — *correlates*
  - [Exploiting Contextual Knowledge inLLMs through𝒱-usable Information based Layer Enhancement](https://aclanthology.org/2025.acl-long.1532.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Fairness through Difference Awareness: MeasuringDesiredGroup Discrimination inLLMs](https://aclanthology.org/2025.acl-long.342.pdf)
- **WildChat** (measurements) — *measured_by*
  - [STAIR: Improving Safety Alignment with Introspective Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cx/zhang25cx.pdf)
- **HumanEval** (measurements) — *measured_by*
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf)
- **MBPP** (measurements) — *measured_by*
  - [Toward Efficient Sparse Autoencoder-Guided Steering for Improved In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.1475.pdf)

### → Harmlessness
- **Safety alignment** (constructs) — *causes*
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **Alignment** (constructs) — *causes*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Activation steering** (measurements) — *causes*
  - [StepER: Step-wise Knowledge Distillation for Enhancing Reasoning Ability in Multi-Step Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.1501.pdf)

### Associated with
- **Helpfulness** (constructs)
  - [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks)
  - [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf)
- **Safety** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
- **Safety alignment** (constructs)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Alignment** (constructs)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
- **Harmless response generation** (behaviors tasks)
  - [RLCD: Reinforcement Learning from Contrastive Distillation for LM Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bd09a559a8c8e230697107b0f353d39-Paper-Conference.pdf)
- **Fairness** (constructs)
  - [Chart2Code53: A Large-Scale Diverse and Complex Dataset for Enhancing Chart-to-Code Generation](https://aclanthology.org/2025.emnlp-main.800.pdf)
- **Trustworthiness** (constructs)
  - [More RLHF, More Trust? On The Impact of Preference Alignment On Trustworthiness](https://proceedings.iclr.cc/paper_files/paper/2025/file/732c5757aa5577de9b103332cf7ac0bf-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)
- **Political bias** (constructs)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
- **Humor understanding** (constructs)
  - [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25h/lin25h.pdf)
- **Social bias** (constructs)
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Error handling** (constructs)
  - [To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hedstrom25a/hedstrom25a.pdf)

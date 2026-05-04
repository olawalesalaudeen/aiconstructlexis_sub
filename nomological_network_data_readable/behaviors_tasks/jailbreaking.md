# Jailbreaking
**Type:** Behavior  
**Referenced in:** 39 papers  
**Also known as:** Jailbreak response generation, Multi-turn jailbreak, Jailbreak attack, Jailbreak compliance, Multi-turn jailbreak persistence, Jailbreak attack resistance, Jailbreak success, Jailbreak detection  

## State of the Field

Across the provided literature, jailbreaking is most commonly defined as the observable behavior of bypassing a model's safety mechanisms to elicit a prohibited response, typically through an adversarial prompt. Several papers frame this as an "attack" using specially crafted inputs, with some work specifying variants like "multi-turn jailbreak" where a conversation gradually shifts from benign to harmful content. The primary and consistently stated outcome of successful jailbreaking is the generation of harmful, toxic, or otherwise undesirable content. The behavior is operationalized by measuring a model's compliance with or resistance to these adversarial prompts, often quantified by an "Attack Success Rate (ASR)". A wide array of measurement instruments are used to evaluate jailbreaking, including benchmarks like AdvBench, Harmbench, SafeBench, MM-SafetyBench, and HADES, as well as specific attack methods such as GCG attack and AutoDAN. The study of this behavior is closely related to the concepts of safety alignment and safety mechanisms, which jailbreaking attempts to circumvent. A related but less frequent framing is "Jailbreak detection," which is defined as the task of identifying malicious input prompts.

## Sources

**[Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://aclanthology.org/2025.naacl-long.281.pdf)**
> The observable behavior of bypassing a model's safety mechanisms to elicit a prohibited response, typically through an adversarial prompt.

**[PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1493.pdf) (as "Jailbreak response generation")**
> Producing unsafe or harmful answers when prompted by adversarial jailbreak instructions.

**[Router-Tuning: A Simple and Effective Approach for Dynamic Depth](https://aclanthology.org/2025.emnlp-main.100.pdf) (as "Multi-turn jailbreak")**
> Responding across multiple conversational turns in a way that gradually shifts from benign to harmful content.

**[CIE: Controlling Language Model Text Generations Using Continuous Signals](https://aclanthology.org/2025.emnlp-main.190.pdf) (as "Jailbreak attack")**
> The act of using specially crafted prompts to circumvent a model's safety alignment and induce it to perform forbidden actions.

**[Mahānāma: A Unique Testbed for Literary Entity Discovery and Linking](https://aclanthology.org/2025.emnlp-main.1270.pdf) (as "Jailbreak compliance")**
> Following adversarial prompts that attempt to induce the model to ignore safety rules and comply with harmful requests.

**[Refining Attention for Explainable and Noise-Robust Fact-Checking with Transformers](https://aclanthology.org/2025.emnlp-main.1296.pdf) (as "Multi-turn jailbreak persistence")**
> The continuation and refinement of a successful jailbreak across multiple interaction turns, where the model updates its harmful response based on new contextual information.

**[SQLWOZ: A Realistic Task-Oriented Dialogue Dataset withSQL-Based Dialogue State Representation for Complex User Requirements](https://aclanthology.org/2025.emnlp-main.384.pdf) (as "Jailbreak attack resistance")**
> The model successfully resists attempts to generate harmful content through adversarial image-text pairs or typographic manipulation.

**[Igniting Creative Writing in Small Language Models:LLM-as-a-Judge versus Multi-Agent Refined Rewards](https://aclanthology.org/2025.emnlp-main.869.pdf) (as "Jailbreak resistance")**
> The model's observable ability to maintain safety constraints even when presented with adversarial prompts designed to bypass ethical guidelines.

**[The Enemy from Within: A Study of Political Delegitimization Discourse in Israeli Political Speech](https://aclanthology.org/2025.emnlp-main.842.pdf) (as "Jailbreak success")**
> The observable generation of harmful content by an LLM in response to a jailbreak prompt, indicating that the model has bypassed its safety alignment.

**[Cross-MoE: An Efficient Temporal Prediction Framework Integrating Textual Modality](https://aclanthology.org/2025.emnlp-main.1521.pdf) (as "Jailbreak detection")**
> The task of identifying whether a given input prompt is designed to bypass a model's safety filters.

## Relationships

### Jailbreaking →
- **Harmful content generation** (behaviors tasks) — *causes*
  > Cleverly crafted prompts like multi-round attacks (Wang et al., 2024c; Dong et al., 2024; Teng et al., 2024) can circumvent the safety mechanisms of LVLMs, leading them to produce harmful content.
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AdvBench** (measurements) — *measured_by*
  - [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf)
- **PAIR** (measurements) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
- **GCG attack** (measurements) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **AutoDAN** (measurements) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **In-context attack** (measurements) — *measured_by*
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Rule-based judge** (measurements) — *measured_by*
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
- **CipherChat** (measurements) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)

### → Jailbreaking
- **AutoDAN** (measurements) — *causes*
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **AdvBench** (measurements) — *measured_by*
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
- **Robustness** (constructs) — *causes*
  - [LLM-Based Explicit Models of Opponents for Multi-Agent Games](https://aclanthology.org/2025.naacl-long.42.pdf)

### Associated with
- **Alignment** (constructs)
  - [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://proceedings.neurips.cc/paper_files/paper/2024/file/70702e8cbb4890b4a467b984ae59828a-Paper-Conference.pdf)
- **PAIR** (measurements)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Safety mechanism** (constructs)
  - [DoRAGSystems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage](https://aclanthology.org/2025.naacl-long.302.pdf)

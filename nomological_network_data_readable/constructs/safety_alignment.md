# Safety alignment
**Type:** Construct  
**Referenced in:** 104 papers  
**Also known as:** Safety policy compliance, Safety compliance  

## State of the Field

Across the provided literature, Safety alignment is predominantly defined as the degree to which a model's behavior conforms to safety guidelines and human values, preventing the generation of harmful or undesirable outputs. While this behavioral focus is prevalent, some definitions extend the concept to include maintaining helpfulness to avoid over-refusal, and a few papers offer more specialized framings, such as adherence to explicit organizational policies or as an internal property reflected in stable gradient patterns. The field operationalizes this construct through a wide array of benchmarks designed to evaluate model responses to unsafe prompts, including AdvBench, SALAD-Bench, and MM-SafetyBench. Other cited measurement approaches include using classifier models like LlamaGuard 3 and analytical techniques like linear probing to assess internal safety features. Safety alignment is frequently positioned as a direct cause of a model's harmlessness and its refusal to answer unsafe queries, thereby preventing harmful content generation. It is also studied alongside helpfulness, adversarial robustness, and faithfulness, with some evidence suggesting a potential trade-off between safety and helpfulness. A recurring theme is that this alignment is not static; it can be undermined by jailbreaking attacks, adversarial prompts, and even standard fine-tuning, making its preservation a common research goal.

## Sources

**[Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf)**
> The degree to which a model's behavior conforms to safety guidelines, preventing it from generating harmful or undesirable outputs.

**[ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf) (as "Safety policy compliance")**
> The latent ability of an agent to adhere to explicit safety rules derived from regulatory or organizational policies across dynamic action sequences.

**[SafeAuto: Knowledge-Enhanced Safe Autonomous Driving with Multimodal Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cm/zhang25cm.pdf) (as "Safety compliance")**
> The latent tendency of the model to generate actions that adhere to traffic rules and safety constraints, verified through structured knowledge integration.

## Relationships

### Safety alignment →
- **AdvBench** (measurements) — *measured_by*
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks) — *causes*
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **FigStep** (measurements) — *measured_by*
  - [Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation](https://aclanthology.org/2025.naacl-long.604.pdf)
- **Harmlessness** (constructs) — *causes*
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *causes*
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **Anthropic HHH** (measurements) — *measured_by*
  - [SimPER: A Minimalist Approach to Preference  Alignment without Hyperparameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/278fb93d93a1a06927f2fdc17af2384e-Paper-Conference.pdf)
- **POSE** (measurements) — *measured_by*
  - [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf)
- **Linear probing** (measurements) — *measured_by*
  > Motivated by this observation, we adopt the widely used interpretability tool, linear probing, to analyze the changes in LLMs’ safety features in this section. (Section 3.2).
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **HEX-PHI** (measurements) — *measured_by*
  > HEX-PHI: introduced in (Qi et al., 2023), it contains 11 categories of harmfulness-inducing instructions. It is used to evaluate the safety alignment of a model (Section 4.1)
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **Anthropic HH (RLHF)** (measurements) — *measured_by*
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *causes*
  > “safety alignment” process prior to deployment, in which models are fine-tuned to better align with human preferences and societal ethical standards ... However, even with safety alignment, LLMs remain vulnerable to jailbreaking attacks, which can lead them to produce outputs that contravene established safety principles
  - [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/45673dbf3f331fbd911b0689872de396-Paper-Conference.pdf)
- **LlamaGuard 3** (measurements) — *measured_by*
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **VLGuard** (measurements) — *measured_by*
  - [Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation](https://aclanthology.org/2025.naacl-long.604.pdf)
- **SIUO** (measurements) — *measured_by*
  - [Single Ground Truth Is Not Enough: Adding Flexibility to Aspect-Based Sentiment Analysis Evaluation](https://aclanthology.org/2025.naacl-long.604.pdf)
- **SALAD-Bench** (measurements) — *measured_by*
  > We use the Antropic Hh-rlhf red-teaming prompts from Antropic (Bai et al., 2022), the Do-Not-Answer dataset (Wang et al., 2024b) and Salad Bench (Li et al., 2024b) as the benchmark. (Section 4.1)
  - [Diffusion Models Through a Global Lens: Are They Culturally Inclusive?](https://aclanthology.org/2025.acl-long.1504.pdf)
- **MM-SafetyBench** (measurements) — *measured_by*
  - [Defending LVLMs Against Vision Attacks Through Partial-Perception Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25z/zhou25z.pdf)
- **HADES** (measurements) — *measured_by*
  - [Defending LVLMs Against Vision Attacks Through Partial-Perception Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhou25z/zhou25z.pdf)
- **AIAH** (measurements) — *measured_by*
  > “AIAH (Yang et al., 2025) first conducted red teaming and benchmarking LALMs’ safety across three audio input settings”
  - [Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf)

### → Safety alignment
- **Logical reasoning** (constructs) — *causes*
  > To tackle these challenges, we propose SHIELDAGENT, the first guardrail agent designed to enforce explicit safety policy compliance for the action trajectory of other protected agents through logical reasoning. (Section 1)
  - [ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ae/chen25ae.pdf)

### Associated with
- **Harmful content generation** (behaviors tasks)
  > “each unaligned data sample maliciously combines a harmful instruction with a harmful response, thereby compromising the model’s reliability and safety.”
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **Helpfulness** (constructs)
  > “Ideally, by training on decentralized data that is aligned with human preferences and safety principles, federated instruction tuning (FedIT) can result in an LLM that could behave helpfully and safely.”
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Refusal to answer** (behaviors tasks)
  - [Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf)
- **Instruction following** (constructs)
  - [Certifying Counterfactual Bias in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c6decac1477fbcc2cbf12d314ce0133-Paper-Conference.pdf)
- **Adversarial robustness** (constructs)
  > RobustKV creates an intriguing evasiveness dilemma for adversaries, forcing them to balance between evading RobustKV and circumventing the LLM’s built-in safeguards. (Section 5.3.2)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
- **Compositional generalization** (constructs)
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **URIAL** (measurements)
  > “we followed the approach outlined in URIAL (Lin et al., 2023), which incorporates three curated stylistic examples along with a system prompt to achieve this safety alignment.”
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
- **Privacy** (constructs)
  - [Ensemble Watermarks for Large Language Models](https://aclanthology.org/2025.acl-long.146.pdf)
- **Harmful query refusal** (behaviors tasks)
  - [Towards Transferable Personality Representation Learning based on Triplet Comparisons and Its Applications](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **Safety awareness** (constructs)
  > These tasks pose significant challenges to the multimodal reasoning and safety alignment capabilities of models (Section 2.1).
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **Visual reasoning** (constructs)
  > This observation highlights a fundamental trade-off: as visual reasoning capabilities increase, safety alignment tends to degrade. (Section 1)
  - [MAKAR: a Multi-Agent framework based Knowledge-Augmented Reasoning for Grounded Multimodal Named Entity Recognition](https://aclanthology.org/2025.emnlp-main.312.pdf)

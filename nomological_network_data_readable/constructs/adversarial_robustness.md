# Adversarial robustness
**Type:** Construct  
**Referenced in:** 62 papers  
**Also known as:** Attack robustness, Security robustness, Adversarial Vulnerability, Attack resistance, Jailbreak robustness, Adversarial susceptibility, Robustness to jailbreaking, Adversarial vulnerability, Robustness to phonetic attacks, Jailbreak effectiveness, Susceptibility to jailbreaking, Jailbreaking resistance, Jailbreak vulnerability, Ethical risk, Jailbreak susceptibility  

## State of the Field

The most prevalent framing of adversarial robustness across the surveyed literature is a model's latent property to maintain its performance and make correct predictions when faced with small, intentionally crafted perturbations to its input. This general concept is applied to various contexts, including maintaining factual accuracy against misleading examples and resisting character-level typos. A substantial and frequently discussed sub-type is "jailbreak robustness," which specifically concerns a model's ability to resist prompts designed to bypass its safety mechanisms and elicit harmful content. A smaller line of work defines robustness in the specific context of watermarking, distinguishing between "attack robustness" (detectability after modification) and "security robustness" (difficulty of reverse-engineering the watermark). The field operationalizes this construct, particularly its jailbreaking dimension, by measuring model performance on benchmarks like AdvBench, Harmbench, and JailbreakBench, and by evaluating its resilience to specific attack methods such as the GCG attack and AutoDAN. General adversarial robustness is also commonly assessed by applying perturbations to standard NLP tasks and measuring performance on datasets including SST-2, GLUE, and AG News. Across the provided work, adversarial robustness is frequently studied in relation to safety alignment, as adversarial attacks are often framed as attempts to circumvent these safeguards.

## Sources

**[An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf)**
> The latent property of a model to maintain its performance and make correct predictions when faced with small, intentionally crafted perturbations to its input.

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf) (as "Attack robustness")**
> The degree to which a watermark remains detectable after semantically invariant modifications to the generated text, such as paraphrasing or synonym substitution.

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf) (as "Security robustness")**
> The difficulty of inferring the watermarking rules from watermarked text, such that adversaries cannot easily reverse-engineer and remove the watermark.

**[Achieving Domain-Independent Certified Robustness via Knowledge Continuity](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cc11cda2a2679e8af5c6317aed0af8-Paper-Conference.pdf) (as "Adversarial Vulnerability")**
> The latent susceptibility of a model to adversarial perturbations, inferred from attack success rates.

**[RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf) (as "Jailbreak robustness")**
> The model's latent ability to resist attacks that use specially crafted prompts to circumvent its safety mechanisms and elicit harmful responses.

**[Scaling Laws for Adversarial Attacks on Language Model Activations and Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434a6b40f8f65488e722bc33d796c8b-Paper-Conference.pdf) (as "Adversarial susceptibility")**
> The degree to which a model's outputs can be manipulated by small, targeted perturbations to its inputs or internal states.

**[Scaling Laws for Adversarial Attacks on Language Model Activations and Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434a6b40f8f65488e722bc33d796c8b-Paper-Conference.pdf) (as "Attack resistance")**
> A model property representing the number of bits the attacker must control on the input to exert a single bit of control on the output.

**[Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb7baa005c239c1c7c4098c2a9e00450-Paper-Conference.pdf) (as "Robustness to jailbreaking")**
> The model's ability to resist attempts to bypass its safety mechanisms and refuse to generate harmful content, even when subjected to adversarial attacks.

**[X-Transfer Attacks: Towards Super Transferable Adversarial Attacks on CLIP](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25h/huang25h.pdf) (as "Adversarial vulnerability")**
> The degree to which a model's performance degrades or its outputs can be manipulated by small, maliciously crafted input perturbations.

**[MiLQ: BenchmarkingIRModels for Bilingual Web Search with Mixed Language Queries](https://aclanthology.org/2025.emnlp-main.1154.pdf) (as "Robustness to phonetic attacks")**
> The model's ability to maintain performance in detecting offensive language when faced with inputs that have been intentionally altered with homophonic substitutions to evade detection.

**[A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Jailbreak effectiveness")**
> The degree to which a jailbreak elicits useful harmful information from a victim model rather than merely a non-refusal or irrelevant response.

**[Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://proceedings.neurips.cc/paper_files/paper/2024/file/70702e8cbb4890b4a467b984ae59828a-Paper-Conference.pdf) (as "Susceptibility to jailbreaking")**
> The model's vulnerability to adversarial prompts designed to bypass its safety mechanisms and elicit prohibited information.

**[CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Jailbreaking resistance")**
> The model's ability to adhere to its intended functions and restrictions when prompted with inputs designed to manipulate or exploit it.

**[Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF](https://proceedings.iclr.cc/paper_files/paper/2024/file/7423902b5534e2b267438c85444a54b1-Paper-Conference.pdf) (as "Jailbreak vulnerability")**
> The susceptibility of an LLM to adversarial inputs that bypass its safety mechanisms and elicit harmful content generation, particularly when non-English or multilingual prompts are used.

**[Automating Steering for Safe Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.42.pdf) (as "Ethical risk")**
> The latent tendency of a model to produce harmful content when exposed to manipulative or adversarial role prompts, reflecting vulnerability in safety alignment.

**[Direct Value Optimization: Improving Chain-of-Thought Reasoning inLLMs with Refined Values](https://aclanthology.org/2025.emnlp-main.669.pdf) (as "Jailbreak susceptibility")**
> The latent tendency of a model to bypass its safety guardrails when exposed to specific fine-tuning or inference-time triggers, reflecting an acquired vulnerability to compliance with harmful requests.

## Relationships

### Adversarial robustness →
- **AdvBench** (measurements) — *measured_by*
  > For robustness evaluations, we take harmful requests from two harmful instruction datasets: HarmBench (Mazeika et al., 2024) and AdvBench (Zou et al., 2023b). (Section 5)
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **GCG attack** (measurements) — *measured_by*
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Harmbench** (measurements) — *measured_by*
  > For robustness evaluations, we take harmful requests from two harmful instruction datasets: HarmBench (Mazeika et al., 2024) and AdvBench (Zou et al., 2023b). (Section 5)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **JailbreakBench** (measurements) — *measured_by*
  > “We additionally evaluate on Adaptive Attack (Andriushchenko et al., 2024), a state-of-the-art adversarial attack method, on JailBreakBench (Chao et al., 2024).”
  - [Robust Prompt Optimization for Defending Language Models Against Jailbreaking Attacks](https://proceedings.neurips.cc/paper_files/paper/2024/file/46ed503889ab232c21c1162340ee17b2-Paper-Conference.pdf)
- **SST-2** (measurements) — *measured_by*
  > To evaluate whether Evoke can improve LLMs’ robustness, we add typos to the datasets. Specifically, we perform character-level adversarial attacks for each sample. (Section 4.2)
  - [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf)
- **AutoDAN** (measurements) — *measured_by*
  > Table 1: General model capability metrics and adversarial robustness (measured as ASR) of three LLMs trained using various safety fine-tuning methods. ... GCG ... PAIR ... AutoDAN ... HumanJailbreaks
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *causes*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **GLUE** (measurements) — *measured_by*
  > “Existing research evaluates adversarial robustness of LLMs on the GLUE dataset (Wang et al., 2018)”
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **DIPPER** (measurements) — *measured_by*
  > “In Table 1, we list the detection accuracy of our watermark algorithm and various baseline algorithms under the no-attack setting and when texts are rewritten using GPT3.5, two different DIPPER settings (Krishna et al., 2023)”
  - [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **Copy-paste attack** (measurements) — *measured_by*
  > In Table 1, we list the detection accuracy of our watermark algorithm and various baseline algorithms under the no-attack setting and when texts are rewritten using GPT3.5, two different DIPPER settings (Krishna et al., 2023) and the copy-paste attack Kirchenbauer et al. (2023b). (Section 6.2)
  - [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **QQP** (measurements) — *measured_by*
  > "Datasets. We adopt two datasets: SST-2 (Socher et al., 2013) is a sentiment classification task ... and QQP (Wang et al., 2019) is a task where we need to determine whether two sentences are paraphrases of each other."
  - [Evoke: Evoking Critical Thinking Abilities in LLMs via Reviewer-Author Prompt Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/1eaa5146756be028ad6fff1efcc8e6bd-Paper-Conference.pdf)
- **FM2** (measurements) — *measured_by*
  - [Towards Understanding Factual Knowledge of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AgentDojo** (measurements) — *measured_by*
  - [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf)
- **StrongReject** (measurements) — *measured_by*
  - [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf)
- **MM-SafetyBench** (measurements) — *measured_by*
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **AG News** (measurements) — *measured_by*
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **MixEval** (measurements) — *measured_by*
  > We also evaluate on the MixEval (Ni et al., 2024) benchmark, which contains downstream tasks, and assess jailbreak robustness; additional details are provided in Appendices F and G.
  - [Learn Your Reference Model for Real Good Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/94d13c2401fe119e57ba325b6fe526e0-Paper-Conference.pdf)
- **FigStep** (measurements) — *measured_by*
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)
- **JailbreakV** (measurements) — *measured_by*
  - [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.261.pdf)

### Associated with
- **Safety alignment** (constructs)
  > RobustKV creates an intriguing evasiveness dilemma for adversaries, forcing them to balance between evading RobustKV and circumventing the LLM’s built-in safeguards. (Section 5.3.2)
  - [RobustKV: Defending Large Language Models against Jailbreak Attacks via KV Eviction](https://proceedings.iclr.cc/paper_files/paper/2025/file/38bbae17d60940f3ee14dfd1035d7542-Paper-Conference.pdf)
- **Reliability** (constructs)
  - [An LLM can Fool Itself: A Prompt-Based Adversarial Attack](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c72285e193ec90dca93258128698cfb-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Machine unlearning** (constructs)
  - [Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1348.pdf)

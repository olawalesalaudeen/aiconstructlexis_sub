# Harmbench
**Type:** Measurement  
**Referenced in:** 71 papers  
**Also known as:** HarmBench, Harmbench-adv, HarmBench-Llama2-13B-Chat, HARMBENCH  

## State of the Field

Across the surveyed literature, Harmbench is predominantly described as a benchmark of harmful instructions or behaviors used to evaluate the safety and robustness of large language models, particularly under adversarial or jailbreak attacks. Papers frequently use Harmbench to measure behaviors such as `Jailbreaking`, `Harmlessness`, `Safety`, and `Adversarial robustness`. It is also employed to assess `Harmful request refusal`, `Harmful content generation`, and the `Generalization` of attack methods. The benchmark is operationalized as a dataset of harmful prompts, with papers citing various sizes from 80 to 400 items; one source specifies a set of "200 standardized harmful behaviors" covering topics like cybercrime and misinformation. Evaluation of model responses is often performed using an associated classifier, with one paper identifying "HarmBench-Llama2-13B-Chat" for this role, while another notes the use of GPT-3.5-turbo to assess jailbreak success. While some definitions focus on specific attack types like "embedding-level SCAV attacks," a smaller line of work frames it as an "'out-of-distribution' test set" to evaluate attack generalization from other datasets. A variant named "Harmbench-adv" is also mentioned as an adversarial set for testing prompt and response classification.

## Sources

**[Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf)**
> A benchmark used to evaluate embedding-level SCAV attacks on harmful instructions.

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf) (as "HarmBench")**
> A benchmark of harmful instructions used to evaluate jailbreak success and safety behavior under adversarial attacks.

**[On Calibration of LLM-based Guard Models for Reliable Content Moderation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a99f732df9b668284b449da0214a3286-Paper-Conference.pdf) (as "Harmbench-adv")**
> An adversarial evaluation set used to test prompt and response classification under jailbreak attacks.

**[Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf) (as "HarmBench-Llama2-13B-Chat")**
> A classifier used to judge whether generated responses are harmless or contain harmful content.

**[DoRAGSystems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage](https://aclanthology.org/2025.naacl-long.302.pdf) (as "HARMBENCH")**
> An 'out-of-distribution' test set consisting of 200 harmful behaviors distinct from ADVBENCH, used to evaluate the generalization of jailbreak attacks.

## Relationships

### → Harmbench
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [Improving Alignment and Robustness with Circuit Breakers](https://proceedings.neurips.cc/paper_files/paper/2024/file/97ca7168c2c333df5ea61ece3b3276e1-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Multilingual Machine Translation with Open Large Language Models at Practical Scale: An Empirical Study](https://aclanthology.org/2025.naacl-long.281.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > For robustness evaluations, we take harmful requests from two harmful instruction datasets: HarmBench (Mazeika et al., 2024) and AdvBench (Zou et al., 2023b). (Section 5)
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmful request refusal** (behaviors tasks) — *measured_by*
  - [Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  - [HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ac2d4db1615bf3736f44a1b4889e666b-Paper-Conference.pdf)
- **Knowledge transfer** (constructs) — *measured_by*
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **Privacy** (constructs) — *measured_by*
  - [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf)

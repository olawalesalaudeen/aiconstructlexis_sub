# Catastrophic forgetting
**Type:** Behavior  
**Referenced in:** 30 papers  
**Also known as:** Knowledge forgetting, Pretraining data injection  

## State of the Field

Across the surveyed literature, Catastrophic forgetting is most commonly defined as the observable phenomenon where a model's performance on previously learned tasks significantly deteriorates after it is trained on new data. This behavior is a frequently discussed challenge within the context of `Continual learning`, but is also studied in relation to `Machine unlearning` and sequential model editing, where it is sometimes referred to as "Knowledge forgetting." To operationalize and measure this phenomenon, researchers evaluate models for performance degradation on general capability benchmarks, with `MMLU`, `GSM8k`, `PIQA`, `BIG-Bench Hard`, and `MMLU-Pro` being explicitly named for this purpose. The most widely reported consequence of this behavior is a degradation of the model's `Generalization` capabilities. Some work also suggests a relationship with `Overfitting`, noting that injecting pretraining data can serve as a regularizer to reduce both. As one study notes, "injecting as little as 1% of pretraining data in the training mix is enough to mitigate forgetting significantly" ("Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection"). A less frequent connection is also drawn to `Hallucination`.

## Sources

**[Learn more, but bother less: parameter efficient continual learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0bc711f48724237b38823c4d9cee10b-Paper-Conference.pdf)**
> The observable phenomenon where a model's performance on previously learned tasks significantly deteriorates after it is trained on new data.

**[CollabEdit: Towards Non-destructive Collaborative Knowledge Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/47eb71e8e778dc9def7780baa7b35687-Paper-Conference.pdf) (as "Knowledge forgetting")**
> Previously edited facts become less accurately retained after many subsequent editing rounds.

**[Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf) (as "Pretraining data injection")**
> The observable behavior of mixing pretraining data into the finetuning data stream according to a specified proportion, used to regularize finetuning and reduce forgetting.

## Relationships

### Catastrophic forgetting →
- **Generalization** (constructs) — *causes*
  > catastrophic forgetting (CF) is still an unavoidable problem during CIT, which refers to the forgetting of previously learned tasks and the deterioration of original generalization ability (Section 1).
  - [Beyond Text Compression: Evaluating Tokenizers Across Scales](https://aclanthology.org/2025.acl-long.1547.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1df1df43b58845650b8dada00fca9772-Paper-Datasets_and_Benchmarks_Track.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  > The fine-tuned models under MDS are evaluated on the general tasks including MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and PIQA (Bisk et al., 2020) to measure the catastrophic forgetting of the PEFT approaches. (Section 4.1)
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf)
- **BIG-Bench Hard** (measurements) — *measured_by*
  > For out-domain evaluations, BIG-Bench-Hard (Suzgun et al., 2022) and MMLU-Pro (Wang et al., 2024b) are used. These benchmarks encompass challenging subsets of tasks across a wide range of domains and are widely employed for evaluating the capabilities of LLMs. Additionally, they include samples that are more complex than those in our training data, ensuring minimal overlap. We use lm-eval (Gao et al., 2024), available with MIT License, for reporting out-domain evaluation. (Section 5.1.1)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.940.pdf)
- **MMLU** (measurements) — *measured_by*
  > The fine-tuned models under MDS are evaluated on the general tasks including MMLU (Hendrycks et al., 2021), GSM8K (Cobbe et al., 2021), and PIQA (Bisk et al., 2020) to measure the catastrophic forgetting of the PEFT approaches. (Section 4.1)
  - [Learning to Solve Domain-Specific Calculation Problems with Knowledge-Intensive Programs Generator](https://aclanthology.org/2025.naacl-long.246.pdf)
- **POPE** (measurements) — *measured_by*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **LLaVA-Bench-in-the-Wild** (measurements) — *measured_by*
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [CultureLLM: Incorporating Cultural Differences into Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a16935bf54c4af233e25d998b7f4a2c-Paper-Conference.pdf)
- **MMLU-Pro** (measurements) — *measured_by*
  > On the knowledge-intensive benchmarks (i.e., WikiBench, MMLU, and MMLU-Pro), Genius can maintain the performances of the base LLMs, avoiding catastrophic forgetting after post-training (Section 3.2).
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.940.pdf)
- **Knowledge forgetting** (constructs) — *causes*
  - [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf)
- **Overfitting** (constructs) — *causes*
  > Injecting pretraining data has a regularizing effect that reduces overfitting and forgetting. (Figure 1 caption)
  - [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bethune25a/bethune25a.pdf)

### → Catastrophic forgetting
- **Instruction fine-tuning** (behaviors tasks) — *causes*
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)
- **Reward hacking** (behaviors tasks) — *causes*
  - [NovelHopQA: Diagnosing Multi-Hop Reasoning Failures in Long Narrative Contexts](https://aclanthology.org/2025.emnlp-main.1329.pdf)

### Associated with
- **Continual learning** (constructs)
  > “Continual Fine-Tuning (Madotto et al., 2021; Wu et al., 2024), which incrementally incorporates new knowledge while mitigating catastrophic forgetting.”
  - [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf)
- **Knowledge retention** (constructs)
  - [Scalable Language Model with Generalized Continual Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fe2c290c0566f88617e9c5bd593441-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Adaptability** (constructs)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.932.pdf)
- **Personalization** (constructs)
  - [Yo'LLaVA: Your Personalized Language and Vision Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/48088756ec0ce6ba362bddc7ebeb3915-Paper-Conference.pdf)
- **Generalization** (constructs)
  > The first limitation is that TPO may introduce a stronger form of “catastrophic forgetting”. The results in Sec. 4.2 indicate that while TPO exhibits excellent performance on in-distribution datasets, it may suffer from performance degradation on out-of-distribution datasets.
  - [Agent Skill Acquisition for Large Language Models via CycleQD](https://proceedings.iclr.cc/paper_files/paper/2025/file/755acd0c7c07180d78959b6d89768207-Paper-Conference.pdf)
- **Language model pre-training** (behaviors tasks)
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **In-context learning** (constructs)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs)
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Task interference** (constructs)
  - [LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks)
  - [ChainEdit: Propagating Ripple Effects inLLMKnowledge Editing through Logical Rule-Guided Chains](https://aclanthology.org/2025.acl-long.666.pdf)
- **Unlearning** (constructs)
  - [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.444.pdf)
- **Multilingual ability** (constructs)
  - [Neutral residues: revisiting adapters for model extension](https://raw.githubusercontent.com/mlresearch/v267/main/assets/talla25a/talla25a.pdf)
- **General capabilities** (constructs)
  > Validated across multiple datasets and models, this method significantly alleviates forgetting in both general and in-context learning abilities, confirming the correlation between FV dynamics and forgetting. (Section 1)
  - [Multilingual Arbitration: Optimizing Data Pools to Accelerate Multilingual Progress](https://aclanthology.org/2025.acl-long.940.pdf)
- **Hallucination** (behaviors tasks)
  > (Zhai et al., 2023) deem that the hallucination in large models is related to the catastrophic forgetting in continual tuning. (Section 5.4. Analysis of Examples)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Generality** (constructs)
  - [Dynamic Model-Bank Test-Time Adaptation for Automatic Speech Recognition](https://aclanthology.org/2025.emnlp-main.1108.pdf)

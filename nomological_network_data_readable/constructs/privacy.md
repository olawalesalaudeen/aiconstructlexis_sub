# Privacy
**Type:** Construct  
**Referenced in:** 54 papers  
**Also known as:** Secrecy maintenance, Low-Test-Error Preference, Dataset membership inference, Information leakage, Dataset membership, Vulnerability, Safety vulnerability, Adversarial vulnerability, Prompt leakage vulnerability, Privacy leakage, Data leakage risk, Privacy risk, Impermissible information leakage, Data leakage vulnerability  

## State of the Field

The most prevalent view of privacy in the provided literature concerns a model's ability to prevent the leakage of sensitive information, whether from its training data, user inputs, or private datastores. This is frequently framed as a vulnerability or risk, with terms like "privacy leakage," "data leakage risk," and "privacy vulnerability" appearing across multiple papers. The core concern is the model revealing personally identifiable, proprietary, or otherwise sensitive information in its outputs. Operationalization of this construct varies, with one common approach being to assess a model's refusal to answer questions containing personal data, as one paper notes, to evaluate its "privacy awareness" ("Benchmarking Large Language Models Under Data Contamination..."). Another prevalent line of work operationalizes privacy by investigating training data exposure through "membership inference attacks," which aim to "determine if a particular record was part of the model’s training data" ("DocMIA: Document-Level Membership Inference Attacks against DocVQA Models"), a task for which the Paired t-test is cited as a measurement method. A more formal definition, present in several papers, characterizes privacy through "differential privacy guarantees," where a model should produce similar outputs even when input exemplars change. A smaller set of studies presents alternative framings, such as "secrecy maintenance" in social interactions or, in one distinct case, a "Low-Test-Error Preference" where in-context learning favors pretraining functions over task adaptation. Across the surveyed work, privacy is studied alongside concepts like faithfulness, memorization, and safety alignment, and is sometimes broken down into components like "privacy awareness" and "privacy leakage" for evaluation.

## Sources

**[Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)**
> The degree to which a model's outputs do not reveal sensitive information from its input exemplars, formalized through differential privacy guarantees.

**[SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3075b88e583a0e98d8b24338a613060-Paper-Conference.pdf) (as "Secrecy maintenance")**
> The ability to protect private information or intentions from being revealed during social interaction, especially when disclosure would reduce strategic advantage.

**[Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf) (as "Low-Test-Error Preference")**
> A disposition where ICL tends to select the pretraining function that minimizes test error rather than adapting to entirely new tasks.

**[JAWAHER: A Multidialectal Dataset ofArabic Proverbs forLLMBenchmarking](https://aclanthology.org/2025.naacl-long.614.pdf) (as "Privacy preservation")**
> The ability of a system to fulfill user requests without revealing personally identifiable information to untrusted components, such as remote API-based models.

**[Exploiting Presentative Feature Distributions for Parameter-Efficient Continual Learning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25j/cheng25j.pdf) (as "Information leakage")**
> The unintended access or reuse of task-specific information (e.g., training data, task identifiers) from previously learned tasks during continual learning, posing privacy risks and enabling unfair performance advantages.

**[STAMP Your Content: Proving Dataset Membership via Watermarked Rephrasings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rastogi25a/rastogi25a.pdf) (as "Dataset membership")**
> The latent property of a language model having been trained on a specific dataset, inferred from systematic differences in likelihood between semantically equivalent but differently watermarked versions of the data.

**[Unlocking Post-hoc Dataset Inference with Synthetic Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25q/zhao25q.pdf) (as "Dataset membership inference")**
> The latent ability of a model or method to determine whether a suspect dataset was used in the training of a target LLM, based on statistical signals extracted from model behavior.

**[VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](https://aclanthology.org/2025.emnlp-main.138.pdf) (as "Vulnerability")**
> The susceptibility of LLM judges to adversarial manipulations such as prompt injection or adversarial phrases that distort judgment outcomes.

**[Generative or Discriminative? Revisiting Text Classification in the Era of Transformers](https://aclanthology.org/2025.emnlp-main.487.pdf) (as "Safety vulnerability")**
> A latent weakness in a model's architecture or alignment that can be exploited to bypass its safety mechanisms.

**[Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.940.pdf) (as "Backdoor vulnerability")**
> The latent susceptibility of a model to hidden malicious behavior that activates upon exposure to a specific trigger, while maintaining normal performance on clean inputs.

**[2025.emnlp-main.1196.checklist](https://aclanthology.org/attachments/2025.emnlp-main.1196.checklist.pdf) (as "Adversarial vulnerability")**
> The degree to which a model's performance can be degraded or its safety mechanisms bypassed by malicious actors using manipulation strategies not covered in its training or benchmark data.

**[EnAnchored-X2X:English-Anchored Optimization for Many-to-Many Translation](https://aclanthology.org/2025.emnlp-main.1082.pdf) (as "Prompt leakage vulnerability")**
> The susceptibility of a large language model to being manipulated by adversarial queries into revealing its confidential system prompt.

**[MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Privacy leakage")**
> The tendency to reveal personal or sensitive information when prompted directly or indirectly.

**[DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf) (as "Privacy vulnerability")**
> The susceptibility of a model to attacks that can reveal sensitive information about its training data.

**[Uncovering Latent Memories in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/442443dbe8c4c7e1df7eda140921de36-Paper-Conference.pdf) (as "Data leakage risk")**
> The tendency for a model to reveal sensitive or proprietary training information in its outputs, creating privacy and misuse concerns.

**[TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf) (as "Privacy risk")**
> The potential for a model to reveal sensitive information about its training data, which can be assessed through training data detection.

**[Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf) (as "Data leakage vulnerability")**
> The tendency of a RAG system to expose private datastore content through model outputs.

**[Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf) (as "Impermissible information leakage")**
> The extent to which a model's outputs, even if individually permissible, reveal dangerous or undesirable knowledge that an adversary can infer.

## Relationships

### Privacy →
- **Harmbench** (measurements) — *measured_by*
  - [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf)
- **Paired t-test** (measurements) — *measured_by*
  > “Using these perplexity scores, we perform a paired t-test to detect membership.”
  - [STAMP Your Content: Proving Dataset Membership via Watermarked Rephrasings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rastogi25a/rastogi25a.pdf)

### → Privacy
- **Safety** (constructs) — *measured_by*
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *causes*
  - [Endless Jailbreaks with Bijection Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b05c1fb3345743dea59f500ec5a0bba0-Paper-Conference.pdf)
- **Knowledge forgetting** (constructs) — *causes*
  - [Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf)

### Associated with
- **Trustworthiness** (constructs)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **In-context learning** (constructs)
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Privacy awareness** (constructs)
  > From the perspectives of consciousness and behaviors [132], we evaluate privacy in terms of awareness and leakage. (Sec. 2.2.5)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Privacy leakage** (behaviors tasks)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Model selection** (constructs)
  > “we theoretically reveal the algorithm-selection mechanism for ICL. We find there simultaneously exist two parallel mechanisms: the Low-test-error preference and the Similar-input-distribution preference.”
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Pre-training data detection** (behaviors tasks)
  - [TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf)
- **Memorization** (constructs)
  - [Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf)
- **Safety alignment** (constructs)
  - [Ensemble Watermarks for Large Language Models](https://aclanthology.org/2025.acl-long.146.pdf)
- **Faithfulness** (constructs)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)

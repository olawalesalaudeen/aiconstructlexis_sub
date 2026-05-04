# Privacy leakage
**Type:** Behavior  
**Referenced in:** 21 papers  
**Also known as:** Private attribute inference, Membership inference, Sensitive information exposure, System prompt extraction, Fragment inference, Data stealing, Sensitive information leakage, Image-text pair leakage, Good faith disclosure, PII leakage, Information leakage  

## State of the Field

Across the surveyed literature, "Privacy leakage" is a broad behavioral category encompassing various forms of unintended or malicious information disclosure by models. The most prevalent framings define this behavior as either the direct reproduction of sensitive or personally identifiable information (PII) from training data in model outputs, or as the ability to infer whether a specific data instance was part of the training set, a task known as "Membership inference." A smaller set of studies focuses on more targeted attack scenarios, such as "Data stealing" (exfiltrating emails or payment methods), "System prompt extraction" (revealing system instructions), and "Fragment inference," where known text fragments are used to uncover unknown ones from the same training sample. Some definitions also consider the context of the disclosure, such as violating a user-defined security policy or naively complying with a request under a "Good faith" assumption. To operationalize and measure this behavior, researchers frequently employ `Membership inference attacks` (MIAs), using specific methods like `LOSS`, `Zlib Entropy`, and `Min-k% Prob` to quantify the risk. Other evaluation instruments mentioned for assessing privacy leakage include the `DecodingTrust` and `MUSE` benchmarks, as well as `InjecAgent`, which is explicitly used to test for data stealing. Several papers report a causal link, arguing that `Memorization` of training data leads to this behavior, with one source stating that "privacy leakage stems from memorized content."

## Sources

**[Private Attribute Inference from Images with Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bb97e9a7c811904c9b01f51fde66edcf-Paper-Conference.pdf) (as "Private attribute inference")**
> The observable task of a model predicting a user's personal information (e.g., location, age, sex, income) based on a provided image, especially one that does not directly depict the person.

**[Data Mixture Inference Attack: BPE Tokenizers Reveal Training Data Compositions](https://proceedings.neurips.cc/paper_files/paper/2024/file/10e6dfea9a673bef4a7b1cb9234891bc-Paper-Conference.pdf) (as "Membership inference")**
> The task of determining whether a specific data instance was included in a model's training set.

**[Fragments to Facts: Partial-Information Fragment Inference from LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rosenblatt25a/rosenblatt25a.pdf) (as "Fragment inference")**
> The observable act of using a small set of known text fragments from a training sample to infer additional, unknown fragments from the same sample by querying a model.

**[The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (and How to Fix Them)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ap/wang25ap.pdf) (as "System prompt extraction")**
> An observable attack behavior where the model is manipulated into revealing its confidential system instructions or prompts.

**[AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25m/xu25m.pdf) (as "Sensitive information exposure")**
> Revealing sensitive information as a result of malicious prompt injection or adversarial manipulation.

**[UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf) (as "Data stealing")**
> The malicious act of accessing and exfiltrating sensitive or private information, such as emails or payment methods.

**[In-Context Learning Boosts Speech Recognition via Human-like Adaptation to Speakers and Language Varieties](https://aclanthology.org/2025.emnlp-main.220.pdf) (as "Sensitive information leakage")**
> The unintended disclosure of hazardous or private knowledge in either final answers or reasoning traces, despite unlearning attempts.

**[ActionStudio: A Lightweight Framework for Data and Training of Large Action Models](https://aclanthology.org/2025.emnlp-main.1091.pdf)**
> The observable reproduction of sensitive or personally identifiable information from training data in model outputs.

**[Improving Zero-shot Sentence Decontextualisation with Content Selection and Planning](https://aclanthology.org/2025.emnlp-main.1259.pdf) (as "Image-text pair leakage")**
> The simultaneous exposure of both a private image and its associated text (e.g., a medical image with its diagnostic caption) from a database.

**[UICOMPASS:UIMap Guided Mobile Task Automation via Adaptive Action Generation](https://aclanthology.org/2025.emnlp-main.1347.pdf) (as "Good faith disclosure")**
> An observable behavior where a model discloses private information under the naive assumption that any request for data is trustworthy and made in good faith.

**[FinetuningLLMs for Human Behavior Prediction in Social Science Experiments](https://aclanthology.org/2025.emnlp-main.1531.pdf) (as "PII leakage")**
> The observable phenomenon where a model includes personally identifiable information from the source document—such as names, ages, locations, or gender—in its generated summary.

**[ViLBench: A Suite for Vision-Language Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.345.pdf) (as "Information leakage")**
> The observable output behavior in which an LLM discloses confidential information that is explicitly prohibited by a user-defined security policy in the context.

## Relationships

### Privacy leakage →
- **Membership inference attack** (behaviors tasks) — *measured_by*
  > “we consider three popular MIA methods: LOSS ... Zlib Entropy ... and Min-k% Prob”
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **DecodingTrust** (measurements) — *measured_by*
  - [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf)
- **MUSE** (measurements) — *measured_by*
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Min-K% Prob** (measurements) — *measured_by*
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Min-K%** (measurements) — *measured_by*
  - [Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf)
- **InjecAgent** (measurements) — *measured_by*
  > “InjecAgent ... tests two types of attacks: direct harm attacks ... and data stealing attacks”
  - [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf)

### → Privacy leakage
- **Memorization** (constructs) — *causes*
  > Based on prior research on LLMs’ ability to memorize training data (Carlini et al., 2021; Nasr et al., 2023; Kassem et al., 2024), we examine how PII embedded in training data from other aligned mergers can be extracted in model merging scenarios. (Section 1)
  - [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf)

### Associated with
- **Privacy** (constructs)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Output diversity** (constructs)
  - [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b69bc53449ba46bb981951078929a5e-Paper-Conference.pdf)

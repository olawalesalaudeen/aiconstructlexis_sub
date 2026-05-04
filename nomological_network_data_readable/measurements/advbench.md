# AdvBench
**Type:** Measurement  
**Referenced in:** 120 papers  
**Also known as:** Advbench, ADVBENCH  

## State of the Field

Across the provided literature, AdvBench is consistently described as a benchmark dataset used to evaluate the safety, alignment, and robustness of language models. Its primary application is to measure model vulnerabilities by presenting them with what are variously termed "harmful behaviors," "malicious prompts," or "harmful instructions" designed to elicit undesirable responses. While its core purpose is stable, the reported size of the dataset varies, with papers citing 50, 500, 520, or 521 items. Researchers use AdvBench to operationalize and measure a suite of related constructs, most commonly `Jailbreaking`, `Safety`, `Safety alignment`, and `Adversarial robustness`. It is also employed to assess `Harmlessness`, `Harmful content generation`, and `Harmfulness detection`. The benchmark serves both to evaluate the effectiveness of adversarial attacks and to test defensive strategies. Though predominantly a text-based instrument, it is also applied as a "text attack benchmark" in multimodal contexts and as an "out-of-domain test set" for safety.

## Sources

**[Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf)**
> A benchmark dataset comprising 500 instances of harmful behaviors expressed as specific instructions, used to evaluate model jailbreak vulnerabilities.

**[Adversarial Representation Engineering: A General Model Editing Framework for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4630f7c0660d944c132455c124e7d90-Paper-Conference.pdf) (as "Advbench")**
> A dataset containing malicious prompts designed to test the alignment and safety of LLMs by attempting to induce harmful responses.

**[DoRAGSystems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage](https://aclanthology.org/2025.naacl-long.302.pdf) (as "ADVBENCH")**
> A benchmark dataset containing 50 harmful behaviors used to evaluate the effectiveness of jailbreak attacks on LLMs.

## Relationships

### AdvBench →
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)

### → AdvBench
- **Safety alignment** (constructs) — *measured_by*
  - [Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Jailbreaking** (behaviors tasks) — *measured_by*
  - [Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/58cbe393b4254da8966780a40d023c0b-Paper-Conference.pdf)
- **Harmlessness** (constructs) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  - [Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d56bc83ae9a4fafdce050bb36f04174-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > For robustness evaluations, we take harmful requests from two harmful instruction datasets: HarmBench (Mazeika et al., 2024) and AdvBench (Zou et al., 2023b). (Section 5)
  - [Fight Back Against Jailbreaking via Prompt Adversarial Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/759ca99a82e2a9137c6bef4811c8d378-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Jailbreak resistance** (behaviors tasks) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Harmfulness detection** (behaviors tasks) — *measured_by*
  > “Dunsafe dataset comprises harmful instructions derived from established benchmarks, including ADVBENCH”
  - [PakBBQ: A Culturally Adapted Bias Benchmark forQA](https://aclanthology.org/2025.emnlp-main.819.pdf)
- **Alignment** (constructs) — *measured_by*
  > "and (3) AdvBench ... a widely used benchmark for safety against adversarial attacks"
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)

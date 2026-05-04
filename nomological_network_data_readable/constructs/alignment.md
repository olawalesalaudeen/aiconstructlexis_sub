# Alignment
**Type:** Construct  
**Referenced in:** 93 papers  
**Also known as:** Model alignment, Self-alignment, Alignment Performance, Alignment performance, Aligning  

## State of the Field

Across the provided literature, Alignment is most commonly characterized as the degree to which a large language model's behavior conforms to human intentions, values, and preferences. This is frequently described in terms of producing outputs that are helpful, harmless, accurate, and truthful, while also adhering to explicit instructions and ethical constraints. For instance, one paper notes the goal is to make generated content "accurate, coherent, and harmless" ("Peering Through Preferences..."), while another specifies adherence to "specific output formats, citing sources, avoiding harmful language, and refusing inappropriate questions" ("DeCAP..."). The field operationalizes and measures this construct using several benchmarks; among the provided sources, the most frequently cited instruments for evaluating alignment are Arena-Hard, MixEval, and AdvBench. While the human-centric definition is prevalent, a distinct line of work defines 'model alignment' as the correspondence between the output distributions of two different models, such as for speculative decoding ("DistillSpec...") or to retain knowledge from a pre-trained model ("PACE..."). Other, less common definitions treat alignment as the downstream performance of a reward model, the internal consistency of an evaluator model, or a model's specific ability to maintain semantic integrity under length constraints. Alignment is studied alongside Safety and is reported in one paper to be influenced by Knowledge transferability.

## Sources

**[#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf)**
> The degree to which a model's behavior adheres to intended rules, instructions, and ethical constraints, including faithfulness to internal states and avoidance of harmful or inconsistent actions.

**[DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf) (as "Model alignment")**
> The degree to which the token-level output distributions of a smaller draft model and a larger target model correspond, which is a critical factor for the efficiency of speculative decoding.

**[DreamBench++: A Human-Aligned Benchmark for Personalized Image Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/71ad539a57b1fd49b19e5c80070cb8b9-Paper-Conference.pdf) (as "Self-alignment")**
> The extent to which the evaluator's internal reasoning and scoring are consistent with its own task understanding and instructions.

**[RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf) (as "Alignment Performance")**
> The downstream effectiveness of a reward model in guiding language model optimization toward human preferences.

**[Learning Dynamics of LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/afe1aa79e5eea7955f553c61a307273e-Paper-Conference.pdf) (as "Alignment performance")**
> The overall quality of an LLM's outputs with respect to human-preferred behavior after finetuning.

**[Can You Really Trust Code Copilot? Evaluating Large Language Models from a Code Security Perspective](https://aclanthology.org/2025.acl-long.850.pdf) (as "Aligning")**
> The latent ability to maintain semantic integrity while dynamically adjusting generation to meet length constraints, avoiding premature termination or content distortion.

## Relationships

### Alignment →
- **Arena-Hard** (measurements) — *measured_by*
  > We evaluate alignment effectiveness using three benchmarks: ... (2) Arena-Hard
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **MT-Bench** (measurements) — *measured_by*
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **AlpacaEval 2.0** (measurements) — *measured_by*
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **Anthropic HHH** (measurements) — *measured_by*
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  - [TaskBench: Benchmarking Large Language Models for Task Automation](https://proceedings.neurips.cc/paper_files/paper/2024/file/085185ea97db31ae6dcac7497616fd3e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Reddit TL;DR dataset** (measurements) — *measured_by*
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
- **Safety** (constructs) — *causes*
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **Trustworthiness** (constructs) — *causes*
  - [Conformal Alignment: Knowing When to Trust Foundation Models with Guarantees](https://proceedings.neurips.cc/paper_files/paper/2024/file/870ccde24673d3970a680bb48496ed63-Paper-Conference.pdf)
- **AlpacaEval 2** (measurements) — *measured_by*
  - [DeCAP: Context-Adaptive Prompt Generation for Debiasing Zero-shot Question Answering in Large Language Models](https://aclanthology.org/2025.naacl-long.625.pdf)
- **TL;DR** (measurements) — *measured_by*
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
- **Instruction following** (constructs) — *causes*
  - [Self-Alignment with Instruction Backtranslation](https://proceedings.iclr.cc/paper_files/paper/2024/file/0f8e3534eb8dee7478d4dc0e9d9a0b1a-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [Toward Automatic Discovery of a Canine Phonetic Alphabet](https://aclanthology.org/2025.acl-long.452.pdf)
- **Harmlessness** (constructs) — *causes*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *causes*
  - [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf)
- **Truthfulness** (constructs) — *causes*
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
- **AdvBench** (measurements) — *measured_by*
  > "and (3) AdvBench ... a widely used benchmark for safety against adversarial attacks"
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf)
- **Safety refusal** (constructs) — *causes*
  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf)
- **MixEval** (measurements) — *measured_by*
  > "We evaluate alignment effectiveness using three benchmarks: (1) MixEval ..."
  - [RMB: Comprehensively benchmarking reward models in LLM alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/427f20d90386fd27804f1831d6a3d48f-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Puzzle: Distillation-Based NAS for Inference-Optimized LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bercovich25a/bercovich25a.pdf)

### → Alignment
- **Knowledge transferability** (constructs) — *causes*
  - [Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion](https://aclanthology.org/2025.naacl-long.88.pdf)
- **Interpretability and explainability** (constructs) — *causes*
  - [SAE-V: Interpreting Multimodal Models for Enhanced Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lou25b/lou25b.pdf)
- **Question difficulty** (constructs) — *causes*
  - [Principled Data Selection for Alignment: The Hidden Risks of Difficult Examples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25f/gao25f.pdf)
- **Robustness** (constructs) — *causes*
  - [On the Robustness of Reward Models for Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hong25d/hong25d.pdf)

### Associated with
- **Instruction following** (constructs)
  - [A Critical Evaluation of AI Feedback for Aligning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/33870b3e099880cd8e705cd07173ac27-Paper-Conference.pdf)
- **Helpfulness** (constructs)
  - [BoNBoN Alignment for Large Language Models and the Sweetness of Best-of-n Sampling](https://proceedings.neurips.cc/paper_files/paper/2024/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf)
- **Jailbreaking** (behaviors tasks)
  - [Tree of Attacks: Jailbreaking Black-Box LLMs Automatically](https://proceedings.neurips.cc/paper_files/paper/2024/file/70702e8cbb4890b4a467b984ae59828a-Paper-Conference.pdf)
- **Safety** (constructs)
  - [Functional Homotopy: Smoothing Discrete Optimization via Continuous Parameters for LLM Jailbreak Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed212957dbe503283c577a94202cb8c-Paper-Conference.pdf)
- **Harmlessness** (constructs)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
- **Human preference alignment** (constructs)
  - [AdvancingArabic Diacritization: Improved Datasets, Benchmarking, and State-of-the-Art Models](https://aclanthology.org/2025.emnlp-main.847.pdf)
- **Reward overoptimization** (constructs)
  - [Geometric-Averaged Preference Optimization for Soft Preference Labels](https://proceedings.neurips.cc/paper_files/paper/2024/file/688c7a82e31653e7c256c6c29fd3b438-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf)
- **Best-of-N** (measurements)
  - [Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf)
- **Reward hacking** (behaviors tasks)
  - [Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking](https://proceedings.iclr.cc/paper_files/paper/2025/file/c78f81a878a72566422f37279bca0fd0-Paper-Conference.pdf)
- **Reasoning faithfulness** (constructs)
  - [SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation](https://proceedings.neurips.cc/paper_files/paper/2024/file/217bb44ab14621754db8a392163e6b07-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmful content generation** (behaviors tasks)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
- **Deception** (constructs)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Manipulation** (constructs)
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **Uniformity** (constructs)
  - [MoMoE: Mixture of Moderation Experts Framework forAI-Assisted Online Governance](https://aclanthology.org/2025.emnlp-main.639.pdf)

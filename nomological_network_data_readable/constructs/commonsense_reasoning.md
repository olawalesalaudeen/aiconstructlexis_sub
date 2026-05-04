# Commonsense reasoning
**Type:** Construct  
**Referenced in:** 326 papers  
**Also known as:** Common sense reasoning, Common-sense reasoning, Commonsense inference, Physical commonsense, Common sense inference, Common sense understanding, Commonsense generation, Commonsense Inference, Commonsense question answering, Common-sense question answering, Commonsense completion  

## State of the Field

The most prevalent definition across the provided literature characterizes commonsense reasoning as the ability to make presumptions, inferences, or judgments about ordinary, everyday situations based on a shared understanding of the world. While this general framing is widespread, a smaller body of work offers more specific definitions, such as inferring plausible physical interactions in embodied settings or applying world knowledge to interpret video content. Across the surveyed papers, this construct is almost universally operationalized through a model's performance on question-answering and completion tasks, frequently evaluated in a zero-shot setting. The field consistently uses a set of benchmarks to measure this ability, with the most commonly cited including HellaSwag, PIQA, WinoGrande, ARC, OpenBookQA, and CommonsenseQA. A few papers define the concept as an observable behavior itself, such as "commonsense question answering" or "commonsense generation," the latter of which is measured by the CommonGen benchmark. Commonsense reasoning is often studied alongside other capabilities like arithmetic and symbolic reasoning, and one study further classifies it into "explanatory, predictive, and counterfactual sub-skills" (Large Language Models as Automated Aligners for  benchmarking  Vision-Language Models). Despite its frequent measurement, at least one paper notes that the concept's boundaries are "vague and ill-defined" (VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models).

## Sources

**[Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf)**
> The ability to make presumptions about the ordinary world, reflecting a shared understanding of everyday situations.

**[Eureka: Human-Level Reward Design via Coding Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/70c26937fbf3d4600b69a129031b66ec-Paper-Conference.pdf) (as "Common sense reasoning")**
> The ability to make sound practical judgments concerning everyday situations or events, such as identifying which state variables are relevant for a physical task.

**[WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/82eec786fdfbbfa53450c5feb7d1ac92-Paper-Conference.pdf) (as "Commonsense inference")**
> The ability to make plausible inferences about everyday situations and concepts that are not explicitly stated.

**[Grounding Language Plans in Demonstrations Through Counterfactual Perturbations](https://proceedings.iclr.cc/paper_files/paper/2024/file/be62c4a943675195ff5a2a98d5b9724f-Paper-Conference.pdf) (as "Common-sense reasoning")**
> The latent ability to infer plausible task structure and physical interactions from language and demonstrations in embodied settings.

**[Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf) (as "Commonsense understanding")**
> The latent ability to answer questions and solve problems that depend on everyday physical or social commonsense knowledge.

**[Neuron-based Multifractal Analysis of Neuron Interaction Dynamics in Large Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6158e152498f8d8b83d14388a7ec1963-Paper-Conference.pdf) (as "Physical commonsense")**
> The latent ability to reason about everyday physical interactions and plausible physical outcomes.

**[SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/693ce820ea7e0f0c70a2a833cbdf7ccc-Paper-Conference.pdf) (as "Common sense inference")**
> The ability to apply general world knowledge to interpret video content and provide a logical framework for understanding events.

**[Understanding and Improving Length Generalization in Recurrent Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/buitrago25a/buitrago25a.pdf) (as "Common sense understanding")**
> The model's ability to comprehend and reason about situations in a way that aligns with general human knowledge and intuition.

**[Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf) (as "Commonsense generation")**
> The task of generating a natural sentence that incorporates a given set of keywords, demonstrating an understanding of their relationships.

**[Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Commonsense Inference")**
> Understanding and reasoning about the relationships between concepts and events based on commonsense and background knowledge.

**[Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf) (as "Commonsense question answering")**
> Selecting the most plausible answer to a question or scenario that depends on everyday knowledge.

**[R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0c165157df7e3082f9c6d70d3a4b6e9-Paper-Conference.pdf) (as "Common-sense question answering")**
> The observable behavior of answering questions that require background knowledge about the world, often in a multiple-choice or completion format.

**[Low-Rank Adapting Models for Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25r/chen25r.pdf) (as "Commonsense completion")**
> The observable behavior of selecting the most plausible continuation for a given text, testing commonsense inference.

## Relationships

### Commonsense reasoning →
- **HellaSwag** (measurements) — *measured_by*
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
- **WinoGrande** (measurements) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
- **CommonsenseQA** (measurements) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **OpenBookQA** (measurements) — *measured_by*
  - [QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e6c2e85db1f1039177c4495ccd399ac4-Paper-Conference.pdf)
- **SIQA** (measurements) — *measured_by*
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **StrategyQA** (measurements) — *measured_by*
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
- **ARC** (measurements) — *measured_by*
  - [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf)
- **OBQA** (measurements) — *measured_by*
  - [AmoebaLLM: Constructing Any-Shape Large Language Models for Efficient and Instant Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f11e548311c7fd3f33596a4d1dd41f0-Paper-Conference.pdf)
- **LLM Evaluation Harness** (measurements) — *measured_by*
  - [Would I Lie To You? Inference Time Alignment of Language Models using Direct Preference Heads](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad3d0ac42b4b5cc3b5f0ca10107d5c84-Paper-Conference.pdf)
- **Commonsense170k** (measurements) — *measured_by*
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
- **MMLU** (measurements) — *measured_by*
  - [Instance-adaptive Zero-shot Chain-of-Thought Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/e304e04a6f455dd82f8a85a0a3679493-Paper-Conference.pdf)
- **SciQ** (measurements) — *measured_by*
  - [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf)
- **XCOPA** (measurements) — *measured_by*
  - [Adapters for Altering LLM Vocabularies: What Languages Benefit the Most?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab5492f57995409351cbf1a1cdf5f1a4-Paper-Conference.pdf)
- **COPA** (measurements) — *measured_by*
  - [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)
- **TruthfulQA** (measurements) — *measured_by*
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
- **SocialIQA** (measurements) — *measured_by*
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **StoryCloze** (measurements) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **Winograd** (measurements) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **MuSR** (measurements) — *measured_by*
  - [MuSR: Testing the Limits of Chain-of-thought with Multistep Soft Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f8c7eb848ffec848f3ed2b7ca44915d-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Creak** (measurements) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **CommonsenseQA 2.0** (measurements) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **ECQA** (measurements) — *measured_by*
  - [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf)
- **Commonsense reasoning benchmark** (measurements) — *measured_by*
  - [From Outcomes to Processes: GuidingPRMLearning fromORMfor Inference-Time Alignment](https://aclanthology.org/2025.acl-long.947.pdf)
- **QASC** (measurements) — *measured_by*
  - [Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Generalization** (constructs) — *causes*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **X-CSQA** (measurements) — *measured_by*
  - [MindMerger: Efficiently Boosting LLM Reasoning in non-English Languages](https://proceedings.neurips.cc/paper_files/paper/2024/file/3bf80b34f731313b8292f4578e820c90-Paper-Conference.pdf)
- **CommonGen** (measurements) — *measured_by*
  - [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf)
- **WikiText** (measurements) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **RiddleSense** (measurements) — *measured_by*
  - [Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **ANLI** (measurements) — *measured_by*
  - [AutoPSV: Automated Process-Supervised Verifier](https://proceedings.neurips.cc/paper_files/paper/2024/file/9246aa822579d9b29a140ecdac36ad60-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [GReaTer: Gradients Over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/18a42aad2fa8aa871e2ee20d425c208d-Paper-Conference.pdf)
- **CNN/DailyMail** (measurements) — *measured_by*
  - [FouRA: Fourier Low-Rank Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/83960718b4d12f799985206f1b1cf00f-Paper-Conference.pdf)
- **Hugging Face Open LLM Leaderboard** (measurements) — *measured_by*
  - [Joint Reward and Policy Learning with Demonstrations and Human Feedback Improves Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/0ad6ebd11593822b8a6d5873ca9c5b0b-Paper-Conference.pdf)
- **XStoryCloze** (measurements) — *measured_by*
  - [Pangea: A Fully Open Multilingual Multimodal LLM for 39 Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf)
- **Exploration** (constructs) — *causes*
  - [Monte Carlo Planning with Large Language Model for Text-Based Game Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/837ff662214b04e7ea8c43f095fe0dd7-Paper-Conference.pdf)
- **MathQA** (measurements) — *measured_by*
  - [Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf)
- **TextWorld** (measurements) — *measured_by*
  - [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/369a30aac2765950865efd318cef7f76-Paper-Conference.pdf)
- **MME** (measurements) — *measured_by*
  - [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf)
- **A-OKVQA** (measurements) — *measured_by*
  - [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf)
- **LogiQA** (measurements) — *measured_by*
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **LogiQA2** (measurements) — *measured_by*
  - [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/923285deb805c3e14e1aeebc9854d644-Paper-Conference.pdf)
- **GPQA** (measurements) — *measured_by*
  - [R-Bind: Unified Enhancement of Attribute and Relation Binding in Text-to-Image Diffusion Models](https://aclanthology.org/2025.emnlp-main.350.pdf)
- **Date Understanding** (measurements) — *measured_by*
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.184.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [AlgoPuzzleVQA: Diagnosing Multimodal Reasoning Challenges of Language Models with Algorithmic Multimodal Puzzles](https://aclanthology.org/2025.naacl-long.487.pdf)
- **WSC** (measurements) — *measured_by*
  - [Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **Wino** (measurements) — *measured_by*
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)
- **OpenCompass** (measurements) — *measured_by*
  - [Mask-Enhanced Autoregressive Prediction: Pay Less Attention to Learn More](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuang25b/zhuang25b.pdf)
- **CommonsenseQA-CoT** (measurements) — *measured_by*
  - [MIO: A Foundation Model on Multimodal Tokens](https://aclanthology.org/2025.emnlp-main.256.pdf)
- **CosmosQA** (measurements) — *measured_by*
  - [EnhancingChinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1155.pdf)
- **QuaRel** (measurements) — *measured_by*
  - [Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning](https://aclanthology.org/2025.emnlp-main.1203.pdf)
- **seqBench** (measurements) — *measured_by*
  - [Image Difference Captioning via Adversarial Preference Optimization](https://aclanthology.org/2025.emnlp-main.1714.pdf)

### Associated with
- **Reasoning** (constructs)
  - [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.309.pdf)
- **Multiple-choice question answering** (behaviors tasks)
  - [Reinforcement Learning for Large Language Models via Group Preference Reward Shaping](https://aclanthology.org/2025.emnlp-main.1086.pdf)
- **MuSR** (measurements)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [TPO: Aligning Large Language Models with Multi-branch & Multi-step Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/42ac0f53b7ffede90aea8275b11b3bb8-Paper-Conference.pdf)
- **Commonsense knowledge** (constructs)
  - [How Private are Language Models in Abstractive Summarization?](https://aclanthology.org/2025.emnlp-main.1532.pdf)
- **Mathematical reasoning** (constructs)
  - [D-LLM: A Token Adaptive Computing Resource Allocation Strategy for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/03469b1a66e351b18272be23baf3b809-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks)
  - [HFT: Half Fine-Tuning for Large Language Models](https://aclanthology.org/2025.acl-long.627.pdf)
- **Rationality** (constructs)
  - [GRADEO: Towards Human-Like Evaluation for Text-to-Video Generation via Multi-Step Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mou25a/mou25a.pdf)
- **Scientific reasoning** (constructs)
  - [PDE-Controller: LLMs for Autoformalization and Reasoning of PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/soroco25a/soroco25a.pdf)

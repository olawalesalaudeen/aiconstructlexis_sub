# World knowledge
**Type:** Construct  
**Referenced in:** 81 papers  
**Also known as:** General knowledge, Real-world knowledge grounding, Common knowledge, Background knowledge, Basic knowledge, World understanding  

## State of the Field

Across the surveyed literature, 'world knowledge' is most commonly characterized as the vast body of general factual and conceptual information about the world that a model internalizes from its training data and stores within its parameters. While the prevailing usage centers on factual recall, a smaller set of studies broadens the definition to include an understanding of real-world properties, societal norms, or scientific intuition, sometimes using related terms like 'general,' 'background,' or 'prior' knowledge. The construct is operationalized and measured through performance on a range of question-answering benchmarks, with papers frequently citing the use of datasets such as Natural Questions, TriviaQA, MMLU, and CommonsenseQA to evaluate this capability. This internalized knowledge is described as a foundational capability, often studied alongside commonsense and reasoning, and is leveraged for tasks like fine-grained visual recognition and claim verification. Some work contrasts this broad knowledge with more specialized information, such as code syntax, while one paper frames it as 'basic knowledge' that is at risk of being forgotten during fine-tuning. In at least one study, performance on world knowledge tasks is used as a direct proxy for measuring the principle of honesty.

## Sources

**[Democratizing Fine-grained Visual Recognition with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/49299a8afda8053932a4cfd62fdfd1b9-Paper-Conference.pdf)**
> The body of general factual information about the world that a model has internalized from its training data.

**[Harnessing Explanations: LLM-to-LM Interpreter for Enhanced Text-Attributed Graph Representation Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/1766d75b077b66457040e4661771aec5-Paper-Conference.pdf) (as "General knowledge")**
> The broad base of factual and conceptual information acquired by a model during pre-training, which can be applied to downstream tasks.

**[Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf) (as "Real-world knowledge grounding")**
> The ability to connect multimodal inputs with factual, external knowledge about the world, enabling accurate and contextually relevant responses.

**[Secret Collusion among AI Agents: Multi-Agent Deception via Steganography](https://proceedings.neurips.cc/paper_files/paper/2024/file/861f7dad098aec1c3560fb7add468d41-Paper-Conference.pdf) (as "Common knowledge")**
> A form of group knowledge where all agents know a fact, know that all other agents know the fact, and so on ad infinitum, which is a prerequisite for certain types of coordination.

**[Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf) (as "Background knowledge")**
> The latent store of general world knowledge and scientific intuition acquired during pre-training that the model can apply to new tasks.

**[Make-it-Real: Unleashing Large Multimodal Model for Painting 3D Objects with Realistic Materials](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf) (as "Prior knowledge")**
> The vast repository of general world knowledge, including facts about objects, their typical materials, and physical properties, that the model possesses from its training.

**[SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models](https://aclanthology.org/2025.acl-long.626.pdf) (as "Basic knowledge")**
> The parametric world knowledge learned during large-scale unsupervised pre-training, which is at risk of being forgotten during fine-tuning.

**[Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf) (as "World understanding")**
> The degree to which a model possesses an internal, coherent representation of concepts and their relationships in the world, beyond surface-level linguistic patterns.

## Relationships

### World knowledge →
- **MMLU** (measurements) — *measured_by*
  - [Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning](https://proceedings.iclr.cc/paper_files/paper/2024/file/160adf2dc118a920e7858484b92a37d8-Paper-Conference.pdf)
- **TriviaQA** (measurements) — *measured_by*
  - [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/665bb142d4b9f55660cb89bb56a66fe1-Paper-Conference.pdf)
- **Natural Questions** (measurements) — *measured_by*
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
- **ARC-Easy** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **WebQuestions** (measurements) — *measured_by*
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **BoolQ** (measurements) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **LAMBADA** (measurements) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [FakeShield: Explainable Image Forgery Detection and Localization via Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d4e0ab9d8ff180bf5b95c258842d16e-Paper-Conference.pdf)
- **ARC-Challenge** (measurements) — *measured_by*
  - [Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum](https://proceedings.neurips.cc/paper_files/paper/2024/file/3f9bf45ea04c98ad7cb857f951f499e2-Paper-Conference.pdf)
- **RACE** (measurements) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **PIQA** (measurements) — *measured_by*
  - [Sparse maximal update parameterization: A holistic approach to sparse training dynamics](https://proceedings.neurips.cc/paper_files/paper/2024/file/3b6aaffec941f98930753fa6d6de7263-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
- **HotpotQA** (measurements) — *measured_by*
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **ComplexWebQuestions** (measurements) — *measured_by*
  - [Mixture of Parrots: Experts improve memorization more than reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc3356e0fa1753fff7e8d6628e71b22-Paper-Conference.pdf)
- **HuggingFace Open LLM Leaderboard 2** (measurements) — *measured_by*
  - [WildChat-50M: A Deep Dive Into the Role of Synthetic Data in Post-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feuer25a/feuer25a.pdf)
- **MMAU** (measurements) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **VoiceBench** (measurements) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **VoxEval** (measurements) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)

### Associated with
- **Question answering** (behaviors tasks)
  - [CorDA: Context-Oriented Decomposition Adaptation of Large Language Models for Task-Aware Parameter-Efficient Fine-tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/83f95bb0ac5046338ea2afe3390e9f4b-Paper-Conference.pdf)
- **OK-VQA** (measurements)
  - [Visual Riddles: a Commonsense and World Knowledge Challenge for Large Vision and Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fbf5efe979e6754dc06a0869233f2510-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Faithfulness** (constructs)
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)

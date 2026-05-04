# Commonsense170k
**Type:** Measurement  
**Referenced in:** 21 papers  
**Also known as:** COMMONSENSE170K, Commonsense170K, Common-sense170K, CSR-170k, Commonsense-170K, CSR170K  

## State of the Field

Across the provided literature, Commonsense170k is predominantly described as a large-scale dataset for supervised fine-tuning of language models on commonsense reasoning tasks. Many papers explicitly state they "fine-tune" models on this dataset, which one source calls "a comprehensive collection of commonsense reasoning questions" (QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation). A less common framing, found in a few papers, treats it as a composite benchmark or "language evaluation suite" for assessing LLM performance, with one source mentioning its use for both fine-tuning and evaluation. Multiple definitions and snippets confirm that the dataset is a combination of eight distinct commonsense reasoning benchmarks, which are identified as BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-Easy, ARC-Challenge, and OpenbookQA. In terms of what it is used to measure, the relationships show it is widely employed to assess a model's "Commonsense understanding" and ability for "Commonsense question answering". Its connection to model training is also reflected in its use to study "Instruction fine-tuning".

## Sources

**[QuanTA: Efficient High-Rank Fine-Tuning of LLMs with Quantum-Informed Tensor Adaptation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a7c17115db36193f6b83b71b0fe1d416-Paper-Conference.pdf) (as "COMMONSENSE170K")**
> A training dataset of commonsense reasoning questions used to fine-tune a single model before evaluation on downstream commonsense benchmarks.

**[SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf) (as "Commonsense170K")**
> A large-scale dataset for supervised fine-tuning focused on commonsense reasoning tasks.

**[OmniFlatten: An End-to-endGPTModel for Seamless Voice Conversation](https://aclanthology.org/2025.acl-long.710.pdf) (as "Common-sense170K")**
> A large training dataset for commonsense reasoning, constructed from eight different subtasks, used for fine-tuning models.

**[SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf) (as "CSR-170k")**
> Commonsense Reasoning 170k, a language evaluation suite containing multiple commonsense reasoning datasets used to assess LLM performance on commonsense question answering tasks.

**[LIFT the Veil for the Truth: Principal Weights Emerge after Rank Reduction for Reasoning-Focused Supervised Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ba/liu25ba.pdf) (as "Commonsense-170K")**
> Dataset used for fine-tuning and evaluating commonsense reasoning across multiple tasks such as BoolQ, PIQA, SIQA, HellaSwag, Wino, ARC-e, ARC-c, and OBQA.

**[SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf) (as "CSR170K")**
> A composite benchmark for commonsense reasoning, comprising eight different datasets including BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-Easy, ARC-Challenge, and OpenbookQA.

## Relationships

### → Commonsense170k
- **Commonsense reasoning** (constructs) — *measured_by*
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)
- **Instruction fine-tuning** (behaviors tasks) — *measured_by*
  - [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a70ad3d9c704fb9b81b5c69eda722dc-Paper-Conference.pdf)
- **Commonsense question answering** (behaviors tasks) — *measured_by*
  - [Sketch to Adapt: Fine-Tunable Sketches for Efficient LLM Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bs/zhang25bs.pdf)

### Associated with
- **BoolQ** (measurements)
  - [ReFT: Representation Finetuning for Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/75008a0fba53bf13b0bb3b7bff986e0e-Paper-Conference.pdf)

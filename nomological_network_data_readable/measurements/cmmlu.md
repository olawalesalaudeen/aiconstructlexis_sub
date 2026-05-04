# CMMLU
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

CMMLU is a benchmark used in the provided literature to evaluate a range of model capabilities, primarily within a Chinese context. It is consistently defined as the "Chinese Massive Multitask Language Understanding" benchmark, with one source also framing it as a "Cultural and Multilingual" instrument for "assessing knowledge in Chinese contexts across various disciplines" (MoH: Multi-Head Attention as Mixture-of-Head Attention). The papers in this set use CMMLU to operationalize and measure several constructs, including `Chinese language understanding`, `Commonsense knowledge`, `Faithfulness`, `Generalization`, and `Language modeling`. One specific application described is its use to evaluate a model's "general capabilities in Chinese" to ensure they "are not compromised after naturalness alignment" (Establishing TrustworthyLLMEvaluation via Shortcut Neuron Analysis). The data also indicates that the benchmark is sometimes administered in a few-shot evaluation setting, as one paper refers to a "5-shot CMMLU" evaluation.

## Sources

**[Establishing TrustworthyLLMEvaluation via Shortcut Neuron Analysis](https://aclanthology.org/2025.acl-long.193.pdf)**
> The Chinese Massive Multitask Language Understanding benchmark, used to evaluate a model's general capabilities in Chinese to ensure they are not compromised after alignment.

## Relationships

### → CMMLU
- **Commonsense knowledge** (constructs) — *measured_by*
  - [Reference Trustable Decoding: A Training-Free Augmentation Paradigm for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/925869234d3aa2a3aad5f05b643974aa-Paper-Conference.pdf)
- **Chinese language understanding** (constructs) — *measured_by*
  - [UNComp: Can Matrix Entropy Uncover Sparsity? — A Compressor Design from an Uncertainty-Aware Perspective](https://aclanthology.org/2025.emnlp-main.210.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Maximizing Intermediate Checkpoint Value in LLM Pretraining with Bayesian Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bv/liu25bv.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Retrieval Enhanced Feedback via In-context Neural Error-book](https://aclanthology.org/2025.emnlp-main.712.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [Enhancing Automated Interpretability with Output-Centric Feature Descriptions](https://aclanthology.org/2025.acl-long.289.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [KV Shifting Attention Enhances Language Modeling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ac/xu25ac.pdf)

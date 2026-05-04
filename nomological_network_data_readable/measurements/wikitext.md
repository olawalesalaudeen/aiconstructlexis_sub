# WikiText
**Type:** Measurement  
**Referenced in:** 53 papers  
**Also known as:** Wikitext  

## State of the Field

Across the surveyed literature, WikiText is predominantly characterized as a benchmark dataset used to evaluate language modeling performance. The most common operationalization involves measuring perplexity on a held-out validation set of its natural text, which one paper notes is sourced from high-quality Wikipedia articles rated as 'Good' or 'Featured' by human editors. This perplexity score is frequently used as a direct measure of a model's `Language modeling` capability, with some papers specifying that it evaluates constructs like `fluency and coherence`. A smaller number of studies also employ WikiText to assess `Generalization` and `Prediction confidence`. Beyond its primary role in perplexity-based evaluation, the dataset serves several other functions. Some research uses it as a corpus for pre-training models or for out-of-domain evaluation of model robustness. In other cases, its validation split is used for analytical purposes, such as "measuring the sparsity and recording preactivation distributions" of models or for "expert parallelism profiling in efficiency evaluation".

## Sources

**[A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)**
> A benchmark dataset used to evaluate language modeling performance by measuring perplexity on a held-out validation set of natural text.

**[Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf) (as "Wikitext")**
> A language-model evaluation benchmark used here to assess long-context language modeling across different context lengths.

## Relationships

### → WikiText
- **Language modeling** (behaviors tasks) — *measured_by*
  > Following previous works on LLM compression (Xiao et al., 2023; Frantar & Alistarh, 2023), we evaluate the perplexity on the held-out WikiText (Merity et al., 2016) validation set. (Section 4)
  - [A Simple and Effective Pruning Approach for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/14c856c7a41297804de4c4890e846b25-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We evaluate LENSLLM’s effectiveness for LLM selection through three analyses: (1) comparing its curve-fitting accuracy during fine-tuning against Rectified Scaling Law... across FLAN, Wikitext, and Gigaword datasets. (Section 4.2)
  - [LensLLM: Unveiling Fine-Tuning Dynamics for LLM Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25g/zeng25g.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3f39e51f5f634fb16cc3e658f8512b9-Paper-Conference.pdf)
- **Long-form text generation** (behaviors tasks) — *measured_by*
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **Fluency** (constructs) — *measured_by*
  - [Logically Consistent Language Models via Neuro-Symbolic Integration](https://proceedings.iclr.cc/paper_files/paper/2025/file/871a06b60cf087bbdb854ebfcdf5349a-Paper-Conference.pdf)
- **Prediction confidence** (constructs) — *measured_by*
  > "WikiText (Merity et al., 2022) to assess the model’s prediction confidence" (Section 5.1, Datasets)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [Decomposition Dilemmas: Does Claim Decomposition Boost or Burden Fact-Checking Performance?](https://aclanthology.org/2025.naacl-long.321.pdf)

### Associated with
- **Faithfulness** (constructs)
  - [Eliciting Implicit Acoustic Styles from Open-domain Instructions to Facilitate Fine-grained Controllable Generation of Speech](https://aclanthology.org/2025.emnlp-main.183.pdf)

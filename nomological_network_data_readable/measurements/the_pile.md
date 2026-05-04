# The Pile
**Type:** Measurement  
**Referenced in:** 43 papers  
**Also known as:** Pile, PILE 10K, D-PILE  

## State of the Field

Across the provided literature, The Pile is consistently characterized as a large and diverse text corpus with two prevalent applications: pre-training language models and evaluating their performance. The most common usage, cited in numerous papers, is as a pre-training dataset, with studies noting they "train autoregressive models on... the Pile from scratch" (Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training). A substantial body of work also employs it for evaluation, where it is used to measure `Language modeling` performance, frequently by calculating perplexity on its validation or test splits. Beyond general language modeling, The Pile is also used to assess more specific behaviors, including `Memorization` by identifying extractable samples, and `Length generalization` using longer sequences. The corpus is described as multi-domain, composed of sources like "arXiv, GitHub, Freelaw, PubMed, DM Math, etc." Researchers utilize specific versions or subsets for different purposes, such as the deduplicated "D-PILE" for pre-training, the "PILE 10K" subset for perplexity evaluation, or domain-specific subsets for creating specialist models. A less common application involves using it to sample a "small calibration set" for quantization.

## Sources

**[In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf)**
> The Pile is a large text corpus used here as a pre-training dataset for language modeling comparisons.

**[Zoology: Measuring and Improving  Recall in Efficient Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/448fc91f669c15d10364ee01d512cc10-Paper-Conference.pdf) (as "Pile")**
> The Pile language modeling dataset used here as a validation and test corpus for measuring next-token prediction and recall-related slices.

**[Residual Matrix Transformers: Scaling the Size of the Residual Stream](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mak25a/mak25a.pdf) (as "PILE 10K")**
> A 10,000-document subset of The Pile, a large and diverse text corpus, used for evaluating language model perplexity.

**[Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf) (as "D-PILE")**
> The deduplicated version of The PILE dataset, a large and diverse text corpus used for pretraining and evaluating language models.

## Relationships

### → The Pile
- **Language modeling** (behaviors tasks) — *measured_by*
  > "Our experiments involved training on a dataset tokenized with the LLaMA tokenizer (Touvron et al., 2023), comprising 56GB of raw data sourced from 91 files sampled from The Pile (Gao et al., 2020)."
  - [MiCEval: Unveiling Multimodal Chain of Thought’s Quality via Image Description and Reasoning Steps](https://aclanthology.org/2025.naacl-long.505.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [MambaExtend: A Training-Free Approach to Improve Long Context Extension of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/f1922bd718528ac3eab114eabbbfa7a0-Paper-Conference.pdf)
- **Pre-training data detection** (behaviors tasks) — *measured_by*
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **Memorization** (constructs) — *measured_by*
  > This dataset contains all 32-extractable samples from the Pile, verified by referencing the training data (Gao et al., 2020).
  - [Recite, Reconstruct, Recollect: Memorization in LMs as a Multifaceted Phenomenon](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd87a328be4c7e43aa0b900a0ebf79a-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  > To assess their capability for length extrapolation, we evaluated the implicit models on the test split of the D-PILE, which was packed with longer sequences consisting of 4096, 8192, and 16384 tokens. (Section 5)
  - [Implicit Language Models are RNNs: Balancing Parallelization and Expressivity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schone25a/schone25a.pdf)

### Associated with
- **Pythia** (measurements)
  > we have full access to both the Pythia model checkpoints from training and the Pile dataset they were trained on (Gao et al., 2020), which is required for our analysis. (Section 2.2)
  - [Compute-Optimal LLMs Provably Generalize Better with Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/4a13396b4c8a90e01dac61d2b0559ef7-Paper-Conference.pdf)
- **Pile-CC** (measurements)
  > We train 70M and 160M language models on the mixture of Github and Pile-CC subset from the Pile dataset (Section 3.1).
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)
- **Books3** (measurements)
  - [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf)

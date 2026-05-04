# Membership inference attack
**Type:** Behavior  
**Referenced in:** 12 papers  
**Also known as:** Membership Inference Attack (MIA), Membership Inference Attack, lossMIA, zlibMIA  

## State of the Field

Across the surveyed literature, a Membership Inference Attack (MIA) is predominantly defined as a privacy evaluation procedure designed to determine if a specific data point was used in a model's training or alignment process. The attack operates by distinguishing member from non-member examples, often by exploiting "distributional differences in certain statistics (e.g., loss) between training (member) and non-training (non-member) data" (MUSE: Machine Unlearning Six-Way Evaluation for Language Models). While some attacks are loss-based, others are designed for "black-box" scenarios that rely "solely on the output texts" without access to logits (Differentially Private Steering for Large Language Model Alignment). The most prevalent use of MIA is to measure `Privacy leakage` and estimate empirical privacy risk. It is also employed to evaluate the efficacy of `Machine unlearning`, assess `Forget quality`, and, in a smaller set of studies, measure `Knowledge memorization`. Specific implementations mentioned include `lossMIA`, which uses a model's loss, and `zlibMIA`, which normalizes loss by zlib compression size. The performance of these attacks is sometimes evaluated using metrics like AUC and TPR at low FPR thresholds. Described as an "established practice," MIA serves as a common tool for auditing privacy in language models.

## Sources

**[Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf) (as "Membership Inference Attack (MIA)")**
> An evaluation procedure designed to audit empirical privacy by attempting to determine whether a specific data sample was used in the model's alignment or training process.

**[MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)**
> A privacy evaluation procedure that tests whether a datapoint was used in training by distinguishing member from non-member examples.

**[Communication Makes Perfect: Persuasion Dataset Construction via Multi-LLMCommunication](https://aclanthology.org/2025.naacl-long.204.pdf) (as "Membership Inference Attack")**
> An evaluation procedure designed to determine whether a specific data sample was part of a model's training set by analyzing its output behavior.

**[Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf) (as "lossMIA")**
> A specific type of Membership Inference Attack that uses a model's loss on a given sample to infer whether that sample was part of the training data.

**[Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf) (as "zlibMIA")**
> A specific type of Membership Inference Attack that uses a model's loss on a sample, normalized by the sample's zlib compression size, to infer membership.

## Relationships

### → Membership inference attack
- **Privacy leakage** (behaviors tasks) — *measured_by*
  > “we consider three popular MIA methods: LOSS ... Zlib Entropy ... and Min-k% Prob”
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Knowledge memorization** (constructs) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Unlearning efficacy** (constructs) — *measured_by*
  - [Machine Unlearning Fails to Remove Data Poisoning Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e810b2c75d69be186cadd2fe3febeab-Paper-Conference.pdf)
- **Forget quality** (constructs) — *measured_by*
  > To determine whether private information still exists in VLMs after unlearning more accurately, we proposed to use MIAs for evaluation. (Section 2.5.3)
  - [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf)

### Associated with
- **Min-K% Prob** (measurements)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)

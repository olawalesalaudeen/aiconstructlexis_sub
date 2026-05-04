# CIFAR-10
**Type:** Measurement  
**Referenced in:** 38 papers  
**Also known as:** CIFAR10  

## State of the Field

Across the provided literature, CIFAR-10 is consistently characterized as a benchmark image dataset, with definitions widely agreeing on its composition of 60,000 32x32 color images in 10 classes. The most prevalent application of this dataset is to measure `Image classification` performance, with numerous papers using it to evaluate, fine-tune, and compare a variety of models, including Vision Transformers and ResNets. Beyond this primary function, CIFAR-10 is also frequently used to assess `Generalization`, for instance by evaluating model performance on "dirty-sample detection under poisoned samples, noisy labels, and hybrid dirty samples." Several papers also employ it as a testbed for model robustness, using it to assess the impact of backdoor attacks or for "automated accuracy prediction under synthetic and natural shifts." Other documented uses include evaluating visual processing capabilities, comparing clustering algorithms, and assessing neural architecture search performance. The dataset is also associated with measuring `Noise robustness` and `Multimodal understanding`, though the specific methods for these evaluations are not detailed in the provided evidence.

## Sources

**[Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf)**
> A standard image dataset with 10 object classes, used to compare the proposed text-conditioned clustering method against classical clustering algorithms.

**[Quantum-PEFT: Ultra parameter-efficient fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e52bbb99690d1e05c7ef7b4c8b3569a-Paper-Conference.pdf) (as "CIFAR10")**
> A dataset of 60,000 32x32 color images in 10 classes, used for image classification tasks.

## Relationships

### → CIFAR-10
- **Image classification** (behaviors tasks) — *measured_by*
  > We compare MCNC on CIFAR-10 and CIFAR-100 (Krizhevsky et al., 2009) with both pruning methods as well as PRANC (Nooralinejad et al., 2023) and NOLA (Koohpayegani et al., 2024) under extreme compression rates. (Section 4.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **Noise robustness** (constructs) — *measured_by*
  - [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > Extensive experiments demonstrate its superior performance and generalization to various categories and types of dirty samples. The results on CIFAR-10, ImageNet-100 and ImageNet-Dog with different poisoning ratios are presented in Tables 1,2,13,14.
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **Zero-shot image classification** (behaviors tasks) — *measured_by*
  > We conduct zero-shot classification experiments on ImageNet-1K (Russakovsky et al., 2015), CIFAR-100, CIFAR-10 (Krizhevsky et al., 2009)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)

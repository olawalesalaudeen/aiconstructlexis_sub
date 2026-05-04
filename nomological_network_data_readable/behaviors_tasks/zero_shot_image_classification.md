# Zero-shot image classification
**Type:** Behavior  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, zero-shot image classification is consistently defined as the task of classifying an image into categories for which the model has seen no training examples. This behavior is operationalized and measured using a wide array of datasets. Several papers report conducting experiments on ImageNet-1k, CIFAR-100, and CIFAR-10. One study, focused on multi-task model merging, evaluates performance across a suite of eight distinct datasets, including SUN397, Cars, GTSRB, MNIST, EuroSAT, SVHN, DTD, and RESISC45. The task is presented as an evaluation method in different contexts, for instance, as an additional benchmark alongside video understanding tasks, as noted in one paper. The available data frames it as an observable task used to assess model capabilities under novel conditions.

## Sources

**[VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf)**
> The task of classifying an image into one of several categories without having seen any training examples for those specific categories.

## Relationships

### Zero-shot image classification →
- **ImageNet-1k** (measurements) — *measured_by*
  > We conduct zero-shot classification experiments on ImageNet-1K (Russakovsky et al., 2015)
  - [TripletCLIP:  Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
- **CIFAR-100** (measurements) — *measured_by*
  > We conduct zero-shot classification experiments on ImageNet-1K (Russakovsky et al., 2015), CIFAR-100, CIFAR-10 (Krizhevsky et al., 2009)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **CIFAR-10** (measurements) — *measured_by*
  > We conduct zero-shot classification experiments on ImageNet-1K (Russakovsky et al., 2015), CIFAR-100, CIFAR-10 (Krizhevsky et al., 2009)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)

### → Zero-shot image classification
- **Multimodal understanding** (constructs) — *causes*
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)

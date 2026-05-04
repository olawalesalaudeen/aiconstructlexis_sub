# DTD
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

The Describable Textures Dataset (DTD) is consistently presented as a measurement instrument for evaluating model performance on computer vision tasks. Its most common application across the surveyed literature is to measure `Image classification` capabilities, where it is frequently included in multi-dataset benchmarks. For instance, several papers use DTD as part of a common suite of datasets—alongside others like Cars, EuroSAT, and SUN397—to fine-tune and assess models such as CLIP-ViT. A more specific framing, offered by one paper, defines DTD as a tool for `texture classification` and for evaluating `few-shot learning performance`. This specialized use is consistent with its inclusion in benchmarks that, as one paper notes, are constructed from "diverse downstream datasets from 5 domains".

## Sources

**[Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf)**
> The Describable Textures Dataset (DTD) is used for texture classification to evaluate few-shot learning performance.

## Relationships

### → DTD
- **Image classification** (behaviors tasks) — *measured_by*
  > We follow the image classification benchmark from Ilharco et al. (2023) and merge models finetuned on eight different datasets: Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), GTSRB Stallkamp et al. (2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016) and SVHN (Netzer et al., 2011). (§ 5.2)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)

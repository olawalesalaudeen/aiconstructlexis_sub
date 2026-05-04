# FGVC
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, FGVC is consistently described as a benchmark for Fine-Grained Visual Classification. Its most prevalent use is to evaluate model performance on specialized `Image classification` tasks, a function supported by multiple papers. A related paper also uses the benchmark to assess the broader capability of `Visual recognition`, and it is listed as a measure for `Data efficiency` in another. The benchmark is operationalized as a collection of datasets focused on specific domains. As one study notes, it comprises "5 specialized tasks" which, according to several sources, include datasets for bird recognition (CUB-Birds, NA-Birds), flower recognition (Oxford Flowers), dog recognition (Stanford Dogs), and car recognition (Stanford Cars).

## Sources

**[SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf)**
> Fine-Grained Visual Classification benchmark evaluating models on specialized image classification tasks such as bird, flower, dog, and car recognition.

## Relationships

### → FGVC
- **Image classification** (behaviors tasks) — *measured_by*
  > We evaluate on 3 major categories - Fine-Grained Visual Classification (FGVC): 5 specialized tasks using CUB-Birds (Van Horn et al., 2015), NA-Birds (Wah et al.), Oxford Flowers (Nilsback & Zisserman, 2008a), Stanford Dogs (Khosla et al., 2011), and Stanford Cars (Gebru et al., 2017). (Section 4.1)
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **Visual recognition** (constructs) — *measured_by*
  > We evaluate WeGeFT on the VTAB-1k benchmark (Zhai et al., 2019) and the fine-grained visual classification (FGVC) benchmark...
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)
- **Data efficiency** (constructs) — *measured_by*
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)

### Associated with
- **CUB-200-2011** (measurements)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
- **Oxford Flowers-102** (measurements)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
- **Stanford Dogs** (measurements)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)
- **Stanford Cars** (measurements)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)

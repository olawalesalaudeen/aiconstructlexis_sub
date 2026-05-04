# SVHN
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, the SVHN dataset is defined as consisting of "images of house numbers". A prevalent application of SVHN is for measuring `Image classification`, where it is frequently used alongside other datasets like Cars, DTD, and MNIST for fine-tuning and evaluation. In a different context, one paper uses SVHN to measure `Out-of-distribution detection`, where it serves as an external OOD dataset for a model trained on another corpus. This contrasts with another study that uses it for "in-distribution image generation and completion tasks". The dataset is also associated with measuring `Optical character recognition`, although the provided materials do not detail this use case.

## Sources

**[Can Generative AI Solve Your In-Context Learning Problem?  A Martingale Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/d90268f01ef06a55630b0588227adf4f-Paper-Conference.pdf)**
> The Street View House Numbers (SVHN) dataset consists of images of house numbers and is used in this paper for in-distribution image generation and completion tasks.

## Relationships

### → SVHN
- **Image classification** (behaviors tasks) — *measured_by*
  > We follow the image classification benchmark from Ilharco et al. (2023) and merge models finetuned on eight different datasets: Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), GTSRB Stallkamp et al. (2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016) and SVHN (Netzer et al., 2011). (§ 5.2)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Out-of-distribution detection** (behaviors tasks) — *measured_by*
  > The model is trained on CIFAR100-LT Krizhevsky & Hinton (2009) with an imbalance ratio of 100, and validated on external OOD datasets including SVHN Netzer et al. (2011), Places365 Zhou et al. (2017), LSUN Yu et al., iSUN Xu et al. and Texture Cimpoi et al. (2014). (Section 3)
  - [Adapting Multi-modal Large Language Model to Concept Drift From Pre-training Onwards](https://proceedings.iclr.cc/paper_files/paper/2025/file/e25d87b8a42ee3f0d5b3ef741ca13031-Paper-Conference.pdf)

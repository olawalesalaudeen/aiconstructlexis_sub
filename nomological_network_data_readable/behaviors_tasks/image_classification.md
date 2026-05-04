# Image classification
**Type:** Behavior  
**Referenced in:** 133 papers  
**Also known as:** Object classification, Visual object categorization, Cell type classification, Species identification, Few-shot classification, Visual classification, Image recognition, Zero-shot object recognition  

## State of the Field

Across the surveyed literature, image classification is most commonly described as the task of assigning a categorical label to an entire image from a predefined set of classes. This behavior is operationalized and measured using a wide range of benchmarks, with ImageNet-1k, CIFAR-10, and CIFAR-100 appearing as the most frequently used datasets for evaluation. A variety of other datasets are also employed, including DTD, VTAB-1k, EuroSAT, and Food101, as well as more specialized collections for fine-grained tasks like Stanford Cars and Oxford Flowers-102. A prevalent line of work defines the task specifically in the context of vision-language models, where classification is performed by comparing an image to text prompts, often in a zero-shot or few-shot setting. In this VLM-centric view, the goal is sometimes framed as finding "class prompts that maximize training accuracy without finetuning the model’s parameters" ("Understanding prompt engineering may not require rethinking generalization"). A smaller set of papers defines more specialized versions of the task, such as "species classification," "cell type classification" in microscopy, or "object classification" for industrial products. The task is frequently used to evaluate a range of model architectures, with Vision Transformers (ViT), CLIP, and ResNet being commonly mentioned. Overall, image classification serves as a recurring downstream task for assessing model performance, with one paper describing it as "the most common challenge for representation learning" ("Frozen Transformers in Language Models Are Effective Visual Encoder Layers").

## Sources

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)**
> Assigning a label to an image using a vision-language model by comparing it to text prompts, in a zero-shot setting.

**[UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Object classification")**
> Observably identifying and classifying objects within images across various categories.

**[DevBench: A multimodal developmental benchmark for language learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8d987b2981388c99c7eab6095d1d29fd-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Visual object categorization")**
> The task of discriminating between pairs of images, where looking time is used as a measure of perceived similarity or dissimilarity.

**[VLM4Bio: A Benchmark Dataset to Evaluate Pretrained Vision-Language Models for Trait Discovery from Biological Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/eced4a5fbc776e81b45e2f72447f0164-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Species classification")**
> The task of identifying and providing the correct scientific name (species class) for an organism shown in an image.

**[Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Cell type classification")**
> The task of identifying the specific type of cell present in a microscopy image.

**[INQUIRE: A Natural World Text-to-Image Retrieval Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4ad9c75f0d60ed75700f020adb3f705-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Species identification")**
> Retrieving images that match a query about a particular species or taxon.

**[Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf) (as "Few-shot classification")**
> An image classification task where the model must generalize to new classes given only a few examples of each.

**[Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf) (as "Visual classification")**
> Assigning an image to one of several classes using a prompt-conditioned multimodal model.

**[Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf) (as "Image recognition")**
> The observable task of classifying an image into one of a predefined set of categories.

**[Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf) (as "Zero-shot object recognition")**
> The task of classifying an image into one of several categories without having seen any training examples for those specific categories.

## Relationships

### Image classification →
- **ImageNet-1k** (measurements) — *measured_by*
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **CIFAR-100** (measurements) — *measured_by*
  > We compare MCNC on CIFAR-10 and CIFAR-100 (Krizhevsky et al., 2009) with both pruning methods as well as PRANC (Nooralinejad et al., 2023) and NOLA (Koohpayegani et al., 2024) under extreme compression rates. (Section 4.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **CIFAR-10** (measurements) — *measured_by*
  > We compare MCNC on CIFAR-10 and CIFAR-100 (Krizhevsky et al., 2009) with both pruning methods as well as PRANC (Nooralinejad et al., 2023) and NOLA (Koohpayegani et al., 2024) under extreme compression rates. (Section 4.1)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **DTD** (measurements) — *measured_by*
  > We follow the image classification benchmark from Ilharco et al. (2023) and merge models finetuned on eight different datasets: Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), GTSRB Stallkamp et al. (2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016) and SVHN (Netzer et al., 2011). (§ 5.2)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
- **Oxford Flowers-102** (measurements) — *measured_by*
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
- **Food101** (measurements) — *measured_by*
  > We evaluate our method on 12 image recognition datasets. We use the ... Food101 (Bossard et al., 2014)... (Section 4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **VTAB-1k** (measurements) — *measured_by*
  > We evaluate the finetuning performance of BOFT on the VTAB-1K benchmark [94], which has been extensively used to evaluate parameter-efficient transfer learning algorithms. VTAB-1K consists of 19 image classification tasks (Section 6.2).
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
- **EuroSAT** (measurements) — *measured_by*
  > We follow the image classification benchmark from Ilharco et al. (2023) and merge models finetuned on eight different datasets: Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), GTSRB Stallkamp et al. (2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016) and SVHN (Netzer et al., 2011). (§ 5.2)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
- **RESISC45** (measurements) — *measured_by*
  > vision classification with CIFAR100 (Krizhevsky et al., 2009), Food-101 (Bossard et al., 2014), Flowers-102 (Nilsback and Zisserman, 2008) and RESISC45 (Cheng et al., 2017)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
- **Sun397** (measurements) — *measured_by*
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **SVHN** (measurements) — *measured_by*
  > We follow the image classification benchmark from Ilharco et al. (2023) and merge models finetuned on eight different datasets: Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), GTSRB Stallkamp et al. (2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016) and SVHN (Netzer et al., 2011). (§ 5.2)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
- **Stanford Cars** (measurements) — *measured_by*
  > We evaluate our method on 12 image recognition datasets. We use the ... Stanford Cars (Krause et al., 2013)... (Section 4)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
- **Caltech101** (measurements) — *measured_by*
  > We evaluate our approach over 11 datasets, including ImageNet(Deng et al., 2009) and publicly available image recognition datasets used in GalLoP(Lafon et al., 2024): ...Caltech101(Li et al., 2017)... (Section 4.1)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
- **FGVC** (measurements) — *measured_by*
  > We evaluate on 3 major categories - Fine-Grained Visual Classification (FGVC): 5 specialized tasks using CUB-Birds (Van Horn et al., 2015), NA-Birds (Wah et al.), Oxford Flowers (Nilsback & Zisserman, 2008a), Stanford Dogs (Khosla et al., 2011), and Stanford Cars (Gebru et al., 2017). (Section 4.1)
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **CUB-200-2011** (measurements) — *measured_by*
  > We evaluate our method on 12 image recognition datasets. We use the CUB200-2011 (Wah et al., 2011) (fine-grained bird species)... (Section 4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
- **Tiny ImageNet** (measurements) — *measured_by*
  - [Efficient Unstructured Pruning of Mamba State-Space Models for Resource-Constrained Environments](https://aclanthology.org/2025.emnlp-main.563.pdf)
- **CelebA** (measurements) — *measured_by*
  > We use six datasets spanning different domains: GLUE for natural language understanding (Wang et al., 2019), DART for RDF-to-text generation (Nan et al., 2021), SAMSum (Gliwa et al., 2019) for summarization, Spider for text-to-SQL generation (Yu et al., 2018), and two vision datasets—CIFAR-10 (Krizhevsky et al., 2009) and CelebA (Liu et al., 2015), with the vision datasets processed by cropping, resizing, and flattening pixel values into space-separated numerical sentences.
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
- **MNIST** (measurements) — *measured_by*
  > “evaluations conducted on standard benchmark datasets, including Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2018), GTSRB (Stallkamp et al., 2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016), and SVHN (Netzer et al., 2011).”
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Oxford-IIIT Pets** (measurements) — *measured_by*
  - [A Grounded Typology of Word Classes](https://aclanthology.org/2025.naacl-long.522.pdf)
- **ImageNet-100** (measurements) — *measured_by*
  > TRAINING IMAGE CLASSIFIERS FROM SCRATCH ImageNet-100 on Vision Transformer Architectures. We begin by evaluating on training Vision Transformers from scratch on the ImageNet-100 dataset (Tian et al., 2020).
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
- **ImageNet-Sketch** (measurements) — *measured_by*
  > TIMM is evaluated on on three image datasets: ImageNet (Deng et al., 2009), ImageNet-Sketch (Sketch) (Wang et al., 2019), and ImageNet-Rendition (ImageNet-r) (Hendrycks et al., 2021).
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **Linear probing** (measurements) — *measured_by*
  > “We analyze this aspect using the protocol adopted by (Yuksekgonul et al., 2023; Zhang et al., 2024), which is based on linear probing the fine-tuned CLIP visual encoder on CIFAR10, CIFAR100 and ImageNet.”
  - [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf)
- **Food-101** (measurements) — *measured_by*
  > vision classification with CIFAR100 (Krizhevsky et al., 2009), Food-101 (Bossard et al., 2014), Flowers-102 (Nilsback and Zisserman, 2008) and RESISC45 (Cheng et al., 2017)
  - [Efficient Unstructured Pruning of Mamba State-Space Models for Resource-Constrained Environments](https://aclanthology.org/2025.emnlp-main.563.pdf)

### → Image classification
- **VTAB-1k** (measurements) — *measured_by*
  - [Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf)

### Associated with
- **In-context learning** (constructs)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
- **Visual understanding** (constructs)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)

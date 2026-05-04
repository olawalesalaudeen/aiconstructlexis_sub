# Oxford Flowers-102
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Flower-102, Flowers-102, Oxford Flowers, OxfordFlowers, Flowers102  

## State of the Field

Across the provided literature, Oxford Flowers-102 is consistently described as a benchmark for flower classification, appearing under various names such as Flowers-102, Flower-102, and Oxford Flowers. Its most prevalent application is to measure `Image classification` performance, a use case supported by multiple papers. A recurring theme is its role as a dataset for fine-grained classification of flower species, used to evaluate Fine-Grained Visual Recognition (FGVR) performance and studied alongside the related concept of `FGVC`. Beyond this general purpose, the benchmark is operationalized in diverse evaluation contexts, including the assessment of zero-shot classification, few-shot learning, and the effectiveness of class descriptions for visual categories. It is also employed to test the general downstream performance of models and to evaluate performance in federated learning settings, where one study uses it to "investigate the task of balancing personalization, generalization and privacy" ("Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models").

## Sources

**[Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf) (as "Flowers-102")**
> An image classification benchmark used for zero-shot classification.

**[Analyzing and Boosting the Power of Fine-Grained Visual Recognition for Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/dfa2f1555d46b553827af4e1557f3c9a-Paper-Conference.pdf) (as "Flower-102")**
> A fine-grained flower classification dataset used to evaluate FGVR performance.

**[Weighted Multi-Prompt Learning with Description-free Large Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/284e7ef68bf3d8fa42abf45a39f29f5e-Paper-Conference.pdf) (as "Oxford Flowers")**
> A dataset for fine-grained classification of flower species, used to evaluate few-shot learning performance.

**[Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf) (as "OxfordFlowers")**
> A visual classification benchmark used to evaluate personalized and generalized performance across clients.

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf) (as "Flowers102")**
> Flowers102, a flower classification benchmark used to evaluate class descriptions for everyday visual categories.

## Relationships

### → Oxford Flowers-102
- **Image classification** (behaviors tasks) — *measured_by*
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)

### Associated with
- **FGVC** (measurements)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)

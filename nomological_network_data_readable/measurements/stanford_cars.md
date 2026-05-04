# Stanford Cars
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** Stanford-Cars, Cars  

## State of the Field

Across the provided literature, Stanford Cars is consistently described as a benchmark for image classification, with a prevailing emphasis on its use for fine-grained tasks. The most common definition frames it as a tool to assess "fine-grained visual discrimination," specifically for car models, with one paper noting it contains 196 classes. Operationally, Stanford Cars is used to measure model capabilities, such as testing the "downstream performance" of architectures like DeiT-B, and to evaluate few-shot learning. Its application is often situated within the broader context of fine-grained visual classification (FGVC) evaluation suites. The dataset is also used alongside other image classification benchmarks, including CUB, Flowers102, and the CIFAR datasets, to evaluate model performance.

## Sources

**[Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)**
> Stanford Cars, a car model classification benchmark used to assess fine-grained visual discrimination.

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf) (as "Stanford-Cars")**
> Stanford-Cars is an image classification benchmark used here to test downstream performance of DeiT-B.

**[Portable Reward Tuning: Towards Reusable Fine-Tuning across Different Pretrained Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chijiwa25a/chijiwa25a.pdf) (as "Cars")**
> The Stanford Cars dataset, a benchmark for fine-grained image classification consisting of 196 classes of cars.

## Relationships

### → Stanford Cars
- **Image classification** (behaviors tasks) — *measured_by*
  > We evaluate our method on 12 image recognition datasets. We use the ... Stanford Cars (Krause et al., 2013)... (Section 4)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)

### Associated with
- **FGVC** (measurements)
  - [Revisiting Prefix-tuning: Statistical Benefits of Reparameterization among Prompts](https://proceedings.iclr.cc/paper_files/paper/2025/file/760dff0f9c0e9ed4d7e22918c73351d4-Paper-Conference.pdf)

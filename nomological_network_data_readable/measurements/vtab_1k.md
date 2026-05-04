# VTAB-1k
**Type:** Measurement  
**Referenced in:** 10 papers  
**Also known as:** VTAB-1K  

## State of the Field

Across the provided literature, VTAB-1k is consistently defined as the Visual Task Adaptation Benchmark, a suite of 19 diverse visual tasks. It is predominantly used to evaluate the fine-tuning and transfer learning capabilities of vision models, particularly for the behavior of `Image classification`. As one paper notes, it has been "extensively used to evaluate parameter-efficient transfer learning algorithms." A smaller number of sources also report its use for measuring the constructs of `Generalization` and `Visual recognition`. The benchmark's 19 tasks are consistently organized into three domains: Natural, Specialized, and Structured. One source specifies this breakdown as seven natural, four specialized, and eight structured datasets, while another provides examples such as "remote sensing and medical images" for specialized tasks and "depth and orientation prediction" for structured ones. The "-1k" in its name is noted by one source to refer to the 1000 training examples provided for each task. In practice, papers report using VTAB-1k to evaluate pre-trained models like ViT-B/16.

## Sources

**[Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf) (as "VTAB-1K")**
> A diverse vision benchmark consisting of 19 image classification tasks across natural, specialized, and structured domains for evaluating transfer learning methods.

**[Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)**
> The Visual Task Adaptation Benchmark (VTAB-1k) is a suite of 19 diverse visual tasks across Natural, Specialized, and Structured domains, used to evaluate the fine-tuning performance of vision models.

## Relationships

### VTAB-1k →
- **Image classification** (behaviors tasks) — *measured_by*
  - [Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf)

### → VTAB-1k
- **Image classification** (behaviors tasks) — *measured_by*
  > We evaluate the finetuning performance of BOFT on the VTAB-1K benchmark [94], which has been extensively used to evaluate parameter-efficient transfer learning algorithms. VTAB-1K consists of 19 image classification tasks (Section 6.2).
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We select a pre-trained ViT/16 (Dosovitskiy et al., 2020) as the vision model and evaluate on VTAB-1k (Zhai et al., 2019) benchmark, which contains 19 visual tasks with three domains: Natural, Specialized, and Structured. (Section 4.4)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **Visual recognition** (constructs) — *measured_by*
  > We evaluate WeGeFT on the VTAB-1k benchmark (Zhai et al., 2019) and the fine-grained visual classification (FGVC) benchmark...
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)

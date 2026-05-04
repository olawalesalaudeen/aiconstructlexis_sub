# VizWiz
**Type:** Measurement  
**Referenced in:** 69 papers  
**Also known as:** Vizwiz, VisWiz  

## State of the Field

Across the provided literature, VizWiz is consistently characterized as a benchmark or dataset for visual question answering (VQA). Its most frequently cited characteristic, mentioned across all definitions, is that it consists of images and questions originating from people who are blind or visually impaired. Consequently, papers widely use VizWiz to measure a model's ability to perform VQA, as well as the broader capabilities of visual and multimodal understanding. Several sources highlight the challenging nature of the dataset, which features "real-world, uncurated images" that are often described as "low-quality" or "visually degraded," making it a common tool for assessing model robustness in real-world scenarios. The benchmark is employed in various evaluation settings, including zero-shot performance and few-shot generalization, with one study noting its utility for testing generalization on unseen data "with a few exemplars" ('MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning'). A smaller set of studies also uses VizWiz to specifically assess "general visual reasoning" or "perception capability." Overall, the prevailing use of VizWiz is as a challenging VQA benchmark that evaluates a model's capacity to handle imperfect, real-world visual inputs.

## Sources

**[DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf)**
> A visual question answering dataset originating from questions asked by people who are blind, often featuring real-world, uncurated images.

**[Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf) (as "Vizwiz")**
> A benchmark consisting of visual questions asked by people who are blind, designed to evaluate a model's ability to answer real-world visual queries.

**[Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf) (as "VisWiz")**
> VisWiz is a visual question answering benchmark based on questions from blind users.

## Relationships

### → VizWiz
- **Visual question answering** (behaviors tasks) — *measured_by*
  > ...general visual question answering (VQA) on VQAv2 (Goyal et al., 2019), OKVQA (Marino et al., 2019), VizWiz (Gurari et al., 2018)... (Section 4.1)
  - [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://proceedings.iclr.cc/paper_files/paper/2024/file/e1762b64958760f7bfabe3a7062d007f-Paper-Conference.pdf)
- **Multimodal understanding** (constructs) — *measured_by*
  > “general visual question answering (VQA) on VQAv2 (Goyal et al., 2019), OKVQA (Marino et al., 2019), VizWiz (Gurari et al., 2018)”
  - [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf)
- **Visual understanding** (constructs) — *measured_by*
  > “we evaluate our methods on seven vision datasets, spanning both image classification tasks (CIFAR-10, CIFAR-100, Food101) and visual question-answering tasks (COCO-Color, COCO-Number, VQAv2 and VizWiz)”
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **In-context learning** (constructs) — *measured_by*
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [Leveraging Visual Tokens for Extended Text Contexts in Multi-Modal Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/19f10adb6749b0c9f1ff7610bd01d44d-Paper-Conference.pdf)
- **Fine-grained visual understanding** (constructs) — *measured_by*
  - [Matryoshka Query Transformer for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/59c147c7d4fdb732daea3064eab949bf-Paper-Conference.pdf)
- **Perception** (constructs) — *measured_by*
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual perception** (constructs) — *measured_by*
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Visual reasoning** (constructs) — *measured_by*
  > VQAv2 Goyal et al. (2017) and VizWiz Gurari et al. (2018) test general visual reasoning
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
- **Visual instruction following** (behaviors tasks) — *measured_by*
  - [MMEvalPro: Calibrating Multimodal Benchmarks Towards Trustworthy and Efficient Evaluation](https://aclanthology.org/2025.naacl-long.248.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)

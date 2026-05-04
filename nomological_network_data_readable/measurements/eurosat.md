# EuroSAT
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, EuroSAT is consistently characterized as a benchmark or dataset for satellite imagery classification. Its most prevalent application is to measure `Image classification` performance, often appearing alongside other datasets like SVHN, DTD, and RESISC45 in evaluation suites for fine-tuning models, with accuracy reported as an evaluation metric. While the dominant framing is general performance evaluation, some papers apply EuroSAT to more specific contexts. For example, one study uses it to assess few-shot learning performance, and another employs it to evaluate descriptions for rare or abstract visual concepts within satellite imagery.

## Sources

**[Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf)**
> A satellite imagery classification benchmark used to evaluate image classification performance.

## Relationships

### → EuroSAT
- **Image classification** (behaviors tasks) — *measured_by*
  > We follow the image classification benchmark from Ilharco et al. (2023) and merge models finetuned on eight different datasets: Cars (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), GTSRB Stallkamp et al. (2011), MNIST (LeCun, 1998), RESISC45 (Cheng et al., 2017), SUN397 (Xiao et al., 2016) and SVHN (Netzer et al., 2011). (§ 5.2)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)

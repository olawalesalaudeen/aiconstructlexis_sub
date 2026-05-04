# CelebA
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided sources, CelebA is consistently described as a large-scale face attributes dataset, with one paper specifying it contains over 200,000 celebrity images with 40 attribute annotations each. The dataset is used to evaluate several model properties. A recurring application is the assessment of fairness; for instance, one study uses it to evaluate fairness in predicting the 'Blond Hair' attribute relative to the 'Male' sensitive attribute. Another common use is to test model robustness, where CelebA serves as a benchmark with known "distribution shifts and spurious attribute correlations." The dataset is explicitly used to measure the behavior of `Image classification`, also referred to as facial attribute recognition. In one such use case, the images are processed by "cropping, resizing, and flattening pixel values into space-separated numerical sentences" for use in language models. The dataset is also listed as a measure for `Image reconstruction`, though no further details on this application are provided in the source materials.

## Sources

**[Debiasing Attention Mechanism in Transformer without Demographics](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f5337a39b1f6d670aad9d32debc0e5d-Paper-Conference.pdf)**
> The Celeb-A dataset, a large-scale face attributes dataset used here to evaluate fairness in predicting the 'Blond Hair' attribute with respect to the 'Male' sensitive attribute.

## Relationships

### → CelebA
- **Image classification** (behaviors tasks) — *measured_by*
  > We use six datasets spanning different domains: GLUE for natural language understanding (Wang et al., 2019), DART for RDF-to-text generation (Nan et al., 2021), SAMSum (Gliwa et al., 2019) for summarization, Spider for text-to-SQL generation (Yu et al., 2018), and two vision datasets—CIFAR-10 (Krizhevsky et al., 2009) and CelebA (Liu et al., 2015), with the vision datasets processed by cropping, resizing, and flattening pixel values into space-separated numerical sentences.
  - [Parameter-Efficient Fine-Tuning of State Space Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/galim25a/galim25a.pdf)
- **Image reconstruction** (behaviors tasks) — *measured_by*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)

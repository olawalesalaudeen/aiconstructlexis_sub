# ADE20K
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Ade20k  

## State of the Field

Across the provided literature, ADE20K is consistently framed as a benchmark or dataset for evaluation purposes. Its most prevalent use is to measure model performance on `Semantic segmentation`, a task for which multiple papers report using it. One paper specifically characterizes it as a "large-scale scene parsing benchmark" for assessing "open-vocabulary semantic segmentation" and notes its diverse object and stuff classes. The A-150 version of the benchmark is also explicitly mentioned. In addition to semantic segmentation, it is also used to measure `Image segmentation`. A less common framing describes it as a potential alternative dataset for a "patch-level probing benchmark," as noted in one paper which states, "we can also use other datasets like Ade20k".

## Sources

**[Text4Seg: Reimagining Image Segmentation as Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/04d8c25cbf0d5e1b70d64e672ac92637-Paper-Conference.pdf)**
> A large-scale scene parsing benchmark (A-150) used for evaluating open-vocabulary semantic segmentation with a diverse set of objects and stuff classes.

**[Locality Alignment Improves Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce6326ac4794bb04d5eb16f597446baf-Paper-Conference.pdf) (as "Ade20k")**
> A semantic segmentation dataset mentioned as an alternative dataset for the patch-level probing benchmark.

## Relationships

### → ADE20K
- **Semantic segmentation** (behaviors tasks) — *measured_by*
  > We evaluate the model’s performance on ADE20K (A-150) (Zhou et al., 2019), PASCAL Context 59 (PC-59) (Mottaghi et al., 2014), and PASCAL VOC 20 (PAS-20) (Everingham, 2009) datasets, using mIoU as the evaluation metric. (Section 4.5)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Image segmentation** (behaviors tasks) — *measured_by*
  - [Transformer Meets Twicing: Harnessing Unattended Residual Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/90cdfb6ac8d9f96bdf0ce92f5f05c391-Paper-Conference.pdf)

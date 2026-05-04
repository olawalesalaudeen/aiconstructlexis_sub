# ImageNet-Sketch
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** ImageNetSketch  

## State of the Field

Across the provided literature, ImageNet-Sketch is consistently described as a dataset or benchmark used to evaluate model performance on out-of-distribution (OOD) data. The definitions agree that it contains "sketch-like images," with one source specifying they are derived from ImageNet. Papers use this instrument to assess constructs like model generalization and model robustness. Specifically, it is used to measure performance on the task of image classification. The framing as an "out-of-distribution benchmark" is a common thread in its description, and its operationalization involves evaluating models on it alongside other image datasets, as one paper notes.

## Sources

**[LiNeS: Post-training Layer Scaling Prevents Forgetting and Enhances Model Merging](https://proceedings.iclr.cc/paper_files/paper/2025/file/43ae0b566b802b2d00e525b672794b82-Paper-Conference.pdf) (as "ImageNetSketch")**
> An out-of-distribution benchmark for ImageNet consisting of sketch-like images to test model generalization.

**[SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)**
> A dataset containing sketch-like images derived from ImageNet, used to evaluate model robustness and generalization for image classification.

## Relationships

### → ImageNet-Sketch
- **Image classification** (behaviors tasks) — *measured_by*
  > TIMM is evaluated on on three image datasets: ImageNet (Deng et al., 2009), ImageNet-Sketch (Sketch) (Wang et al., 2019), and ImageNet-Rendition (ImageNet-r) (Hendrycks et al., 2021).
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)

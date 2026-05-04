# Image reconstruction
**Type:** Behavior  
**Referenced in:** 6 papers  

## State of the Field

Image reconstruction is predominantly defined as the task of encoding an image into a compressed representation and then decoding it back to its original form to measure fidelity. A related framing describes it as producing reconstructed versions of input images or their latent visual representations, as one study aims to "supervise visual outputs by reconstruction" ("Reconstructive Visual Instruction Tuning"). This process can also involve recovering "clean fine-grained tokens... from noisy tokens" ("Reconstructive Visual Instruction Tuning"). This behavior is operationalized and evaluated using several datasets, including MS-COCO, CUB-200-2011, and CelebA. The literature suggests that performing image reconstruction can influence other model capabilities. It is reported to improve representation quality and is linked to enhanced fine-grained understanding. One paper specifically argues that this approach encourages models to maintain low-level details, thereby "enhancing their fine-grained comprehension abilities and reducing hallucinations" ("Reconstructive Visual Instruction Tuning").

## Sources

**[LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)**
> The task of encoding an image into a compressed representation and then decoding it back to its original form to measure fidelity.

## Relationships

### Image reconstruction →
- **CelebA** (measurements) — *measured_by*
  - [Graph-based Unsupervised Disentangled Representation Learning via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/bac4d92b3f6decfe47eab9a5893dd1f6-Paper-Conference.pdf)
- **CUB-200-2011** (measurements) — *measured_by*
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **MS-COCO** (measurements) — *measured_by*
  - [LG-VQ: Language-Guided Codebook Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Fine-grained understanding** (constructs) — *causes*
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks) — *causes*
  > This approach encourages LMMs to maintain low-level details, thereby enhancing their fine-grained comprehension abilities and reducing hallucinations. (Section 1)
  - [Reconstructive Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/259a5df46308d60f8454bd4adcc3b462-Paper-Conference.pdf)
- **Representation quality** (constructs) — *causes*
  - [DS-VLM: Diffusion Supervision Vision Language Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25p/sun25p.pdf)

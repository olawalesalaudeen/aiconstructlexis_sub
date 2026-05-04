# Image restoration
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Image colorization, Image dehazing, Low-light enhancement, Snow removal, Super-resolution, Blind restoration, Haze removal, Noise removal, Rain removal, Shadow removal, Low-light image enhancement  

## State of the Field

Across the provided literature, image restoration is consistently framed as the process of recovering high-quality images from degraded observations, with one paper describing it as a "classical research area in computer vision" ("RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models"). This behavior is operationalized through a variety of specific sub-tasks, with low-light enhancement, snow removal, watermark removal, and haze/dehazing being mentioned across multiple sources. Other documented restoration tasks include colorization, super-resolution, and the removal of noise, rain, or shadows, all aimed at improving visual quality by, for example, "enhancing brightness, and reducing noise" ("I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing"). A common approach described in the data involves guiding the restoration process with textual instructions, such as using the prompt "Improve the visibility of the image by reducing haze" for dehazing ("PromptFix: You Prompt and We Fix the Photo"). In contrast, a variant called "blind restoration" is also described, which restores images "without the need to provide instructions" by relying on an automatically generated analysis of the image ("PromptFix: You Prompt and We Fix the Photo"). The provided research also connects image restoration with `Zero-shot learning`, `Generalization`, `Safety`, `Object detection`, and `Semantic segmentation`.

## Sources

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Image colorization")**
> The task of adding color to a grayscale image based on a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Image dehazing")**
> The task of removing haze or fog from an image to improve visibility, guided by a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Low-light enhancement")**
> The task of improving the brightness and visibility of an image taken in low-light conditions, guided by a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Snow removal")**
> The task of removing snow from an image, guided by a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Super-resolution")**
> The task of increasing the resolution and detail of a low-resolution image, guided by a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Watermark removal")**
> The task of removing a visible watermark from an image, guided by a textual instruction.

**[PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf) (as "Blind restoration")**
> The task of restoring a degraded image without explicit instructions specifying the type of degradation, instead relying on an automatically generated analysis of the image.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Haze removal")**
> The observable task of eliminating or reducing atmospheric haze or fog from an image to improve visibility and restore color.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Noise removal")**
> The observable task of reducing or eliminating unwanted visual noise from an image.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Rain removal")**
> The observable task of eliminating or reducing the visual effects of raindrops or rain streaks from an image.

**[I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf) (as "Shadow removal")**
> The observable task of reducing or eliminating unwanted shadows from an image to enhance visibility.

**[RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf) (as "Low-light image enhancement")**
> The task of improving the brightness and visibility of an image taken in low-light conditions.

**[RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c78f639424b8d89ceb4f2efbb4dfe4f4-Paper-Conference.pdf)**
> The process of recovering high-quality images from degraded observations by applying restoration algorithms.

## Relationships

### Associated with
- **Zero-shot learning** (constructs)
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Generalization** (constructs)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Robustness** (constructs)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Object detection** (behaviors tasks)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)
- **Semantic segmentation** (behaviors tasks)
  - [DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation](https://proceedings.neurips.cc/paper_files/paper/2024/file/6452474601429509f3035dc81c233226-Paper-Conference.pdf)

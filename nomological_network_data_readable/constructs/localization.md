# Localization
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Localization capability, Localization ability  

## State of the Field

Across the provided literature, Localization is consistently defined as a model's latent ability or capacity to accurately identify the spatial position and boundaries of objects or instances within visual content. This construct is operationalized and evaluated through specific tasks and benchmarks. For instance, one paper notes that the Referring Expression Comprehension (REC) task "serves as a critical benchmark to evaluate the localization capabilities" and uses accuracy metrics at various IoU thresholds for assessment. The MMLongBench-Doc benchmark is also reported as a tool for measuring localization. The concept is frequently discussed in the context of model limitations, with some work observing that the localization ability of VLMs can be "less accurate" or "weaker" than that of specialized perception models. This "localization limitation" is presented as a problem to be addressed. Finally, the construct of Localization is studied in relation to the task of Object detection.

## Sources

**[A Large-Scale Human-Centric Benchmark for Referring Expression Comprehension in the LMM Era](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f0cd0305f7741659304f5325f3bf6d-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Localization capability")**
> The latent ability of a model to accurately identify and specify the position of target instances within visual content.

**[Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf) (as "Localization ability")**
> The model's latent capacity to accurately determine the spatial position and boundaries of objects within an image.

## Relationships

### Localization →
- **MMLongBench-Doc** (measurements) — *measured_by*
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Object detection** (behaviors tasks)
  - [Contrastive Localized Language-Image Pre-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ah/chen25ah.pdf)

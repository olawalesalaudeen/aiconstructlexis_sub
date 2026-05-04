# Open-vocabulary object detection
**Type:** Behavior  
**Referenced in:** 5 papers  
**Also known as:** Open-ended object detection, Open-world object detection  

## State of the Field

Across the surveyed literature, open-vocabulary object detection is a behavior centered on identifying objects from categories not seen during training. While this is the common thread, the provided papers offer distinct framings. The most specific definition, termed 'open-vocabulary object detection,' requires using textual descriptions to detect these novel objects. A related framing, 'open-ended object detection,' is described as a more general task of discovering unseen objects without any predefined categories provided at inference. A third variant, 'open-world object detection,' adds a temporal learning component, defining the task as detecting both known and novel objects and then having the 'ability to incrementally learn the new categories over time' (UMB: Understanding Model Behavior for Open-World Object Detection). This behavior is situated within the broader context of object detection. To operationalize this task, the Visual Genome dataset is used as a measurement instrument.

## Sources

**[FineCLIP: Self-distilled Region-based CLIP for Better Fine-grained Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/3122aaa22b2fe83f9cead1a696f65ceb-Paper-Conference.pdf)**
> Detecting objects in an image belonging to categories not seen during training, using textual descriptions.

**[Training-Free Open-Ended Object Detection and Segmentation via Attention as Prompts](https://proceedings.neurips.cc/paper_files/paper/2024/file/80f48ffa8022773973a4a5cec7cce19c-Paper-Conference.pdf) (as "Open-ended object detection")**
> The task of identifying and locating objects in an image without being provided with a predefined set of object categories during inference.

**[UMB: Understanding Model Behavior for Open-World Object Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/8766fbc68e1ed1cdef712ce273e0a363-Paper-Conference.pdf) (as "Open-world object detection")**
> The task of detecting objects from both known, annotated categories and identifying objects from novel, unknown categories in an image, with the ability to incrementally learn the new categories over time.

## Relationships

### Open-vocabulary object detection →
- **Visual Genome** (measurements) — *measured_by*
  - [FlexCap: Describe Anything in Images in Controllable Detail](https://proceedings.neurips.cc/paper_files/paper/2024/file/c91b6f7e0152b7a95ee777e987fe811e-Paper-Conference.pdf)

### Associated with
- **Object detection** (behaviors tasks)
  - [Open-Det: An Efficient Learning Framework for Open-Ended Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25h/cao25h.pdf)

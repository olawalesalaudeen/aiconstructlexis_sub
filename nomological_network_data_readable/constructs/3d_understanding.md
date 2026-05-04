# 3D understanding
**Type:** Construct  
**Referenced in:** 8 papers  
**Also known as:** 3D awareness, Object-level 3D awareness, 3D-related reasoning, 3D scene understanding  

## State of the Field

Across the provided literature, "3D understanding" is most commonly framed as a model's ability to comprehend and reason about objects, their attributes, and their spatial relationships within a three-dimensional environment. Definitions vary slightly in scope, with some focusing on inferring 3D structure from 2D inputs, while others, using the term "3D-related reasoning," emphasize reasoning about properties like pose and distance. A more specific line of work treats this concept as "object-level 3D awareness," defined as the degree to which a model's "internal representations encode discriminative information about the 3D structure and viewpoint of objects" (ImageNet3D: Towards General-Purpose Object-Level 3D Understanding). This latent trait is operationalized by evaluating a model's frozen feature representations on a 3D viewpoint classification task. More broadly, the construct of 3D understanding is measured using benchmarks such as ScanQA and SQA3D. The concept is studied in relation to Visual grounding and 3D question answering, and is described as a prerequisite for higher-level tasks like motion planning.

## Sources

**[SpatialPIN: Enhancing Spatial Reasoning Capabilities of Vision-Language Models through Prompting and Interacting 3D Priors](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f2257d2b291b8d7e712c70b67e09412-Paper-Conference.pdf)**
> The model's ability to infer and represent the three-dimensional structure, layout, and properties of a scene and its objects from two-dimensional inputs.

**[$\textit{Bifr\"ost}$: 3D-Aware Image Compositing with Language Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea011cd13bcdf7ca38506c844dccfee8-Paper-Conference.pdf) (as "3D awareness")**
> The latent capacity to account for depth and three-dimensional geometry when placing or compositing objects into a scene.

**[ImageNet3D: Towards General-Purpose Object-Level 3D Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae51515c1cfecf544963a527260f94e9-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Object-level 3D awareness")**
> The degree to which a model's internal representations encode discriminative information about the 3D structure and viewpoint of objects.

**[ImageNet3D: Towards General-Purpose Object-Level 3D Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae51515c1cfecf544963a527260f94e9-Paper-Datasets_and_Benchmarks_Track.pdf) (as "3D-related reasoning")**
> The cognitive ability of a model, particularly an LLM, to reason about object properties like pose, distance, and spatial relationships using integrated 3D information.

**[Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf) (as "3D scene understanding")**
> The ability to comprehend and reason about the objects, their attributes, and their spatial relationships within a three-dimensional environment.

## Relationships

### 3D understanding →
- **ScanQA** (measurements) — *measured_by*
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **SQA3D** (measurements) — *measured_by*
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)

### Associated with
- **Visual grounding** (constructs)
  - [Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers](https://proceedings.neurips.cc/paper_files/paper/2024/file/cebbd24f1e50bcb63d015611fe0fe767-Paper-Conference.pdf)
- **3D question answering** (behaviors tasks)
  - [3D Question Answering via only 2D Vision-Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ef/wang25ef.pdf)

# Scene graph generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Scene graph generation is characterized in the provided literature as a task for creating a structured representation of a scene, though the input modality varies across papers. The most prevalent definition describes it as converting a natural language caption into a graph of objects, their attributes, and their relationships. In this context, one paper notes the process is "Inspired by SPICE" and operationalizes the output as a graph `{Oi n, Ri n, Ai n}` to measure consistency between captions. A different framing defines the task as producing a structured representation directly from an image, with an emphasis on capturing "the essential spatial relation between visual concepts." This approach is operationalized using specific tools, such as a "robust SGG engine" called HiKER-SGG. In both documented uses, the output is a structured graph that represents entities and their relations within a scene.

## Sources

**[Learnability Matters: Active Learning for Video Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/43069caa6776eac8bca4bfd74d4a476d-Paper-Conference.pdf)**
> The task of converting a natural language caption into a structured representation of objects, their attributes, and their relationships.

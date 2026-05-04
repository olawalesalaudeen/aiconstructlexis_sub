# Multi-image visual question answering
**Type:** Behavior  
**Referenced in:** 3 papers  
**Also known as:** Multi-image question answering  

## State of the Field

Multi-image visual question answering is consistently defined across the provided sources as the task of answering a question by reasoning over the content of multiple images. The definitions are highly aligned, framing the behavior as requiring a model to process information from two or more visual inputs, with one paper specifying the need to understand both the "content and relationships" of the images ("MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs"). This behavior is operationalized through benchmarks that present models with a question alongside a set of images. For instance, one source notes that questions can involve anywhere from 2 to 20 images. The task can also be situated within a broader conversational context, such as in dialogues that combine both single-image and multi-image questions. The central challenge presented by this task is the requirement for models to "reason over multiple images for VQA" ("JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images").

## Sources

**[MMDU: A Multi-Turn Multi-Image Dialog Understanding Benchmark and Instruction-Tuning Dataset for LVLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/1057053100de064a44286239724f7865-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Multi-image question answering")**
> Answering a user's question based on the content and relationships of two or more provided images.

**[JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/734abb86d3caa949f44da8a093717f61-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The task of answering a question by reasoning over the content of multiple provided images.

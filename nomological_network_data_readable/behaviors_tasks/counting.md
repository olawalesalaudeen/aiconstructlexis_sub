# Counting
**Type:** Behavior  
**Referenced in:** 22 papers  
**Also known as:** Object count, Action count, Vertex count, Hyperedge count, Counting ability  

## State of the Field

Across the surveyed literature, the most prevalent usage of "Counting" refers to the behavior of reporting the number of objects or shapes within a visual medium. This is frequently defined as the task to "accurately count the number of objects in the image" (neurips24, Understanding the Limits...). This concept is extended to other modalities, including counting object instances or action occurrences in videos, determining the occurrences of sounds in audio, and enumerating items in a sequence. A distinct application involves counting abstract elements like vertices and hyperedges in hypergraphs. While most papers treat counting as an observable task, a few frame it as a latent "cognitive capability" (neurips24, VisMin) that models may lack. This behavior is operationalized and measured using specific benchmarks; for example, MUIRBENCH is used to "evaluate the ability of models to count the number of specific objects across multiple images" (iclr25, MuirBench), and Video-MME is used for video-based counting. Some evaluation approaches also include questions where the correct answer is zero to test for hallucination, a concept that is also studied in relation to counting.

## Sources

**[Understanding the Limits of Vision Language Models Through the Lens of the Binding Problem](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdcc6d47c1627350014a3076112ab824-Paper-Conference.pdf)**
> Reporting the number of objects or shapes visible in an image.

**[Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf) (as "Object count")**
> Counting how many instances of an object appear in a video.

**[Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf) (as "Action count")**
> Counting how many times an action occurs in a video.

**[Beyond Graphs: Can Large Language Models Comprehend Hypergraphs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/690fc970014e4ecebc8068bbc03b35e6-Paper-Conference.pdf) (as "Vertex count")**
> The task of counting the total number of vertices in a given hypergraph.

**[Beyond Graphs: Can Large Language Models Comprehend Hypergraphs?](https://proceedings.iclr.cc/paper_files/paper/2025/file/690fc970014e4ecebc8068bbc03b35e6-Paper-Conference.pdf) (as "Hyperedge count")**
> The task of counting the total number of hyperedges in a given hypergraph.

**[Safety Alignment via Constrained Knowledge Unlearning](https://aclanthology.org/2025.acl-long.1241.pdf) (as "Object counting")**
> The observable task of determining the number of instances of a specific object present in an image.

**[VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf) (as "Counting ability")**
> The cognitive capability to accurately determine the number of objects in an image as specified by a caption.

## Relationships

### Counting →
- **Video-MME** (measurements) — *measured_by*
  > Leveraging the question types defined in the Video-MME benchmark, we conduct a comparative analysis among three methods... across six distinct categories of questions. (Section 4.2, RQ5)
  - [Frame-Voyager: Learning to Query Frames for Video Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d18d208fa9c333483e5724ade7beff0f-Paper-Conference.pdf)
- **MUIRBENCH** (measurements) — *measured_by*
  > [COUNTING] aims to evaluate the ability of models to count the number of specific objects across multiple images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [MMDT: Decoding the Trustworthiness and Safety of Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bcfb525c8f8f07ae10a93d0b2a40e00-Paper-Conference.pdf)

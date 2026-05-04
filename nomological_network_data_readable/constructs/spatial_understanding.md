# Spatial understanding
**Type:** Construct  
**Referenced in:** 24 papers  
**Also known as:** Spatial awareness, Spatial comprehension, Spatial structure understanding  

## State of the Field

Across the provided literature, the prevailing usage of spatial understanding refers to the ability to perceive and reason about the spatial arrangement, positions, and relationships of objects within a visual scene. This core definition is shared across multiple papers, with "spatial awareness" often used as a synonym. However, a smaller set of studies applies the concept to more specialized domains; for instance, one paper defines it as understanding the topological properties of road networks, while another frames it as reasoning about "spatially distributed findings" in medical images. A single paper also extends the concept to non-visual contexts, such as understanding positional sequences in structured data. The construct is operationalized and measured using the MM-Vet benchmark. It is also frequently assessed within broader behaviors like Video question answering, through questions about "the position of items and their relation to other items," and is considered a component of Embodied question answering and Medical visual reasoning. The literature also positions spatial understanding in relation to other constructs like Faithfulness and Referring expression understanding.

## Sources

**[Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Spatial awareness")**
> The ability to perceive and reason about the spatial arrangement and relationships of objects in a visual scene.

**[DenseFusion-1M: Merging Vision Experts for Comprehensive Multimodal Perception](https://proceedings.neurips.cc/paper_files/paper/2024/file/20ffc2b42c7de4a1960cfdadf305bbe2-Paper-Datasets_and_Benchmarks_Track.pdf)**
> The ability to perceive and reason about the spatial arrangement, positions, and relationships of objects within an image.

**[SMART: Scalable Multi-agent Real-time Motion Generation via Next-token Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/cef5c8dec67597b854f0162ad76d92d2-Paper-Conference.pdf) (as "Spatial comprehension")**
> The latent ability to understand and model the structural and topological properties of a road network, such as the connectivity and continuity between road segments.

**[OMS: On-the-fly, Multi-Objective, Self-Reflective Ad Keyword Generation viaLLMAgent](https://aclanthology.org/2025.emnlp-main.939.pdf) (as "Spatial structure understanding")**
> The ability to reason about spatially distributed findings and structural relationships within medical images.

## Relationships

### Spatial understanding →
- **MM-Vet** (measurements) — *measured_by*
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)

### Associated with
- **Grounding** (constructs)
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
- **Video question answering** (behaviors tasks)
  > We annotate 98 videos and provide 882 question-answer pairs that target three types of questions: 1) descriptive questions regarding the attributes of the objects (colour, shape, number), 2) spatial Understanding about the position of items and their relation to other items, and 3) adversarial questions about items not present in the video.
  - [Dehumanizing Machines: Mitigating Anthropomorphic Behaviors in Text Generation Systems](https://aclanthology.org/2025.acl-long.1260.pdf)
- **Embodied question answering** (behaviors tasks)
  > complex embodied tasks like Embodied Question Answering (EQA) where nuanced evaluation of agents’ spatial, temporal, and logical understanding is critical yet not considered by generic approaches. (Abstract)
  - [Parallel Continuous Chain-of-Thought with Jacobi Iteration](https://aclanthology.org/2025.emnlp-main.48.pdf)
- **Medical visual reasoning** (constructs)
  > Med-VRAgent achieved top performance across several medical multimodal benchmark datasets, demonstrating proficiency in image-text alignment, spatial structure understanding, and lesion recognition. (Section 6)
  - [OMS: On-the-fly, Multi-Objective, Self-Reflective Ad Keyword Generation viaLLMAgent](https://aclanthology.org/2025.emnlp-main.939.pdf)

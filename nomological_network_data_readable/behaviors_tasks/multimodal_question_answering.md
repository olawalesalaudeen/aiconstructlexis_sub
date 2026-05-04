# Multimodal question answering
**Type:** Behavior  
**Referenced in:** 15 papers  
**Also known as:** Multi-modal question answering  

## State of the Field

Multimodal question answering is most commonly defined as the task of answering questions about inputs from various data modalities. The prevailing definition is broad, encompassing image, video, audio, depth, and point cloud data, though many specific examples in the provided sources focus on the joint understanding of text and images. The task is framed as requiring the "processing and integrating" of information from these sources, with some work noting that it "often requires reasoning over visual, auditory, and sensor inputs to extract the most relevant evidence." To operationalize and measure this behavior, researchers use instruments such as the Visual7W benchmark. The expected output from the model varies across studies, including multiple-choice selections, short answers like a "single word or phrase," or fully generated natural language answers. The concept is also studied in relation to Information retrieval. As one paper notes, the task can be formulated as QA specifically so that "multimodal capabilities can be evaluated directly on the downstream task."

## Sources

**[LLMs Can Evolve Continually on Modality for $\mathbb{X}$-Modal Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/5942d10ae51b6bd07648e54df07ef9cd-Paper-Conference.pdf)**
> Answering questions about inputs from different modalities such as image, video, audio, depth, and point cloud.

**[AdaSteer: Your AlignedLLMis Inherently an Adaptive Jailbreak Defender](https://aclanthology.org/2025.emnlp-main.1249.pdf) (as "Multi-modal question answering")**
> The task of answering questions that require processing and integrating information from multiple data modalities, such as text and images.

## Relationships

### Multimodal question answering →
- **Visual7W** (measurements) — *measured_by*
  - [A Stronger Mixture of Low-Rank Experts for Fine-Tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25s/sun25s.pdf)

### Associated with
- **Retrieval-augmented generation** (behaviors tasks)
  - [BioBridge: Bridging Biomedical Foundation Models via Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a5a9f5c15632e9f52c9c1ba4134f13c-Paper-Conference.pdf)

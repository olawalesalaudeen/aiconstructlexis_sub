# Detailed description generation
**Type:** Behavior  
**Referenced in:** 4 papers  
**Also known as:** Defect description  

## State of the Field

Across the provided literature, detailed description generation is most commonly defined as the task of producing an elaborate and thorough natural language description of a visual scene. The source of the visual information is specified as either images or fMRI brain recordings corresponding to a scene. A more specialized framing appears in the context of industrial anomaly detection, where the behavior is termed "Defect description" and focuses on detailing the "visible appearance characteristics of the defect," such as its size or color. The behavior is operationalized and measured using benchmarks like LLaVA-Bench, which contains a category of questions for detailed descriptions. This task is often positioned within a spectrum of language generation capabilities, presented as a more comprehensive alternative to "brief descriptions" and frequently grouped with other tasks like "simple QA" and "complex reasoning."

## Sources

**[Neuro-Vision to Language: Enhancing Brain Recording-based Visual Reconstruction and Language Interaction](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1c62bdeee97b38c34dcda152c829511-Paper-Conference.pdf)**
> The task of generating an elaborate, detailed natural language description of a visual scene from the corresponding fMRI brain recordings.

**[MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf) (as "Defect description")**
> Describing the visible appearance characteristics of a defect, such as size, color, or shape.

## Relationships

### Detailed description generation →
- **LLaVA-Bench** (measurements) — *measured_by*
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)

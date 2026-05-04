# MME-RealWorld
**Type:** Measurement  
**Referenced in:** 5 papers  
**Also known as:** MME-RW  

## State of the Field

Across the provided literature, MME-RealWorld is consistently described as a benchmark for evaluating multimodal models on real-world, vision-language tasks. The benchmark is frequently characterized as being "manually curated" or "manually annotated," with one source noting it features high-resolution images with an "average resolution of 2000×1500." Its structure is defined by multiple categories and sub-tasks; one paper states it "encompasses five primary categories and 43 sub-class tasks," while another lists examples including monitoring, autonomous driving, and OCR. The primary use of MME-RealWorld in this set of papers is to measure a range of model capabilities. Specifically, it is used to assess `Optical character recognition`, `Commonsense knowledge`, `Object counting`, `Action prediction`, and `Relational reasoning`. Additionally, it is employed to evaluate `Chart and diagram understanding`. One study also uses a subset of the benchmark to explicitly test for `Generalization`.

## Sources

**[Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf) (as "MME-RW")**
> A benchmark for real-world multi-modal tasks used to assess vision-language performance.

**[Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25at/wang25at.pdf)**
> A manually curated multimodal benchmark for real-world scenarios with multiple categories and sub-tasks, including monitoring, autonomous driving, OCR, property, and text/address tasks.

## Relationships

### → MME-RealWorld
- **Object counting** (behaviors tasks) — *measured_by*
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Action prediction** (behaviors tasks) — *measured_by*
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Relational reasoning** (constructs) — *measured_by*
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Optical character recognition** (behaviors tasks) — *measured_by*
  > RAP improves the performance of LLaVA-v1.5-13B on most sub-tasks, especially on MO/Orientation (+7.3%), AD/Intention (+6.0%), and OCR/license (+10.3%). (Section 5.2)
  - [Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25at/wang25at.pdf)
- **Chart and diagram understanding** (behaviors tasks) — *measured_by*
  - [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.711.pdf)
- **Generalization** (constructs) — *measured_by*
  > After creating an Error-book based on MME-RealWorld-Lite (Reasoning) subset, we applied it directly to the remaining MME-RealWorld Reasoning subset, excluding the Lite portion to rigorously test generalization (Section 4.1).
  - [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.711.pdf)

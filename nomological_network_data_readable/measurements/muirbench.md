# MUIRBENCH
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** MuirBench  

## State of the Field

Across the provided literature, MUIRBENCH is consistently defined as a multimodal benchmark for evaluating a model's ability to reason across and integrate information from multiple images. Its primary stated purpose is to "rigorously assess and evaluate multi-image understanding," as described in the paper "MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding." To achieve this, the benchmark is used to measure several specific abilities, including counting objects across images, understanding diagrams, chronological ordering of images based on text, and scene understanding from multiple views. It is also used to evaluate visual grounding, which involves locating an object within multiple images, and information retrieval, such as identifying images containing the same building. While it assesses various image relationships, one paper notes that "MUIRBENCH... does not consider spatial relationships between objects in multiple images" ("MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models"). In practice, it is used to report and compare the performance of different models, as seen in the "HSCR..." paper.

## Sources

**[MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf)**
> A multi-image evaluation benchmark that assesses various image relationships but does not cover spatial relationships.

**[HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.680.pdf) (as "MuirBench")**
> Multimodal benchmark evaluating reasoning across multiple images, testing a model's ability to integrate information from diverse visual inputs.

## Relationships

### → MUIRBENCH
- **Multi-image understanding** (constructs) — *measured_by*
  > we introduce MUIRBENCH (MULTI-IMAGE UNDERSTANDING BENCHMARK), a comprehensive benchmark designed to rigorously assess and evaluate multi-image understanding by multimodal LLMs. (Section 2)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Counting** (behaviors tasks) — *measured_by*
  > [COUNTING] aims to evaluate the ability of models to count the number of specific objects across multiple images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Chart and diagram understanding** (behaviors tasks) — *measured_by*
  > [DIAGRAM UNDERSTANDING] aims to evaluate the ability of models to understand information conveyed in diagram images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Cross-modal retrieval** (behaviors tasks) — *measured_by*
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Chronological ordering** (behaviors tasks) — *measured_by*
  > [ORDERING] aims to evaluate the ability of models to order a series of images based on the textual description. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Scene understanding** (constructs) — *measured_by*
  > [SCENE UNDERSTANDING] aims to evaluate the ability of models to understand a scene comprised of multiple views from multiple surveillance images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Visual grounding** (constructs) — *measured_by*
  > [VISUAL GROUNDING] aims to evaluate the ability of models to ground a specific object and seek information about it within multiple images. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  > [VISUAL RETRIEVAL] aims to evaluate the ability of models to retrieval images that contain the same building. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)

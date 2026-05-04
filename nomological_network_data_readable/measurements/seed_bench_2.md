# SEED-Bench-2
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** Seed-Bench-2, SeedBench-2, Seed-bench-2  

## State of the Field

Across the provided literature, SEED-Bench-2 is consistently characterized as a multimodal benchmark for evaluating language and vision models. Its most frequently mentioned application is assessing a model's ability to handle multiple images, with one paper defining its purpose as evaluating the "ability to comprehend and reason about multimodal inputs containing multiple images" (Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning). This benchmark is explicitly used to measure the construct of "Understanding" in this multi-image context. This focus is extended by another study that frames it as a benchmark for "long-context tasks that require identifying relevant information from image sequences" (MatViX: Multimodal Information Extraction from Visually Rich Articles), a use supported by its relationship with "Long-context processing". A more general application is also described, where the benchmark is used to evaluate the "general performance of Vision-Language Assistants," particularly after debiasing methods have been applied. In practice, it is used alongside other multimodal benchmarks and also serves as a "non-synthetic comparison point" to validate the evaluation rankings produced by other systems.

## Sources

**[Revealing and Reducing Gender Biases in Vision and Language Assistants (VLAs)](https://proceedings.iclr.cc/paper_files/paper/2025/file/189b0101331a7a87bf7686d8bb20e12d-Paper-Conference.pdf) (as "Seed-Bench-2")**
> Seed-Bench-2 (Li et al., 2023a; 2024a) is a multimodal benchmark used to evaluate the general performance of Vision-Language Assistants after applying debiasing methods.

**[Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2372bb107ef0ba85e47c6a2dc7dafda-Paper-Conference.pdf) (as "SeedBench-2")**
> SeedBench-2, a benchmark used in the paper as a non-synthetic comparison point for LVLM evaluation rankings.

**[Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning](https://aclanthology.org/2025.naacl-long.170.pdf)**
> A benchmark that evaluates a model's ability to comprehend and reason about multimodal inputs containing multiple images.

**[MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.186.pdf) (as "Seed-bench-2")**
> Seed-bench-2 is a benchmark for evaluating multimodal agents in long-context tasks that require identifying relevant information from image sequences.

## Relationships

### → SEED-Bench-2
- **Understanding** (constructs) — *measured_by*
  > Multi-image Tasks: Seed-Bench-2 (Li et al., 2024) evaluates the ability to comprehend multimodal inputs containing multiple images.
  - [Smurfs: Multi-Agent System using Context-EfficientDFSDTfor Tool Planning](https://aclanthology.org/2025.naacl-long.170.pdf)

# Object counting
**Type:** Behavior  
**Referenced in:** 18 papers  

## State of the Field

Across the surveyed literature, object counting is defined in two distinct modalities, though the most frequent formal definition describes a vision-based task: "Determining the number of instances of a specific object category present in an image." This visual behavior is operationalized and measured using benchmarks such as CV-Bench, MME, MME-RealWorld, and Waste-Bench. For instance, the MME benchmark is used to "measure object-level hallucination" through subsets focused on object count. In contrast, a subset of the literature operationalizes object counting as a purely textual task, defined as "counting the number of objects described in a textual context" and exemplified by queries like "I have a chicken, a frog... How many animals do I have?" This text-based version is associated with BBH Object Counting and the BIG-Bench suite. The task is also studied alongside `Multimodal reasoning` and is employed as a method to measure the construct of `Faithfulness`.

## Sources

**[Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf)**
> Determining the number of instances of a specific object category present in an image.

## Relationships

### Object counting →
- **MME** (measurements) — *measured_by*
  > Following Yin et al. (2023), we evaluate hallucination using four subtasks: Existence, Count, Position, and Color, with performance measured by the combined metric of accuracy and accuracy+ (Section 4.1).
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **MME-RealWorld** (measurements) — *measured_by*
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **Waste-Bench** (measurements) — *measured_by*
  - [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1578.pdf)

### Associated with
- **Multimodal reasoning** (constructs)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
- **BIG-Bench** (measurements)
  - [The Validation Gap: A Mechanistic Analysis of How Language Models Compute Arithmetic but Fail to Validate It](https://aclanthology.org/2025.emnlp-main.1496.pdf)

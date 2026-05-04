# MMAU
**Type:** Measurement  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, MMAU is presented as a benchmark with two distinct applications: one for evaluating expert-level audio processing and another for assessing agentic capabilities. In the context of audio, it is defined as a benchmark for "expert-level audio reasoning" with "sound and music subsets that assess complex understanding beyond basic classification" (Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities). This version is used to evaluate a model’s "understanding and reasoning capabilities in complex audio QA tasks" (MATS: An Audio Language Model under Text-only Supervision). A separate line of work uses MMAU to evaluate agent capabilities, particularly `Tool use`. In this usage, the benchmark is described as evaluating performance across five domains: "tool use, graph-based reasoning, data science, programming, and mathematics" (Instruction-Following Pruning for Large Language Models). More broadly, MMAU is also positioned as a measure for general cognitive constructs, including `Domain-specific knowledge`, `Information extraction`, and `Commonsense knowledge` or `Commonsense understanding`.

## Sources

**[Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf)**
> A benchmark for evaluating expert-level audio reasoning, with sound and music subsets that assess complex understanding beyond basic classification.

## Relationships

### → MMAU
- **Domain-specific knowledge** (constructs) — *measured_by*
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Information extraction** (behaviors tasks) — *measured_by*
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Reasoning** (constructs) — *measured_by*
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **Tool use** (behaviors tasks) — *measured_by*
  > MMAU (Yin et al., 2024) evaluates agent capabilities across five domains—tool use, graph-based reasoning, data science, programming, and mathematics.
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **Audio understanding** (constructs) — *measured_by*
  > To further evaluate our model’s understanding and reasoning capabilities in complex audio QA tasks, we conducted experiments on AIR-Bench Chat (Yang et al., 2024) and MMAU (Sakshi et al., 2024) benchmarks. (Section 4.2.2)
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
- **Audio reasoning** (constructs) — *measured_by*
  - [MATS: An Audio Language Model under Text-only Supervision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ai/wang25ai.pdf)
- **World knowledge** (constructs) — *measured_by*
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.514.pdf)

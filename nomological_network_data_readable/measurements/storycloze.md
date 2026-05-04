# StoryCloze
**Type:** Measurement  
**Referenced in:** 14 papers  

## State of the Field

Across the provided literature, StoryCloze is predominantly described as a benchmark for evaluating a model's commonsense reasoning and story understanding. The task is consistently framed as a cloze-style challenge requiring the selection of a correct ending for a short story, though papers vary on whether the story context consists of four or five sentences. It is most frequently positioned as an instrument for measuring `Commonsense understanding`, narrative understanding, and script knowledge. Several papers specify using StoryCloze for zero-shot performance evaluation, often listing it alongside other reasoning benchmarks like PIQA, ARC, and HellaSwag. While its primary use is as a multiple-choice task for understanding, a less common application adapts the dataset for generative purposes. For instance, one study uses it to measure `Text generation` and `Creative writing` by repurposing its stories for an open-ended generation task, noting it was "originally used for story understanding" ("Forking Paths in Neural Text Generation").

## Sources

**[Dynamic Sparse No Training:  Training-Free Fine-tuning for Sparse LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/0147d967a5db3b8dde08d2a327b24568-Paper-Conference.pdf)**
> A commonsense reasoning benchmark for evaluating story understanding and script knowledge, requiring the selection of a correct ending to a four-sentence story.

## Relationships

### → StoryCloze
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Jointly Training Large Autoregressive Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d564edd2bf015ac07c8031ab3f9839b0-Paper-Conference.pdf)
- **Multiple-choice question answering** (behaviors tasks) — *measured_by*
  - [Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf)
- **Creative writing** (behaviors tasks) — *measured_by*
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)

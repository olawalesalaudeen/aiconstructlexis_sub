# Sentence completion
**Type:** Behavior  
**Referenced in:** 24 papers  
**Also known as:** Fill-in-the-blank completion  

## State of the Field

Across the provided literature, sentence completion is most commonly defined as the task of either selecting or generating the most plausible continuation of a sentence or context. This behavior is operationalized in two primary ways. In its generative form, models are prompted to produce text to continue a given phrase, sometimes with explicit instructions like "Complete the sentence:", a technique used for fine-tuning and bias probing. In its selection-based form, the task requires choosing the most likely continuation from a set of options and is measured using benchmarks such as HellaSwag and SWAG. A more specific, minority framing treats this as a "fill-in-the-blank" task, where completing a sentence with a missing knowledge point is used to probe for knowledge memorization. The StereoSet benchmark is also used to measure this behavior. Additionally, sentence completion is studied in relation to textual reasoning.

## Sources

**[ESPACE: Dimensionality Reduction of Activations for Model Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf)**
> Selecting or generating the most plausible continuation of a sentence or context.

**[RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Fill-in-the-blank completion")**
> The observable task of completing a sentence where a specific knowledge point has been replaced with a blank, used to probe for knowledge memorization.

## Relationships

### Sentence completion →
- **StereoSet** (measurements) — *measured_by*
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **HellaSwag** (measurements) — *measured_by*
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
- **SWAG** (measurements) — *measured_by*
  - [NoVo: Norm Voting off Hallucinations with Attention Heads in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/db6461eaf0eaeaad1d9c4a70e4818cbd-Paper-Conference.pdf)

### Associated with
- **Textual reasoning** (behaviors tasks)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)

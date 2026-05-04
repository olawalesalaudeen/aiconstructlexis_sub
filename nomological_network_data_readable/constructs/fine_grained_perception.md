# Fine-grained perception
**Type:** Construct  
**Referenced in:** 11 papers  

## State of the Field

Across the provided papers, 'Fine-grained perception' is consistently defined as a model's ability to recognize, discern, and utilize detailed and subtle visual information. The specific attributes mentioned include object locations, counts, spatial relationships, celebrity identities, and clothing styles, with some definitions specifying this as operating at the 'pixel-level' or 'instance-level'. This construct is operationalized and measured using several benchmarks; papers report using MMBench and MMStar to evaluate it, and one source notes that the MMVP benchmark 'mainly focuses on fine-grained perception'. The literature frequently frames this as a foundational capability whose absence is a drawback. For instance, one study states that weakness in fine-grained perception 'may inhibit the performance of the next reasoning and creation tasks' (ConvBench...). Another paper suggests a directional relationship, proposing that it 'enhances image-based logical reasoning' (HaploVL...).

## Sources

**[ConvBench: A Multi-Turn Conversation Evaluation Benchmark with Hierarchical Ablation Capability for Large Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b69396afc07a9ca3428d194f4db84c02-Paper-Datasets_and_Benchmarks_Track.pdf)**
> A specific facet of perception involving the ability to recognize detailed and specific visual attributes, such as object locations, celebrity identities, or clothing styles.

## Relationships

### Fine-grained perception →
- **MMStar** (measurements) — *measured_by*
  > The evaluation dataset is MMStar. (Figure 1 Caption)
  - [Are We on the Right Way for Evaluating Large Vision-Language Models?](https://proceedings.neurips.cc/paper_files/paper/2024/file/2f8ee6a3d766b426d2618e555b5aeb39-Paper-Conference.pdf)
- **MMBench** (measurements) — *measured_by*
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **MMVP** (measurements) — *measured_by*
  > Among these benchmarks, MMVP mainly focuses on fine-grained perception. (Section 4.1)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)
- **Logical reasoning** (constructs) — *causes*
  > This suggests that fusing raw image and text embeddings in a single transformer is beneficial for fine-grained perception and subsequently enhances image-based logical reasoning. (Section 4.3)
  - [HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ab/yang25ab.pdf)

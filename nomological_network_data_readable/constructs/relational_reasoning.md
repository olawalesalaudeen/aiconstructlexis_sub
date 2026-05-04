# Relational reasoning
**Type:** Construct  
**Referenced in:** 24 papers  
**Also known as:** Relation reasoning, Relational inference, Geometric relationship identification, Inter-relationship analysis, Relation analysis, Relation mining, Spatial relation inference, Composition identification, Relationship identification, Interaction relation understanding, Spatial relationship understanding  

## State of the Field

Relational reasoning is most frequently defined as the ability to understand and operate on abstract relationships between symbols, independent of the symbols' specific identities. This framing is described as a foundational capability for abstraction and systematic generalization, often tested by evaluating models on symbols not seen during training ("When can transformers reason with abstract symbols?"). A substantial body of work, however, defines the construct more concretely within specific domains, such as identifying relationships between entities in visual scenes, inferring multi-hop connections in knowledge graphs, or understanding geometric structures. The construct is operationalized and measured using several benchmarks; for instance, papers use GQA to assess "general visual understanding and relational reasoning," and also employ MMBench and MME-RealWorld for its evaluation. Other work has developed specific datasets like GeomRel to isolate and evaluate the sub-skill of geometric relationship identification. Relational reasoning is studied alongside related constructs like abstract reasoning, visual reasoning, and information extraction. One study reports that integrating explicit relational mechanisms into an architecture can lead to improved data and parameter efficiency ("Disentangling and Integrating Relational and Sensory Information in Transformer Architectures").

## Sources

**[When can transformers reason with abstract symbols?](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a78459dbbcdc90783d183999e72176c-Paper-Conference.pdf)**
> The ability to understand and operate on abstract relationships between symbols, independent of the specific identity of those symbols.

**[DreamLLM: Synergistic Multimodal Comprehension and Creation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a7a22152cd21f0ca3c0f8139bb32905-Paper-Conference.pdf) (as "Relation reasoning")**
> The ability to reason about relationships among entities in visual scenes and multimodal contexts.

**[Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf) (as "Relational inference")**
> The ability to reason about the compatibility and interactions between different shopping concepts, such as between product categories and attributes.

**[Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf) (as "Geometric relationship identification")**
> The specific cognitive skill of correctly identifying explicit or implicit geometric relationships between elements like points, lines, and shapes from a textual description.

**[Synthetic continued pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf) (as "Relation analysis")**
> The task of describing the relationships between a given set of entities within the context of a source document.

**[Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf) (as "Inter-relationship analysis")**
> Analyzing and describing the connections or relationships between different marked regions or objects in an image.

**[Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf) (as "Relation mining")**
> The observable task of identifying relationships between entities or concepts using Multimodal Large Language Models.

**[VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf) (as "Relationship identification")**
> Identifying which properties stay the same or change between images in a visual analogy.

**[Do Vision-Language Models Represent Space and How? Evaluating Spatial Frame of Reference under Ambiguities](https://proceedings.iclr.cc/paper_files/paper/2025/file/af2d9fb5bcee19ef2dfa70d843520c97-Paper-Conference.pdf) (as "Spatial relation inference")**
> The task of determining whether a stated spatial relation (e.g., 'to the left of', 'in front of') holds true for a pair of objects depicted in an image, typically by answering a yes/no question.

**[A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d355518527578ce26b80da96e9fc2750-Paper-Conference.pdf) (as "Composition identification")**
> Determining spatial, orientational, occlusion, size-comparison, or arrangement relations among objects in an image.

**[MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf) (as "Interaction relation understanding")**
> The task of reasoning about the dynamic interactions between different agents in a traffic scene, such as an ego vehicle's reaction to others.

**[MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf) (as "Spatial relationship understanding")**
> Determining the positional or relational configuration between objects in an image.

## Relationships

### Relational reasoning →
- **MMBench** (measurements) — *measured_by*
  - [Accelerating Pre-training of Multimodal LLMs via Chain-of-Sight](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a54a80ffc2834689ffdd0920202018e-Paper-Conference.pdf)
- **MME-RealWorld** (measurements) — *measured_by*
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **GQA** (measurements) — *measured_by*
  > “for general VQA tasks, we use VizWiz (Gurari et al., 2018) and GQA (Hudson & Manning, 2019) to test general visual understanding and relational reasoning.”
  - [LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)
- **Data efficiency** (constructs) — *causes*
  > Our results demonstrate that integrating explicit relational computational mechanisms into the Transformer architecture leads to significant performance gains in terms of data efficiency and parameter efficiency. (Section 1)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
- **Parameter efficiency** (constructs) — *causes*
  > Our results demonstrate that integrating explicit relational computational mechanisms into the Transformer architecture leads to significant performance gains in terms of data efficiency and parameter efficiency. (Section 1)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)

### Associated with
- **Information extraction** (behaviors tasks)
  > EntiGraph consists of two steps/prompts: extracting entities from the document and analyzing relations among an arbitrary subset of the entities (Figure 1). (Section 2.2)
  - [Synthetic continued pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf)
- **Referring expression understanding** (behaviors tasks)
  - [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/329ad516cf7a6ac306f29882e9c77558-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Abstract reasoning** (constructs)
  > Analogical reasoning consists of diverse atomic abilities; perceptual understanding, mapping abstract relationships between visual contents... and transferring relational patterns to novel cases.
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)
- **Visual reasoning** (constructs)
  - [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf)
- **Geometric reasoning** (constructs)
  > the measurement of geometric ability is lossless as it only involves one skill of identifying relationships, which is the foundation of reasoning ability.
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
- **Intention recognition** (behaviors tasks)
  - [Rank-Awareness and Angular Constraints: A New Perspective on Learning Sentence Embeddings fromNLIData](https://aclanthology.org/2025.emnlp-main.1130.pdf)

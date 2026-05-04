# Representation learning
**Type:** Construct  
**Referenced in:** 15 papers  
**Also known as:** Feature learning, Semantic representation learning  

## State of the Field

Across the surveyed literature, representation learning is most commonly defined as a model's ability to encode input data into a latent space where similar instances are represented closely, facilitating downstream tasks. Some papers offer more specific framings, such as `Feature learning`, which focuses on capturing "invariant or environment-relevant patterns" (Context is Environment), or `Semantic representation learning`, which contrasts learning "semantic meaning" with learning "superficial token patterns" (What Factors Affect Multi-Modal In-Context Learning?). The process is often described as a transformation occurring in a model's intermediate layers, which, as one paper notes, "prepares it into a certain format" for subsequent processing (How Do Transformers Learn In-Context Beyond Simple Functions?). The quality of these learned representations is operationalized and evaluated through performance on various downstream tasks. For instance, one study uses the `Nucleotide Transformer Benchmark` to assess representations by fine-tuning a model on genomic classification benchmarks. Representation learning is frequently studied alongside `In-context and few-shot learning`, with some work viewing it as the underlying mechanism for ICL. A few papers also report that it influences `Generalization`, `Commonsense knowledge`, and `Output diversity`.

## Sources

**[Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf) (as "Feature learning")**
> The model's capacity to learn useful representations of input data that capture invariant or environment-relevant patterns, which can be enhanced through context-based training.

**[How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf)**
> The ability of a model to learn to encode input data into a latent space where similar instances are represented closely, facilitating downstream tasks.

**[What Factors Affect Multi-Modal In-Context Learning? An In-Depth Exploration](https://proceedings.neurips.cc/paper_files/paper/2024/file/deeb4d6bdb5860fd7faf321dd5486d25-Paper-Conference.pdf) (as "Semantic representation learning")**
> The ability to learn and utilize semantic meaning rather than superficial token patterns, which VLLMs rely on for effective MM-ICL performance.

## Relationships

### Representation learning →
- **In-context learning** (constructs) — *causes*
  - [Transformers are Minimax Optimal Nonparametric In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/c11daad0a48ea5f3c5c6390c7b060720-Paper-Conference.pdf)
- **Nucleotide Transformer Benchmark** (measurements) — *measured_by*
  > To evaluate the learned representations, we fine-tuned our MLM-pretrained, short-context DNA-xLSTM models ... while the DNA-xLSTM-2M model was fine-tuned on the Nucleotide Transformers Tasks (Dalla-Torre et al., 2024) (Section 4.1)
  - [Bio-xLSTM: Generative modeling, representation and in-context learning of biological and chemical sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/60cefc59610f8f59ea10099f99a36726-Paper-Conference.pdf)
- **Generalization** (constructs) — *causes*
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Commonsense knowledge** (constructs) — *causes*
  - [Adaptive Prompting: Ad-hoc Prompt Composition for Social Bias Detection](https://aclanthology.org/2025.naacl-long.123.pdf)
- **Generation diversity** (constructs) — *causes*
  - [Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf)

### Associated with
- **In-context learning** (constructs)
  - [How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf)

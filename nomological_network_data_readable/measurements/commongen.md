# CommonGen
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

Across the provided literature, CommonGen is consistently characterized as a dataset for commonsense-guided text generation. The core task requires a model to generate a coherent sentence describing a scenario from a given set of concepts, which some papers refer to as "keywords." One source specifies that each instance contains three to five such keywords. The prevailing use of CommonGen is to measure the behavior of `Text generation` and the construct of `Text generation quality`, with one study specifically labeling the task "concept-to-sentence generation." A common alternative framing describes it as a benchmark for `generative commonsense reasoning`. Additionally, some work uses the dataset to assess more specific constructs like `conceptual coherence` and `generative fluency`. A smaller number of papers frame it as a "struct-to-text" task or employ it to evaluate model adaptation under concept-based distribution shifts.

## Sources

**[Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)**
> A commonsense-guided text generation dataset that requires models to generate a sentence describing a scenario using a given set of concepts.

## Relationships

### → CommonGen
- **Text generation quality** (constructs) — *measured_by*
  > We conduct experiments to compare the text generation and evaluation abilities of LLMs using the CommonGen (Lin et al., 2020) task, which involves generating a sentence that describes an everyday scenario based on a given set of common concepts (Section 4.1)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *measured_by*
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > We evaluate Plugin on four text generation benchmarks: (a) E2E NLG (Duˇsek et al., 2020), (b) Web NLG (Gardent et al., 2017), (c) CommonGen (Lin et al., 2020), and (d) the Adidas product description dataset (adi, 2023). (Section 7)
  - [Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf)
- **Constraint satisfaction** (constructs) — *measured_by*
  - [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.239.pdf)
- **Constrained decoding** (behaviors tasks) — *measured_by*
  - [CEAES: Bidirectional Reinforcement Learning Optimization for Consistent and Explainable Essay Assessment](https://aclanthology.org/2025.acl-long.1274.pdf)

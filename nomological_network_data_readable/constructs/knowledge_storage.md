# Knowledge storage
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Information storage, Knowledge storage capacity  

## State of the Field

Across the surveyed literature, knowledge storage is predominantly defined as the internal, latent mechanism by which a language model encodes and retains factual information from its pre-training data within its parameters, also referred to as its 'parametric memory'. A more quantitative framing treats the concept as "knowledge storage capacity," focusing on the amount of factual information, measured in bits, that a model can store and retrieve, particularly in studies of scaling laws. The construct is operationalized and measured through performance on tasks requiring factual recall, with one paper using the MMLU benchmark for its "QA evals" to assess it. Some research investigates the specific locus of this mechanism, with one study proposing that "the shallow layers likely play a critical role in the storing of knowledge," while deeper layers are for computation ("The Unreasonable Ineffectiveness of the Deeper Layers"). The concept is also studied in relation to Hallucination.

## Sources

**[Knowledge Circuits in Pretrained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf)**
> The internal mechanisms and structures by which a language model encodes and retains information within its parameters.

**[Understanding Information Storage and Transfer in Multi-Modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf) (as "Information storage")**
> The latent mechanism by which factual information from a pre-training dataset is encoded and retained within a model's parameters, also referred to as its parametric memory.

**[Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](https://proceedings.iclr.cc/paper_files/paper/2025/file/26d3c9a66836ded8f34a944f2bfe868e-Paper-Conference.pdf) (as "Knowledge storage capacity")**
> The amount of factual information, measured in bits, that a language model can store in its parameters and later retrieve.

## Relationships

### Knowledge storage →
- **MMLU** (measurements) — *measured_by*
  > "For our QA evals, we used Massive Multitask Language Understanding (MMLU) (Hendrycks et al., 2020), a common world-knowledge and problem solving benchmark"
  - [The Unreasonable Ineffectiveness of the Deeper Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbabc2f70de2dd09f491a8715ec3e80f-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behaviors tasks)
  - [Knowledge Circuits in Pretrained Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6df31b1be98e04be48af8bedb95b499-Paper-Conference.pdf)

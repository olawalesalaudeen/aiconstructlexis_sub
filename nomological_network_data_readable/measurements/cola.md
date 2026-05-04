# CoLA
**Type:** Measurement  
**Referenced in:** 34 papers  
**Also known as:** Cola, COLA, GLUE-COLA, GLUE-CoLA  

## State of the Field

The name "CoLA" refers to two distinct benchmarks in the provided literature, with one usage being substantially more prevalent. The dominant framing identifies CoLA as the Corpus of Linguistic Acceptability, a task frequently situated within the GLUE benchmark. This instrument is consistently used to measure a model's capacity for `grammatical acceptability judgment` and `linguistic acceptability judgment`, operationalized as a single-sentence binary classification task where models must determine if a sentence is grammatically correct. Performance on this linguistic task, which uses text from "books and journal articles," is reported using the "Matthews correlation" metric and is also used to assess broader constructs like `natural language understanding` and `generalization`. In a separate, smaller set of papers, "CoLA" or "Cola" refers to a vision-language benchmark designed to evaluate `compositional reasoning`. This second benchmark is a text-to-image retrieval task where a Vision-Language Model must match captions describing entity relationships to the correct images, sometimes from a database containing distractors.

## Sources

**[Fast-ELECTRA for Efficient Pre-training](https://proceedings.iclr.cc/paper_files/paper/2024/file/1e5f58d98523298cba093f658cfdf2d6-Paper-Conference.pdf)**
> The Corpus of Linguistic Acceptability benchmark, used here as a downstream grammatical acceptability evaluation.

**[CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf) (as "Cola")**
> Text-to-image retrieval benchmark that assesses compositional ability by matching captions describing relations between entities to correct images.

**[ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/28aad3b3b315d86910d7f4ee2867dfa4-Paper-Datasets_and_Benchmarks_Track.pdf) (as "COLA")**
> A benchmark that evaluates compositional reasoning by tasking a VLM with retrieving correct images based on specific configurations of attributes and objects from a database containing distractor images.

**[ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf) (as "GLUE-COLA")**
> The Corpus of Linguistic Acceptability, a task from the GLUE benchmark for determining if a sentence is grammatically correct.

**[TDDBench: A Benchmark for Training data detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4db8a681ae1e58376dc6227978829063-Paper-Conference.pdf) (as "GLUE-CoLA")**
> A dataset of text from books and journal articles, part of the GLUE benchmark, used in TDDBench to evaluate TDD algorithms.

## Relationships

### → CoLA
- **Natural language understanding** (constructs) — *measured_by*
  - [UniCoTT: A Unified Framework for Structural Chain-of-Thought Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca642f8e1174012d67c05c1c9f969644-Paper-Conference.pdf)
- **Compositional reasoning** (constructs) — *measured_by*
  > We first evaluate our CoVLM on compositional reasoning tasks, including... matching the correct captions describing the relation between two images with similar entities (Cola, (Ray et al., 2023))... (Section 4.1)
  - [CoVLM: Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding](https://proceedings.iclr.cc/paper_files/paper/2024/file/47561f5e1dc53c7d119185e217b523d0-Paper-Conference.pdf)
- **Grammatical acceptability judgment** (behaviors tasks) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Text classification** (behaviors tasks) — *measured_by*
  - [Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Linguistic acceptability judgment** (behaviors tasks) — *measured_by*
  - [Primus: A Pioneering Collection of Open-Source Datasets for CybersecurityLLMTraining](https://aclanthology.org/2025.emnlp-main.528.pdf)
- **Generalization** (constructs) — *measured_by*
  - [ELICIT: LLM Augmentation Via External In-context Capability](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ffd6024f02b92a52abe8e79a78e9064-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurements)
  - [KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)

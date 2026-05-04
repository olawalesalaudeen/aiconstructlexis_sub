# SciQA
**Type:** Measurement  
**Referenced in:** 10 papers  

## State of the Field

Across the provided literature, SciQA is a question-answering dataset used to evaluate a range of model capabilities. The common definition describes it as consisting of "science exam questions with rich domain-specific language and complex reasoning." The most prevalent application in this set of papers is to measure visual understanding, with multiple sources listing it among "commonly used vision understanding benchmarks." It is also used to assess visual question answering. In contrast, other work operationalizes SciQA as a text-based evaluation. For instance, it is categorized as a reading comprehension task and is also used to measure text generation, particularly for what one paper calls "knowledge-intensive reasoning." This paper further specifies that SciQA "challenges models using the Open Research Knowledge Graph." Thus, the provided data shows SciQA being applied as an evaluation tool for both visual and text-centric reasoning capabilities.

## Sources

**[DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)**
> A question-answering dataset consisting of science exam questions with rich domain-specific language and complex reasoning.

## Relationships

### → SciQA
- **Visual understanding** (constructs) — *measured_by*
  > “We compare LLaVA-Mini with LLaVA-v1.5 across 11 benchmarks to thoroughly assess the performance of LLaVA-Mini with minimal vision tokens.”
  - [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://proceedings.iclr.cc/paper_files/paper/2025/file/8400a2ec9ba85bfdb41eb2a584c0876d-Paper-Conference.pdf)
- **Visual question answering** (behaviors tasks) — *measured_by*
  - [Octopus: A Multi-modal LLM with Parallel Recognition and Sequential Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a3eadeebbc9eecd621086f6978865a85-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > "For knowledge-intensive reasoning, we use datasets that require deep domain understanding. ARC (Clark et al., 2018) tests advanced reasoning with grade-school science questions, PubMedQA (Jin et al., 2019) assesses biomedical reasoning from abstracts, and SciQA (Auer et al., 2023) challenges models using the Open Research Knowledge Graph."
  - [OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf)
- **Reading comprehension** (constructs) — *measured_by*
  - [LLM Data Selection and Utilization via Dynamic Bi-level Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25g/yu25g.pdf)

# Textual reasoning
**Type:** Behavior  
**Referenced in:** 12 papers  
**Also known as:** Verbal reasoning, Natural language reasoning  

## State of the Field

Across the provided literature, textual reasoning is predominantly characterized as the behavior of solving problems or drawing inferences using natural language, often explicitly contrasted with methods that rely on executable code or mathematical calculation. The definitions converge on this point, describing it as "drawing inferences or making judgments from text-based premises" or, more specifically, "answering a problem directly in natural language without relying on executable code." To operationalize and evaluate this behavior, researchers in this set of papers employ several benchmarks, including XNLI, Hendrycks MATH, and AlpacaEval v1.0. Textual reasoning is frequently studied in conjunction with other language-based tasks such as natural language inference, sentence completion, coreference resolution, and language understanding, as well as with broader concepts like complex reasoning and mathematical reasoning. A recurring theme is its relationship with non-textual modalities; some work investigates how it co-occurs with visual understanding, with one paper noting that models can "struggle to handle visual understanding with textual reasoning simultaneously." Another study suggests that for vision-language models, reasoning challenges may lie more in the visual components than the textual ones. Additionally, a single paper reports a directional relationship where textual reasoning influences code debugging.

## Sources

**[Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf) (as "Verbal reasoning")**
> The observable task of solving reasoning problems expressed in natural language without relying primarily on mathematical calculation.

**[Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf) (as "Natural language reasoning")**
> Drawing inferences or making judgments from text-based premises in benchmark tasks.

**[Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)**
> Answering a problem directly in natural language without relying on executable code.

## Relationships

### Textual reasoning →
- **XNLI** (measurements) — *measured_by*
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Hendrycks MATH** (measurements) — *measured_by*
  - [Learning to Plan Before Answering: Self-Teaching LLMs to Learn Abstract Plans for Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/821a6e5681b072351fd3c21fac44739a-Paper-Conference.pdf)
- **AlpacaEval v1.0** (measurements) — *measured_by*
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **Code debugging** (behaviors tasks) — *causes*
  - [MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation](https://aclanthology.org/2025.emnlp-main.80.pdf)

### Associated with
- **Mathematical reasoning** (constructs)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Complex reasoning** (behaviors tasks)
  - [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0356216f73660e15670510f5e42b5fa6-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Sentence completion** (behaviors tasks)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Coreference resolution** (behaviors tasks)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Planning** (constructs)
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **Visual interpretation** (constructs)
  > This indicates that VLMs are capable of textual reasoning. This finding suggests that the reasoning challenge does not mainly lie in the VLM’s textual components but in the visual ones. (Page 8)
  - [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf)
- **Language understanding** (behaviors tasks)
  - [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Visual understanding** (constructs)
  > “the four datasets where ORM performs better (MathVista, MathVerse, MMStar, and MMMU Pro) primarily feature formal reasoning and mathematical problems, whereas RealWorldQA focuses on real-world scenarios.”
  - [When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using SmallVLMs](https://aclanthology.org/2025.emnlp-main.1614.pdf)

# Code understanding
**Type:** Construct  
**Referenced in:** 29 papers  
**Also known as:** Code comprehension, Verilog understanding, Cross-file understanding, Program semantics understanding, Program comprehension, Code-level understanding  

## State of the Field

Across the surveyed literature, "Code understanding" is predominantly framed as a latent ability to interpret the syntax, semantics, and functionality of programming code. This concept, also referred to as "code comprehension" or "program comprehension," involves grasping the logic, structure, and behavior of code beyond just its static text patterns. Several papers emphasize that this requires understanding execution effects and implicit logic, with one study noting that models can "generate syntactically correct code while failing to grasp semantic meaning" (RuCCoD: Towards AutomatedICDCoding inRussian). The construct is operationalized and measured through a wide range of downstream behaviors, including code summarization, bug and defect detection, code translation, and predicting execution outcomes, with one paper explicitly linking it to the "Code-to-Text (C2T)" task (LLM Augmented LLMs: Expanding Capabilities through Composition).

Evaluation approaches mentioned in the data include the CodeMMLU benchmark, execution-based validation, and, for specialized variants like Verilog understanding, LLM-as-a-judge and Human evaluation. Code understanding is frequently studied alongside Code generation as a primary capability of large language models for code. It is reported to enable Explanation generation and is also studied in relation to Type inference and Code navigation. Some research identifies specific limitations in current models, such as a "weak sense of data types" and "implicit code semantics" (Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain), while other work proposes more granular versions of the construct like Cross-file understanding.

## Sources

**[Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)**
> The latent ability to interpret the syntax, semantics, and functionality of programming code, enabling explanation and reasoning about code behavior.

**[LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf) (as "Code comprehension")**
> The model's underlying ability to understand the semantics and predict the outcome of a given piece of code.

**[DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf) (as "Verilog understanding")**
> The latent ability of a model to comprehend Verilog code and summarize its high-level functionality in natural language.

**[Investigating Neurons and Heads in Transformer-basedLLMs for Typographical Errors](https://aclanthology.org/2025.emnlp-main.314.pdf) (as "Cross-file understanding")**
> The ability to track and integrate information distributed across multiple files in a code repository when implementing a target function.

**[SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/6efcc7fd8efeee29a050a79c843c90e0-Paper-Conference.pdf) (as "Program semantics understanding")**
> The latent ability of a model to grasp the meaning, behavior, and execution effects of code beyond static text patterns.

**[LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf) (as "Program comprehension")**
> The latent ability of a model to understand the semantic properties, structures, and relationships within source code.

**[RZ-NAS: Enhancing LLM-guided Neural Architecture Search via Reflective Zero-Cost Strategy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ji25a/ji25a.pdf) (as "Code-level understanding")**
> The latent ability of the LLM to comprehend and reason about neural architecture search tasks through executable code representations of network construction and zero-cost proxy computation.

## Relationships

### Code understanding →
- **Code explanation** (behaviors tasks) — *causes*
  - [LLM Augmented LLMs: Expanding Capabilities through Composition](https://proceedings.iclr.cc/paper_files/paper/2024/file/008a16ead32f932b711788c276890456-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  > To tackle this issue, we take the initiative to apply embedding similarity and GPT score for evaluation, both of which assess semantic similarity more effectively. (Section 1)
  - [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > To further validate our model’s performance, we have conducted human evaluations, which show that DeepRTL-220m, GPT-4, and o1-preview achieve accuracies of 78%, 72%, and 67%, respectively. (Section 5.2)
  - [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf)

### → Code understanding
- **Long-context understanding** (constructs) — *measured_by*
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)

### Associated with
- **Type inference** (behaviors tasks)
  - [TypyBench: Evaluating LLM Type Inference for Untyped Python Repositories](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25l/dong25l.pdf)
- **Code navigation** (behaviors tasks)
  - [Position: Future Research and Challenges Remain Towards AI for Software Engineering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gu25e/gu25e.pdf)

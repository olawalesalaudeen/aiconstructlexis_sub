# Grammatical acceptability judgment
**Type:** Behavior  
**Referenced in:** 18 papers  
**Also known as:** Subject-verb agreement, Syntactic well-formedness detection, Grammaticality judgment  

## State of the Field

Across the provided literature, "Grammatical acceptability judgment" is predominantly framed as the task of determining whether a sentence adheres to the grammatical rules of a language. While most definitions focus on syntactic correctness, a smaller set of papers broadens this to "linguistic acceptability," which also includes semantic well-formedness. The most common operationalization of this behavior is as a classification task, where a model must label a sentence as either grammatically acceptable or unacceptable. An alternative operationalization involves a comparative judgment, where the model chooses between a correct and a corrupted version of a sentence or, as one paper notes, is evaluated on whether it "assigned a higher probability to the acceptable sentence" ("Speech Vecalign: an Embedding-based Method for Aligning Parallel Speech Documents"). A more specific instance of this task is subject-verb agreement, where the model's goal is to "choose the appropriate verb inflection" ("Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models"). This behavior is frequently measured using the CoLA benchmark and is also evaluated with instruments like BLiMP. The task is studied in relation to language proficiency, with one paper using a "discriminative grammar judgment experiment" to test a model's acquisition of grammar knowledge ("Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?").

## Sources

**[Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3ba4d47a83e498c2b1a0868cba20f6de-Paper-Conference.pdf) (as "Subject-verb agreement")**
> Choosing the appropriate verb inflection based on the grammatical number of the subject.

**[Emergence of a High-Dimensional Abstraction Phase in Language Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/57568e093cbe0a222de0334b36e83cf5-Paper-Conference.pdf) (as "Syntactic well-formedness detection")**
> The observable task of determining whether a given sentence adheres to the grammatical rules of a language.

**[TopoNets: High performing vision and language models with brain-like topography](https://proceedings.iclr.cc/paper_files/paper/2025/file/6191ab7080c840f67eaf5dff7d5edfcb-Paper-Conference.pdf) (as "Linguistic acceptability judgment")**
> The task of determining whether a sentence is grammatically or semantically well-formed, as evaluated by benchmarks like BLiMP.

**[Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf) (as "Grammaticality judgment")**
> The task of determining whether a given sentence is grammatically correct according to the rules of a language, often by choosing between a correct and a corrupted version.

**[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)**
> The task of classifying a sentence as either grammatically acceptable or unacceptable.

**[DiplomacyAgent: DoLLMs Balance Interests and Ethical Principles in International Events?](https://aclanthology.org/2025.emnlp-main.694.pdf) (as "Grammatical judgment")**
> The task of determining whether a sentence is grammatically correct.

## Relationships

### Grammatical acceptability judgment →
- **CoLA** (measurements) — *measured_by*
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Causal tracing** (measurements) — *measured_by*
  - [What does the Knowledge Neuron Thesis Have to do with Knowledge?](https://proceedings.iclr.cc/paper_files/paper/2024/file/013d743db3c684957305d32017f13339-Paper-Conference.pdf)

### Associated with
- **Language proficiency** (constructs)
  - [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf)

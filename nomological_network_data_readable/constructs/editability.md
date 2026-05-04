# Editability
**Type:** Construct  
**Referenced in:** 5 papers  
**Also known as:** Multiple edits, Code editing ability, Lifelong knowledge editing  

## State of the Field

Across the provided literature, Editability is conceptualized in a few distinct ways, with the prevailing usage concerning a model's capacity to integrate new information while preserving existing knowledge. This is variously defined as the ability to handle a continuous stream of factual updates, referred to as "lifelong knowledge editing," or to accumulate "multiple edits... without forgetting previous edits" (BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing). Some work frames this more broadly as an "inherent capacity" to be modified while maintaining overall performance, noting that sequential updates can cause a "degradation in... editability" (Towards Lifelong Model Editing via Simulating Ideal Editor). A distinct, more domain-specific framing defines Editability as the latent ability to perform code modifications from natural language instructions. This code-focused aspect of the construct is operationalized and measured using performance on benchmarks such as HumanEval, CanItEdit, HumanEvalFix, NoFunEval, Aider, and Aider Polyglot. The construct is also studied alongside Compositionality and is reported to be caused by Instruction fine-tuning.

## Sources

**[NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf) (as "Code editing ability")**
> The latent capacity of a model to understand and implement diverse code modifications based on natural language instructions, across varying code granularities and edit types.

**[Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)**
> The inherent capacity of a large language model to be successfully and efficiently modified by editing techniques while maintaining its overall performance.

**[BalancEdit: Dynamically Balancing the Generality-Locality Trade-off in Multi-modal Model Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25e/guo25e.pdf) (as "Multiple edits")**
> The latent ability of a model editing system to accumulate and retain multiple knowledge updates over time without forgetting previous edits or causing interference.

**[WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thede25a/thede25a.pdf) (as "Lifelong knowledge editing")**
> The ability of a model to continuously integrate a stream of new or updated factual information while retaining previously acquired knowledge.

## Relationships

### Editability →
- **HumanEval** (measurements) — *measured_by*
  > We use CanItEdit (Cassano et al., 2023), HumanEvalFix (Muennighoff et al., 2023), NoFunEval (Singhal et al., 2024), Aider (Gauthier, 2024a) and Aider Polyglot (Gauthier, 2024b) to evaluate on code-editing tasks. (Section 5.1)
  - [NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aggarwal25b/aggarwal25b.pdf)

### → Editability
- **Instruction fine-tuning** (behaviors tasks) — *causes*
  - [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf)

### Associated with
- **Compositionality** (constructs)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)

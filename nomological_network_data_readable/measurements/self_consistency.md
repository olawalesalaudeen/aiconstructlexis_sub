# Self-consistency
**Type:** Measurement  
**Referenced in:** 46 papers  
**Also known as:** Self-Consistency, Solution consistency  

## State of the Field

Across the provided literature, 'Self-consistency' is predominantly characterized as an inference or evaluation procedure, while a smaller set of studies treat it as a property of model reasoning or outputs. The prevailing procedural definition involves sampling multiple diverse reasoning paths for a given prompt and then selecting the most frequent final answer through a majority vote. This approach, often used with Chain-of-thought reasoning, is based on the premise that "correct reasoning is more likely to converge on a single answer" (Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models). It is frequently studied alongside other inference techniques like Best-of-N and Self-Refine to enhance accuracy. In contrast, some papers define self-consistency as a property of logical coherence. This alternative framing refers to the degree to which a model's beliefs do not contradict each other, the alignment between an answer and its rationale, or the maintenance of correctness "throughout the entire reasoning process" (Step-by-Step Reasoning for Math Problems  via Twisted Sequential Monte Carlo). In this context, it is studied in relation to Faithfulness and Hallucination and is reported to be measured by instruments like CC-SHAP. The concept is applied to tasks ranging from mathematical problem-solving on benchmarks like GSM8k to long-form text generation.

## Sources

**[Token-Supervised Value Models for Enhancing Mathematical Problem-Solving Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0801fccb1d705a9e6747e138d9a0056a-Paper-Conference.pdf)**
> An inference procedure where multiple reasoning paths are sampled and the most frequent final answer is selected, leveraging the idea that correct reasoning is more likely to converge on a single answer.

**[DeLLMa: Decision Making Under Uncertainty with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6cd3ac24cdb789beeaa9f7145670fcae-Paper-Conference.pdf) (as "Self-Consistency")**
> A prompting-based evaluation procedure that samples multiple responses and uses majority vote for decision-making tasks.

**[Step-by-Step Reasoning for Math Problems  via Twisted Sequential Monte Carlo](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4d92f656cc99f60fe1bfc98386aee34-Paper-Conference.pdf) (as "Solution consistency")**
> The degree to which the model maintains logical coherence and correctness throughout the entire reasoning process.

## Relationships

### Self-consistency →
- **CC-SHAP** (measurements) — *measured_by*
  - [Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Factuality** (constructs) — *causes*
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
- **Explanation generation** (behaviors tasks) — *causes*
  - [CanLLMs Reason Abstractly Over Math Word Problems WithoutCoT? Disentangling Abstract Formulation From Arithmetic Computation](https://aclanthology.org/2025.emnlp-main.724.pdf)

### → Self-consistency
- **Data augmentation** (behaviors tasks) — *causes*
  - [Transformers Provably Solve Parity Efficiently with Chain of Thought](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e2986deda273d8fb903342841fcc4dc-Paper-Conference.pdf)

### Associated with
- **Majority voting** (measurements)
  - [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://proceedings.neurips.cc/paper_files/paper/2024/file/639d992f819c2b40387d4d5170b8ffd7-Paper-Conference.pdf)
- **Faithfulness** (constructs)
  - [Efficient One-shot Compression via Low-Rank Local Feature Distillation](https://aclanthology.org/2025.naacl-long.292.pdf)
- **Trustworthiness** (constructs)
  - [Beyond Accuracy: Evaluating Self-Consistency of Code Large Language Models with IdentityChain](https://proceedings.iclr.cc/paper_files/paper/2024/file/16371a9d5fed65d6d78ca3a7fa6e598c-Paper-Conference.pdf)
- **Multi-agent debate** (behaviors tasks)
  - [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf)
- **GSM8k** (measurements)
  - [The Consensus Game: Language Model Generation via Equilibrium Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/17a9bfda8be2301e24f232fb32f1e0fa-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (constructs)
  - [Upsample or Upweight? Balanced Training on Heavily Imbalanced Datasets](https://aclanthology.org/2025.naacl-long.172.pdf)
- **Long-form text generation** (behaviors tasks)
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
- **Hallucination** (behaviors tasks)
  - [Integrative Decoding: Improving Factuality via Implicit Self-consistency](https://proceedings.iclr.cc/paper_files/paper/2025/file/adaf1463442f5986fe81dc6c719a13a1-Paper-Conference.pdf)
- **Confidence estimation** (constructs)
  - [Self-Consistency Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/prasad25a/prasad25a.pdf)
- **Explanation generation** (behaviors tasks)
  - [Do Vision & Language Decoders use Images and Text equally? How Self-consistent are their Explanations?](https://proceedings.iclr.cc/paper_files/paper/2025/file/37294f033582ac0064bf90fa557c2573-Paper-Conference.pdf)
- **Logical consistency** (constructs)
  - [MS-RAG: Simple and Effective Multi-Semantic Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1152.pdf)

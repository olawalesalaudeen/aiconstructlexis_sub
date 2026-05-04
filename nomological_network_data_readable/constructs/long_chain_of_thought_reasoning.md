# Long Chain-of-Thought reasoning
**Type:** Construct  
**Referenced in:** 4 papers  
**Also known as:** Long chain-of-thought reasoning  

## State of the Field

Long Chain-of-Thought (CoT) reasoning is characterized as a model's capacity for extended, multi-step problem-solving, though definitions vary in their specifics. One definition presents it as an "emergent capability... to perform deep, structured natural language reasoning" that enables planning and self-reflection, while another describes it more broadly as the ability to generate "extended, coherent, and step-by-step reasoning processes." A recurring theme is its application to formal reasoning, with one paper noting that "Long CoT is designed to perform deep integration between Natural Language (NL) and Formal Language (FL) reasoning." This construct is operationalized and measured using benchmarks including AIME 2024, MATH-500, and GPQA-Diamond. The reasoning process itself is described as an "extended sequence of reasoning tokens" that demonstrates sophisticated behaviors, with one paper explicitly identifying "Branching and Backtracking" as an example. This capability is also associated with solving complex tasks like "IMO-level problems" through reflection. Finally, one study reports that a "high-quality, emergent long CoT pattern leads to significantly better generalization."

## Sources

**[MA-LoT: Model-Collaboration Lean-based Long Chain-of-Thought Reasoning enhances Formal Theorem Proving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25cb/wang25cb.pdf)**
> The emergent capability of a model to perform deep, structured natural language reasoning before generating formal outputs, enabling high-level planning and self-reflection in problem solving.

**[LVLMs are Bad at Overhearing Human Referential Communication](https://aclanthology.org/2025.emnlp-main.850.pdf) (as "Long chain-of-thought reasoning")**
> The ability to generate extended, coherent, and step-by-step reasoning processes to solve complex problems.

## Relationships

### Long Chain-of-Thought reasoning →
- **AIME 2024** (measurements) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Generalization** (constructs) — *causes*
  > SFT initialization matters: high-quality, emergent long CoT pattern leads to significantly better generalization and RL gains. (Takeaway 3.3)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Backtracking** (behaviors tasks) — *causes*
  > “we introduce a cosine length-scaling reward with a repetition penalty, which stabilizes CoT growth while encouraging emergent reasoning behaviors such as branching and backtracking”
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **MATH-500** (measurements) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **GPQA-Diamond** (measurements) — *measured_by*
  - [Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency](https://aclanthology.org/2025.emnlp-main.1751.pdf)

### Associated with
- **Backtracking** (behaviors tasks)
  > In this work, we use the term long chain-of-thought (long CoT) to describe an extended sequence of reasoning tokens that not only exhibits a larger-than-usual token length but also demonstrates more sophisticated behaviors such as: 1) Branching and Backtracking... (Section 2.1)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
- **Critique** (behaviors tasks)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)

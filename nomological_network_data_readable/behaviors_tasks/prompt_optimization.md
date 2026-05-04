# Prompt optimization
**Type:** Behavior  
**Referenced in:** 5 papers  

## State of the Field

Across the provided literature, prompt optimization is most commonly defined as the process of selecting or constructing prompts to improve a model's performance on question answering. However, the specific goals and methods of this behavior vary. One line of work operationalizes it as an iterative refinement of prompts for system components using an optimizer like MIPRO v2, which evaluates prompts against quality and privacy metrics on training data. A different application frames it as an adversarial process, where an attacker model refines prompts through a feedback loop to maximize the chance a victim model will reproduce its training data. The methods for this optimization include using gauges like pointwise mutual information or question likelihood, as noted in one study, or employing dedicated optimizers and reward functions. The effectiveness of prompt optimization is evaluated using benchmarks such as GSM8k and BBH. Additionally, prompt optimization is reported to cause task decomposition.

## Sources

**[GroundCocoa: A Benchmark for Evaluating Compositional & Conditional Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.421.pdf)**
> Selecting or constructing prompts to improve model performance on question answering.

## Relationships

### Prompt optimization →
- **GSM8k** (measurements) — *measured_by*
  - [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf)
- **BBH** (measurements) — *measured_by*
  - [Large Language Models as Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/3339f19c5fcee3ad74502947a32be9e6-Paper-Conference.pdf)
- **Task decomposition** (behaviors tasks) — *causes*
  - [POQD: Performance-Oriented Query Decomposer for Multi-vector retrieval](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ag/liu25ag.pdf)

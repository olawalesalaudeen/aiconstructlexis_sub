# AUTO-J
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** Auto-J, AutoJ  

## State of the Field

The provided literature presents AUTO-J in two distinct ways: as a specific generative judge model and as a benchmark for evaluating other models. Several papers define it as a 13B-parameter generative model that functions as an automated evaluator. In this capacity, it is used to operationalize the construct of `Helpfulness` by rating model responses on a numeric scale. One paper also groups it with other LLM judges used to 'assess the distance between reference and output' ('SePer: Measure Retrieval Utility Through The Lens Of Semantic Perplexity Reduction'). Alternatively, other work treats AUTO-J as a benchmark for the 'meta-evaluation of LLM judges' ('Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement') and for evaluating reward models. When used as a benchmark, it is sometimes deployed alongside other instruments like RewardBench and MT-Bench. A single paper also suggests a relationship where AUTO-J is used to generate `Critique`.

## Sources

**[Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)**
> A 13B-parameter generative judge model used as an automated evaluator to rate the helpfulness of model responses on a numeric scale.

**[Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement](https://proceedings.iclr.cc/paper_files/paper/2025/file/08dabd5345b37fffcbe335bd578b15a0-Paper-Conference.pdf) (as "Auto-J")**
> A curated benchmark for meta-evaluation of LLM judges.

**[Advancing LLM Reasoning Generalists with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e2c12c1a41af7c19c5b38e0837a52d1-Paper-Conference.pdf) (as "AutoJ")**
> An automated judge benchmark used to evaluate reward models, particularly on their correlation with human expert judgments.

## Relationships

### AUTO-J →
- **Critique** (behaviors tasks) — *causes*
  - [CriticEval: Evaluating Large-scale Language Model as Critic](https://proceedings.neurips.cc/paper_files/paper/2024/file/7b7d7985f62284060d65f532ed2ea5fa-Paper-Conference.pdf)

### → AUTO-J
- **Helpfulness** (constructs) — *measured_by*
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)

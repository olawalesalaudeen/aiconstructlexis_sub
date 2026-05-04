# Hypothesis generation
**Type:** Behavior  
**Referenced in:** 16 papers  
**Also known as:** Scientific hypothesis generation  

## State of the Field

Across the surveyed literature, hypothesis generation is predominantly characterized as the behavior of producing candidate explanations, rules, or strategies based on available information. This behavior is studied in several contexts, including proposing explanations for another agent's latent goals, generating rules for inductive reasoning problems, and formulating potential solutions within optimization processes. Operationally, this behavior is elicited by prompting a large language model to propose these hypotheses based on inputs like past observations or input-output examples. For instance, one approach is to "prompt an LLM to propose multiple abstract hypotheses about the problem, in natural language" (Hypothesis Search: Inductive Reasoning with Language Models). While the output is frequently a natural language statement, it can also be a combination of natural language and code or a structured representation like a causal graph. Several papers position this behavior as a preliminary step in a larger reasoning sequence, where an agent might "hypothesize and evaluate strategies before execution" (Evaluation ofLLMVulnerabilities to Being Misused for Personalized Disinformation Generation). While most definitions describe it as an "observable act," a minority of papers frame it differently, defining it as a "latent ability" or "capacity" to form plausible explanations from incomplete information.

## Sources

**[Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/12f483f624b378f9f3058d8ecd3c7ff5-Paper-Conference.pdf)**
> The observable act of producing natural language statements that propose explanations for another agent's latent strategies or goals.

**[Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf) (as "Scientific hypothesis generation")**
> Generating candidate scientific hypotheses from evidence, constraints, and anomalies.

## Relationships

### Hypothesis generation →
- **DiscoveryBench** (measurements) — *measured_by*
  - [Context-aware Biases for Length Extrapolation](https://aclanthology.org/2025.emnlp-main.1546.pdf)

### → Hypothesis generation
- **Commonsense understanding** (constructs) — *causes*
  - [NeSyC: A Neuro-symbolic Continual Learner For Complex Embodied Tasks in Open Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/d569e4655e2835e3d38310b67c5ad646-Paper-Conference.pdf)

### Associated with
- **Evaluation** (behaviors tasks)
  - [Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement](https://proceedings.iclr.cc/paper_files/paper/2024/file/05d2175de7ee637588d1b5ced8b15b32-Paper-Conference.pdf)
- **Causal inference** (behaviors tasks)
  - [Causal Modelling Agents: Causal Graph Discovery through Synergising Metadata- and Data-driven Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe90657b12193c7b52a3418bdc351807-Paper-Conference.pdf)
- **Inductive reasoning** (constructs)
  - [CORG: Generating Answers from Complex, Interrelated Contexts](https://aclanthology.org/2025.naacl-long.429.pdf)
- **Self-correction** (behaviors tasks)
  - [MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses](https://proceedings.iclr.cc/paper_files/paper/2025/file/51fd9a7d1706023cb9f8210cc6ac357c-Paper-Conference.pdf)

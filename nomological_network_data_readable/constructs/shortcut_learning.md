# Shortcut learning
**Type:** Construct  
**Referenced in:** 12 papers  
**Also known as:** Reliance on spurious correlations, Spurious correlation capture, Spurious correlation detection, Task-specific heuristics  

## State of the Field

Across the surveyed literature, shortcut learning is most commonly defined as a model's tendency to rely on spurious correlations between input features and labels that are prevalent in training data but irrelevant to the intended task. Alternative framings describe this as developing narrow, "task-specific heuristics that fail to generalize" or simply as a "reliance on spurious correlations." This behavior is often attributed to training objectives like Empirical Risk Minimization (ERM), which, as one paper notes, "incentivizes models to exploit shortcuts" (The MaleCEOand the Female Assistant...). Another study points to a more specific mechanism, suggesting models "are likely to capture spurious correlations in mini-batches" (Watch Out Your Album! On the Inadvertent Privacy Memorization in Multi-Modal Large Language Models). A recurring theme is that shortcut learning leads to negative outcomes, with the most frequently cited consequence being poor generalization on minority or out-of-distribution examples. As a construct, it is operationalized by observing this performance drop, such as when "apparent task proficiency may stem from shortcut learning rather than genuine understanding" on controlled evaluations (Core Knowledge Deficits in Multi-Modal Language Models). The provided data also indicates that shortcut learning is reported to causally affect both Generalization and Safety. While most papers focus on the model's propensity to learn these correlations, one study introduces the concept of "spurious correlation detection" as a latent ability to identify such patterns.

## Sources

**[The MaleCEOand the Female Assistant: Evaluation and Mitigation of Gender Biases in Text-To-Image Generation of Dual Subjects](https://aclanthology.org/2025.acl-long.450.pdf)**
> The tendency of models to rely on spurious correlations between input features and labels that are prevalent in majority training data but irrelevant to the actual task, leading to poor generalization on minority or out-of-distribution examples.

**[KG-Agent: An Efficient Autonomous Agent Framework for Complex Reasoning over Knowledge Graph](https://aclanthology.org/2025.acl-long.469.pdf) (as "Reliance on spurious correlations")**
> The model's tendency to use superficial or statistically common but causally unrelated patterns in the training data to make predictions, rather than learning the intended underlying task features.

**[Watch Out Your Album! On the Inadvertent Privacy Memorization in Multi-Modal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ju25a/ju25a.pdf) (as "Spurious correlation capture")**
> The model's propensity to learn and encode spurious patterns that appear correlated with the objective within a specific mini-batch, even if they are globally irrelevant.

**[Are Sparse Autoencoders Useful? A Case Study in Sparse Probing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kantamneni25a/kantamneni25a.pdf) (as "Spurious correlation detection")**
> The latent ability to identify non-causal, dataset-specific patterns that appear predictive but do not reflect true semantic relationships.

**[What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf) (as "Task-specific heuristics")**
> The tendency of a foundation model to develop narrow, non-generalizable strategies for specific tasks rather than learning a unified, interpretable world model, leading to poor extrapolation under distribution shift.

## Relationships

### Shortcut learning →
- **Generalization** (constructs) — *causes*
  - [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.416.pdf)
- **Robustness** (constructs) — *causes*
  - [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.416.pdf)

# CosmosQA
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Cosmos QA  

## State of the Field

Across the provided literature, CosmosQA is consistently described as a dataset of questions used to evaluate commonsense reasoning and reading comprehension. The format is specified as multiple-choice questions that require, as one paper notes, "inferring about human behaviors, intentions, and social interactions" (EnhancingChinese Offensive Language Detection with Homophonic Perturbation). Reflecting this focus, papers use CosmosQA to measure several related capabilities, most frequently commonsense understanding and reading comprehension, but also question answering and chain-of-thought reasoning. While the prevailing usage centers on these specific cognitive abilities, a few definitions frame its application more broadly as a tool for evaluating general "NLP classification performance" or for studying weak-to-strong generalization in narrative understanding.

## Sources

**[Relating Misfit to Gain in Weak-to-Strong Generalization Beyond the Squared Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mulgund25a/mulgund25a.pdf)**
> A large-scale dataset of commonsense-based reading comprehension questions, used to evaluate NLP classification performance.

**[Representations Shape Weak-to-Strong Generalization: Theoretical Insights and Empirical Predictions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xue25d/xue25d.pdf) (as "Cosmos QA")**
> Reading comprehension dataset involving commonsense reasoning, used to evaluate W2SG in narrative understanding and inference.

## Relationships

### → CosmosQA
- **Reading comprehension** (constructs) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Chain-of-thought reasoning** (constructs) — *measured_by*
  - [LBC: Language-Based-Classifier for Out-Of-Variable Generalization](https://aclanthology.org/2025.naacl-long.584.pdf)
- **Question answering** (behaviors tasks) — *measured_by*
  - [Can Large Language Models Tackle Graph Partitioning?](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Commonsense reasoning** (constructs) — *measured_by*
  - [EnhancingChinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1155.pdf)

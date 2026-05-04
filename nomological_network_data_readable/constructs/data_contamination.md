# Data contamination
**Type:** Construct  
**Referenced in:** 27 papers  
**Also known as:** Benchmark contamination, Contamination, Test set contamination, Dataset contamination, Contamination resilience, Train-test overlap, Entity contamination, Fact contamination, Semantic contamination, Training data pollution, Robustness to data leakage, Training data leakage, Training on the test task, Data contamination susceptibility  

## State of the Field

Across the provided literature, "Data contamination" is most commonly defined as the presence of evaluation or test data within a model's pre-training corpus. The prevailing concern, as expressed in papers like "Time Travel in LLMs," is that this overlap invalidates evaluations by artificially inflating performance metrics, leading to models succeeding through recall rather than demonstrating true capability. This phenomenon is frequently studied alongside `Memorization`, which is often treated as the mechanism or evidence of contamination, and its presence is seen as undermining the assessment of a model's `Generalization` ability. To operationalize and measure this construct, researchers employ several methods, including longitudinal analyses using benchmarks like `Codeforces` and `Project Euler` against model training cutoffs, quantifying overlap percentages from dataset collections like `PromptSource`, and using `Human evaluation` to identify exact matches. While most definitions focus on direct textual overlap, a smaller line of work introduces more nuanced forms, such as `Semantic contamination` (conceptual similarity), `Entity contamination` (memorized entity knowledge), and `Fact contamination` (memorized factual events). A few papers also discuss related concepts, with one framing "training on the test task" more neutrally as a set of practices utilizing knowledge of evaluation tasks. Finally, some work characterizes the inverse of this problem, using terms like `Contamination resistance` or `Robustness to data leakage` to describe a model's stability despite exposure to test data.

## Sources

**[What's In My Big Data?](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f7336fd66b6e6e63d1801fdd5930a5a-Paper-Conference.pdf) (as "Benchmark contamination")**
> The degree to which evaluation datasets are present in pretraining corpora, potentially invalidating model evaluations due to data leakage.

**[To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf) (as "Contamination")**
> The latent exposure of an LLM to training data that overlaps with evaluation benchmarks, leading to inflated performance estimates due to prior exposure rather than general capability.

**[Proving Test Set Contamination in Black-Box Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf) (as "Test set contamination")**
> The latent presence of benchmark datasets in a model's training data, inferred from statistically significant deviations in log probabilities between canonical and shuffled dataset orderings.

**[Time Travel in LLMs: Tracing Data Contamination in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc39a59c49b731c51398ad6b12f301d3-Paper-Conference.pdf)**
> The presence of test data from downstream evaluation tasks within the pre-training data of a large language model, which can inflate performance metrics.

**[Towards Efficient and Multifaceted Computer-assisted Pronunciation Training Leveraging Hierarchical Selective State Space Model and Decoupled Cross-entropy Loss](https://aclanthology.org/2025.naacl-long.99.pdf) (as "Dataset contamination")**
> A latent condition where a model's training data includes examples from a benchmark's evaluation set, which can artificially inflate performance and undermine true capability assessment.

**[CKnowEdit: A NewChinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction inLLMs](https://aclanthology.org/2025.acl-long.431.pdf) (as "Contamination resistance")**
> The degree to which a model's performance remains stable and reliable despite exposure to benchmark data during pre-training, reflecting its ability to generalize rather than memorize.

**[Diversity-oriented Data Augmentation with Large Language Models](https://aclanthology.org/2025.acl-long.1085.pdf) (as "Contamination resilience")**
> The degree to which a model's evaluation performance remains stable and avoids artificial inflation when potentially exposed to test data during its training phase.

**[Position: Language model developers should report train-test overlap](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25dt/zhang25dt.pdf) (as "Train-test overlap")**
> The latent extent to which a language model's training data includes content from its evaluation test sets, influencing performance validity and generalization assessment.

**[The discordance between embedded ethics and cultural inference in large language models](https://aclanthology.org/2025.emnlp-main.744.pdf) (as "Entity contamination")**
> The degree to which a model has encoded prior knowledge about specific entities appearing in evaluation items, causing its predictions to depend on entity-specific memorization or bias.

**[The discordance between embedded ethics and cultural inference in large language models](https://aclanthology.org/2025.emnlp-main.744.pdf) (as "Fact contamination")**
> The degree to which a model has memorized factual events, contexts, or details from the evaluation content during training, affecting predictions through recall rather than inference.

**[The discordance between embedded ethics and cultural inference in large language models](https://aclanthology.org/2025.emnlp-main.744.pdf) (as "Semantic contamination")**
> A form of benchmark data contamination where a model's performance is influenced by subtle conceptual similarities between its training data and evaluation data, rather than direct text overlap.

**[Logical Reasoning with Outcome Reward Models for Test-Time Scaling](https://aclanthology.org/2025.emnlp-main.1327.pdf) (as "Training data pollution")**
> The latent presence of undesirable, uncommon, or useless content in the pre-training dataset of an LLM, which manifests through the formation of polluted tokens during tokenization.

**[BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf) (as "Robustness to data leakage")**
> The degree to which model performance remains stable when benchmark data is exposed during large-scale pre-training, indicating resistance to contamination.

**[Training on the Test Task Confounds Evaluation and Emergence](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab8c971c2ccd12bac0ab249f75e2c16d-Paper-Conference.pdf) (as "Training on the test task")**
> The extent to which a model has been exposed during training to knowledge, formats, or data patterns that are relevant to downstream evaluation tasks.

**[A Statistical Approach for Controlled Training Data Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/c859b99b5d717c9035e79d43dfd69435-Paper-Conference.pdf) (as "Training data leakage")**
> The risk or phenomenon where private or copyrighted content from the training corpus is exposed or inferred through the model's outputs or internal signals.

**[CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf) (as "Data contamination susceptibility")**
> The degree to which a model's performance on a benchmark is inflated due to the presence of test data or highly similar data in its pre-training corpus.

## Relationships

### Data contamination →
- **PromptSource** (measurements) — *measured_by*
  > We present the results in Figure 5. We showcase all benchmarks whose contamination percentages are at least 5% in one of the four corpora. We find that RedPajama is the most contaminated dataset out of the four... (Figure 5 caption: Most contaminated evaluations test sets out of 82 PromptSource (Bach et al., 2022) datasets).
  - [What's In My Big Data?](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f7336fd66b6e6e63d1801fdd5930a5a-Paper-Conference.pdf)
- **Human evaluation** (measurements) — *measured_by*
  > We undertake a human evaluation, led by two domain experts, to characterize contamination by identifying both exact matches and near-exact matches of individual instances. (Section 4)
  - [Time Travel in LLMs: Tracing Data Contamination in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc39a59c49b731c51398ad6b12f301d3-Paper-Conference.pdf)
- **Codeforces** (measurements) — *measured_by*
  > we conduct the first thorough longitudinal analysis of data contamination in LLMs by using the natural experiment of training cutoffs in GPT models to look at benchmarks released over time. Specifically, we consider two code/mathematical problem-solving datasets, Codeforces and Project Euler
  - [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf)
- **Project Euler** (measurements) — *measured_by*
  > we conduct the first thorough longitudinal analysis of data contamination in LLMs by using the natural experiment of training cutoffs in GPT models to look at benchmarks released over time. Specifically, we consider two code/mathematical problem-solving datasets, Codeforces and Project Euler
  - [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf)
- **Information retrieval** (behaviors tasks) — *measured_by*
  - [What's In My Big Data?](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f7336fd66b6e6e63d1801fdd5930a5a-Paper-Conference.pdf)

### Associated with
- **Memorization** (constructs)
  > This post-cutoff performance degradation provides evidence of contamination and/or memorization of pre-cutoff problems from Codeforces and Project Euler by GPT-3.5-Turbo and GPT-4. (Section 5.1)
  - [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf)
- **Generalization** (constructs)
  > “the contamination of evaluation metrics through direct memorization of test samples, which undermines the assessment of a model’s capabilities by allowing it to succeed through recall rather than by applying intended skills (Dataset Contamination).”
  - [Towards Efficient and Multifaceted Computer-assisted Pronunciation Training Leveraging Hierarchical Selective State Space Model and Decoupled Cross-entropy Loss](https://aclanthology.org/2025.naacl-long.99.pdf)
- **Mathematical reasoning** (constructs)
  > However, the ability to recover from or correct errors in the reasoning process is generally poor across most models. This can be attributed to data memorization and potential contamination in training datasets, where models may have encountered similar/same problems before.
  - [SeaKR: Self-aware Knowledge Retrieval for Adaptive Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1313.pdf)
- **Reasoning** (constructs)
  - [The discordance between embedded ethics and cultural inference in large language models](https://aclanthology.org/2025.emnlp-main.744.pdf)

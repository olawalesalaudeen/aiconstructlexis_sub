# HaluEval
**Type:** Measurement  
**Referenced in:** 15 papers  

## State of the Field

HaluEval is consistently described across the provided literature as a large-scale benchmark for evaluating factual hallucination in model-generated responses. Its primary and most frequent application is to measure the construct of `Hallucination`, with several papers also using it to specifically assess `Hallucination detection`. One paper notes the benchmark is built from "synthetically generated hallucination data," while another specifies that its question-answering (QA) track provides a question, reference knowledge, a correct answer, and a hallucinated answer. The operationalization of HaluEval varies across studies, reflecting different facets of hallucination evaluation. A prevalent use is in QA tasks, where performance is measured by metrics such as "Accuracy", "Correctness", and "Exact Match". A different approach, reported by one study, uses it for a binary classification task to evaluate a model’s ability "to judge whether an answer to a question contains a hallucination or not." The benchmark is situated within the context of "factual reasoning" and is also used to validate `Generalization` in at least one paper.

## Sources

**[AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios](https://aclanthology.org/2025.naacl-long.258.pdf)**
> Large-scale benchmark for evaluating factual hallucination in model-generated responses.

## Relationships

### → HaluEval
- **Hallucination** (behaviors tasks) — *measured_by*
  > TruthfulQA (Lin et al., 2022) and HaluEval (Li et al., 2023) for factual reasoning and ARC-Challenge (Clark et al., 2018) for scientific reasoning (Section 4.1, Datasets).
  - [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Hallucination detection** (behaviors tasks) — *measured_by*
  > "First we evaluate a model’s ability to judge whether an answer to a question contains a hallucination or not using the HaluEval dataset"
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
- **Generalization** (constructs) — *measured_by*
  > "we directly apply the directions and hyperparameters learned from TruthfulQA to HaluEval (Li et al., 2023) and TrivialQA (Joshi et al., 2017) to validate the generalizability of TAE."
  - [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf)
- **Document summarization** (behaviors tasks) — *measured_by*
  - [Benchmarking LLMs via Uncertainty Quantification](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bdcb065d40203a00bd39831153338bb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Truthfulness** (constructs) — *measured_by*
  - [Spectral Editing of Activations for Large Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [DREAM: Improving Video-Text Retrieval Through Relevance-Based Augmentation Using Large Foundation Models](https://aclanthology.org/2025.naacl-long.157.pdf)
- **Knowledge transferability** (constructs) — *measured_by*
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)

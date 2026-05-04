# AlpacaEval v1.0
**Type:** Measurement  
**Referenced in:** 114 papers  
**Also known as:** AlpacaEval, Alpaca Eval, Alpaca-Eval, Alpaca, Alpaca-Eval v1.0, alpaca-eval  

## State of the Field

AlpacaEval is predominantly characterized across the provided literature as an automatic evaluation framework that uses a strong LLM, most commonly GPT-4, as a judge. The evaluation is operationalized through a pairwise comparison where the judge model computes a win rate for a candidate model's responses against those of a reference model, which is frequently identified as `text-davinci-003`. Several papers specify that this evaluation is conducted on a set of 805 prompts. Across the surveyed work, AlpacaEval is most commonly used to measure a model's `instruction following` capabilities, and is also frequently employed to assess related constructs such as `human preference alignment`, `helpfulness`, `faithfulness`, and general `output quality`. A smaller set of studies uses it to evaluate more specific aspects like `conversational ability`, `out-of-distribution generalization`, and `linguistic quality`, with one paper detailing its use to assess metrics including "coherence, consistency, fact omission, fluency, and relevance" ("Seq1F1B: Efficient Sequence-Level Pipeline Parallelism for Large Language Model Training"). While the LLM-as-judge framework is the prevailing usage, a few papers describe it differently, for instance as a "leaderboard and associated dataset" or an "out-of-distribution evaluation test set". In a notable departure from its primary use as an evaluation tool, one paper utilizes AlpacaEval as a "downstream fine-tuning dataset", and another defines the related term "Alpaca" as a dataset of demonstrations rather than an evaluation benchmark.

## Sources

**[#InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/9dae2a90bae49dc874ce1ca8fcc20879-Paper-Conference.pdf) (as "AlpacaEval")**
> An automatic evaluation framework that uses GPT-4 to judge the quality of model outputs and compute a pairwise win rate against a reference model.

**[Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf) (as "Alpaca Eval")**
> A benchmark that uses LLMs as judges to evaluate model performance, particularly for instruction-following capabilities.

**[The Impossibility of FairLLMs](https://aclanthology.org/2025.acl-long.6.pdf) (as "Alpaca-Eval")**
> An LLM-based evaluation framework that uses GPT-4 to judge the quality of model outputs in open-ended conversation tasks by comparing them to reference responses.

**[Investigating and Extending Homans’ Social Exchange Theory with Large Language Model based Agents](https://aclanthology.org/2025.acl-long.482.pdf) (as "Alpaca")**
> A dataset of instruction-following demonstrations used for fine-tuning and evaluating models on their ability to respond to complex user queries.

**[Learning Distribution-wise Control in Representation Space for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deng25a/deng25a.pdf) (as "Alpaca-Eval v1.0")**
> An evaluation suite for assessing instruction-following capabilities, which uses GPT-4 as a judge to calculate a win rate against a baseline model.

**[Learning to Reason via Program Generation, Emulation, and Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/401ece9f5d1cfa8600c22049ef43930e-Paper-Conference.pdf) (as "alpaca-eval")**
> An evaluation suite used to compare the instruction-following capabilities of models.

## Relationships

### → AlpacaEval v1.0
- **Instruction following** (constructs) — *measured_by*
  - [OpenChat: Advancing Open-source Language Models with Mixed-Quality Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc8781fb328fb1fd069584a4519a2709-Paper-Conference.pdf)
- **Human preference alignment** (constructs) — *measured_by*
  - [Advantage-Guided Distillation for Preference Alignment in Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f891d026c7ba978168621842bc6fe73-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
- **Response quality** (constructs) — *measured_by*
  - [NEFTune: Noisy Embeddings Improve Instruction Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4bdeeaeb380b35302bbda1823d328c22-Paper-Conference.pdf)
- **Helpfulness** (constructs) — *measured_by*
  - [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf)
- **Fluency** (constructs) — *measured_by*
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Alignment** (constructs) — *measured_by*
  - [Toward Automatic Discovery of a Canine Phonetic Alphabet](https://aclanthology.org/2025.acl-long.452.pdf)
- **Conversational ability** (constructs) — *measured_by*
  - [CompKBQA: Component-wise Task Decomposition for Knowledge Base Question Answering](https://aclanthology.org/2025.emnlp-main.17.pdf)
- **Out-of-distribution generalization** (constructs) — *measured_by*
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Open-ended question answering** (behaviors tasks) — *measured_by*
  - [Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing](https://aclanthology.org/2025.acl-long.625.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **Coherence** (constructs) — *measured_by*
  - [ReSURE: Regularizing Supervision Unreliability for Multi-turn Dialogue Fine-tuning](https://aclanthology.org/2025.emnlp-main.960.pdf)
- **Linguistic quality** (constructs) — *measured_by*
  - [Seq1F1B: Efficient Sequence-Level Pipeline Parallelism for Large Language Model Training](https://aclanthology.org/2025.naacl-long.455.pdf)
- **Language understanding** (behaviors tasks) — *measured_by*
  - [LACA: Improving Cross-lingual Aspect-Based Sentiment Analysis withLLMData Augmentation](https://aclanthology.org/2025.acl-long.42.pdf)
- **Activation steering** (measurements) — *measured_by*
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Textual reasoning** (behaviors tasks) — *measured_by*
  - [ModelCitizens: Representing Community Voices in Online Safety](https://aclanthology.org/2025.emnlp-main.1572.pdf)

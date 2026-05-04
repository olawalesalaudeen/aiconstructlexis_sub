# AG News
**Type:** Measurement  
**Referenced in:** 59 papers  
**Also known as:** AG-News, AGNews, AGNEWS, AGnews, AgNews, AG's News, AG News Corpus, AG’s News  

## State of the Field

Across the surveyed literature, AG News is consistently described as a benchmark dataset for topic classification, composed of news articles sorted into four categories, which several papers specify as "World, Sports, Business, Sci/Tech." The dataset's primary and most prevalent application is to measure the behavior of `Text classification`. It is frequently used to evaluate models in various settings, including few-shot, zero-shot, and in-context learning, as well as for fine-tuning. Beyond this core use, a smaller set of studies employs AG News to measure `Adversarial robustness`, particularly in the context of backdoor attacks and defenses. It is also used more broadly to assess general `Downstream task performance` after fine-tuning.

## Sources

**[Out-of-Distribution Detection by Leveraging Between-Layer Transformation Smoothness](https://proceedings.iclr.cc/paper_files/paper/2024/file/0a2f65c9d2313b71005e600bd23393fe-Paper-Conference.pdf) (as "AG-News")**
> A topic classification dataset (AGN) constructed from news articles, categorized into four classes.

**[EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)**
> The AG News dataset, a benchmark for topic classification of news articles into four categories.

**[Revisiting In-context Learning Inference Circuit in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/22d4f952efa13970f0b1ffb22170d416-Paper-Conference.pdf) (as "AGNews")**
> The AG News dataset, a topic classification benchmark with four categories of news articles.

**[Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf) (as "AGNEWS")**
> The AG News (AGNEWS) corpus is a benchmark dataset for topic classification of news articles, used here as a user fine-tuning task.

**[Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf) (as "AGnews")**
> A news topic classification benchmark used to evaluate text classification and generation settings in the paper.

**[OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e9dbfc971b5f8e74f41e335ff3d658-Paper-Conference.pdf) (as "AgNews")**
> A topic classification benchmark used in the paper's in-context learning and instruction-tuning analysis.

**[Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf) (as "AG's News")**
> A topic classification benchmark used to evaluate model behavior on news-topic categorization.

**[LegalViz: Legal Text Visualization by Text To Diagram Generation](https://aclanthology.org/2025.naacl-long.340.pdf) (as "AG News Corpus")**
> News topic classification benchmark containing news articles across four categories, used to assess few-shot performance on balanced multi-class text classification.

**[ICLShield: Exploring and Mitigating In-Context Learning Backdoor Attacks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ren25b/ren25b.pdf) (as "AG’s News")**
> Text classification dataset used to evaluate news topic classification under backdoor attacks and defenses.

## Relationships

### → AG News
- **Text classification** (behaviors tasks) — *measured_by*
  > performing classification on two common datasets...: SST-2, AG-News and one modern dataset: StrategyQA
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **Adaptability** (constructs) — *measured_by*
  - [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)
- **News categorization** (behaviors tasks) — *measured_by*
  - [Vaccine: Perturbation-aware Alignment for Large Language Models against Harmful Fine-tuning Attack](https://proceedings.neurips.cc/paper_files/paper/2024/file/873c86d9a979ab80d8e2919510d4446b-Paper-Conference.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  > We conducted our confidence elicitation attacks on Meta-Llama-3-8B-Instruct (Touvron et al., 2023) and Mistral-7B-Instruct-v0.2 (Jiang et al., 2023) while performing classification on two common datasets to evaluate adversarial robustness: SST-2, AG-News and one modern dataset: StrategyQA (Geva et al., 2021). (Section 4)
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Confidence Elicitation: A New Attack Vector for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/04bb76a98d9f32226b3beba7bd26a51f-Paper-Conference.pdf)
- **Downstream task performance** (behaviors tasks) — *measured_by*
  > For fine-tuning tasks, we consider four different datasets, i.e., SST2, AGNEWS, GSM8K and AlpacaEval. (Sec. 5.1)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **General capabilities** (constructs) — *measured_by*
  - [DebateCoder: Towards Collective Intelligence ofLLMs via Test Case DrivenLLMDebate for Code Generation](https://aclanthology.org/2025.acl-long.590.pdf)

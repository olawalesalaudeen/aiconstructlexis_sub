# StrongReject
**Type:** Measurement  
**Referenced in:** 13 papers  
**Also known as:** StrongREJECT, STRONG REJECT  

## State of the Field

Across the provided literature, 'StrongReject' refers to two related but distinct measurement instruments: a dataset of harmful prompts and a safety classifier model. The most prevalent usage is as a safety evaluation dataset containing what one paper calls "manually constructed, more realistic and specific examples" of harmful prompts ("Investigating the (De)Composition Capabilities of Large Language Models in Natural-to-Formal Language Conversion"). This dataset includes "highly adversarial and unsafe prompts" such as instructions on how to make a nail bomb, and is used to measure constructs like `Safety`, `Harmlessness`, and `Adversarial robustness`. Papers operationalize it to assess a model's "safety violation rate" and evaluate performance against jailbreak techniques. A separate line of work defines StrongReject as a "safety classifier model based on Gemma-2B," which functions as an LLM-as-a-judge. In this capacity, it is used to measure the behavior of `Harmful content generation` by evaluating the harmfulness of model responses. Some sources describe it as a combined "dataset and scoring system," suggesting the dataset provides the prompts while a scoring mechanism quantifies the resulting responses ("The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions").

## Sources

**[Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)**
> A safety classifier model based on Gemma-2B, used as an LLM-as-a-judge to evaluate the harmfulness of model responses.

**[Backtracking Improves Generation Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/65beb73449888fabcf601b3a3ef4b3a7-Paper-Conference.pdf) (as "StrongREJECT")**
> An open-source safety evaluation dataset (SR) used to assess a model's safety violation rate.

**[The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25f/pan25f.pdf) (as "STRONG REJECT")**
> A dataset and scoring system used to provide toxic sample prompts for safety fine-tuning and to quantify the harmfulness of model responses during evaluation.

## Relationships

### → StrongReject
- **Harmlessness** (constructs) — *measured_by*
  - [The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Analysis of Orthogonal Safety Directions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25f/pan25f.pdf)
- **Safety** (constructs) — *measured_by*
  - [REFFLY: Melody-Constrained Lyrics Editing Model](https://aclanthology.org/2025.naacl-long.565.pdf)
- **Adversarial robustness** (constructs) — *measured_by*
  - [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: ... and the Gemma-2B version of the StrongReject safety classifier (Souly et al., 2024). (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)

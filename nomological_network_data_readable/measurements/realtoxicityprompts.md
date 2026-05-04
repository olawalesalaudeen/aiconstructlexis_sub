# RealToxicityPrompts
**Type:** Measurement  
**Referenced in:** 21 papers  
**Also known as:** REALTOXICITYPROMPTS, Real Toxicity Prompts, RealToxicity  

## State of the Field

Across the surveyed literature, RealToxicityPrompts is consistently characterized as a benchmark dataset or prompt set used for evaluation. Its primary application is to measure constructs related to model safety, including `Harmful content generation`, `Harmlessness`, and general `Safety`. The prevailing definition describes it as a collection of prompts, often sourced from the web, that are specifically designed to be likely to elicit toxic generations from language models. One paper provides a more specific origin, stating it is a "dataset of incomplete prompts designed to elicit toxic completions from GPT-2" ("When Bad Data Leads to Good Models"). In practice, researchers use the instrument by sampling prompts, and several papers note that the dataset contains distinct subsets of both toxic and non-toxic prompts for controlled testing. For instance, studies report drawing "10K toxic and 10K non-toxic prompts" or using specific portions like the "'challenging' split" for their evaluations. The overarching goal reflected in the data is to assess a model's propensity for generating toxic content and to evaluate its toxicity avoidance.

## Sources

**[Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf)**
> A prompt set used to elicit toxic generations from language models for toxicity evaluation.

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf) (as "REALTOXICITYPROMPTS")**
> A dataset of text prompts designed to be likely to elicit toxic generations from language models.

**[Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf) (as "RealToxicity")**
> A dataset used to evaluate the toxicity of generated text, providing a score based on the likelihood of the text being perceived as toxic.

**[Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf) (as "Real Toxicity Prompts")**
> A dataset of prompts from the web that are likely to elicit toxic generations from language models.

## Relationships

### RealToxicityPrompts →
- **Harmful content generation** (behaviors tasks) — *causes*
  - [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf)

### → RealToxicityPrompts
- **Harmlessness** (constructs) — *measured_by*
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
- **Harmful content generation** (behaviors tasks) — *measured_by*
  > Existing approaches mostly rely on static benchmarks, e.g., REALTOXICITYPROMPTS (Gehman et al., 2020) and HARM-BENCH (Mazeika et al., 2024) targeting harmfulness... (Introduction)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)

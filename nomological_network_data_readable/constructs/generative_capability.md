# Generative capability
**Type:** Construct  
**Referenced in:** 11 papers  
**Also known as:** Generation ability, Generative ability  

## State of the Field

Across the surveyed literature, generative capability is commonly described as a latent ability of large language models to produce fluent and coherent text. While one definition presents it as a general proficiency for creating contextually appropriate text for various tasks, other framings are more specific. For instance, one line of work defines it by its contrast to multiple-choice formats, emphasizing the production of diverse, free-form outputs like code, JSON, or open-ended text. Another paper frames this ability in the context of a specific application, defining it as the capacity to generate text adaptable into robust jailbreak prompts. To measure this construct, researchers in this set use generation-based benchmarks, with performance on TruthfulQA and GSM8k being used to operationalize it. As one study on model compression notes, a score of zero on these datasets indicates that models "totally lose their generation ability." The concept is also discussed alongside "language understanding" and "reasoning capabilities" and is considered susceptible to degradation or "catastrophic forgetting" under certain conditions.

## Sources

**[One Model Transfer to All: On Robust Jailbreak Prompts Generation against LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/124cc3a6e8f563555c8bba9f5ded690f-Paper-Conference.pdf) (as "Generation ability")**
> The latent ability of an LLM to produce fluent, coherent text outputs that can be adapted into robust jailbreak prompts.

**[Towards Robust and Parameter-Efficient Knowledge Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3076133f08b40607d00a8f48f6acd71c-Paper-Conference.pdf)**
> The model's general proficiency in producing fluent, coherent, and contextually appropriate text for various generation tasks.

**[MEGA-Bench: Scaling Multimodal Evaluation to over 500 Real-World Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/461f1fd5f92e5ca95764a88304dc39f7-Paper-Conference.pdf) (as "Generative ability")**
> The latent ability to produce free-form or non-multiple-choice outputs in diverse formats such as numbers, phrases, code, JSON, or open-ended text.

## Relationships

### Generative capability →
- **TruthfulQA** (measurements) — *measured_by*
  > the results on two generation datasets (TruthfulQA, GSM8K) of all three baselines when compression ratios are 60% and above are zero, meaning that the compressed LLMs totally lose their generation ability. (Section 4.1)
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **GSM8k** (measurements) — *measured_by*
  - [SVD-LLM: Truncation-aware Singular Value Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/3104e1ab39875cf54fe1eb4473e7c5a1-Paper-Conference.pdf)
- **WikiText-2** (measurements) — *measured_by*
  - [Molecular String Representation Preferences in PretrainedLLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.57.pdf)
- **C4** (measurements) — *measured_by*
  - [Molecular String Representation Preferences in PretrainedLLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.57.pdf)

### Associated with
- **Understanding** (constructs)
  - [The Generative AI Paradox: “What It Can Create, It May Not Understand”](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce208d95d020b023cba9e64031db2584-Paper-Conference.pdf)
- **Text generation** (behaviors tasks)
  - [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf)

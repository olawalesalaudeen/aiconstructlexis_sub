# E2E NLG Challenge
**Type:** Measurement  
**Referenced in:** 11 papers  
**Also known as:** E2E NLG, E2E  

## State of the Field

Across the provided literature, the E2E NLG Challenge is consistently presented as a benchmark dataset for evaluating natural language generation systems. Its primary application is to assess model performance on generating text from structured meaning representations, a task some papers also refer to as data-to-text generation. Multiple sources specify that this benchmark is situated within the restaurant domain. One paper further characterizes the structured input as "key-value attribute pairs" that require verbalization. The relationship data confirms its prevalent use as an evaluation tool, showing it is used to measure both "Text generation" and "Data-to-text generation" behaviors. For instance, several studies report using the E2E dataset to evaluate the performance of fine-tuned GPT-2 models. The provided materials show a consensus in using this benchmark to evaluate a model's ability to translate structured data into fluent, domain-specific text.

## Sources

**[KaSA: Knowledge-Aware Singular-Value Adaptation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8aec95bc5344290249c32841c07c9dd1-Paper-Conference.pdf)**
> A benchmark for evaluating natural language generation systems in the restaurant domain, focusing on generating text from structured meaning representations.

**[Logits are All We Need to Adapt Closed Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hiranandani25a/hiranandani25a.pdf) (as "E2E NLG")**
> E2E NLG is a text generation benchmark used to evaluate generation from structured meaning representations to natural language.

**[Joint Localization and Activation Editing for Low-Resource Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lai25a/lai25a.pdf) (as "E2E")**
> The E2E NLG Challenge dataset, focused on generating text from structured meaning representations in the restaurant domain.

## Relationships

### → E2E NLG Challenge
- **Text generation** (behaviors tasks) — *measured_by*
  > For NLG tasks, we assess our method with GPT-2 (Radford et al., 2019) on the E2E NLG Challenge (Novikova et al., 2017) benchmark. (Section 4)
  - [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf)
- **Data-to-text generation** (behaviors tasks) — *measured_by*
  - [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf)

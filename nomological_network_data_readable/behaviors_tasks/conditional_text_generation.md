# Conditional text generation
**Type:** Behavior  
**Referenced in:** 4 papers  

## State of the Field

Across the provided sources, conditional text generation is consistently defined as the behavior of producing fluent and coherent text completions based on given input contexts. This behavior is operationalized through several tasks, including text summarization, data-to-text generation, and text infilling, where the goal is to generate remaining tokens when some are provided in advance. To evaluate performance on this behavior, researchers use instruments such as the MAUVE and ParaDetox benchmarks, as well as datasets like WikiText-103, with one study specifically using its validation set. A recurring theme in the data is the connection between this behavior and model failure; one paper reports that conditional text generation by Large Language Models often causes hallucinations, where the output is unfaithful to the source context.

## Sources

**[SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)**
> Producing fluent and coherent text completions based on provided input contexts.

## Relationships

### Conditional text generation →
- **Hallucination** (behaviors tasks) — *causes*
  > Large Language Models (LLMs), when used for conditional text generation, often produce hallucinations, i.e., information that is unfaithful or not grounded in the input context. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **MAUVE** (measurements) — *measured_by*
  - [Beyond Autoregression: Fast LLMs via Self-Distillation Through Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  > For all methods, we use the same set of 2,000 text sequences from the validation set of WikiText-103 (Merity et al., 2022). (Section 6.2)
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
- **ParaDetox** (measurements) — *measured_by*
  - [Judging Quality Across Languages: A Multilingual Approach to Pretraining Data Filtering with Language Models](https://aclanthology.org/2025.emnlp-main.450.pdf)

### Associated with
- **Text summarization** (behaviors tasks)
  > This issue arises in typical conditional text generation tasks, such as text summarization and data-to-text generation, where the goal is to produce fluent text based on contextual input. (ABSTRACT)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Data-to-text generation** (behaviors tasks)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Text infilling** (behaviors tasks)
  > We now move on to conditional text generation, where certain tokens are provided in advance, and the task is to generate the remaining tokens. (Section 6.2)
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)

# Autoregressive language modeling
**Type:** Behavior  
**Referenced in:** 72 papers  
**Also known as:** Next-token prediction, Next token prediction, Next-word prediction, Word prediction, Token prediction  

## State of the Field

Across the provided literature, autoregressive language modeling is overwhelmingly defined as the task of predicting the next token in a sequence given the preceding tokens, a behavior frequently referred to as 'next-token prediction.' This is consistently described as a fundamental task and a common pretraining objective for language models. The process is operationalized by having a model generate a probability distribution over its vocabulary for the subsequent token, with training aimed at optimizing the autoregressive log-likelihood, often via a cross-entropy loss function. Performance on this task is measured using datasets such as C4, WikiText-103, and RedPajama, and one paper mentions perplexity as an evaluation metric. While the core definition is consistent, a few papers introduce variations, such as extending the task to multimodal contexts involving visual information or framing it as predicting a word that requires a broader discourse context. This behavior is also noted as being related to text generation.

## Sources

**[Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf) (as "Next-token prediction")**
> The fundamental task of predicting the next token in a sequence given all of the preceding tokens.

**[SLTrain: a sparse plus low rank approach for parameter and memory efficient pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/d63cf0622eed012a17fe88fced64dcb8-Paper-Conference.pdf) (as "Next token prediction")**
> The task of generating the most probable next token in a sequence given the preceding tokens, a common objective for pretraining language models.

**[fMRI predictors based on language models of increasing complexity recover brain left lateralization](https://proceedings.neurips.cc/paper_files/paper/2024/file/e28e19d00b23fe0265f433fa05a96b06-Paper-Conference.pdf) (as "Next-word prediction")**
> Predicting the next token or word in a sequence as an autoregressive language-model objective.

**[Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3848fef259495bfd04d60cdc5c1b4db7-Paper-Conference.pdf) (as "Word prediction")**
> The task of predicting a specific missing or final word in a sentence or passage, often requiring understanding of a broader context.

**[A Concept-Based Explainability Framework for Large Multimodal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f4fba41b554f9aaa013c4062a1c40518-Paper-Conference.pdf) (as "Token prediction")**
> Predicting the next text token in an autoregressive multimodal language model given prior visual and textual context.

**[LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts](https://aclanthology.org/2025.emnlp-main.369.pdf) (as "Causal language modeling")**
> The observable task of sequentially predicting the next token in a text given the preceding tokens.

**[TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters](https://proceedings.iclr.cc/paper_files/paper/2025/file/4da4dd613cc9e63932d643b9c6e8f86f-Paper-Conference.pdf)**
> The task of predicting the next token in a sequence given the preceding tokens, optimized by maximizing the autoregressive log-likelihood.

## Relationships

### Autoregressive language modeling →
- **C4** (measurements) — *measured_by*
  - [Mixture of Tokens: Continuous MoE through Cross-Example Aggregation](https://proceedings.neurips.cc/paper_files/paper/2024/file/bc427eb348789b190e3ea050cceff8a3-Paper-Conference.pdf)
- **WikiText-103** (measurements) — *measured_by*
  - [ZETA: Leveraging $Z$-order Curves for Efficient Top-$k$ Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/b508c1737d9242e40552699a6e98c87b-Paper-Conference.pdf)
- **RedPajama** (measurements) — *measured_by*
  > We train all models using the Llama2 recipe (Touvron et al., 2023) (with ALiBi instead of RoPE) and the RedPajama (Computer, 2023) dataset in JAX... (Sec. 5.5)
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)

### Associated with
- **Text generation** (behaviors tasks)
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)

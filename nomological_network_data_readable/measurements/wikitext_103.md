# WikiText-103
**Type:** Measurement  
**Referenced in:** 58 papers  
**Also known as:** Wikitext-103, WIKITEXT-103, Wikitext103, WIKITEXT103, WikiText103, EnWik-8, wikitext-103-v1  

## State of the Field

Across the provided literature, WikiText-103 is consistently defined as a large-scale language modeling benchmark derived from high-quality Wikipedia articles. Its most prevalent application is the evaluation of language modeling performance, with perplexity being the most frequently cited metric for assessing tasks like next-token prediction and general language understanding. Papers use this benchmark to measure a range of behaviors, most commonly language modeling and autoregressive language modeling, but also text generation, generation quality, and long-context processing. A smaller set of studies uses it to assess more specific phenomena like knowledge forgetting and text infilling. Beyond evaluation, WikiText-103 also serves as a dataset for pre-training models, such as GPT-2 and RoBERTa, as noted in one study: "We train a GPT2-large model on the WikiText-103 dataset" (Error Norm Truncation: Robust Training in the Presence of Data Noise for Text Generation Models). Finally, some researchers leverage it as a source of general-domain text for various experiments, including generating embeddings, studying sentence-level effects, or analyzing word tokenization.

## Sources

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf)**
> A larger version of the WikiText benchmark, derived from high-quality Wikipedia articles for language modeling evaluation.

**[Language Model Decoding as Direct Metrics Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/7416573f05b50beac6d0aef3abc805c0-Paper-Conference.pdf) (as "Wikitext-103")**
> A large-scale language modeling corpus derived from high-quality Wikipedia articles, used here as an evaluation domain for open-ended text generation.

**[Efficient Perplexity Bound and Ratio Matching in Discrete Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/23e6f78bdec844a9f7b6c957de2aae91-Paper-Conference.pdf) (as "Wikitext103")**
> A larger version of the Wikitext dataset, derived from Wikipedia articles and used for evaluating language model perplexity.

**[Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf) (as "WIKITEXT103")**
> A benchmark dataset derived from high-quality Wikipedia articles, used for evaluating language modeling performance.

**[Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/a365e37c18fb91af547a2f0012a89e98-Paper-Conference.pdf) (as "WikiText103")**
> A larger language modeling benchmark used to evaluate zero-shot text likelihood on a held-out corpus.

**[From Tokens to Words: On the Inner Lexicon of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/aef75887979ae1287b5deb54a1e3cbda-Paper-Conference.pdf) (as "WIKITEXT-103")**
> A large English language modeling dataset used to source text for experiments on splitting single-token words and analyzing attention patterns.

**[Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf) (as "EnWik-8")**
> A character-level language modeling benchmark used to evaluate pretraining performance.

**[From Language Models over Tokens to Language Models over Characters](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vieira25a/vieira25a.pdf) (as "wikitext-103-v1")**
> A large language modeling corpus derived from high-quality Wikipedia articles, used in this paper as a source of character strings for evaluating model performance.

## Relationships

### → WikiText-103
- **Language modeling** (behaviors tasks) — *measured_by*
  > To evaluate the performance of the model’s pre-training task, we measure perplexity on the Wikipedia 103 corpus (Merity et al., 2016) available through HuggingFace. (Section 2.4)
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
- **Autoregressive language modeling** (behaviors tasks) — *measured_by*
  - [ZETA: Leveraging $Z$-order Curves for Efficient Top-$k$ Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/b508c1737d9242e40552699a6e98c87b-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [COAT: Compressing Optimizer states and Activations for Memory-Efficient FP8 Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/6ac807c9b296964409b277369e55621a-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Text completion** (behaviors tasks) — *measured_by*
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **Conditional text generation** (behaviors tasks) — *measured_by*
  > For all methods, we use the same set of 2,000 text sequences from the validation set of WikiText-103 (Merity et al., 2022). (Section 6.2)
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
- **Text infilling** (behaviors tasks) — *measured_by*
  > Evaluation of text infilling performance using the MAUVE score (↑) with 5 prompt masks... For all methods, we use the same set of 2,000 text sequences from the validation set of WikiText-103
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [Reading between the Lines: CanLLMs Identify Cross-Cultural Communication Gaps?](https://aclanthology.org/2025.naacl-long.410.pdf)

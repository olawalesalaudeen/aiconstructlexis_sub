# WikiText-2
**Type:** Measurement  
**Referenced in:** 126 papers  
**Also known as:** Wikitext-2, wikitext-2, WikiText2, Wikitext2, WikiText-V2, WikiText2-v1  

## State of the Field

Across the provided literature, WikiText-2 is prevalently characterized as a language modeling benchmark derived from high-quality Wikipedia articles. Its most common application is to evaluate model performance, operationalized almost universally through the measurement of perplexity on a validation or test set. Papers frequently use this perplexity score to assess a model's `Language modeling` capabilities and `Text generation` quality. A recurring context for its use is the evaluation of compressed models, with numerous studies employing it to assess the performance of "pruned", "quantized", or "sparsified" LLMs. For instance, one study's goal is to "assess the performance of pruned models by calculating the perplexity of language generation experiments on separate validation sets derived from WikiText2" (Dynamic Sparse No Training:  Training-Free Fine-tuning for Sparse LLMs). While evaluation is the dominant use, a smaller stream of work uses WikiText-2 as a training dataset to observe model dynamics from scratch. Additionally, several papers utilize it as a "calibration dataset" or "calibration source", particularly for post-training quantization methods. Some evaluations are explicitly conducted in a "zero-shot setting", where models are assessed without prior fine-tuning on the dataset.

## Sources

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)**
> Language modeling benchmark that evaluates perplexity on a standard validation set to assess generative performance of pruned LLMs.

**[The LLM Surgeon](https://proceedings.iclr.cc/paper_files/paper/2024/file/38a1671ab0747b6ffe4d1c6ef117a3a9-Paper-Conference.pdf) (as "wikitext-2")**
> A standard benchmark dataset derived from Wikipedia articles, used to evaluate the language modeling capabilities of models after compression.

**[JoMA: Demystifying Multilayer Transformers via Joint Dynamics of MLP and Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/9c93b3cd3bc60c0fe7b0c2d74a2da966-Paper-Conference.pdf) (as "Wikitext-2")**
> A language modeling dataset (Wikitext2) used to train models from scratch and observe their training dynamics.

**[CBQ: Cross-Block Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/15212bd2265c4a3ab0dbc1b1982c1b69-Paper-Conference.pdf) (as "WikiText2")**
> A language modeling dataset used here as a generation evaluation dataset for measuring quantized model performance.

**[Dobi-SVD: Differentiable SVD for LLM Compression and Some New Perspectives](https://proceedings.iclr.cc/paper_files/paper/2025/file/218ca0d92e6ed8f9db00621e103dc70c-Paper-Conference.pdf) (as "Wikitext2")**
> A language modeling benchmark dataset (also known as WikiText-2) used to evaluate model performance via perplexity.

**[PICASO: Permutation-Invariant Context Composition with State Space Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0730b81dbc16cce7e85b519cb7fe5a8d-Paper-Conference.pdf) (as "WikiText-V2")**
> A large-scale language modeling benchmark dataset derived from high-quality Wikipedia articles, used to evaluate a model's ability to predict text continuations.

**[Demystifying Singular Defects in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25es/wang25es.pdf) (as "WikiText2-v1")**
> A dataset of over 100 million tokens from high-quality Wikipedia articles, used in this paper for analyzing hidden states and evaluating model perplexity after quantization.

## Relationships

### → WikiText-2
- **Language modeling** (behaviors tasks) — *measured_by*
  > “we assess the performance of pruned models by calculating the perplexity of language generation experiments on separate validation sets derived from WikiText2”
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > To pre-process WikiText-V2 for our use case, we split each passage in the dataset into two equal context “segments”, with the goal of predicting the second (continuation) from the first (query). (Section 6.1)
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
- **Generation quality** (constructs) — *measured_by*
  > “To evaluate the generative capability of the sparsified models, we conducted comprehensive perplexity experiments across different sparsity levels” and “we use the model’s perplexity on the WikiText2 (Merity et al., 2016) as the evaluation metric.”
  - [EMO: EARTH MOVER DISTANCE OPTIMIZATION FOR AUTO-REGRESSIVE LANGUAGE MODELING](https://proceedings.iclr.cc/paper_files/paper/2024/file/1626be0ab7f3d7b3c639fbfd5951bc40-Paper-Conference.pdf)
- **Faithfulness** (constructs) — *measured_by*
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
- **Quantization robustness** (constructs) — *measured_by*
  - [SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf)
- **Commonsense knowledge** (constructs) — *measured_by*
  - [LLMCBench: Benchmarking Large Language Model Compression for Efficient Deployment](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f4cc62d0632911c63163ea3d9ec19bd-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Causal language modeling** (behaviors tasks) — *measured_by*
  - [Empowering Retrieval-based Conversational Recommendation with Contrasting User Preferences](https://aclanthology.org/2025.naacl-long.393.pdf)
- **SmoothQuant** (measurements) — *measured_by*
  > PPL is the perplexity on the validation set of WikiText2-v1. (Table 1)
  - [Demystifying Singular Defects in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25es/wang25es.pdf)
- **Error handling** (constructs) — *measured_by*
  > “Following pruning, we evaluate model perplexity on the WikiText-2 dataset”
  - [Targeted Low-rank Refinement: Enhancing Sparse Language Models with Precision](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25e/shen25e.pdf)
- **Long-context understanding** (constructs) — *measured_by*
  - [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention for Long-Context LLM Serving](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ro25a/ro25a.pdf)
- **Long-context processing** (constructs) — *measured_by*
  - [LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shi25b/shi25b.pdf)
- **Generative capability** (constructs) — *measured_by*
  - [Molecular String Representation Preferences in PretrainedLLMs: A Comparative Study in Zero- & Few-Shot Molecular Property Prediction](https://aclanthology.org/2025.emnlp-main.57.pdf)

### Associated with
- **LLM Evaluation Harness** (measurements)
  > We use lm-evaluation-harness to report results on Wikitext2 (Merity et al., 2016), ARC (challenge) (Clark et al., 2018), BoolQ (Clark et al., 2019), CommonSenseQA (Talmor et al., 2019), Winogrande (Sakaguchi et al., 2019), MMLU (Hendrycks et al., 2021), and BigBench-Hard (Suzgun et al., 2022).
  - [QERA: an Analytical Framework for Quantization Error Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2025/file/21718991f6acf19a42376b5c7a8668c5-Paper-Conference.pdf)

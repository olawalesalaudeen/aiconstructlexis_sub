# Penn Treebank (PTB)
**Type:** Measurement  
**Referenced in:** 31 papers  
**Also known as:** PTB, Penn Treebank  

## State of the Field

Across the provided literature, Penn Treebank (PTB) is predominantly characterized as a benchmark for evaluating language modeling. It is most frequently used to assess model performance via the perplexity metric, often alongside other datasets like WikiText2 and C4. A recurring application is the evaluation of compressed models, including those subjected to pruning, quantization, and binarization. For example, studies report its use for measuring the "Perplexity of C4, wikitext2 and PTB on LLaMA-7b quantized with PTQ methods." While language modeling is the most common behavior measured with PTB, several papers also use it to evaluate text generation, and a single paper uses it to assess multilingual generalization. A less common framing defines it as a corpus for measuring log-loss improvements. In a distinct application, one paper utilizes PTB not for performance benchmarking but as a source of American English sentences for analyzing grammatical features.

## Sources

**[A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf) (as "PTB")**
> PTB (Penn Treebank) is a language-modeling benchmark used to evaluate pruned models via perplexity.

**[Language Models over Canonical Byte-Pair Encodings](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vieira25b/vieira25b.pdf) (as "Penn Treebank")**
> Corpus used for evaluating language models, specifically its test split containing 3761 strings, used here to measure log-loss improvements under canonicality enforcement.

## Relationships

### → Penn Treebank (PTB)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)

# Proof-pile
**Type:** Measurement  
**Referenced in:** 7 papers  
**Also known as:** Proof-Pile  

## State of the Field

Across the provided literature, Proof-pile is consistently used as a dataset to evaluate language modeling performance, with a recurring focus on long sequences. The most common description characterizes it as a 'cleaned Arxiv Math dataset' composed of 'long mathematical documents,' as noted in "PoSE: Efficient Context Window Extension of LLMs via Positional Skip-wise Training". A less frequent, though compatible, definition describes it more broadly as a collection of 'scientific and technical texts' for assessing performance on domain-specific content. The primary operationalization, mentioned in multiple papers, is the calculation of perplexity on the dataset's test set. This is used to measure the behavior of language modeling, particularly for extended context windows, with one study specifying its use for sequences of 'at least 128k tokens' ("YaRN: Efficient Context Window Extension of Large Language Models").

## Sources

**[LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/211ab571cc9f3802afa6ffff52ae3e5b-Paper-Conference.pdf)**
> Cleaned Arxiv Math dataset used for evaluating long-sequence language modeling performance in scientific domains via perplexity.

**[MorphMark: Flexible Adaptive Watermarking for Large Language Models](https://aclanthology.org/2025.acl-long.241.pdf) (as "Proof-Pile")**
> A dataset of scientific and technical texts used for evaluating language modeling performance on domain-specific long-form content.

## Relationships

### → Proof-pile
- **Language modeling** (behaviors tasks) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)

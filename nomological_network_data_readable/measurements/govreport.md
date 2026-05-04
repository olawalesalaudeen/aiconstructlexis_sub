# GovReport
**Type:** Measurement  
**Referenced in:** 13 papers  

## State of the Field

GovReport is consistently characterized across the provided literature as a dataset for evaluating language models on long documents, composed of U.S. government and congressional reports. The prevailing use of this benchmark is to measure `Text summarization` capabilities, with papers describing it as a "generic summarization dataset" and a tool to test "long text summarization capacity." Some sources specify its use for abstractive summarization in long-context scenarios. A smaller set of studies uses GovReport to evaluate `Language modeling` performance, particularly for "long sequence language modeling." One paper also positions it as a benchmark for assessing `Length generalization` or "long-context extrapolation." The dataset's documents are noted for their length, with an average of 7,866 tokens, and one source identifies GovReport as part of the SCROLL benchmark.

## Sources

**[In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)**
> Summarization dataset of U.S. government and congressional reports, used to evaluate language modeling performance on long documents with an average length of 7,866 tokens.

## Relationships

### → GovReport
- **Text summarization** (behaviors tasks) — *measured_by*
  - [Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/ee71a4b14ec26710b39ee6be113d7750-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)
- **Length generalization** (constructs) — *measured_by*
  > As shown in Fig.2, we evaluate the models' capacity to extrapolate to sequences of up to 20K tokens across six long-context benchmarks.
  - [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf)

# XLSum
**Type:** Measurement  
**Referenced in:** 9 papers  
**Also known as:** XLSUM, XL-Sum  

## State of the Field

Across the provided literature, XLSum is consistently characterized as a dataset or benchmark for evaluating summarization capabilities in language models. The most prevalent framing describes it as a multilingual or cross-lingual instrument, with one paper noting it covers 45 languages and another defining it as a benchmark for a model's ability to "condense text." It is used to measure both general "Text summarization" and, more specifically, "Abstractive summarization." Several papers define it as a dataset for news summarization, with one source describing it as "the largest publicly available summarization dataset" containing over 300,000 training samples. In practice, researchers use it for both fine-tuning and evaluation. For instance, one study utilizes its English subset, while another reports sampling 500 data points from its test set for evaluation purposes.

## Sources

**[Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)**
> A summarization dataset used to evaluate text summarization from projected embeddings.

**[Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf) (as "XLSUM")**
> A large, publicly available multilingual dataset for news summarization, used in this work for its English subset to fine-tune and evaluate Llama models.

**[Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization](https://proceedings.iclr.cc/paper_files/paper/2025/file/d24b7366d714b09a977946ef0d9bf3ad-Paper-Conference.pdf) (as "XL-Sum")**
> Cross-lingual summarization benchmark evaluating the model's ability to condense text.

## Relationships

### → XLSum
- **Text summarization** (behaviors tasks) — *measured_by*
  - [How do Large Language Models Handle Multilingualism?](https://proceedings.neurips.cc/paper_files/paper/2024/file/1bd359b32ab8b2a6bbafa1ed2856cf40-Paper-Conference.pdf)
- **Abstractive summarization** (behaviors tasks) — *measured_by*
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)

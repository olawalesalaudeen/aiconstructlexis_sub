# RedPajama
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** REDPAJAMA, Redpajama  

## State of the Field

Across the provided literature, RedPajama is consistently characterized as a large, multi-domain dataset for language models, with one paper specifying it is derived from the CommonCrawl corpus. Its application spans several stages of the model development lifecycle. A prevalent use is as an evaluation instrument; papers report using it to measure `Language modeling` performance, often by calculating perplexity on its "general web data." It is also used to evaluate `Autoregressive language modeling` and `Locality`. Beyond perplexity, some work employs RedPajama to simulate and measure generation throughput. Another application is in post-training quantization, where it serves as a calibration dataset intended to represent "typical input distributions." In addition to its measurement functions, RedPajama is also used as a source corpus for pre-training models and as a baseline for data selection and cleaning pipelines.

## Sources

**[Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf) (as "REDPAJAMA")**
> A multi-domain pretraining corpus from which samples are used to evaluate language modeling perplexity on general web data.

**[Relaxed Recursive Transformers: Effective Parameter Sharing with Layer-wise LoRA](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d6a55225cebbdc16fbb0e45c5bdf2b-Paper-Conference.pdf)**
> An open-source project to create a large, high-quality dataset for training language models, used here for simulating generation throughput.

**[Data Selection via Optimal Control for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf) (as "Redpajama")**
> A pre-training dataset derived from the CommonCrawl corpus, used as a source and baseline for data selection.

## Relationships

### → RedPajama
- **Locality** (constructs) — *measured_by*
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **Language modeling** (behaviors tasks) — *measured_by*
  - [Scaling Retrieval-Based Language Models with a Trillion-Token Datastore](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5d8aba27dfef4e849e8cb03fb87a954-Paper-Conference.pdf)
- **Autoregressive language modeling** (behaviors tasks) — *measured_by*
  > We train all models using the Llama2 recipe (Touvron et al., 2023) (with ALiBi instead of RoPE) and the RedPajama (Computer, 2023) dataset in JAX... (Sec. 5.5)
  - [STAR: Synthesis of Tailored Architectures](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc300c4d75b94b211b149ae4bcbbf2d2-Paper-Conference.pdf)

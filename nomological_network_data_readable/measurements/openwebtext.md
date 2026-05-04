# OpenWebText
**Type:** Measurement  
**Referenced in:** 31 papers  
**Also known as:** Openwebtext, OPENWEBTEXT  

## State of the Field

Across the surveyed literature, OpenWebText is consistently defined as a large-scale text dataset, with the most prevalent framing being an open-source replication of the WebText dataset. It is frequently specified as an English corpus scraped from the web, with one source noting it contains approximately 8 billion tokens. The dataset's most common application is for language model pre-training, with numerous papers citing its use for training GPT-2 models of various sizes from scratch. In addition to pre-training, OpenWebText is also used for validation and evaluation, where it serves as a benchmark to measure `Language modeling` performance using metrics like perplexity and validation loss. For instance, one study presents a figure showing the "Validation perplexity of GPT2-Small and GPT2-Large on OpenWebText." While its main role is as a training and evaluation corpus, one paper also uses it as a source of prompts for a sentence continuation task. The provided data also indicates it is used to measure `Causal language modeling`, `Text generation`, and `Generalization`.

## Sources

**[Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)**
> A large-scale text dataset, created as an open-source replication of the WebText dataset, used for pre-training and validating language models.

**[Adam-mini: Use Fewer Learning Rates To Gain More](https://proceedings.iclr.cc/paper_files/paper/2025/file/45ae878717399e6f62d57c65f052cd46-Paper-Conference.pdf) (as "Openwebtext")**
> A large-scale English corpus used for training and validating GPT-2 series language models.

**[Neural ODE Transformers: Analyzing Internal Dynamics and Adaptive Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/82e3509393670d9d478c359b4ce6f950-Paper-Conference.pdf) (as "OPENWEBTEXT")**
> A large-scale English text dataset, scraped from the web, commonly used for pre-training large language models.

## Relationships

### → OpenWebText
- **Language modeling** (behaviors tasks) — *measured_by*
  > We use two text datasets: 1) Text8 (Mahoney, 2006), a relatively small-scale, character-level text modeling benchmark extracted from English Wikipedia, and 2) OpenWebText, an open-source replica of the unreleased WebText (Gokaslan & Cohen, 2019) dataset used to train GPT-2.
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)
- **Language model pre-training** (behaviors tasks) — *measured_by*
  - [Adam-mini: Use Fewer Learning Rates To Gain More](https://proceedings.iclr.cc/paper_files/paper/2025/file/45ae878717399e6f62d57c65f052cd46-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  - [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf)
- **Causal language modeling** (behaviors tasks) — *measured_by*
  > We pre-train the AoT-MSSA-L and AoT-MHSA-L models of different sizes, along with GPT-2 (see Table 3 for model sizes), on OpenWebText (Gokaslan & Cohen, 2019).
  - [Attention-Only Transformers via Unrolled Subspace Denoising](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bu/wang25bu.pdf)

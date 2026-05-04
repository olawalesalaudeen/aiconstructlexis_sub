# Text generation quality
**Type:** Construct  
**Referenced in:** 14 papers  
**Also known as:** Generative ability, Generative quality, Text generation ability  

## State of the Field

Across the provided literature, "Text generation quality" is predominantly framed as a latent ability or inherent capacity of a language model to produce text that is coherent, fluent, relevant, and useful. Most definitions converge on this idea of overall textual excellence, with some explicitly contrasting it with simple metric optimization and emphasizing human preference. The construct is operationalized through a combination of automated metrics, benchmark tasks, and direct human judgment. Perplexity is a frequently mentioned metric, though some sources note its limitations, as "repetitive text also achieves low perplexity," while another paper uses the MAUVE score to capture "the overall usefulness of the generated text." Performance on generative tasks like CommonGen is also used as a measure of this ability. More direct operationalizations include human evaluation, which assesses dimensions such as "fluency, coherence, informativeness, and grammar," and evaluation using LLM-as-a-judge. The concept is often studied in contexts where it might be compromised; for instance, it is reported to be degraded by model compression and watermarking techniques. A distinct line of inquiry contrasts this construct with understanding, with one paper arguing that a model's "generative capabilities... can therefore exceed—their ability to understand those same types of outputs."

## Sources

**[Branch-GAN: Improving Text Generation with (not so) Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/02a92b52670752daf17b53f04f1ab405-Paper-Conference.pdf)**
> The latent ability of a language model to produce text that is coherent, fluent, and preferred by humans over alternatives, reflecting overall textual excellence beyond simple metric optimization.

**[SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf) (as "Generative quality")**
> The overall quality and coherence of text produced by the model in generative tasks, which can be degraded by compression.

**[A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf) (as "Text quality")**
> The overall quality of generated text, which can be degraded by watermarking techniques and is often measured by metrics like perplexity.

**[On the Learnability of Watermarks for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a86d17b6cd70366d56ab48d2a05a4df1-Paper-Conference.pdf) (as "Generation quality")**
> The overall quality of a model's generated output, encompassing aspects like coherence, relevance, and usefulness.

**[Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf) (as "Generative capability")**
> The inherent ability of a language model to produce high-quality, diverse, and contextually appropriate text, which can be better surfaced through improved sampling strategies.

**[Bridging Vision and Language Spaces with Assignment Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/file/3f20f2b0315c72201e23512fdbd1ee91-Paper-Conference.pdf) (as "Generative ability")**
> The capacity of an LLM to produce fluent text outputs conditioned on prompts and multimodal inputs.

**[Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf) (as "Text generation ability")**
> The latent capacity to produce coherent, accurate, and contextually appropriate text in response to a given prompt or task.

## Relationships

### Text generation quality →
- **Human evaluation** (measurements) — *measured_by*
  > “we find a similar-sized effect in the opposite direction, suggesting model quality according to humans may have slightly degraded.”
  - [Branch-GAN: Improving Text Generation with (not so) Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/02a92b52670752daf17b53f04f1ab405-Paper-Conference.pdf)
- **CommonGen** (measurements) — *measured_by*
  > We conduct experiments to compare the text generation and evaluation abilities of LLMs using the CommonGen (Lin et al., 2020) task, which involves generating a sentence that describes an everyday scenario based on a given set of common concepts (Section 4.1)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurements) — *measured_by*
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)

### Associated with
- **Language modeling** (behaviors tasks)
  > While we believe that perplexity measurements and generation quality are strongly related, this is a hypothesis we aim to investigate in future work. (Section 6)
  - [SpQR: A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/1787533e171dcc8549cc2eb5a4840eec-Paper-Conference.pdf)
- **Critique** (behaviors tasks)
  - [Language Model Self-improvement by Reinforcement Learning Contemplation](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5a655b8b373737b4f2aea8f78e5e754-Paper-Conference.pdf)

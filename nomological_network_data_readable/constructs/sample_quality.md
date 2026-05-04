# Sample quality
**Type:** Construct  
**Referenced in:** 4 papers  

## State of the Field

Across the provided literature, 'Sample quality' is consistently defined as the overall quality of a model's generated text, with 'coherence' being a commonly cited property. One definition expands this to also include the 'correctness' and 'relevance' of the output. The construct is operationalized and quantified using 'Generative perplexity,' a metric that one paper uses to compute the likelihood of generated samples under a more capable model. Discussions of sample quality appear when comparing model architectures, with one study noting its model's samples 'approach the quality of AR' models ("Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models"). The concept is also linked to generation settings, as 'excessively high temperatures can introduce many low-quality samples' ("Optimizing Temperature for Language Models with Multi-Sample Inference"). In this context, a 'sudden rise in the entropy curve' is inferred to imply a 'substantial drop in sample quality'.

## Sources

**[Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)**
> The overall quality of generated text as judged by coherence and related generation properties.

## Relationships

### Sample quality →
- **Generative perplexity** (measurements) — *measured_by*
  > In order to quantify sample quality, we use “generative perplexity”, a metric that computes the likelihood of generated samples under a more capable model... (Sec. 5.3)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)

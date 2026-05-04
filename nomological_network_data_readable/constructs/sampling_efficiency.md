# Sampling efficiency
**Type:** Construct  
**Referenced in:** 5 papers  

## State of the Field

Based on the provided data, sampling efficiency is defined as the degree to which a model can generate text with fewer denoising steps or less wall-clock time while maintaining quality. This framing, from "Energy-Based Diffusion Language Models for Text Generation," presents the construct as a trade-off between generation speed and output quality. The construct is operationalized by measuring reductions in the number of sampling steps or increases in sampling speed. For instance, one paper cites a "1.3× sampling speedup" as evidence of improved efficiency. Beyond being a direct target for optimization, sampling efficiency is also positioned as an outcome of other model capabilities. One paper suggests that it is causally influenced by a model's reasoning quality.

## Sources

**[Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)**
> The degree to which a model can generate text with fewer denoising steps or less wall-clock time while maintaining quality.

## Relationships

### → Sampling efficiency
- **Reasoning quality** (constructs) — *causes*
  - [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://aclanthology.org/2025.naacl-long.184.pdf)

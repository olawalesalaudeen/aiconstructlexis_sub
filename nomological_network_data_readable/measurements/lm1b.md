# lm1b
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** LM1B  

## State of the Field

Across the provided literature, lm1b is consistently characterized as a dataset for evaluating language models. The most prevalent framing identifies it as the "One-Billion Word Language Model Benchmark (LM1B)" used specifically to assess `Language modeling` performance. This operationalization is common, with one paper stating its use to "evaluate on prompts from a wide range of datasets and tasks, including language modeling with one-billion language benchmark (LM1B)" (Block Verification Accelerates Speculative Decoding). A slightly different framing describes it as a dataset for validating experimental methods across different data sources, noting its use alongside other benchmarks to "observe similar results" (Selective Attention Improves Transformer). A single paper also lists lm1b as a measure for `Multilingual generalization`, although no direct evidence for this application is provided in the input.

## Sources

**[Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)**
> A dataset used for running experiments to observe results similar to those on C4, validating the method across different data sources.

**[Block Verification Accelerates Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e710b42b1a9ed898f607ec0f4fcc971-Paper-Conference.pdf) (as "LM1B")**
> The One-Billion Word Language Model Benchmark (LM1B), a dataset used for evaluating language modeling performance.

## Relationships

### → lm1b
- **Language modeling** (behaviors tasks) — *measured_by*
  > We also ran experiments with WikiText (Merity et al., 2016), and lm1b (Chelba et al., 2014) and observed similar results. (Section 5)
  - [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf)
- **Zero-shot generalization** (constructs) — *measured_by*
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)

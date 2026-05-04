# WNLI
**Type:** Measurement  
**Referenced in:** 4 papers  

## State of the Field

Across the provided sources, WNLI is consistently characterized as a benchmark for natural language inference (NLI). Its formal definition states it is used to evaluate "sentence-level understanding and pronoun reasoning." This is reflected in its application, where it is used to measure both natural language inference and broader language understanding. A distinct use case appears in at least one paper, where WNLI is employed as an "out-of-domain" task to assess model adaptability and generalization capabilities. The benchmark is frequently identified as being part of the GLUE collection and is commonly used alongside other NLU datasets such as RTE, SNLI, CoLA, and MNLI.

## Sources

**[HeadMap: Locating and Enhancing Knowledge Circuits in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/52fc02778520b240c57046b3f7588ba1-Paper-Conference.pdf)**
> A natural language inference benchmark used to evaluate sentence-level understanding and pronoun reasoning.

## Relationships

### → WNLI
- **Language understanding** (behaviors tasks) — *measured_by*
  - [Collaborative Discrete-Continuous Black-Box Prompt Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8353c5035fe18b4fadd350228b4e0688-Paper-Conference.pdf)
- **Natural language inference** (behaviors tasks) — *measured_by*
  > for inference tasks, the RTE and WNLI (both from GLUE) datasets (Section 4).
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)
- **Generalization** (constructs) — *measured_by*
  > We then assessed the performance of the merged LoRA on these in-domain tasks as well as on two additional out-of-domain tasks, SNLI and WNLI, to evaluate its adaptability and generalization capabilities.
  - [Merging LoRAs like Playing LEGO: Pushing the Modularity of LoRA to Extremes Through Rank-Wise Clustering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b54e0146a82945f01e69c2e3309ba925-Paper-Conference.pdf)

### Associated with
- **GLUE** (measurements)
  > RTE and WNLI (both from GLUE)
  - [PortLLM: Personalizing Evolving Large Language Models with Training-Free and Portable Model Patches](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c444334e6bcf4e796f59f6d0bcae2a-Paper-Conference.pdf)

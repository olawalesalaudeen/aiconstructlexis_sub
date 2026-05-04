# Novelty
**Type:** Construct  
**Referenced in:** 14 papers  

## State of the Field

Across the provided literature, Novelty is consistently framed as the degree to which generated content is original, non-redundant, and dissimilar from existing information. While this core concept is shared, its application varies across domains, from the structural dissimilarity of generated proteins from known databases to the originality of generated research hypotheses. The operationalization of this construct differs accordingly; in protein generation, it is measured quantitatively using TMScore against the PDB database, where lower scores indicate greater novelty. In contrast, when evaluating textual content like scientific ideas, novelty is more commonly measured through human evaluation, with studies using surveys to assess "perceived clarity, novelty, and plausibility" or direct human judgment on research proposals. The provided data also indicates that LLM-based evaluation is used as a measurement instrument. Novelty is frequently assessed as one of several quality dimensions, studied alongside constructs such as utility, feasibility, relevance, and depth. One paper contrasts novel content with "vanilla-retrieved information" which is described as tending to "lack depth, novelty, and suffers from redundancy" (Refusal-Aware Red Teaming).

## Sources

**[DPLM-2: A Multimodal Diffusion Protein Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/57c30b677add9aa78e1745f0643104d0-Paper-Conference.pdf)**
> The degree to which generated protein structures are dissimilar from known, existing structures in protein databases.

## Relationships

### Novelty →
- **Human evaluation** (measurements) — *measured_by*
  > we also assess the intrinsic quality of the generated content. Specifically, we focus on two key dimensions: novelty and feasibility...human evaluation includes results on 40 of them. (Section 10, Table 4)
  - [ResearchTown: Simulator of Human Research Community](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25i/yu25i.pdf)
- **LLM-based evaluation** (measurements) — *measured_by*
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-DeviceLLM](https://aclanthology.org/2025.emnlp-main.534.pdf)

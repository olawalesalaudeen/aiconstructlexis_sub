# OpenOrca
**Type:** Measurement  
**Referenced in:** 6 papers  
**Also known as:** ORCA, Orca  

## State of the Field

Across the surveyed literature, OpenOrca is consistently presented as a dataset with a dual purpose: for supervised fine-tuning (SFT) and for the evaluation of large language models. It is most frequently used to assess "general reasoning and comprehension performance" and "instruction-following capabilities." One study also employs it to "validate model’s self-information retention and sequence-level semantic aggregation." There is some variation in how its composition is described. One framing presents the broader "Orca" family, which includes OpenOrca, as being "derived from explanations of chain-of-thought reasoning steps from larger models." Another common description characterizes it as an SFT collection that "samples from and combines prior SFT collections, including T0, FLAN, NIV, and CoT." The dataset is referred to interchangeably as "OpenOrca," "Orca," and as part of the "ORCA" family, which also contains a distilled version named SLIMORCA.

## Sources

**[Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates](https://proceedings.neurips.cc/paper_files/paper/2024/file/d6f034bb216b472fc7d32ec7aff20342-Paper-Conference.pdf)**
> An instruction/reasoning dataset used to fine-tune and evaluate general reasoning and comprehension performance.

**[SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf) (as "ORCA")**
> A dataset family (including OPENORCA and SLIMORCA) used for evaluating instruction-following capabilities, derived from explanations of chain-of-thought reasoning steps from larger models.

**[Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf) (as "Orca")**
> SFT collection that aggregates data from prior instruction-tuning datasets like FLAN, T0, and CoT, used for re-weighting and downstream evaluation.

## Relationships

### → OpenOrca
- **Instruction following** (constructs) — *measured_by*
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)

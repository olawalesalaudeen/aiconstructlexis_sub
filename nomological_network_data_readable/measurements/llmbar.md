# LLMBar
**Type:** Measurement  
**Referenced in:** 9 papers  

## State of the Field

LLMBar is most commonly described as a meta-evaluation benchmark or dataset designed to assess the capabilities of LLM evaluators. Across the provided sources, its primary stated purpose is to measure an evaluator's ability to distinguish instruction-following in model outputs, with one paper noting it emphasizes "instruction-following precision." The data also indicates it is used to measure commonsense knowledge and critique. Papers consistently state that LLMBar is structured with both "natural and adversarial subsets" for this assessment, with one source specifying these include "Neighbor, GPTInst, GPTOut, and Manual." The evaluation format is typically pairwise comparison, and one source highlights its use of "high-quality human annotations with a high level of inter-annotator agreement." A less common usage is also documented, where LLMBar is treated as a "referenced evaluation setup" by providing a specific prompt template for judging model responses.

## Sources

**[SaMer: A Scenario-aware Multi-dimensional Evaluator for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/646ca7b994bc46afe33d680dbe7ed67a-Paper-Conference.pdf)**
> A meta-evaluation benchmark for assessing LLM evaluators' ability to distinguish instruction-following outputs across natural and adversarial subsets.

## Relationships

### → LLMBar
- **Instruction following** (constructs) — *measured_by*
  > LLMBar (Zeng et al., 2023): meta-evaluation benchmark aimed at assessing LLM evaluators’ ability to distinguish instruction-following outputs.
  - [Evaluating Large Language Models at Evaluating Instruction Following](https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf)
- **Critique** (behaviors tasks) — *measured_by*
  - [SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/abe1eb21ceb046209c96a0f5e7544ccc-Paper-Conference.pdf)

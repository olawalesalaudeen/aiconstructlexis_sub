# TRACE
**Type:** Measurement  
**Referenced in:** 6 papers  

## State of the Field

Across the provided sources, TRACE is consistently characterized as a public benchmark for continual learning and continual instruction tuning. Its primary function is to evaluate model performance across a sequence of diverse tasks, particularly in the context of multi-round or sequential fine-tuning. The benchmark is most frequently stated to measure abilities like `code generation` and `mathematical reasoning`, with multi-choice QA and summarization also listed as component tasks. A less common framing, found in one paper, describes TRACE as being designed to evaluate broader capabilities, including `general ability`, `instruction following`, and `safety`. The provided data also indicates that TRACE is used to measure `commonsense knowledge` and `complex instruction following`, although specific evidence for these connections is not present in the source snippets.

## Sources

**[Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)**
> A public benchmark for continual learning that includes a sequence of tasks such as multi-choice QA, code generation, mathematical reasoning, and summarization.

## Relationships

### → TRACE
- **Mathematical reasoning** (constructs) — *measured_by*
  > we also addressed the effectiveness of our approach on the public benchmark TRACE Wang et al. (2023c), which includes a learning sequence comprised of multi-choice QA, code generation, mathematical reasoning, and summarization tasks. (Section 6)
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **Code completion** (behaviors tasks) — *measured_by*
  - [Spurious Forgetting in Continual Learning of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf)
- **Complex instruction following** (constructs) — *measured_by*
  - [Aligned but Blind: Alignment Increases Implicit Bias by Reducing Awareness of Race](https://aclanthology.org/2025.acl-long.1079.pdf)
- **Safety** (constructs) — *measured_by*
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)

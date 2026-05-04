# FLAN
**Type:** Measurement  
**Referenced in:** 4 papers  
**Also known as:** FLAN Collection  

## State of the Field

Across the provided literature, FLAN is consistently characterized as a multi-task benchmark or dataset used for robust evaluation. It is defined as a collection of diverse tasks—with one paper noting a sample of 66 tasks—that are expressed as natural language instructions. Some sources, referring to it as the "FLAN Collection," highlight that it features data for evaluating instruction following, chain-of-thought, and in-context few-shot learning. The tasks are described as varied and include free-form generation such as translation and summarization. Papers commonly use FLAN to measure model `Generalization` and robustness, with one study including it as a reference dataset to "demonstrate the generalizability and robustness" of their method. It is also reported to be used for assessing `Commonsense knowledge` and `Safety`.

## Sources

**[BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)**
> A benchmark of diverse tasks including free-form generation tasks such as translation and summarization, used here as a large multi-task evaluation set.

**[MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf) (as "FLAN Collection")**
> The FLAN Collection is a dataset composed of various tasks formatted as instructions, used to evaluate instruction-following, chain-of-thought, and few-shot learning capabilities.

## Relationships

### → FLAN
- **Generalization** (constructs) — *measured_by*
  > To demonstrate the generalizability and robustness of our method, we include FLAN (Chung et al., 2024) (a mix of multiple NLP tasks) as reference datasets .
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)
- **Instruction following** (constructs) — *measured_by*
  - [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Harnessing Diversity for Important Data Selection in Pretraining Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/b588d9b67932b459ea66ff6e2804c6b3-Paper-Conference.pdf)

### Associated with
- **Free-form generation** (behaviors tasks)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)

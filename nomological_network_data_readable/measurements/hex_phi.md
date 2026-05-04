# HEX-PHI
**Type:** Measurement  
**Referenced in:** 12 papers  
**Also known as:** HEx-PHI  

## State of the Field

Across the provided literature, HEX-PHI is consistently characterized as a safety benchmark or dataset composed of harmful instructions designed to evaluate language models. Several papers specify its composition, noting that it consists of 330 harmful queries or instructions distributed across 11 categories. The primary application of this benchmark is to evaluate a model's safety-related properties. It is most frequently used to measure a model's general 'safety' and 'safety alignment', with one paper stating its purpose is to "evaluate the safety alignment of a model" (SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection). Other papers use it to assess 'harmlessness' and to evaluate model responses in the context of 'adversarial attacks'. The evaluation generally focuses on determining whether models "comply with harmful requests and produce unsafe outputs" (Safety Alignment Should be Made More Than Just a Few Tokens Deep). A smaller portion of the literature also highlights its use for assessing compliance with "privacy-harming and personally harmful instructions" (AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset).

## Sources

**[SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)**
> A dataset containing 11 categories of harmfulness-inducing instructions, specifically designed to evaluate the safety alignment of a language model.

**[Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf) (as "HEx-PHI")**
> HEx-PHI safety benchmark consisting of harmful instructions used to evaluate whether models comply with harmful requests and produce unsafe outputs.

## Relationships

### → HEX-PHI
- **Harmlessness** (constructs) — *measured_by*
  - [CausalEval: Towards Better Causal Reasoning in Language Models](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Safety alignment** (constructs) — *measured_by*
  > HEX-PHI: introduced in (Qi et al., 2023), it contains 11 categories of harmfulness-inducing instructions. It is used to evaluate the safety alignment of a model (Section 4.1)
  - [SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d5d91b4525151fc0fee1048332bfb6d-Paper-Conference.pdf)
- **Adversarial attacks** (behaviors tasks) — *measured_by*
  > "We also consider two additional harmfulness evaluation datasets: HEx-PHI (Qi et al., 2023) and SORRY-bench (Xie et al., 2024)."
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **Safety** (constructs) — *measured_by*
  - [Powerformer: Efficient and High-Accuracy Privacy-Preserving Language Model with Homomorphic Encryption](https://aclanthology.org/2025.acl-long.544.pdf)

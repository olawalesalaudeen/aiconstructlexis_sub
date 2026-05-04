# TOFU
**Type:** Measurement  
**Referenced in:** 24 papers  
**Also known as:** TOFU dataset  

## State of the Field

Across the provided literature, TOFU is consistently characterized as a synthetic benchmark dataset used to evaluate machine unlearning in large language models. It is most commonly described as consisting of question-answer pairs based on fictitious author biographies or fictional characters, with several papers specifying its scale as 200 authors and 4,000 total QA pairs. The primary application of TOFU is to operationalize and measure unlearning-related constructs; papers use it to assess "Machine unlearning," "Unlearning effectiveness," and "Forget quality," with some using metrics like "Forget Quality (FQ) and Model Utility (MU)" that were proposed alongside the dataset. Its usage also extends to evaluating "Verbatim memorization" and "Faithfulness." The benchmark is framed as simulating scenarios where personal or infringed-upon information must be removed from a model, as one paper notes it "focuses on unlearning knowledge related to fictional characters, simulating scenarios where personal information is infringed upon by LLMs and must be removed." One source contrasts TOFU's synthetic data with the MUSE benchmark, which is positioned as addressing "real-world unlearning challenges."

## Sources

**[Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf)**
> The TOFU benchmark, used here to evaluate recovery of unlearned author-related knowledge and keywords from fictitious QA pairs.

**[LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf) (as "TOFU dataset")**
> A synthetic question-answering dataset focused on fictitious author biographies, designed to evaluate entity unlearning.

## Relationships

### → TOFU
- **Faithfulness** (constructs) — *measured_by*
  - [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b69bc53449ba46bb981951078929a5e-Paper-Conference.pdf)
- **Forget quality** (constructs) — *measured_by*
  > To assess forget quality and model utility, we mainly use two metrics proposed alongside the TOFU dataset, Forget Quality (FQ) and Model Utility (MU) (Maini et al., 2024a). (Section 4.3)
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
- **Unlearning effectiveness** (constructs) — *measured_by*
  > We conduct experiments on TOFU (Maini et al., 2024), which consists of 200 fictitious author profiles split into a retain and forget set, where the retain set is used to maintain model capabilities and the forget set is used for unlearning (Section 6).
  - [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b69bc53449ba46bb981951078929a5e-Paper-Conference.pdf)
- **Text generation** (behaviors tasks) — *measured_by*
  > The closest work to ours is TOFU (Maini et al., 2024), a benchmark featuring 200 synthetic author profiles, each with 20 question-answer pairs, divided into forget and retain sets. (Section 6)
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
- **Machine unlearning** (constructs) — *measured_by*
  - [Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wuerkaixi25a/wuerkaixi25a.pdf)
- **Verbatim memorization** (constructs) — *measured_by*
  - [Using Text-Based Causal Inference to Disentangle Factors Influencing Online Review Ratings](https://aclanthology.org/2025.naacl-long.563.pdf)

### Associated with
- **MUSE** (measurements)
  > Unlike the previous benchmark TOFU (Maini et al., 2024), which evaluates unlearning on synthetic Q&A datasets, MUSE tackles real-world unlearning challenges (Table 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)

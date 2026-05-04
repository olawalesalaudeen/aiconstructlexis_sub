# AQuA-RAT
**Type:** Measurement  
**Referenced in:** 56 papers  
**Also known as:** AQUA, AQuA, AQUA-RAT, AquaRAT  

## State of the Field

Across the provided literature, AQuA-RAT is predominantly used as a benchmark to evaluate mathematical reasoning. The instrument is consistently defined as a dataset of algebraic word problems, with a prevailing description of them being in a multiple-choice format. While there is broad agreement on this structure, one paper specifies a "4-option multiple choice format," while another describes it as having "five multiple-choice options (A to E)." Several definitions, particularly those using the "-RAT" suffix or expanding the acronym to "Algebra Question Answering with Rationales," state that the dataset includes rationales for the solutions, requiring multi-step reasoning. Papers use this benchmark to measure a range of abilities, with the most common being `Mathematical reasoning`, alongside more specific framings like "arithmetic reasoning," "numerical reasoning," and "quantitative reasoning." In experimental setups, it is frequently evaluated alongside other math datasets such as GSM8K and SVAMP. Some specific applications mentioned include testing the transferability of optimized prompts and assessing performance with few-shot demonstrations.

## Sources

**[Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf) (as "AQuA")**
> Dataset of algebraic word problems with multiple-choice answers, used to test transferability of optimized prompts across math reasoning tasks.

**[DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf) (as "AQUA")**
> Multiple-choice math word problem dataset requiring reasoning over quantitative and qualitative relationships.

**[Enhancing Automated Interpretability with Output-Centric Feature Descriptions](https://aclanthology.org/2025.acl-long.289.pdf) (as "AQUA-RAT")**
> A dataset of algebraic word problems with rationales, requiring multi-step reasoning.

**[SIRIUS : Contexual Sparisty with Correction for Efficient LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ae6b2bdf3a179e3e24129e2c54bd871-Paper-Conference.pdf)**
> A dataset of algebraic word problems requiring rationales for their solutions, used to test arithmetic reasoning.

**[Sample Efficient Demonstration Selection for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/purohit25a/purohit25a.pdf) (as "AquaRAT")**
> A benchmark of algebraic and quantitative reasoning questions used here to evaluate numerical reasoning with few-shot demonstrations.

## Relationships

### → AQuA-RAT
- **Mathematical reasoning** (constructs) — *measured_by*
  - [Boosting of Thoughts: Trial-and-Error Problem Solving with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b6f6bfbd260fbf2f5acb0a1d6439ca0e-Paper-Conference.pdf)

# Verification ability
**Type:** Construct  
**Referenced in:** 3 papers  
**Also known as:** Verification capability  

## State of the Field

Across the provided literature, Verification ability is consistently framed as a latent capacity of a model to evaluate and select among multiple candidate outputs. Definitions describe this as the ability to judge the 'quality or correctness' of outputs better than chance, or more specifically, to 'identify and select the correct solution trajectory from a set of candidates' ("Process Reward Model with Q-value Rankings"). The construct is operationalized and measured using a best-of-n sampling procedure. This evaluation assesses the correctness of the single trajectory a model prefers most out of a set of 'n' candidates. The datasets used in this measurement process include GSM-Plus and MATH-500, with one study using a corpus of 128 solutions for each question from these sources. Another line of work discusses this capability in the context of a 'verifier model g' whose capacity influences outcomes. Thus, the concept is primarily used to characterize a model's judgment capabilities, which are then empirically tested by its performance in a selection task.

## Sources

**[Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)**
> The latent capacity of a model to identify and select the correct solution trajectory from a set of candidates.

**[Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63943ee9fe347f3d95892cf87d9a42e6-Paper-Conference.pdf) (as "Verification capability")**
> The latent ability of a model to judge the quality or correctness of candidate outputs better than chance.

## Relationships

### Verification ability →
- **Best-of-N** (measurements) — *measured_by*
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)
- **MATH-500** (measurements) — *measured_by*
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)
- **GSM-Plus** (measurements) — *measured_by*
  > “The test corpus includes 128 solutions for each question from GSM-Plus (Li et al., 2024) and MATH500 (Hendrycks et al., 2021) datasets.”
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)

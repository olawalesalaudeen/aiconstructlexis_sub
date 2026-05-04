# GSM-Plus
**Type:** Measurement  
**Referenced in:** 8 papers  
**Also known as:** GSM-PLUS  

## State of the Field

Across the provided literature, GSM-Plus is consistently framed as a benchmark derived from GSM8k. The most common description is as an "adversarial version of the GSM8k benchmark," with a less frequent framing calling it an "extension." Its primary application is to evaluate mathematical reasoning, particularly on grade-school math problems, and it is frequently used alongside other math benchmarks. A related and commonly mentioned use is to specifically assess model robustness; one paper states it "measures resilience to adversarial perturbations" and categorizes it as a "robustness benchmark." A more distinct application appears in one study where questions from GSM-Plus are used to construct a test corpus for evaluating a model's verification ability.

## Sources

**[Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)**
> An adversarial version of the GSM8k benchmark, designed to be more challenging and test the robustness of a model's mathematical reasoning.

**[Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf) (as "GSM-PLUS")**
> The GSM-PLUS benchmark, an extension of GSM8K, used to evaluate mathematical reasoning on grade-school math problems.

## Relationships

### → GSM-Plus
- **Mathematical reasoning** (constructs) — *measured_by*
  > The model’s performance is evaluated on two grade school math benchmarks: GSM8k (Cobbe et al., 2021) and GSM-Plus (Li et al., 2024), which is an adversarial version of GSM8k. (Section 4.4)
  - [Noise Contrastive Alignment of Language Models with Explicit Rewards](https://proceedings.neurips.cc/paper_files/paper/2024/file/d5a58d198afa370a3dff0e1ca4fe1802-Paper-Conference.pdf)
- **Robustness** (constructs) — *measured_by*
  - [Forewarned is Forearmed:  Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
- **Verification ability** (constructs) — *measured_by*
  > “The test corpus includes 128 solutions for each question from GSM-Plus (Li et al., 2024) and MATH500 (Hendrycks et al., 2021) datasets.”
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)

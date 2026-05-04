# Unlearning efficacy
**Type:** Construct  
**Referenced in:** 5 papers  

## State of the Field

The construct of "Unlearning efficacy" is conceptualized in two related but distinct ways within the provided literature. One definition, found across multiple papers, frames it as a dual objective: the degree to which a model successfully erases targeted knowledge while simultaneously remaining useful on non-targeted data. A different, more formal definition is also offered, describing efficacy as the degree to which an unlearning method makes a model "statistically indistinguishable from one retrained from scratch without the data intended to be forgotten" ("Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning"). This latter view is conceptually operationalized by comparing the behavior of the unlearned model (Munlearn) to a retrained model (Mretrain) to ensure they are approximately equivalent on any corpus. The assessment of this construct is also discussed in the context of developing more "equitable and comprehensive assessments," with one paper proposing a "minority-aware evaluation framework" to achieve a more holistic understanding.

## Sources

**[Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/3a91841d2bcc0b13a3d0d5d60c9f0581-Paper-Conference.pdf)**
> The degree to which an LLM successfully erases targeted knowledge while remaining useful on non-targeted data.

## Relationships

### Unlearning efficacy →
- **Membership inference attack** (behaviors tasks) — *measured_by*
  - [Machine Unlearning Fails to Remove Data Poisoning Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e810b2c75d69be186cadd2fe3febeab-Paper-Conference.pdf)
- **WMDP** (measurements) — *measured_by*
  - [Exploring Criteria of Loss Reweighting to Enhance LLM Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ak/yang25ak.pdf)

### Associated with
- **Memorization** (constructs)
  - [Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf)
